from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ManualStockAdjustmentDialog(object):
    def setupUi(self, ManualStockAdjustmentDialog):
        ManualStockAdjustmentDialog.setObjectName("ManualStockAdjustmentDialog")
        ManualStockAdjustmentDialog.resize(1050, 750)
        ManualStockAdjustmentDialog.setStyleSheet("\n"
"            QDialog { background-color: #F8F9FA; }\n"
"            QLabel { font-size: 14pt; font-weight: 500; color: #495057; }\n"
"            QLabel#label_title { \n"
"                font-size: 28pt; \n"
"                font-weight: bold; \n"
"                color: #28A745; /* Yeşil Rengi */\n"
"                margin-bottom: 10px;\n"
"            }\n"
"            QLineEdit, QComboBox {\n"
"                padding: 12px;\n"
"                border: 1px solid #CED4DA;\n"
"                border-radius: 8px;\n"
"                font-size: 16pt;\n"
"                background-color: white;\n"
"            }\n"
"            QPushButton {\n"
"                border-radius: 8px;\n"
"                padding: 12px 25px;\n"
"                font-weight: bold;\n"
"                font-size: 14pt;\n"
"            }\n"
"            QPushButton#btn_search {\n"
"                background-color: #007BFF;\n"
"                color: white;\n"
"            }\n"
"            QPushButton#btn_search:hover { background-color: #0056b3; }\n"
"            QPushButton#btn_save_changes {\n"
"                background-color: #28A745;\n"
"                color: white;\n"
"                font-size: 16pt;\n"
"                padding: 15px;\n"
"            }\n"
"            QPushButton#btn_save_changes:hover { background-color: #218838; }\n"
"            QPushButton#btn_cancel {\n"
"                background-color: #DC3545;\n"
"                color: white;\n"
"                font-size: 16pt;\n"
"                padding: 15px;\n"
"            }\n"
"            QPushButton#btn_cancel:hover { background-color: #c82333; }\n"
"            QTableWidget {\n"
"                border: 1px solid #DEE2E6;\n"
"                border-radius: 8px;\n"
"                background-color: white;\n"
"                selection-background-color: #E2E6EA;\n"
"                selection-color: black;\n"
"                font-size: 14pt;\n"
"            }\n"
"            QHeaderView::section {\n"
"                background-color: #E9ECEF;\n"
"                padding: 8px;\n"
"                border: none;\n"
"                font-weight: bold;\n"
"                font-size: 14pt;\n"
"                color: #495057;\n"
"            }\n"
"        ")
        self.verticalLayout = QtWidgets.QVBoxLayout(ManualStockAdjustmentDialog)
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")       
        self.label_title = QtWidgets.QLabel(ManualStockAdjustmentDialog)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout.addWidget(self.label_title)       
        self.horizontalLayout_search = QtWidgets.QHBoxLayout()
        self.horizontalLayout_search.setSpacing(15)
        self.horizontalLayout_search.setObjectName("horizontalLayout_search")       
        self.lineEdit_search_barcode = QtWidgets.QLineEdit(ManualStockAdjustmentDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed) # Genişlemesi için ayar
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_search_barcode.sizePolicy().hasHeightForWidth())
        self.lineEdit_search_barcode.setSizePolicy(sizePolicy)
        self.lineEdit_search_barcode.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit_search_barcode.setObjectName("lineEdit_search_barcode")
        self.horizontalLayout_search.addWidget(self.lineEdit_search_barcode, 1)       
        self.btn_search = QtWidgets.QPushButton(ManualStockAdjustmentDialog)
        self.btn_search.setMinimumSize(QtCore.QSize(150, 50))
        self.btn_search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_search.setIconSize(QtCore.QSize(24, 24))
        self.btn_search.setObjectName("btn_search")
        self.horizontalLayout_search.addWidget(self.btn_search)
        self.verticalLayout.addLayout(self.horizontalLayout_search)
        self.label_instruction = QtWidgets.QLabel(ManualStockAdjustmentDialog)
        self.label_instruction.setObjectName("label_instruction")
        self.verticalLayout.addWidget(self.label_instruction)       
        self.tableWidget_stock_list = QtWidgets.QTableWidget(ManualStockAdjustmentDialog)
        self.tableWidget_stock_list.setRowCount(0)
        self.tableWidget_stock_list.setColumnCount(4)
        self.tableWidget_stock_list.setObjectName("tableWidget_stock_list")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_stock_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_stock_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_stock_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_stock_list.setHorizontalHeaderItem(3, item)
        self.tableWidget_stock_list.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_stock_list.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.verticalLayout.addWidget(self.tableWidget_stock_list)
        self.horizontalLayout_actions = QtWidgets.QHBoxLayout()
        self.horizontalLayout_actions.setSpacing(20)
        self.horizontalLayout_actions.setObjectName("horizontalLayout_actions")   
        self.btn_cancel = QtWidgets.QPushButton(ManualStockAdjustmentDialog)
        self.btn_cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_actions.addWidget(self.btn_cancel)  
        self.btn_save_changes = QtWidgets.QPushButton(ManualStockAdjustmentDialog)
        self.btn_save_changes.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_save_changes.setObjectName("btn_save_changes")
        self.horizontalLayout_actions.addWidget(self.btn_save_changes)   
        self.verticalLayout.addLayout(self.horizontalLayout_actions)
        self.retranslateUi(ManualStockAdjustmentDialog)
        QtCore.QMetaObject.connectSlotsByName(ManualStockAdjustmentDialog)
    def retranslateUi(self, ManualStockAdjustmentDialog):
        _translate = QtCore.QCoreApplication.translate
        ManualStockAdjustmentDialog.setWindowTitle(_translate("ManualStockAdjustmentDialog", "Manuel Stok Düzeltme / Giriş"))
        self.label_title.setText(_translate("ManualStockAdjustmentDialog", "STOK DÜZELTME VE MANUEL GİRİŞ"))
        self.lineEdit_search_barcode.setPlaceholderText(_translate("ManualStockAdjustmentDialog", "Barkod/Ürün Adı ile ara..."))
        self.btn_search.setText(_translate("ManualStockAdjustmentDialog", "ARA"))
        self.label_instruction.setText(_translate("ManualStockAdjustmentDialog", "Listelenen ürünlerin 'Yeni Stok Miktarı' sütununa güncel miktarı girin."))
        item = self.tableWidget_stock_list.horizontalHeaderItem(0)
        item.setText(_translate("ManualStockAdjustmentDialog", "Barkod"))
        item = self.tableWidget_stock_list.horizontalHeaderItem(1)
        item.setText(_translate("ManualStockAdjustmentDialog", "Ürün Adı"))
        item = self.tableWidget_stock_list.horizontalHeaderItem(2)
        item.setText(_translate("ManualStockAdjustmentDialog", "Mevcut Stok"))
        item = self.tableWidget_stock_list.horizontalHeaderItem(3)
        item.setText(_translate("ManualStockAdjustmentDialog", "Yeni Stok Miktarı"))
        self.btn_cancel.setText(_translate("ManualStockAdjustmentDialog", "VAZGEÇ"))
        self.btn_save_changes.setText(_translate("ManualStockAdjustmentDialog", "KAYDET"))