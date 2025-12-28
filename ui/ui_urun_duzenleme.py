from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditProductListDialog(object):
    def setupUi(self, EditProductListDialog):
        EditProductListDialog.setObjectName("EditProductListDialog")
        EditProductListDialog.resize(1000, 700)       
        EditProductListDialog.setStyleSheet("\n"
"    QDialog { background-color: #F8F9FA; }\n"
"    \n"
"    /* Başlık Stili */\n"
"    QLabel#label_title { \n"
"        font-size: 28pt; \n"
"        font-weight: bold; \n"
"        color: #DC3545; /* Kırmızı/Uyarı Rengi */\n"
"        margin-bottom: 10px;\n"
"    }\n"
"    \n"
"    /* Arama Çubuğu Stili */\n"
"    QLineEdit {\n"
"        padding: 12px;\n"
"        border: 2px solid #007bff; /* Mavi Çerçeve */\n"
"        border-radius: 8px;\n"
"        font-size: 16pt;\n"
"        background-color: white;\n"
"    }\n"
"    \n"
"    /* Tablo Stili */\n"
"    QTableWidget {\n"
"        border: 1px solid #CED4DA;\n"
"        border-radius: 8px;\n"
"        font-size: 12pt; \n"
"        alternate-background-color: #F0F0F0; /* Okunurluğu Artırır */\n"
"    }\n"
"    QHeaderView::section { \n"
"        background-color: #343A40; /* Koyu Başlık */\n"
"        color: white; \n"
"        font-weight: bold; \n"
"        font-size: 12pt; \n"
"        padding: 8px; \n"
"        border: none;\n"
"    }\n"
"\n"
"    /* Butonlar Stili */\n"
"    QPushButton {\n"
"        border-radius: 6px;\n"
"        padding: 10px 15px;\n"
"        font-weight: bold;\n"
"        font-size: 12pt;\n"
"    }\n"
"   ")
        self.verticalLayout_main = QtWidgets.QVBoxLayout(EditProductListDialog)
        self.verticalLayout_main.setContentsMargins(30,30,30,30)
        self.verticalLayout_main.setSpacing(20)
        self.verticalLayout_main.setObjectName("verticalLayout_main")        
        self.label_title = QtWidgets.QLabel(EditProductListDialog)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_main.addWidget(self.label_title)        
        self.horizontalLayout_search = QtWidgets.QHBoxLayout()
        self.horizontalLayout_search.setSpacing(10)
        self.horizontalLayout_search.setObjectName("horizontalLayout_search")    
        self.lineEdit_search = QtWidgets.QLineEdit(EditProductListDialog)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.horizontalLayout_search.addWidget(self.lineEdit_search)       
        self.btn_search = QtWidgets.QPushButton(EditProductListDialog)
        self.btn_search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_search.setStyleSheet("background-color: #17A2B8; color: white; font-size: 14pt; padding: 10px 30px;")
        self.btn_search.setObjectName("btn_search")
        self.horizontalLayout_search.addWidget(self.btn_search)       
        self.verticalLayout_main.addLayout(self.horizontalLayout_search)
        self.tableWidget_products = QtWidgets.QTableWidget(EditProductListDialog)
        self.tableWidget_products.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers) # Düzenleme kapalı
        self.tableWidget_products.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows) # Satır seçimi
        self.tableWidget_products.setAlternatingRowColors(True) # Satır renkleri
        self.tableWidget_products.setColumnCount(6) # Sütun sayısı
        self.tableWidget_products.setObjectName("tableWidget_products")
        self.tableWidget_products.setRowCount(0)
        self.tableWidget_products.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget_products.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        for i in range(6):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_products.setHorizontalHeaderItem(i, item)            
        self.verticalLayout_main.addWidget(self.tableWidget_products)        
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_main.addItem(spacerItem)        
        self.horizontalLayout_actions = QtWidgets.QHBoxLayout()
        self.horizontalLayout_actions.setObjectName("horizontalLayout_actions")        
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_actions.addItem(spacerItem1)       
        self.btn_close = QtWidgets.QPushButton(EditProductListDialog)
        self.btn_close.setStyleSheet("background-color: #6C757D; color: white;")
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_actions.addWidget(self.btn_close)       
        self.verticalLayout_main.addLayout(self.horizontalLayout_actions)
        self.retranslateUi(EditProductListDialog)
        QtCore.QMetaObject.connectSlotsByName(EditProductListDialog)
    def retranslateUi(self, EditProductListDialog):
        _translate = QtCore.QCoreApplication.translate
        EditProductListDialog.setWindowTitle(_translate("EditProductListDialog", "Ürün Düzenle ve Sil"))
        self.label_title.setText(_translate("EditProductListDialog", "ÜRÜN DÜZENLEME VE SİLME"))
        self.lineEdit_search.setPlaceholderText(_translate("EditProductListDialog", "Ürün adı veya barkod girin..."))
        self.btn_search.setText(_translate("EditProductListDialog", "ARA"))        
        headers = ["Barkod", "Ürün Adı", "Satış Fiyatı", "Stok", "Son Güncelleme", "İşlemler"]
        for i, h in enumerate(headers):
            item = self.tableWidget_products.horizontalHeaderItem(i)
            item.setText(_translate("EditProductListDialog", h))            
        self.btn_close.setText(_translate("EditProductListDialog", "GERİ"))