from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MenuDialog(object):
    def setupUi(self, MenuDialog):
        MenuDialog.setObjectName("MenuDialog")
        MenuDialog.resize(500, 750)
        MenuDialog.setStyleSheet("\n"
"    /* Genel Stil */\n"
"    QDialog { background-color: #F8F9FA; } /* Açık Gri Arkaplan */\n"
"    \n"
"    /* Tüm Menü Butonları için Temel Stil */\n"
"    QPushButton { \n"
"        border: 1px solid #CED4DA; /* Hafif Çerçeve */\n"
"        border-radius: 10px; \n"
"        padding: 20px; \n"
"        font-weight: bold; \n"
"        font-size: 16pt;\n"
"        color: #343A40; /* Koyu Gri Metin */\n"
"        background-color: #FFFFFF; /* Beyaz Butonlar */\n"
"        text-align: left; /* Metni sola hizala */\n"
"        min-height: 40px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #E9ECEF; /* Hafif Hover Efekti */\n"
"    }\n"
"   ")
        self.verticalLayout = QtWidgets.QVBoxLayout(MenuDialog)
        self.verticalLayout.setContentsMargins(20,20,20,20)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_menu_title = QtWidgets.QLabel(MenuDialog)
        self.label_menu_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_menu_title.setStyleSheet("font-size: 24pt; font-weight: bold; color: #495057; margin-bottom: 10px;")
        self.label_menu_title.setObjectName("label_menu_title")
        self.verticalLayout.addWidget(self.label_menu_title)
        self.btn_product_operations = QtWidgets.QPushButton(MenuDialog)
        self.btn_product_operations.setStyleSheet("\n"
"       background-color: #E6F7FF; /* Açık Mavi */\n"
"       border: 1px solid #91D5FF;\n"
"       font-size: 16pt;\n"
"      ")
        self.btn_product_operations.setObjectName("btn_product_operations")
        self.verticalLayout.addWidget(self.btn_product_operations)
        self.btn_reports = QtWidgets.QPushButton(MenuDialog)
        self.btn_reports.setObjectName("btn_reports")
        self.verticalLayout.addWidget(self.btn_reports)
        self.btn_last_sale = QtWidgets.QPushButton(MenuDialog)
        self.btn_last_sale.setObjectName("btn_last_sale")
        self.verticalLayout.addWidget(self.btn_last_sale)
        self.btn_settings = QtWidgets.QPushButton(MenuDialog)
        self.btn_settings.setObjectName("btn_settings")
        self.verticalLayout.addWidget(self.btn_settings)
        self.btn_kullanim = QtWidgets.QPushButton(MenuDialog)
        self.btn_kullanim.setObjectName("btn_kullanim")
        self.verticalLayout.addWidget(self.btn_kullanim)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btn_exit = QtWidgets.QPushButton(MenuDialog)
        self.btn_exit.setMinimumSize(QtCore.QSize(0, 60))
        self.btn_exit.setStyleSheet("\n"
"       background-color: #DC3545; /* Kırmızı */\n"
"       color: white; \n"
"       font-weight: bold; \n"
"       font-size: 18pt;\n"
"       border: none;\n"
"       border-radius: 10px;\n"
"      ")
        self.btn_exit.setObjectName("btn_exit")
        self.verticalLayout.addWidget(self.btn_exit)
        self.retranslateUi(MenuDialog)
        QtCore.QMetaObject.connectSlotsByName(MenuDialog)
    def retranslateUi(self, MenuDialog):
        _translate = QtCore.QCoreApplication.translate
        MenuDialog.setWindowTitle(_translate("MenuDialog", "Yönetim Menüsü"))
        self.label_menu_title.setText(_translate("MenuDialog", "YÖNETİM VE İŞLEMLER"))
        self.btn_product_operations.setText(_translate("MenuDialog", "1. ÜRÜN İŞLEMLERİ (Ekle/Düzenle/Stok)"))
        self.btn_reports.setText(_translate("MenuDialog", "2. RAPORLAR"))
        self.btn_last_sale.setText(_translate("MenuDialog", "3. SON SATIŞ"))
        self.btn_settings.setText(_translate("MenuDialog", "4. SİSTEM AYARLARI"))
        self.btn_kullanim.setText(_translate("MenuDialog", "5. KULLANIM KILAVUZU"))
        self.btn_exit.setText(_translate("MenuDialog", "ANA EKRANA DÖN"))