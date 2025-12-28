from pymongo import MongoClient
from datetime import datetime
class DatabaseManager:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="POS_System_DB"):
        self.client = None
        self.db = None
        self.connected = False 
        try:
            self.client = MongoClient(uri, serverSelectionTimeoutMS=5000)
            self.db = self.client[db_name]
            self.products = self.db.products 
            self.sales = self.db.sales       
            self.client.admin.command('ping')
            self.connected = True 
            print("MongoDB baglantisi basarili.")
            self.initialize_data()
        except Exception as e:
            print(f"MongoDB baglanti hatasi: {e}")
            self.connected = False
      
    def initialize_data(self):
        if self.connected and self.products.count_documents({}) == 0:
            initial_products = [
                {"barcode": "1234567890123", "name": "EKMEK", "purchase_price": 5.0, "sale_price": 7.50, "stock_quantity": 50, "last_updated": datetime.now()},
            ]
            self.products.insert_many(initial_products)

    def find_product_by_barcode(self, barcode):
        if self.connected:
            return self.products.find_one({"barcode": barcode})
        return None

    def find_product_by_name(self, name):
        if self.connected:
            return self.products.find_one({"name": {"$regex": f"^{name}$", "$options": "i"}})
             # bu sorgu ile EKMEK ekmek Ekmek aynı kabul edilirler.
        return None

    def get_all_products(self):
        if not self.connected:
            return []

        try:
            collection = getattr(self, 'products', getattr(self, 'products_collection', None))
            if collection is None:
                return []
            return list(collection.find({}, {"_id": 0}).sort("name", 1))
        
        except Exception as e:
            print(f"Hata get_all_products: {e}")
            return []

    def insert_product(self, data):
        if not self.connected: return False
        try:
            if self.products.find_one({"barcode": data['barcode']}):
                return False
            data['created_at'] = datetime.now()
            data['last_updated'] = datetime.now()
            self.products.insert_one(data)
            return True
        except: return False

    def update_product_by_barcode(self, barcode, updated_data):
        if not self.connected: return False
        try:
            updated_data['last_updated'] = datetime.now()
            #güncellenen alanın son güncellenme tarihini kaydediyor.
            if '_id' in updated_data: del updated_data['_id']
            #id alanını siliyor mongodb'den dolayı
            result = self.products.update_one({"barcode": barcode}, {"$set": updated_data})
            # sadece verilen alanı değiştir kısmı(set)
            return result.modified_count > 0
        except Exception as e:
            print(f"Guncelleme hatasi: {e}")
            return False

    def delete_product_by_barcode(self, barcode):
        if not self.connected: return False
        try:
            result = self.products.delete_one({"barcode": barcode})
            return result.deleted_count > 0
        except: return False

    def update_stock_by_barcode(self, barcode, new_stock):
        if not self.connected: return False
        try:
            self.products.update_one({"barcode": barcode}, {"$set": {"stock_quantity": int(new_stock), "last_updated": datetime.now()}})
            return True
        except: return False

    def satis_kaydi(self, sale_data):
        if self.connected:
            now = datetime.now()
            sale_data['created_at'] = now
            sale_data['date'] = now  
            
            for item in sale_data.get('items', []):
                self.products.update_one(
                    {"barcode": item['barcode']},
                    {"$inc": {"stock_quantity": -int(item['quantity'])}}
                )
            self.sales.insert_one(sale_data)
            return True
        return False

    def log_return(self, return_data):
        if self.connected:
            now = datetime.now()
            return_data['created_at'] = now
            return_data['date'] = now
            
            return_data['payment_type'] = 'İade' 
            
            try:
                amount = float(return_data.get('total_amount', 0))
                if amount > 0:
                    return_data['total_amount'] = -amount
            except:
                pass

            for item in return_data.get('items', []):
                self.products.update_one(
                    {"barcode": item['barcode']},
                    {"$inc": {"stock_quantity": int(item['quantity'])}}
                )
            
            self.sales.insert_one(return_data)
            return True
        return False

    def get_last_sales(self, limit=100):
        if self.connected:
            return list(self.sales.find({}).sort("date", -1).limit(limit))
        return []
    
    def get_sales_report(self, start_date, end_date):
        if not self.connected:
            return []
        
        try:
            collection = getattr(self, 'sales', getattr(self, 'sales_collection', None))    
            if collection is None:
                return []
            query = {
                "created_at": {
                    "$gte": start_date,
                    "$lte": end_date
                }
            }
            results = list(collection.find(query).sort("created_at", -1))
            return results

        except Exception as e:
            return []
        

    def check_login(self, username, password):
        #kullanıcı adı ve şifreyi kontrol eder.
        try:
            user = self.db.users.find_one({"username": username, "password": password})
            return user is not None
        except Exception as e:
            print(f"Login hatası: {e}")
            return False

    def update_password(self, username, old_password, new_password):
        #şifre değiştirme işlemi
        try:
            if self.check_login(username, old_password):
                result = self.db.users.update_one(
                    {"username": username},
                    {"$set": {"password": new_password}}
                )
                return result.modified_count > 0
            else:
                return False
        except Exception as e:
            print(f"Şifre güncelleme hatası: {e}")
            return False

    def create_default_admin(self):
        #veritabanı boşsa varsayılan  olarak admin oluşturulur
        try:
            if self.db.users.count_documents({}) == 0:
                self.db.users.insert_one({"username": "admin", "password": "123"})
                print("Varsayılan kullanıcı oluşturuldu: admin / 123")
        except Exception as e:
            print(f"Kullanıcı oluşturma hatası: {e}")


    def add_user(self, username, password):
        #yeni kullanıcı oluşturulur
        try:
            if self.db.users.find_one({"username": username}):
                return False, "Bu kullanıcı adı zaten kullanılıyor."
            
            self.db.users.insert_one({
                "username": username, 
                "password": password,
                "role": "personel" 
            })
            return True, "Kullanıcı başarıyla eklendi."
        except Exception as e:
            return False, str(e)

    def get_all_users(self):
        #tüm kullanıcıları döndürür
        try:
            users = self.db.users.find({}, {"_id": 0, "username": 1})
            return [user['username'] for user in users]
        except Exception:
            return []

    def delete_user(self, username):
        #kullanıcıları siler
        if username == "admin":
            return False 
        
        try:
            self.db.users.delete_one({"username": username})
            return True
        except Exception:
            return False