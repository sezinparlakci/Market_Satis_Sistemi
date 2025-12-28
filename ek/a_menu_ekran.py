from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui.ui_menu_ekran import Ui_MenuDialog 
from ek.a_urun_kontrolu import UrunIslemleriMenuUygulamasi 
from ek.a_rapor_ekrani import RaporUygulamasi
from ui.ui_son_satis_ekran import Ui_LastSaleScreen
from ui.ui_ayarlar import Ui_Settings
from ui.ui_kullanim import Ui_HelpScreen

class SonSatisUygulamasi(QDialog):
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.ui = Ui_LastSaleScreen()
        self.ui.setupUi(self)
        self.db = db
        self.setup_connections()
        self.populate_table_with_sales_data()

    def setup_connections(self):
        self.ui.btn_close.clicked.connect(self.close)

    def populate_table_with_sales_data(self):
        sales_data = self.db.get_last_sales()
        
        self.ui.tableWidget_sales.setRowCount(len(sales_data))
        for row, sale in enumerate(sales_data):
            no = str(sale.get("_id", "")) 
            date = sale.get("date").strftime("%Y-%m-%d %H:%M") if sale.get("date") else "N/A"
            total = sale.get("total_amount", 0.0)
            payment = sale.get("payment_type", "Bilinmiyor")
            status = sale.get("status", "Tamamlandi")
            
            self.ui.tableWidget_sales.setItem(row, 0, QTableWidgetItem(no))
            self.ui.tableWidget_sales.setItem(row, 1, QTableWidgetItem(date))
            self.ui.tableWidget_sales.setItem(row, 2, QTableWidgetItem(f"₺ {total:.2f}"))
            self.ui.tableWidget_sales.setItem(row, 3, QTableWidgetItem(payment))
            self.ui.tableWidget_sales.setItem(row, 4, QTableWidgetItem(status))
    
    def search_sales(self, text):
        for i in range(self.ui.tableWidget_sales.rowCount()):
            match = False
            for j in range(self.ui.tableWidget_sales.columnCount()):
                item = self.ui.tableWidget_sales.item(i, j)
                if item and text.lower() in item.text().lower():
                    match = True
                    break
            self.ui.tableWidget_sales.setRowHidden(i, not match)
            
class MenuEkranUygulamasi(QDialog):
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.db = db
        self.main_app_parent = parent 
        self.menu_ui = Ui_MenuDialog()
        self.menu_ui.setupUi(self)
        self.setup_connections()
        self.showMaximized()

    def setup_connections(self):
        self.menu_ui.btn_product_operations.clicked.connect(self.show_product_operations_menu)
        self.menu_ui.btn_last_sale.clicked.connect(self.show_last_sale_screen)
        self.menu_ui.btn_settings.clicked.connect(self.show_settings_screen)
        self.menu_ui.btn_kullanim.clicked.connect(self.show_kullanim_screen)
        self.menu_ui.btn_exit.clicked.connect(self.close) 
        self.menu_ui.btn_reports.clicked.connect(self.show_reports_screen)
    
    def show_product_operations_menu(self):
        try:
            self.product_operations_window = UrunIslemleriMenuUygulamasi(self.db, self)
            self.product_operations_window.exec_()
        except Exception as e:
            QMessageBox.critical(self, "Hata")
    def show_reports_screen(self):
        self.report_window = RaporUygulamasi(self.db, self)
        self.report_window.exec_()
    def show_last_sale_screen(self):
        try:
            self.last_sale_window = SonSatisUygulamasi(self.db, self)
            self.last_sale_window.exec_()
        except Exception as e:
            QMessageBox.critical(self, "Hata")

    def show_settings_screen(self):
        try:
            self.settings_window = SistemAyarlariUygulamasi(self.db, self)
            self.settings_window.exec_()
        except Exception as e:
            QMessageBox.critical(self, "Hata")

    def show_kullanim_screen(self):
        try:
            self.calculator_window = YardimUygulamasi(self)
            self.calculator_window.exec_()
        except Exception as e:
            QMessageBox.critical(self, "Hata")


class SistemAyarlariUygulamasi(QDialog):
    def __init__(self, db, parent=None):
        super(SistemAyarlariUygulamasi, self).__init__(parent)
        self.db = db
        
        self.ui = Ui_Settings()
        self.ui.setupUi(self)


    
        self.ui.lblStatus.setText(f"Veritabanı: {'✅ Bağlı' if self.db.connected else '❌ Hatalı'}")
        self.refresh_user_list()
        
        self.ui.btnClose.clicked.connect(self.close)
        self.ui.btnUpdatePass.clicked.connect(self.update_password)
        self.ui.btnAddUser.clicked.connect(self.add_new_user)
        self.ui.btnDeleteUser.clicked.connect(self.delete_selected_user)

    def refresh_user_list(self):
        self.ui.listUsers.clear()
        users = self.db.get_all_users()
        for u in users:
            self.ui.listUsers.addItem(u)

    def add_new_user(self):
        username = self.ui.lineNewUsername.text().strip()
        password = self.ui.lineNewUserPass.text().strip()
        
        if not username or not password:
            QMessageBox.warning(self, "Hata", "Kullanıcı adı ve şifre boş olamaz.")
            return

        success, message = self.db.add_user(username, password)
        if success:
            QMessageBox.information(self, "Başarılı", message)
            self.ui.lineNewUsername.clear()
            self.ui.lineNewUserPass.clear()
            self.refresh_user_list()
        else:
            QMessageBox.warning(self, "Hata", message)

    def delete_selected_user(self):
        selected_item = self.ui.listUsers.currentItem()
        if not selected_item:
            QMessageBox.warning(self, "Uyarı", "Lütfen silinecek kullanıcıyı seçin.")
            return
            
        username = selected_item.text()
        
        if username == "admin":
            QMessageBox.warning(self, "Hata", "Admin kullanıcısı silinemez!")
            return

        confirm = QMessageBox.question(self, "Onay", f"{username} kullanıcısını silmek istediğinize emin misiniz?", 
                                               QMessageBox.Yes | QMessageBox.No)
        
        if confirm == QMessageBox.Yes:
            if self.db.delete_user(username):
                self.refresh_user_list()
                QMessageBox.information(self, "Bilgi", "Kullanıcı silindi.")
            else:
                QMessageBox.warning(self, "Hata", "Silme işlemi başarısız.")

    def update_password(self):
        old = self.ui.lineOldPass.text()
        new = self.ui.lineNewPass.text()
        
        if not old or not new:
             QMessageBox.warning(self, "Uyarı", "Lütfen alanları doldurunuz.")
             return

        if self.db.update_password("admin", old, new):
            QMessageBox.information(self, "Başarılı", "Admin şifresi güncellendi.")
            self.ui.lineOldPass.clear()
            self.ui.lineNewPass.clear()
        else:
            QMessageBox.warning(self, "Hata", "Eski şifre yanlış veya veritabanı hatası.")

class YardimUygulamasi(QDialog):
    def __init__(self, parent=None):
        super(YardimUygulamasi, self).__init__(parent)
        self.ui = Ui_HelpScreen()
        self.ui.setupUi(self)


        self.help_data = {
            "1. Sisteme Giriş": """
                <h3>Sisteme Nasıl Giriş Yapılır?</h3>
                <p>Programı açtığınızda karşınıza gelen ekranda kullanıcı adı ve şifrenizi giriniz.</p>
                <ul>
                    <li><b>Varsayılan Yönetici:</b> admin / 123</li>
                </ul>
            """,
            
            "2. Satış Ekranı Kullanımı": """
                <h3>Satış Yapma Adımları</h3>
                <ol>
                    <li><b>Barkod Okutma:</b> Ürün barkodunu okutun veya elle girip Enter'a basın.</li>
                    <li><b>Miktar:</b> Aynı üründen birden fazla varsa tekrar okutabilir veya adet girebilirsiniz.</li>
                    <li><b>Sepetten Çıkarma:</b> Yanlış eklenen ürünü tablodan seçip 'Sil' butonuna basın.</li>
                    <li><b>Ödeme:</b> Sağ taraftaki 'Nakit' veya 'Kredi Kartı' butonları ile satışı tamamlayın.</li>
                </ol>
            """,
            
            "3. Raporlar Ekranı": """
                <h3>Raporları Anlama</h3>
                <p>Bu ekranda işletmenizin durumunu analiz edebilirsiniz.</p>
                <ul>
                    <li><b>Günlük Rapor:</b> Hangi gün ne kadar ciro ve kâr yaptığınızı gösterir.</li>
                </ul>
                <p style='color:red;'>Not: Kâr/Zarar durumu eksiye düşerse kırmızı renk ile uyarılırsınız.</p>
            """,
            
            "4. Stok ve Ürün Ekleme": """
                <h3>Yeni Ürün Nasıl Eklenir?</h3>
                <p>Veritabanına ürün eklemek için ürün işlemleri kısmını kullanmalısınız..</p>
                <p><b>Dikkat Edilmesi Gerekenler:</b></p>
                <ul>
                    <li>Barkod benzersiz olmalıdır.</li>
                    <li>Alış Fiyatı (Maliyet) girilmesi kâr hesaplaması için kritiktir.</li>
                </ul>
            """,
            
            "5. Ayarlar ve Şifre Değiştirme": """
                <h3>Şifre Değiştirme</h3>
                <p>Ayarlar menüsünden  Şifre sekmesine gelin.</p>
                <p>Eski şifrenizi ve yeni şifrenizi girerek 'Güncelle' butonuna basınız.</p>
                <br>
                <h3>Kullanıcı Yönetimi</h3>
                <p>Yeni personel eklemek veya eski personeli silmek için 'Kullanıcı Yönetimi' sekmesini kullanın.</p>
            """
        }

        self.setup_connections()
        self.load_topics()

    def setup_connections(self):
        self.ui.btnClose.clicked.connect(self.close)
        self.ui.listTopics.currentItemChanged.connect(self.display_topic)

    def load_topics(self):
        """Konu başlıklarını listeye ekler"""
        self.ui.listTopics.clear()
        for topic in self.help_data.keys():
            self.ui.listTopics.addItem(topic)
        
        self.ui.listTopics.setCurrentRow(0)

    def display_topic(self, current_item, previous_item):
        if not current_item:
            return
            
        topic_title = current_item.text()
        content = self.help_data.get(topic_title, "İçerik bulunamadı.")        
        self.ui.textBrowser.setHtml(content)