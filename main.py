import sys
from PyQt5.QtWidgets import * 
from datetime import datetime
from ek.a_veri_tabani import DatabaseManager
from ek.a_menu_ekran import MenuEkranUygulamasi 
from ui.ui_ana_ekran import Ui_Dialog as Ui_AnaEkran 
from ek.a_kamera_modulu import KameraThread
from ui.ui_login import Ui_LoginScreen  


class LoginScreen(QDialog):
    def __init__(self, db_manager):
        super().__init__()
        self.db = db_manager
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self)
        self.ui.btnLogin.clicked.connect(self.handle_login)
        self.ui.linePassword.returnPressed.connect(self.handle_login)

    def handle_login(self):
        username = self.ui.lineUsername.text()
        password = self.ui.linePassword.text()

        if not username or not password:
            QMessageBox.warning(self, "Uyarı", "Lütfen kullanıcı adı ve şifre giriniz.")
            return

        if self.db.check_login(username, password):
            self.accept() 
        else:
            QMessageBox.warning(self, "Hata", "Hatalı kullanıcı adı veya şifre!")
            self.ui.linePassword.clear()


class AnaEkranUygulamasi(QDialog):
    def __init__(self):
        super().__init__()
        self.db = DatabaseManager() 
        self.ana_ekran_ui = Ui_AnaEkran() 
        self.ana_ekran_ui.setupUi(self)
        self.showMaximized()

        
        self.mevcut_sepet = {} 
        self.setup_connections()
        self.sepet_tablosu() 
        
        self.camera_thread = KameraThread() 
        #barkod okutulduğunda fonksyion tetikle
        self.camera_thread.barcode_scanned.connect(self.handle_scanned_barcode) 
        self.camera_thread.start() 

    def setup_connections(self):
        self.ana_ekran_ui.pushButton_menu.clicked.connect(self.menu_goster)
        self.ana_ekran_ui.pushButton_cash.clicked.connect(lambda: self.odeme_yontemi("Nakit"))
        self.ana_ekran_ui.pushButton_card.clicked.connect(lambda: self.odeme_yontemi("Kart"))
        self.ana_ekran_ui.pushButton_return.clicked.connect(self.iade_et)
        self.setup_keypad_connections()
        self.ana_ekran_ui.btn_enter.clicked.connect(self.sepete_ekleme)
        self.ana_ekran_ui.lineEdit_barcode.returnPressed.connect(self.sepete_ekleme) 
        quick_buttons = {
                    self.ana_ekran_ui.ekmek:    "1",  
                    self.ana_ekran_ui.sakiz:    "78", 
                    self.ana_ekran_ui.lolipop:  "869000000003",
                    self.ana_ekran_ui.pil_2li:  "869000000004",
                    self.ana_ekran_ui.pil_4lu:  "869000000005",
                    self.ana_ekran_ui.vb:       "869000000006",  
                    self.ana_ekran_ui.placeholder_7:  "869000000007",
                    self.ana_ekran_ui.placeholder_8:  "869000000008",
                    self.ana_ekran_ui.placeholder_9:  "869000000009",
                    self.ana_ekran_ui.placeholder_10: "869000000010",
                    self.ana_ekran_ui.placeholder_11: "869000000011",
                    self.ana_ekran_ui.placeholder_12: "869000000012",
                    self.ana_ekran_ui.placeholder_13: "869000000013",
                    self.ana_ekran_ui.placeholder_14: "869000000014",
                    self.ana_ekran_ui.placeholder_15: "869000000015",
                    self.ana_ekran_ui.placeholder_16: "869000000016",
                    self.ana_ekran_ui.placeholder_17: "869000000017",
                    self.ana_ekran_ui.placeholder_18: "869000000018bi ",

                }

        for btn, barcode in quick_buttons.items():
 
            try:
                btn.clicked.connect(lambda checked, b=barcode: self.buton_sepete_ekleme(b))
            except Exception as e:
                print(f"Buton bağlama hatası: {e}")
        if hasattr(self.ana_ekran_ui, 'btn_ekmek'):
            self.ana_ekran_ui.btn_ekmek.clicked.connect(lambda: self.buton_sepete_ekleme("1234567890123"))

    def sepet_tablosu(self):
        table = self.ana_ekran_ui.tableWidget_sepet 
        #tablo temizleme 
        table.setRowCount(0)
        total_amount = 0.0     
        for idx, (barcode, item) in enumerate(self.mevcut_sepet.items()):
            table.insertRow(idx)
            table.setItem(idx, 0, QTableWidgetItem(item.get('barcode', '')))      
            table.setItem(idx, 1, QTableWidgetItem(item['name']))                 
            table.setItem(idx, 2, QTableWidgetItem(f"{item['quantity']}"))        
            table.setItem(idx, 3, QTableWidgetItem(f"₺ {item['price']:.2f}"))     
            total_amount += item['total']
        self.ana_ekran_ui.label_total_value.setText(f"₺ {total_amount:.2f}")

    def odeme_yontemi(self, payment_type):
        if not self.mevcut_sepet:
            QMessageBox.warning(self, "Hata", "Sepet boş!")
            return

        total_text = self.ana_ekran_ui.label_total_value.text()
        total = float(total_text.replace('₺', '').replace(',', '.').strip())
            
        sale_data = {
            "items": list(self.mevcut_sepet.values()), 
            "total_amount": total,
            "payment_type": payment_type,
            "status": "Tamamlandi",
            "created_at": datetime.now() 
        }
        
        if self.db.satis_kaydi(sale_data): 
            QMessageBox.information(self, "Başarılı", f"Satış ({payment_type}) tamamlandı ve stok güncellendi.")
            self.mevcut_sepet = {}
            self.sepet_tablosu()

    def iade_et(self):
        if not self.mevcut_sepet:
            QMessageBox.warning(self, "Hata", "İade için sepete ürün ekleyin!")
            return

        confirm = QMessageBox.question(self, "İade Onayı", "Seçili ürünleri iade etmek istiyor musunuz?", 
                                               QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            total_text = self.ana_ekran_ui.label_total_value.text()
            total = float(total_text.replace('₺', '').replace(',', '.').strip())
            
            return_data = {
                "items": list(self.mevcut_sepet.values()),
                "total_amount": total,
                "payment_type": "IADE"
            }
            if self.db.log_return(return_data):
                QMessageBox.information(self, "Başarılı", "İade işlemi tamamlandı, ürünler stoğa geri eklendi.")
                self.mevcut_sepet = {}
                self.sepet_tablosu()

    def sepete_ekleme(self):
        barcode = self.ana_ekran_ui.lineEdit_barcode.text().strip()
        miktar = self.ana_ekran_ui.spinBox_quantity.value()
        if not barcode: return
            
        product = self.db.find_product_by_barcode(barcode)
        if product:
            price = product.get('sale_price', 0.0)
            if barcode in self.mevcut_sepet:
                self.mevcut_sepet[barcode]['quantity'] += miktar
                self.mevcut_sepet[barcode]['total'] = self.mevcut_sepet[barcode]['quantity'] * price
            else:
                self.mevcut_sepet[barcode] = {
                    'name': product.get('name'), 'quantity': miktar, 
                    'price': price, 'total': miktar * price, 'barcode': barcode 
                }
            self.sepet_tablosu()
            self.ana_ekran_ui.lineEdit_barcode.clear()
            self.ana_ekran_ui.spinBox_quantity.setValue(1)
        else:
            QMessageBox.warning(self, "Hata", "Urun bulunamadi.")

    def setup_keypad_connections(self):
        for i in range(10):
            button_name = f"btn_large_{i}" 
            button = getattr(self.ana_ekran_ui, button_name, None)
            if button:
                button.clicked.connect(lambda checked=False, text=str(i): self.digit_input(text))
        self.ana_ekran_ui.btn_large_dot.clicked.connect(lambda: self.digit_input(".")) 
        self.ana_ekran_ui.btn_large_clear.clicked.connect(self.clear_input) 
        self.ana_ekran_ui.btn_large_back.clicked.connect(self.backspace_input) 
        self.ana_ekran_ui.btn_large_delete_item.clicked.connect(self.sepetten_silme)

    def handle_scanned_barcode(self, barcode):
        self.ana_ekran_ui.lineEdit_barcode.setText(barcode)
        self.sepete_ekleme()

    def digit_input(self, text):
        self.ana_ekran_ui.lineEdit_barcode.setText(self.ana_ekran_ui.lineEdit_barcode.text() + text)
        
    def clear_input(self): 
        self.ana_ekran_ui.lineEdit_barcode.clear()
        
    def backspace_input(self): 
        self.ana_ekran_ui.lineEdit_barcode.backspace()
    
    def sepetten_silme(self):
        table = self.ana_ekran_ui.tableWidget_sepet
        row = table.currentRow()
        if row >= 0:
            barcode = table.item(row, 0).text()
            if barcode in self.mevcut_sepet:
                del self.mevcut_sepet[barcode]
                self.sepet_tablosu()

    def buton_sepete_ekleme(self, barcode):
        self.ana_ekran_ui.lineEdit_barcode.setText(barcode)
        self.sepete_ekleme()

    def menu_goster(self):
        self.menu_window = MenuEkranUygulamasi(self.db, self)
        self.menu_window.exec_()

    def closeEvent(self, event):
        self.camera_thread.stop()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    db = DatabaseManager()
    if hasattr(db, 'create_default_admin'):
        db.create_default_admin()
    
    login = LoginScreen(db)
    
    if login.exec_() == QDialog.Accepted:
        window = AnaEkranUygulamasi() 
        window.show()
        sys.exit(app.exec_())
    else:
        sys.exit()


