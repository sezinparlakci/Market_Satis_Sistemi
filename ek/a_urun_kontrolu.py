from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from datetime import datetime 
from ui.ui_urun_ekran import Ui_ProductOperationsMenu 
from ui.ui_urun_ekleme import Ui_AddProductDialog 
from ui.ui_urun_duzenleme import Ui_EditProductListDialog 
from ek.a_stok_durumu import StokDuzenlemeUygulamasi 

class UrunEklemeUygulamasi(QDialog):
    def __init__(self, db, parent=None, edit_data=None): 
        super().__init__(parent)
        self.db = db
        self.edit_data = edit_data
        self.ui = Ui_AddProductDialog() 
        self.ui.setupUi(self)

        
        if self.edit_data:
            self.setWindowTitle("Ürün Düzenle")
            self.ui.btn_save.setText("Güncelle")
            self.ui.lineEdit_barcode.setEnabled(False) # Barkod düzenlenemez
            self.fill_form()
        else:
            self.setWindowTitle("Yeni Ürün Ekle")

        self.ui.btn_cancel.clicked.connect(self.close)
        self.ui.btn_save.clicked.connect(self.save_product)

    def fill_form(self):
        self.ui.lineEdit_barcode.setText(str(self.edit_data.get('barcode', '')))
        self.ui.lineEdit_name.setText(self.edit_data.get('name', ''))
        self.ui.spinBox_stock.setValue(self.edit_data.get('stock_quantity', 0))
        self.ui.doubleSpinBox_purchase_price.setValue(self.edit_data.get('purchase_price', 0.0))
        self.ui.doubleSpinBox_sale_price.setValue(self.edit_data.get('sale_price', 0.0))

    def save_product(self):
        barcode = self.ui.lineEdit_barcode.text().strip()
        name = self.ui.lineEdit_name.text().strip()
        
        if not barcode or not name:
            QMessageBox.warning(self, "Hata", "Barkod ve isim boş olamaz!")
            return

        if not self.edit_data:
            if self.db.find_product_by_name(name):
                QMessageBox.warning(self, "Hata", f"'{name}' zaten kayıtlı!")
                return
            if self.db.find_product_by_barcode(barcode):
                QMessageBox.warning(self, "Hata", f"'{barcode}' zaten kullanımda!")
                return

        data = {
            'barcode': barcode,
            'name': name,
            'stock_quantity': self.ui.spinBox_stock.value(),
            'purchase_price': self.ui.doubleSpinBox_purchase_price.value(),
            'sale_price': self.ui.doubleSpinBox_sale_price.value(),
            'last_updated': datetime.now()
        }

        try:
            success = False
            if self.edit_data:
                success = self.db.update_product_by_barcode(barcode, data)
                msg = "Ürün güncellendi."
            else:
                success = self.db.insert_product(data)
                msg = "Yeni ürün eklendi."

            if success:
                QMessageBox.information(self, "Başarılı", msg)
                self.accept()
            else:
                QMessageBox.critical(self, "Hata", "Veritabanı işlem hatası.")
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Kaydetme hatası: {str(e)}")

class UrunDuzenlemeUygulamasi(QDialog):
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.db = db
        self.ui = Ui_EditProductListDialog() 
        self.ui.setupUi(self)
        self.setWindowTitle("Ürün Yönetimi")

        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_search.clicked.connect(self.search_products)
        self.ui.lineEdit_search.returnPressed.connect(self.search_products)
        self.ui.lineEdit_search.textChanged.connect(self.auto_reset)
        
        self.load_product_list()

    def auto_reset(self):
        if not self.ui.lineEdit_search.text().strip():
            self.load_product_list()

    def search_products(self):
        search_text = self.ui.lineEdit_search.text().strip().lower()
        if not search_text:
            self.load_product_list()
            return

        try:
            all_products = self.db.get_all_products()
            # Python tarafında basit filtreleme
            filtered_products = [
                p for p in all_products 
                if search_text in str(p.get('name', '')).lower() or search_text in str(p.get('barcode', '')).lower()
            ]
            self.fill_table(filtered_products)
        except Exception as e:
            print(f"Arama hatası: {e}")

    def load_product_list(self):
        try:
            products = self.db.get_all_products()
            self.fill_table(products)
        except Exception as e:
            print(f"Ürün listesi hatası: {e}")

    def fill_table(self, products):
        table = self.ui.tableWidget_products
        table.setRowCount(0)
        
        # Dinamik buton stili (Tek sefer tanımlandı)
        btn_style = "QPushButton { border: none; background: transparent; font-weight: bold; font-size: 13px; margin: 0px; }"
        
        for row, p in enumerate(products):
            table.insertRow(row)
            barcode = str(p.get('barcode', ''))
            
            table.setItem(row, 0, QTableWidgetItem(barcode))
            table.setItem(row, 1, QTableWidgetItem(p.get('name', '')))
            table.setItem(row, 2, QTableWidgetItem(f"{p.get('sale_price', 0.0):.2f} ₺"))
            table.setItem(row, 3, QTableWidgetItem(str(p.get('stock_quantity', 0))))
            
            last_up = p.get('last_updated')
            date_str = last_up.strftime("%d.%m.%Y") if isinstance(last_up, datetime) else "-"
            table.setItem(row, 4, QTableWidgetItem(date_str))

            container = QWidget()
            layout = QHBoxLayout(container)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(10)

            btn_edit = QPushButton("Düzenle")
            btn_edit.setStyleSheet(btn_style + " color: #007bff;") 
            btn_edit.setCursor(Qt.PointingHandCursor)
            btn_edit.clicked.connect(lambda _, b=barcode: self.edit_action(b))

            btn_del = QPushButton("Sil")
            btn_del.setStyleSheet(btn_style + " color: #dc3545;") 
            btn_del.setCursor(Qt.PointingHandCursor)
            btn_del.clicked.connect(lambda _, b=barcode: self.delete_action(b))

            layout.addWidget(btn_edit)
            layout.addWidget(btn_del)
            layout.setAlignment(Qt.AlignCenter)
            
            table.setCellWidget(row, 5, container)

    def edit_action(self, barcode):
        product_data = self.db.find_product_by_barcode(barcode)
        if product_data:
            dialog = UrunEklemeUygulamasi(self.db, self, edit_data=product_data)
            if dialog.exec_(): 
                self.load_product_list()

    def delete_action(self, barcode):
        reply = QMessageBox.question(self, "Sil", "Bu ürünü silmek istediğinize emin misiniz?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            if self.db.delete_product_by_barcode(barcode): 
                self.load_product_list()

class UrunIslemleriMenuUygulamasi(QDialog):
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.db = db
        self.ui = Ui_ProductOperationsMenu() 
        self.ui.setupUi(self)
        self.showMaximized()

        
        self.ui.btn_add_product.clicked.connect(lambda: UrunEklemeUygulamasi(self.db, self).exec_())
        self.ui.btn_edit_delete_product.clicked.connect(lambda: UrunDuzenlemeUygulamasi(self.db, self).exec_())
        self.ui.btn_stock_adjustment.clicked.connect(lambda: StokDuzenlemeUygulamasi(self.db, self).exec_())
        self.ui.btn_exit.clicked.connect(self.close)