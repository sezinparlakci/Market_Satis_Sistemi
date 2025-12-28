from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ProductOperationsMenu(object):
    def setupUi(self, ProductOperationsMenu):
        ProductOperationsMenu.setObjectName("ProductOperationsMenu")
        ProductOperationsMenu.resize(550, 650)
        ProductOperationsMenu.setStyleSheet("\n"
"    QDialog { background-color: #F8F9FA;\n"
"}\n"
"    \n"
"    QPushButton { \n"
"        border: 1px solid #007bff;\n"
"/* Mavi Çerçeve */\n"
"        border-radius: 10px; \n"
"        padding: 15px; \n"
"        font-weight: bold; \n"
"        font-size: 16pt;\n"
"color: #343A40; \n"
"        background-color: #FFFFFF;\n"
"        text-align: left; \n"
"        min-height: 50px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #E9ECEF;\n"
"}\n"
"    /* Ana Butonların Stili */\n"
"    #btn_add_product {\n"
"        background-color: #E6F7FF;\n"
"/* Açık Mavi */\n"
"        border-left: 8px solid #007bff;\n"
"/* Sol Tarafta Kalın Çizgi */\n"
"    }\n"
"    #btn_exit {\n"
"        background-color: #6c757d;\n"
"/* Gri */\n"
"        color: white; \n"
"        border: none;\n"
"        border-radius: 10px;\n"
"        font-size: 18pt;\n"
"}\n"
"   ")
        self.verticalLayout_main = QtWidgets.QVBoxLayout(ProductOperationsMenu)
        self.verticalLayout_main.setContentsMargins(20,20,20,20)
        self.verticalLayout_main.setSpacing(15)
        self.verticalLayout_main.setObjectName("verticalLayout_main")
        self.label_title = QtWidgets.QLabel(ProductOperationsMenu)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setStyleSheet("font-size: 26pt; font-weight: bold; color: #007bff;\n"
"margin-bottom: 10px;")
        self.label_title.setObjectName("label_title")
        self.verticalLayout_main.addWidget(self.label_title)
        self.btn_add_product = QtWidgets.QPushButton(ProductOperationsMenu)
        self.btn_add_product.setObjectName("btn_add_product")
        self.verticalLayout_main.addWidget(self.btn_add_product)
        self.btn_edit_delete_product = QtWidgets.QPushButton(ProductOperationsMenu)
        self.btn_edit_delete_product.setObjectName("btn_edit_delete_product")
        self.verticalLayout_main.addWidget(self.btn_edit_delete_product)
        self.btn_stock_adjustment = QtWidgets.QPushButton(ProductOperationsMenu)
        self.btn_stock_adjustment.setObjectName("btn_stock_adjustment")
        self.verticalLayout_main.addWidget(self.btn_stock_adjustment)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_main.addItem(spacerItem)
        self.btn_exit = QtWidgets.QPushButton(ProductOperationsMenu)
        self.btn_exit.setMinimumSize(QtCore.QSize(0, 60))
        self.btn_exit.setObjectName("btn_exit")
        self.verticalLayout_main.addWidget(self.btn_exit)
        self.retranslateUi(ProductOperationsMenu)
        QtCore.QMetaObject.connectSlotsByName(ProductOperationsMenu)
    def retranslateUi(self, ProductOperationsMenu):
        _translate = QtCore.QCoreApplication.translate
        ProductOperationsMenu.setWindowTitle(_translate("ProductOperationsMenu", "Ürün Yönetimi Alt Menüsü"))
        self.label_title.setText(_translate("ProductOperationsMenu", "ÜRÜN İŞLEMLERİ"))
        self.btn_add_product.setText(_translate("ProductOperationsMenu", "1. YENİ ÜRÜN EKLE"))
        self.btn_edit_delete_product.setText(_translate("ProductOperationsMenu", "2. ÜRÜN DÜZENLE / SİL"))
        self.btn_stock_adjustment.setText(_translate("ProductOperationsMenu", "3. STOK GİRİŞİ / DÜZELTME"))
        self.btn_exit.setText(_translate("ProductOperationsMenu", "GERİ"))
