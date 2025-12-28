from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 800)
        Dialog.setStyleSheet("\n"
"    QDialog { background-color: rgb(245, 245, 245);\n"
" }\n"
"    QPushButton { \n"
"        border-radius: 8px; \n"
"        padding: 10px; \n"
"        font-weight: bold;\n"
"        transition: background-color 0.2s;\n"
"    }\n"
"    QLineEdit, QSpinBox {\n"
"        border: 1px solid rgb(200, 200, 200);\n"
"        border-radius: 6px;\n"
"        padding: 5px;\n"
"        background-color: white;\n"
"    }\n"
"   ")
        self.horizontalLayout_main = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_main.setObjectName("horizontalLayout_main")
        self.verticalLayout_left_column = QtWidgets.QVBoxLayout()
        self.verticalLayout_left_column.setObjectName("verticalLayout_left_column")
        self.verticalLayout_input = QtWidgets.QVBoxLayout()
        self.verticalLayout_input.setObjectName("verticalLayout_input")
        self.label_quantity = QtWidgets.QLabel(Dialog)
        self.label_quantity.setStyleSheet("font-size: 14pt;\n"
" font-weight: bold; color: #81C784; /* Soft Green */")
        self.label_quantity.setObjectName("label_quantity")
        self.verticalLayout_input.addWidget(self.label_quantity)
        self.spinBox_quantity = QtWidgets.QSpinBox(Dialog)
        self.spinBox_quantity.setMinimum(1)
        self.spinBox_quantity.setMaximum(999)
        self.spinBox_quantity.setProperty("value", 1)
        self.spinBox_quantity.setStyleSheet("font-size: 18pt;\n"
" height: 40px;")
        self.spinBox_quantity.setObjectName("spinBox_quantity")
        self.verticalLayout_input.addWidget(self.spinBox_quantity)
        self.lineEdit_barcode = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_barcode.setStyleSheet("font-size: 22pt; height: 50px; /* Büyütülmüş Barkod Girişi */\n"
" border-color: #64B5F6; /* Soft Blue */")
        self.lineEdit_barcode.setObjectName("lineEdit_barcode")
        self.verticalLayout_input.addWidget(self.lineEdit_barcode)
        self.btn_enter = QtWidgets.QPushButton(Dialog)
        self.btn_enter.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_enter.setStyleSheet("font-size: 16pt;\n"
" background-color: #81C784; color: black; font-weight: bold; height: 40px;")
        self.btn_enter.setObjectName("btn_enter")
        self.verticalLayout_input.addWidget(self.btn_enter)
        self.verticalLayout_left_column.addLayout(self.verticalLayout_input)
        self.tableWidget_sepet = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_sepet.setMinimumSize(QtCore.QSize(0, 200))
        self.tableWidget_sepet.setStyleSheet("\n"
"        QHeaderView::section { \n"
"            background-color: #B0BEC5; /* Soft Gray-Blue */\n"
"            color: black; \n"
"            font-weight: bold;\n"
"            font-size: 11pt; \n"
"            padding: 6px; \n"
"            border: none;\n"
"        }\n"
"        QTableWidget { \n"
"            font-size: 10pt;\n"
"            alternate-background-color: #EEEEEE; \n"
"            selection-background-color: #CFD8DC; /* Light selection */\n"
"            border-radius: 8px;\n"
"        }\n"
"        ")
        self.tableWidget_sepet.setColumnCount(4)
        self.tableWidget_sepet.setObjectName("tableWidget_sepet")
        self.tableWidget_sepet.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sepet.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sepet.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sepet.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sepet.setHorizontalHeaderItem(3, item)
        self.verticalLayout_left_column.addWidget(self.tableWidget_sepet)
        self.horizontalLayout_total_payment = QtWidgets.QHBoxLayout()
        self.horizontalLayout_total_payment.setObjectName("horizontalLayout_total_payment")
        self.total_price_widget = QtWidgets.QWidget(Dialog)
        self.total_price_widget.setStyleSheet("\n"
"           QWidget { \n"
"            background-color: #FFFFFF;\n"
"            border: 2px solid #81C784; /* Soft Green Border */\n"
"            border-radius: 10px;\n"
"            padding: 10px;\n"
"           }\n"
"          ")
        self.total_price_widget.setObjectName("total_price_widget")
        self.horizontalLayout_total = QtWidgets.QHBoxLayout(self.total_price_widget)
        self.horizontalLayout_total.setObjectName("horizontalLayout_total")
        self.label_total_text = QtWidgets.QLabel(self.total_price_widget)
        self.label_total_text.setStyleSheet("font-size: 20pt;\n"
" font-weight: bold; color: #81C784; /* Soft Green */")
        self.label_total_text.setObjectName("label_total_text")
        self.horizontalLayout_total.addWidget(self.label_total_text)
        self.label_total_value = QtWidgets.QLabel(self.total_price_widget)
        self.label_total_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.label_total_value.setStyleSheet("font-size: 22pt;\n"
" font-weight: bold; color: #81C784; /* Soft Green */")
        self.label_total_value.setObjectName("label_total_value")
        self.horizontalLayout_total.addWidget(self.label_total_value)
        self.horizontalLayout_total_payment.addWidget(self.total_price_widget)
        self.payment_buttons_widget = QtWidgets.QWidget(Dialog)
        self.payment_buttons_widget.setObjectName("payment_buttons_widget")
        self.gridLayout_payment = QtWidgets.QGridLayout(self.payment_buttons_widget)
        self.gridLayout_payment.setObjectName("gridLayout_payment")
        self.pushButton_cash = QtWidgets.QPushButton(self.payment_buttons_widget)
        self.pushButton_cash.setStyleSheet("background-color: #81C784; /* Soft Green */\n"
" color: black; font-size: 14pt;")
        self.pushButton_cash.setObjectName("pushButton_cash")
        self.gridLayout_payment.addWidget(self.pushButton_cash, 0, 0, 1, 1)
        self.pushButton_card = QtWidgets.QPushButton(self.payment_buttons_widget)
        self.pushButton_card.setStyleSheet("background-color: #64B5F6; /* Soft Blue */\n"
" color: white; font-size: 14pt;")
        self.pushButton_card.setObjectName("pushButton_card")
        self.gridLayout_payment.addWidget(self.pushButton_card, 0, 1, 1, 1)
        self.pushButton_return = QtWidgets.QPushButton(self.payment_buttons_widget)
        self.pushButton_return.setStyleSheet("background-color: #FFAB91; /* Soft Red */\n"
" color: black; font-size: 14pt;")
        self.pushButton_return.setObjectName("pushButton_return")
        self.gridLayout_payment.addWidget(self.pushButton_return, 1, 0, 1, 2)
        self.horizontalLayout_total_payment.addWidget(self.payment_buttons_widget)
        self.verticalLayout_left_column.addLayout(self.horizontalLayout_total_payment)
        self.horizontalLayout_main.addLayout(self.verticalLayout_left_column)
        self.verticalLayout_right_column = QtWidgets.QVBoxLayout()
        self.verticalLayout_right_column.setObjectName("verticalLayout_right_column")
        self.keypad_large_widget = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.keypad_large_widget.sizePolicy().hasHeightForWidth())
        self.keypad_large_widget.setSizePolicy(sizePolicy)
        self.keypad_large_widget.setObjectName("keypad_large_widget")
        self.gridLayout_keypad_large = QtWidgets.QGridLayout(self.keypad_large_widget)
        self.gridLayout_keypad_large.setObjectName("gridLayout_keypad_large")
        self.btn_large_7 = QtWidgets.QPushButton(self.keypad_large_widget)
        self.btn_large_7.setStyleSheet("font-size: 26pt; height: 50px; background-color: #FFFFFF;")
        self.btn_large_7.setObjectName("btn_large_7")
        self.gridLayout_keypad_large.addWidget(self.btn_large_7, 0, 0, 1, 1)
        self.btn_large_8 = QtWidgets.QPushButton(self.keypad_large_widget)
        self.btn_large_8.setStyleSheet("font-size: 26pt; height: 50px;\n"
" background-color: #FFFFFF;")
        self.btn_large_8.setObjectName("btn_large_8")
        self.gridLayout_keypad_large.addWidget(self.btn_large_8, 0, 1, 1, 1)
        self.btn_large_9 = QtWidgets.QPushButton(self.keypad_large_widget)
        self.btn_large_9.setStyleSheet("font-size: 26pt; height: 50px;\n"
" background-color: #FFFFFF;")
        self.btn_large_9.setObjectName("btn_large_9")
        self.gridLayout_keypad_large.addWidget(self.btn_large_9, 0, 2, 1, 1)
        self.btn_large_clear = QtWidgets.QPushButton(self.keypad_large_widget)
        self.btn_large_clear.setStyleSheet("font-size: 20pt; height: 50px;\n"
" background-color: #FFAB91; color: black; /* Soft Red */")
        self.btn_large_clear.setObjectName("btn_large_clear")
        self.gridLayout_keypad_large.addWidget(self.btn_large_clear, 0, 3, 1, 1)
        self.btn_large_4 = QtWidgets.QPushButton(self.keypad_large_widget)
        self.btn_large_4.setStyleSheet("font-size: 26pt; height: 50px;\n"
" background-color: #FFFFFF;")
        self.btn_large_4.setObjectName("btn_large_4")
        self.gridLayout_keypad_large.addWidget(self.btn_large_4, 1, 0, 1, 1)
        self.btn_large_5 = QtWidgets.QPushButton(self.keypad_large_widget)
        self.btn_large_5.setStyleSheet("font-size: 26pt; height: 50px;\n"
" background-color: #FFFFFF;")
        self.btn_large_5.setObjectName("btn_large_5")
        self.gridLayout_keypad_large.addWidget(self.btn_large_5, 1, 1, 1, 1)
        self.btn_large_6 = QtWidgets.QPushButton(self.keypad_large_widget)
        self.btn_large_6.setStyleSheet("font-size: 26pt; height: 50px;\n"
" background-color: #FFFFFF;")
        self.btn_large_6.setObjectName("btn_large_6")
        self.gridLayout_keypad_large.addWidget(self.btn_large_6, 1, 2, 1, 1)
        self.btn_large_back = QtWidgets.QPushButton(self.keypad_large_widget)
        self.btn_large_back.setStyleSheet("font-size: 20pt; height: 50px;\n"
" background-color: #FFCC80; color: black; /* Soft Orange */")
        self.btn_large_back.setObjectName("btn_large_back")
        self.gridLayout_keypad_large.addWidget(self.btn_large_back, 1, 3, 1, 1)
        self.btn_large_1 = QtWidgets.QPushButton(self.keypad_large_widget)
        self.btn_large_1.setStyleSheet("font-size: 26pt; height: 50px;\n"
" background-color: #FFFFFF;")
        self.btn_large_1.setObjectName("btn_large_1")
        self.gridLayout_keypad_large.addWidget(self.btn_large_1, 2, 0, 1, 1)
        self.btn_large_2 = QtWidgets.QPushButton(self.keypad_large_widget)
        self.btn_large_2.setStyleSheet("font-size: 26pt; height: 50px;\n"
" background-color: #FFFFFF;")
        self.btn_large_2.setObjectName("btn_large_2")
        self.gridLayout_keypad_large.addWidget(self.btn_large_2, 2, 1, 1, 1)
        self.btn_large_3 = QtWidgets.QPushButton(self.keypad_large_widget)
        self.btn_large_3.setStyleSheet("font-size: 26pt; height: 50px;\n"
" background-color: #FFFFFF;")
        self.btn_large_3.setObjectName("btn_large_3")
        self.gridLayout_keypad_large.addWidget(self.btn_large_3, 2, 2, 1, 1)
        self.btn_large_0 = QtWidgets.QPushButton(self.keypad_large_widget)
        self.btn_large_0.setStyleSheet("font-size: 26pt; height: 50px;\n"
" background-color: #FFFFFF;")
        self.btn_large_0.setObjectName("btn_large_0")
        self.gridLayout_keypad_large.addWidget(self.btn_large_0, 3, 0, 1, 3)
        self.btn_large_delete_item = QtWidgets.QPushButton(self.keypad_large_widget)
        self.btn_large_delete_item.setStyleSheet("font-size: 16pt; height: 50px;\n"
" background-color: #FFAB91; color: black; /* Soft Red */")
        self.btn_large_delete_item.setObjectName("btn_large_delete_item")
        self.gridLayout_keypad_large.addWidget(self.btn_large_delete_item, 2, 3, 1, 1)
        self.btn_large_dot = QtWidgets.QPushButton(self.keypad_large_widget)
        self.btn_large_dot.setStyleSheet("font-size: 26pt; height: 50px;\n"
" background-color: #FFFFFF;")
        self.btn_large_dot.setObjectName("btn_large_dot")
        self.gridLayout_keypad_large.addWidget(self.btn_large_dot, 3, 3, 1, 1)
        self.verticalLayout_right_column.addWidget(self.keypad_large_widget)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_products = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_products.setObjectName("gridLayout_products")
        self.ekmek = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.ekmek.setStyleSheet("background-color: #F5F5F5;\n"
" font-size: 14pt; height: 55px;")
        self.ekmek.setObjectName("ekmek")
        self.gridLayout_products.addWidget(self.ekmek, 0, 0, 1, 1)
        self.sakiz = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.sakiz.setStyleSheet("background-color: #F5F5F5;\n"
" font-size: 14pt; height: 55px;")
        self.sakiz.setObjectName("sakiz")
        self.gridLayout_products.addWidget(self.sakiz, 0, 1, 1, 1)
        self.lolipop = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lolipop.setStyleSheet("background-color: #F5F5F5;\n"
" font-size: 14pt; height: 55px;")
        self.lolipop.setObjectName("lolipop")
        self.gridLayout_products.addWidget(self.lolipop, 0, 2, 1, 1)
        self.pil_2li = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pil_2li.setStyleSheet("background-color: #F5F5F5;\n"
" font-size: 14pt; height: 55px;")
        self.pil_2li.setObjectName("pil_2li")
        self.gridLayout_products.addWidget(self.pil_2li, 1, 0, 1, 1)
        self.pil_4lu = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pil_4lu.setStyleSheet("background-color: #F5F5F5;\n"
" font-size: 14pt; height: 55px;")
        self.pil_4lu.setObjectName("pil_4lu")
        self.gridLayout_products.addWidget(self.pil_4lu, 1, 1, 1, 1)
        self.vb = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.vb.setStyleSheet("background-color: #F5F5F5;\n"
" font-size: 14pt; height: 55px;")
        self.vb.setObjectName("vb")
        self.gridLayout_products.addWidget(self.vb, 1, 2, 1, 1)
        self.placeholder_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.placeholder_7.setStyleSheet("background-color: #F5F5F5; font-size: 14pt; height: 55px;")
        self.placeholder_7.setObjectName("placeholder_7")
        self.gridLayout_products.addWidget(self.placeholder_7, 2, 0, 1, 1)
        self.placeholder_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.placeholder_8.setStyleSheet("background-color: #F5F5F5; font-size: 14pt; height: 55px;")
        self.placeholder_8.setObjectName("placeholder_8")
        self.gridLayout_products.addWidget(self.placeholder_8, 2, 1, 1, 1)
        self.placeholder_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.placeholder_9.setStyleSheet("background-color: #F5F5F5; font-size: 14pt; height: 55px;")
        self.placeholder_9.setObjectName("placeholder_9")
        self.gridLayout_products.addWidget(self.placeholder_9, 2, 2, 1, 1)
        self.placeholder_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.placeholder_10.setStyleSheet("background-color: #F5F5F5; font-size: 14pt; height: 55px;")
        self.placeholder_10.setObjectName("placeholder_10")
        self.gridLayout_products.addWidget(self.placeholder_10, 3, 0, 1, 1)
        self.placeholder_11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.placeholder_11.setStyleSheet("background-color: #F5F5F5; font-size: 14pt; height: 55px;")
        self.placeholder_11.setObjectName("placeholder_11")
        self.gridLayout_products.addWidget(self.placeholder_11, 3, 1, 1, 1)
        self.placeholder_12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.placeholder_12.setStyleSheet("background-color: #F5F5F5; font-size: 14pt; height: 55px;")
        self.placeholder_12.setObjectName("placeholder_12")
        self.gridLayout_products.addWidget(self.placeholder_12, 3, 2, 1, 1)
        self.placeholder_13 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.placeholder_13.setStyleSheet("background-color: #F5F5F5; font-size: 14pt; height: 55px;")
        self.placeholder_13.setObjectName("placeholder_13")
        self.gridLayout_products.addWidget(self.placeholder_13, 4, 0, 1, 1)
        self.placeholder_14 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.placeholder_14.setStyleSheet("background-color: #F5F5F5; font-size: 14pt; height: 55px;")
        self.placeholder_14.setObjectName("placeholder_14")
        self.gridLayout_products.addWidget(self.placeholder_14, 4, 1, 1, 1)
        self.placeholder_15 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.placeholder_15.setStyleSheet("background-color: #F5F5F5; font-size: 14pt; height: 55px;")
        self.placeholder_15.setObjectName("placeholder_15")
        self.gridLayout_products.addWidget(self.placeholder_15, 4, 2, 1, 1)
        self.placeholder_16 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.placeholder_16.setStyleSheet("background-color: #F5F5F5; font-size: 14pt; height: 55px;")
        self.placeholder_16.setObjectName("placeholder_16")
        self.gridLayout_products.addWidget(self.placeholder_16, 5, 0, 1, 1)
        self.placeholder_17 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.placeholder_17.setStyleSheet("background-color: #F5F5F5; font-size: 14pt; height: 55px;")
        self.placeholder_17.setObjectName("placeholder_17")
        self.gridLayout_products.addWidget(self.placeholder_17, 5, 1, 1, 1)
        self.placeholder_18 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.placeholder_18.setStyleSheet("background-color: #F5F5F5; font-size: 14pt; height: 55px;")
        self.placeholder_18.setObjectName("placeholder_18")
        self.gridLayout_products.addWidget(self.placeholder_18, 5, 2, 1, 1)
        self.verticalLayout_right_column.addWidget(self.gridLayoutWidget)
        self.pushButton_menu = QtWidgets.QPushButton(Dialog)
        self.pushButton_menu.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_menu.setFont(font)
        self.pushButton_menu.setStyleSheet("background-color: #B39DDB; color: white; font-size: 16pt; /* Soft Lavender */")
        self.pushButton_menu.setObjectName("pushButton_menu")
        self.verticalLayout_right_column.addWidget(self.pushButton_menu)
        self.horizontalLayout_main.addLayout(self.verticalLayout_right_column)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "POS Sistemi"))
        self.label_quantity.setText(_translate("Dialog", "Adet:"))
        self.lineEdit_barcode.setPlaceholderText(_translate("Dialog", "Barkod giriniz..."))
        self.btn_enter.setText(_translate("Dialog", "ÜRÜN EKLE (ENTER)"))
        item = self.tableWidget_sepet.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Barkod"))
        item = self.tableWidget_sepet.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Ürün Adı"))
        item = self.tableWidget_sepet.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Adet"))
        item = self.tableWidget_sepet.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Fiyat (TL)"))
        self.label_total_text.setText(_translate("Dialog", "TOPLAM TUTAR:"))
        self.label_total_value.setText(_translate("Dialog", "0.00 TL"))
        self.pushButton_cash.setText(_translate("Dialog", "NAKİT"))
        self.pushButton_card.setText(_translate("Dialog", "KART"))
        self.pushButton_return.setText(_translate("Dialog", "İADE"))
        self.btn_large_7.setText(_translate("Dialog", "7"))
        self.btn_large_8.setText(_translate("Dialog", "8"))
        self.btn_large_9.setText(_translate("Dialog", "9"))
        self.btn_large_clear.setText(_translate("Dialog", "C"))
        self.btn_large_4.setText(_translate("Dialog", "4"))
        self.btn_large_5.setText(_translate("Dialog", "5"))
        self.btn_large_6.setText(_translate("Dialog", "6"))
        self.btn_large_back.setText(_translate("Dialog", "<-"))
        self.btn_large_1.setText(_translate("Dialog", "1"))
        self.btn_large_2.setText(_translate("Dialog", "2"))
        self.btn_large_3.setText(_translate("Dialog", "3"))
        self.btn_large_0.setText(_translate("Dialog", "0"))
        self.btn_large_delete_item.setText(_translate("Dialog", "SİL"))
        self.btn_large_dot.setText(_translate("Dialog", "."))
        self.ekmek.setText(_translate("Dialog", "EKMEK"))
        self.sakiz.setText(_translate("Dialog", "TEKLİ SAKIZ"))
        self.lolipop.setText(_translate("Dialog", "LOLİPOP"))
        self.pil_2li.setText(_translate("Dialog", "2\'Lİ PİL"))
        self.pil_4lu.setText(_translate("Dialog", "4\'LÜ PİL"))
        self.vb.setText(_translate("Dialog", "FALIM"))
        self.placeholder_7.setText(_translate("Dialog", "5L SU"))
        self.placeholder_8.setText(_translate("Dialog", "19L SU"))
        self.placeholder_9.setText(_translate("Dialog", "CİNO"))
        self.placeholder_10.setText(_translate("Dialog", "SELPAK"))
        self.placeholder_11.setText(_translate("Dialog", "ISLAKM."))
        self.placeholder_12.setText(_translate("Dialog", "JAPON YA."))
        self.placeholder_13.setText(_translate("Dialog", "KOLONYA"))
        self.placeholder_14.setText(_translate("Dialog", "ÇORAP"))
        self.placeholder_15.setText(_translate("Dialog", "PASTİL"))
        self.placeholder_16.setText(_translate("Dialog", "NESTFİT"))
        self.placeholder_17.setText(_translate("Dialog", "HOBİ"))
        self.placeholder_18.setText(_translate("Dialog", "PARFÜM"))
        self.pushButton_menu.setText(_translate("Dialog", "MENÜ"))