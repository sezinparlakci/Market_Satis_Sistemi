from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui.ui_stok_ekle import Ui_ManualStockAdjustmentDialog

class StokDuzenlemeUygulamasi(QDialog):
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.ui = Ui_ManualStockAdjustmentDialog()
        self.ui.setupUi(self)
        self.db = db
        self.load_products() 
        self.setup_connections()


    def setup_connections(self):
        self.ui.btn_cancel.clicked.connect(self.close)
        self.ui.btn_search.clicked.connect(self.filter_products)
        self.ui.lineEdit_search_barcode.returnPressed.connect(self.filter_products)
        self.ui.lineEdit_search_barcode.textChanged.connect(self.auto_reset_search)
        self.ui.btn_save_changes.clicked.connect(self.save_stock_changes)

    def load_products(self):
        if not self.db.connected:
            QMessageBox.warning(self, "Bağlantı Hatası", "Veritabanı bağlı değil! Ürünler listelenemiyor.")
            return

        try:
            if hasattr(self.db, 'get_all_products'):
                products = self.db.get_all_products()
            else:
                products = list(self.db.products.find({}))
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Ürünler çekilirken hata oluştu: {str(e)}")
            return

        if not products:
            QMessageBox.information(self, "Bilgi", "Veritabanında kayıtlı hiç ürün bulunamadı.")
        
        self.ui.tableWidget_stock_list.setRowCount(0)
        self.ui.tableWidget_stock_list.setRowCount(len(products))
        
        for row, product in enumerate(products):
            barcode = str(product.get("barcode", ""))
            name = str(product.get("name", ""))
            current_stock = product.get("stock_quantity", product.get("stock", 0))

            self.ui.tableWidget_stock_list.setItem(row, 0, QTableWidgetItem(barcode))
            self.ui.tableWidget_stock_list.setItem(row, 1, QTableWidgetItem(name))
            
            item_stock = QTableWidgetItem(str(current_stock))
            item_stock.setFlags(item_stock.flags() & ~Qt.ItemIsEditable) # bu değişitirilemez olduğunu anlatır
            self.ui.tableWidget_stock_list.setItem(row, 2, item_stock)
            self.ui.tableWidget_stock_list.setItem(row, 3, QTableWidgetItem(str(current_stock)))

    def filter_products(self):
        search_text = self.ui.lineEdit_search_barcode.text().lower().strip()
        row_count = self.ui.tableWidget_stock_list.rowCount()
        match_count = 0
        
        for row in range(row_count):
            item_barcode = self.ui.tableWidget_stock_list.item(row, 0)
            item_name = self.ui.tableWidget_stock_list.item(row, 1)
            
            if item_barcode and item_name:
                barcode_text = item_barcode.text().lower()
                name_text = item_name.text().lower()
                
                if (search_text == "") or (search_text in barcode_text) or (search_text in name_text):
                    self.ui.tableWidget_stock_list.setRowHidden(row, False)
                    match_count += 1
                else:
                    self.ui.tableWidget_stock_list.setRowHidden(row, True)
        

        if match_count == 0 and search_text != "":
            QMessageBox.information(self, "Sonuç", "Aradığınız kriterlere uygun ürün bulunamadı.")

    def auto_reset_search(self):
        if self.ui.lineEdit_search_barcode.text().strip() == "":
            for row in range(self.ui.tableWidget_stock_list.rowCount()):
                self.ui.tableWidget_stock_list.setRowHidden(row, False)

    def save_stock_changes(self):
        if not self.db.connected:
            QMessageBox.warning(self, "Hata", "Veritabanı bağlantısı yok.")
            return

        reply = QMessageBox.question(self, 'Onay', 
            "Stok değişikliklerini kaydetmek istiyor musunuz?", 
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            count = 0
            for row in range(self.ui.tableWidget_stock_list.rowCount()):
                if self.ui.tableWidget_stock_list.isRowHidden(row):
                    continue 

                try:
                    barcode = self.ui.tableWidget_stock_list.item(row, 0).text()
                    old_stock = int(self.ui.tableWidget_stock_list.item(row, 2).text())
                    
                    item_new_stock = self.ui.tableWidget_stock_list.item(row, 3)
                    if not item_new_stock: continue
                    
                    new_stock = int(item_new_stock.text())
                        
                    if new_stock != old_stock:
                        self.db.products.update_one(
                            {"barcode": barcode},
                            {"$set": {"stock_quantity": new_stock}} 
                        )
                        count += 1
                except ValueError:
                    continue 
            
            QMessageBox.information(self, "Bilgi", f"{count} ürün başarıyla güncellendi.")
            self.load_products() 
            self.ui.lineEdit_search_barcode.clear()