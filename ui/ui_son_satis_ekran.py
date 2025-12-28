from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LastSaleScreen(object):
    def setupUi(self, LastSaleScreen):
        LastSaleScreen.setObjectName("LastSaleScreen")
        LastSaleScreen.resize(1000, 700)
        LastSaleScreen.setWindowTitle("Son Satışlar ve İşlemler")
        LastSaleScreen.setStyleSheet(
            "QDialog { background-color: #F8F9FA; }\n"
            "QLabel#label_title { \n"
            "    font-size: 28pt; \n"
            "    font-weight: bold; \n"
            "    color: #7B1FA2; \n"
            "    margin-bottom: 10px;\n"
            "}\n"
            "QLineEdit {\n"
            "    padding: 12px;\n"
            "    border: 2px solid #7B1FA2;\n"
            "    border-radius: 8px;\n"
            "    font-size: 16pt;\n"
            "    background-color: white;\n"
            "}\n"
            "QTableWidget {\n"
            "    border: 1px solid #CED4DA;\n"
            "    border-radius: 8px;\n"
            "    font-size: 12pt; \n"
            "    alternate-background-color: #F0F0F0;\n"
            "    gridline-color: #E9ECEF;\n"
            "}\n"
            "QHeaderView::section { \n"
            "    background-color: #343A40; \n"
            "    color: white; \n"
            "    font-weight: bold; \n"
            "    font-size: 12pt; \n"
            "    padding: 8px; \n"
            "    border: none;\n"
            "}\n"
            "QPushButton {\n"
            "    border-radius: 6px;\n"
            "    padding: 10px 15px;\n"
            "    font-weight: bold;\n"
            "    font-size: 12pt;\n"
            "}\n"
            "QPushButton#btn_close {\n"
            "    background-color: #6C757D; \n"
            "    color: white;\n"
            "}"
        )
        self.verticalLayout_main = QtWidgets.QVBoxLayout(LastSaleScreen)
        self.verticalLayout_main.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_main.setSpacing(20)
        self.verticalLayout_main.setObjectName("verticalLayout_main")
        self.label_title = QtWidgets.QLabel(LastSaleScreen)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_main.addWidget(self.label_title)       
        self.tableWidget_sales = QtWidgets.QTableWidget(LastSaleScreen)
        self.tableWidget_sales.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_sales.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_sales.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_sales.setColumnCount(5)
        self.tableWidget_sales.setObjectName("tableWidget_sales")        
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sales.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sales.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sales.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sales.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sales.setHorizontalHeaderItem(4, item)
        self.verticalLayout_main.addWidget(self.tableWidget_sales)        
        self.horizontalLayout_actions = QtWidgets.QHBoxLayout()
        self.horizontalLayout_actions.setObjectName("horizontalLayout_actions")       
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_actions.addItem(spacerItem)        
        self.btn_close = QtWidgets.QPushButton(LastSaleScreen)
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_actions.addWidget(self.btn_close)       
        self.verticalLayout_main.addLayout(self.horizontalLayout_actions)
        self.retranslateUi(LastSaleScreen)
        QtCore.QMetaObject.connectSlotsByName(LastSaleScreen)
    def retranslateUi(self, LastSaleScreen):
        _translate = QtCore.QCoreApplication.translate
        self.label_title.setText(_translate("LastSaleScreen", "SON SATIŞLAR VE İŞLEMLER"))        
        item = self.tableWidget_sales.horizontalHeaderItem(0)
        item.setText(_translate("LastSaleScreen", "Fiş No"))
        item = self.tableWidget_sales.horizontalHeaderItem(1)
        item.setText(_translate("LastSaleScreen", "Tarih / Saat"))
        item = self.tableWidget_sales.horizontalHeaderItem(2)
        item.setText(_translate("LastSaleScreen", "Toplam Tutar"))
        item = self.tableWidget_sales.horizontalHeaderItem(3)
        item.setText(_translate("LastSaleScreen", "Ödeme Türü"))
        item = self.tableWidget_sales.horizontalHeaderItem(4)
        item.setText(_translate("LastSaleScreen", "Durum"))
        self.btn_close.setText(_translate("LastSaleScreen", "GERİ"))