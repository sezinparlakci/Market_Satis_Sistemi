from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddProductDialog(object):
    def setupUi(self, AddProductDialog):
        AddProductDialog.setObjectName("AddProductDialog")
        AddProductDialog.resize(750, 650)
        AddProductDialog.setStyleSheet("\n"
"    QDialog { background-color: #F8F9FA; }\n"
"    QLabel { font-size: 14pt; font-weight: 500; color: #495057; }\n"
"    \n"
"    /* Giriş Alanları Stili */\n"
"    QLineEdit, QDoubleSpinBox, QSpinBox, QComboBox {\n"
"        padding: 12px;\n"
"        border: 1px solid #CED4DA;\n"
"        border-radius: 8px;\n"
"        font-size: 16pt;\n"
"        background-color: white;\n"
"    }\n"
"    \n"
"    /* Butonlar Stili */\n"
"    QPushButton {\n"
"        border-radius: 8px;\n"
"        padding: 15px;\n"
"        font-weight: bold;\n"
"        font-size: 16pt;\n"
"        min-height: 40px;\n"
"    }\n"
"    \n"
"    /* Başlık Stili */\n"
"    QLabel#label_title { \n"
"        font-size: 28pt; \n"
"        font-weight: bold; \n"
"        color: #007BFF;\n"
"        margin-bottom: 10px;\n"
"    }\n"
"   ")
        self.verticalLayout_main = QtWidgets.QVBoxLayout(AddProductDialog)
        self.verticalLayout_main.setContentsMargins(40, 40, 40, 40)
        self.verticalLayout_main.setSpacing(15)
        self.verticalLayout_main.setObjectName("verticalLayout_main")
        self.label_title = QtWidgets.QLabel(AddProductDialog)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_main.addWidget(self.label_title, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_input = QtWidgets.QGridLayout()
        self.gridLayout_input.setHorizontalSpacing(20)
        self.gridLayout_input.setVerticalSpacing(15)
        self.gridLayout_input.setObjectName("gridLayout_input")
        self.label_barcode = QtWidgets.QLabel(AddProductDialog)
        self.label_barcode.setObjectName("label_barcode")
        self.gridLayout_input.addWidget(self.label_barcode, 0, 0, 1, 1)
        self.lineEdit_barcode = QtWidgets.QLineEdit(AddProductDialog)
        self.lineEdit_barcode.setObjectName("lineEdit_barcode")
        self.gridLayout_input.addWidget(self.lineEdit_barcode, 0, 1, 1, 1)
        self.label_name = QtWidgets.QLabel(AddProductDialog)
        self.label_name.setObjectName("label_name")
        self.gridLayout_input.addWidget(self.label_name, 1, 0, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(AddProductDialog)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout_input.addWidget(self.lineEdit_name, 1, 1, 1, 1)
        self.label_product_group = QtWidgets.QLabel(AddProductDialog)
        self.label_product_group.setObjectName("label_product_group")
        self.gridLayout_input.addWidget(self.label_product_group, 2, 0, 1, 1)
        self.horizontalLayout_group_kdv = QtWidgets.QHBoxLayout()
        self.horizontalLayout_group_kdv.setSpacing(10)
        self.horizontalLayout_group_kdv.setObjectName("horizontalLayout_group_kdv")
        self.comboBox_product_group = QtWidgets.QComboBox(AddProductDialog)
        self.comboBox_product_group.setObjectName("comboBox_product_group")
        self.comboBox_product_group.addItem("")
        self.comboBox_product_group.addItem("")
        self.comboBox_product_group.addItem("")
        self.horizontalLayout_group_kdv.addWidget(self.comboBox_product_group)
        self.label_kdv_value = QtWidgets.QLabel(AddProductDialog)
        self.label_kdv_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_kdv_value.setObjectName("label_kdv_value")
        self.horizontalLayout_group_kdv.addWidget(self.label_kdv_value)
        self.gridLayout_input.addLayout(self.horizontalLayout_group_kdv, 2, 1, 1, 1)
        self.label_purchase_price = QtWidgets.QLabel(AddProductDialog)
        self.label_purchase_price.setObjectName("label_purchase_price")
        self.gridLayout_input.addWidget(self.label_purchase_price, 3, 0, 1, 1)
        self.doubleSpinBox_purchase_price = QtWidgets.QDoubleSpinBox(AddProductDialog)
        self.doubleSpinBox_purchase_price.setMaximum(99999.99)
        self.doubleSpinBox_purchase_price.setObjectName("doubleSpinBox_purchase_price")
        self.gridLayout_input.addWidget(self.doubleSpinBox_purchase_price, 3, 1, 1, 1)
        self.label_sale_price = QtWidgets.QLabel(AddProductDialog)
        self.label_sale_price.setObjectName("label_sale_price")
        self.gridLayout_input.addWidget(self.label_sale_price, 4, 0, 1, 1)
        self.doubleSpinBox_sale_price = QtWidgets.QDoubleSpinBox(AddProductDialog)
        self.doubleSpinBox_sale_price.setMaximum(99999.99)
        self.doubleSpinBox_sale_price.setObjectName("doubleSpinBox_sale_price")
        self.gridLayout_input.addWidget(self.doubleSpinBox_sale_price, 4, 1, 1, 1)
        self.label_pos_sale_price = QtWidgets.QLabel(AddProductDialog)
        self.label_pos_sale_price.setObjectName("label_pos_sale_price")
        self.gridLayout_input.addWidget(self.label_pos_sale_price, 5, 0, 1, 1)
        self.doubleSpinBox_pos_sale_price = QtWidgets.QDoubleSpinBox(AddProductDialog)
        self.doubleSpinBox_pos_sale_price.setMaximum(99999.99)
        self.doubleSpinBox_pos_sale_price.setObjectName("doubleSpinBox_pos_sale_price")
        self.gridLayout_input.addWidget(self.doubleSpinBox_pos_sale_price, 5, 1, 1, 1)
        self.label_stock = QtWidgets.QLabel(AddProductDialog)
        self.label_stock.setObjectName("label_stock")
        self.gridLayout_input.addWidget(self.label_stock, 6, 0, 1, 1)
        self.spinBox_stock = QtWidgets.QSpinBox(AddProductDialog)
        self.spinBox_stock.setMaximum(99999)
        self.spinBox_stock.setProperty("value", 0)
        self.spinBox_stock.setObjectName("spinBox_stock")
        self.gridLayout_input.addWidget(self.spinBox_stock, 6, 1, 1, 1)
        self.verticalLayout_main.addLayout(self.gridLayout_input)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_main.addItem(spacerItem)
        self.horizontalLayout_actions = QtWidgets.QHBoxLayout()
        self.horizontalLayout_actions.setSpacing(15)
        self.horizontalLayout_actions.setObjectName("horizontalLayout_actions")
        self.btn_cancel = QtWidgets.QPushButton(AddProductDialog)
        self.btn_cancel.setStyleSheet("background-color: #6c757d; color: white;")
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_actions.addWidget(self.btn_cancel)
        self.btn_save = QtWidgets.QPushButton(AddProductDialog)
        self.btn_save.setStyleSheet("background-color: #28a745; color: white;")
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_actions.addWidget(self.btn_save)
        self.verticalLayout_main.addLayout(self.horizontalLayout_actions)
        self.retranslateUi(AddProductDialog)
        QtCore.QMetaObject.connectSlotsByName(AddProductDialog)
    def retranslateUi(self, AddProductDialog):
        _translate = QtCore.QCoreApplication.translate
        AddProductDialog.setWindowTitle(_translate("AddProductDialog", "Yeni Ürün Ekleme"))
        self.label_title.setText(_translate("AddProductDialog", "YENİ ÜRÜN BİLGİLERİ GİRİŞİ"))
        self.label_barcode.setText(_translate("AddProductDialog", "1. Barkod Numarası:"))
        self.lineEdit_barcode.setPlaceholderText(_translate("AddProductDialog", "Barkod okutun veya manuel girin"))
        self.label_name.setText(_translate("AddProductDialog", "2. Ürün Adı:"))
        self.lineEdit_name.setPlaceholderText(_translate("AddProductDialog", "Ürün adını girin (Örn: Coca Cola 1 Lt)"))
        self.label_product_group.setText(_translate("AddProductDialog", "3. Ürün Grubu (KDV İçin):"))
        self.comboBox_product_group.setPlaceholderText(_translate("AddProductDialog", "Grup Seçiniz"))
        self.comboBox_product_group.setItemText(0, _translate("AddProductDialog", "Gıda (%1 KDV)"))
        self.comboBox_product_group.setItemText(1, _translate("AddProductDialog", "Temel Tüketim (%10 KDV)"))
        self.comboBox_product_group.setItemText(2, _translate("AddProductDialog", "Diğer Mal ve Hizmetler (%20 KDV)"))
        self.label_kdv_value.setText(_translate("AddProductDialog", "KDV: %"))
        self.label_purchase_price.setText(_translate("AddProductDialog", "4. Alış Fiyatı (TL):"))
        self.doubleSpinBox_purchase_price.setPrefix(_translate("AddProductDialog", "₺ "))
        self.label_sale_price.setText(_translate("AddProductDialog", "5. Mağaza Satış Fiyatı (TL):"))
        self.doubleSpinBox_sale_price.setPrefix(_translate("AddProductDialog", "₺ "))
        self.label_pos_sale_price.setText(_translate("AddProductDialog", "6. POS Satış Fiyatı (TL):"))
        self.doubleSpinBox_pos_sale_price.setPrefix(_translate("AddProductDialog", "₺ "))
        self.label_stock.setText(_translate("AddProductDialog", "7. Başlangıç Stok Miktarı:"))
        self.btn_cancel.setText(_translate("AddProductDialog", "VAZGEÇ"))
        self.btn_save.setText(_translate("AddProductDialog", "ÜRÜNÜ KAYDET"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddProductDialog = QtWidgets.QDialog()
    ui = Ui_AddProductDialog()
    ui.setupUi(AddProductDialog)
    AddProductDialog.show()
    sys.exit(app.exec_())
