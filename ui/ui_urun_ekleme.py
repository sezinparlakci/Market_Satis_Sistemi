from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddProductDialog(object):
    def setupUi(self, AddProductDialog):
        AddProductDialog.setObjectName("AddProductDialog")
        AddProductDialog.resize(650, 580)
        AddProductDialog.setStyleSheet("\n"
"    QDialog { background-color: #F8F9FA; }\n"
"    QLabel { font-size: 14pt; font-weight: 500; color: #495057; }\n"
"    \n"
"    /* Giriş Alanları Stili */\n"
"    QLineEdit, QDoubleSpinBox, QSpinBox {\n"
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
"   ")
        self.verticalLayout_main = QtWidgets.QVBoxLayout(AddProductDialog)
        self.verticalLayout_main.setContentsMargins(30,30,30,30)
        self.verticalLayout_main.setSpacing(20)
        self.verticalLayout_main.setObjectName("verticalLayout_main")
        self.label_title = QtWidgets.QLabel(AddProductDialog)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setStyleSheet("font-size: 28pt; font-weight: bold; color: #007bff; margin-bottom: 10px;")
        self.label_title.setObjectName("label_title")
        self.verticalLayout_main.addWidget(self.label_title)
        self.formLayout_product_details = QtWidgets.QFormLayout()
        self.formLayout_product_details.setSpacing(20)
        self.formLayout_product_details.setObjectName("formLayout_product_details")
        self.label_barcode = QtWidgets.QLabel(AddProductDialog)
        self.label_barcode.setObjectName("label_barcode")
        self.formLayout_product_details.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_barcode)
        self.lineEdit_barcode = QtWidgets.QLineEdit(AddProductDialog)
        self.lineEdit_barcode.setObjectName("lineEdit_barcode")
        self.formLayout_product_details.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_barcode)
        self.label_name = QtWidgets.QLabel(AddProductDialog)
        self.label_name.setObjectName("label_name")
        self.formLayout_product_details.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_name)
        self.lineEdit_name = QtWidgets.QLineEdit(AddProductDialog)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.formLayout_product_details.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_name)
        self.label_purchase_price = QtWidgets.QLabel(AddProductDialog)
        self.label_purchase_price.setObjectName("label_purchase_price")
        self.formLayout_product_details.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_purchase_price)
        self.doubleSpinBox_purchase_price = QtWidgets.QDoubleSpinBox(AddProductDialog)
        self.doubleSpinBox_purchase_price.setMaximum(99999.99)
        self.doubleSpinBox_purchase_price.setDecimals(2)
        self.doubleSpinBox_purchase_price.setObjectName("doubleSpinBox_purchase_price")
        self.formLayout_product_details.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_purchase_price)
        self.label_sale_price = QtWidgets.QLabel(AddProductDialog)
        self.label_sale_price.setObjectName("label_sale_price")
        self.formLayout_product_details.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_sale_price)
        self.doubleSpinBox_sale_price = QtWidgets.QDoubleSpinBox(AddProductDialog)
        self.doubleSpinBox_sale_price.setMaximum(99999.99)
        self.doubleSpinBox_sale_price.setDecimals(2)
        self.doubleSpinBox_sale_price.setProperty("value", 1.0)
        self.doubleSpinBox_sale_price.setObjectName("doubleSpinBox_sale_price")
        self.formLayout_product_details.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_sale_price)
        self.label_stock = QtWidgets.QLabel(AddProductDialog)
        self.label_stock.setObjectName("label_stock")
        self.formLayout_product_details.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_stock)
        self.spinBox_stock = QtWidgets.QSpinBox(AddProductDialog)
        self.spinBox_stock.setMaximum(99999)
        self.spinBox_stock.setProperty("value", 0)
        self.spinBox_stock.setObjectName("spinBox_stock")
        self.formLayout_product_details.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spinBox_stock)
        self.verticalLayout_main.addLayout(self.formLayout_product_details)
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
        self.label_barcode.setText(_translate("AddProductDialog", "Barkod Numarası:"))
        self.lineEdit_barcode.setPlaceholderText(_translate("AddProductDialog", "Barkod okutun veya manuel girin"))
        self.label_name.setText(_translate("AddProductDialog", "Ürün Adı:"))
        self.lineEdit_name.setPlaceholderText(_translate("AddProductDialog", "Ürün adını girin (Örn: Coca Cola 1 Lt)"))
        self.label_purchase_price.setText(_translate("AddProductDialog", "Alış Fiyatı (TL):"))
        self.doubleSpinBox_purchase_price.setPrefix(_translate("AddProductDialog", "₺ "))
        self.label_sale_price.setText(_translate("AddProductDialog", "Satış Fiyatı (TL):"))
        self.doubleSpinBox_sale_price.setPrefix(_translate("AddProductDialog", "₺ "))
        self.label_stock.setText(_translate("AddProductDialog", "Başlangıç Stok Miktarı:"))
        self.btn_cancel.setText(_translate("AddProductDialog", "VAZGEÇ"))
        self.btn_save.setText(_translate("AddProductDialog", "ÜRÜNÜ KAYDET"))
