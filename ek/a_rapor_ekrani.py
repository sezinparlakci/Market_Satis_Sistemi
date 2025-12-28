import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from datetime import datetime, timedelta 
from collections import defaultdict  
from ui.ui_rapor_ekran import Ui_ReportScreen

class RaporUygulamasi(QDialog):
    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.ui = Ui_ReportScreen()
        self.ui.setupUi(self)
        self.db = db
        self.showMaximized()

        self.güncel_alis_maliyet_list = {} 

        header = self.ui.tableWidget_report.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        
        self.setup_connections()

    def setup_connections(self):
        self.ui.btn_close_report.clicked.connect(self.close)
        self.ui.btn_daily_sales.clicked.connect(self.generate_report)

    #üstteki kısmı günceller totalde durumun ne olduğunu
    def update_dashboard_cards(self, revenue, cost, profit):
        self.ui.lbl_total_revenue.setText(f"₺ {revenue:,.2f}")
        self.ui.lbl_total_cost.setText(f"₺ {cost:,.2f}")
        self.ui.lbl_total_profit.setText(f"₺ {profit:,.2f}")
        
        palette = self.ui.lbl_total_profit.palette()
        if profit >= 0:
            palette.setColor(QPalette.WindowText, Qt.darkGreen)
        else:
            palette.setColor(QPalette.WindowText, Qt.red)
        self.ui.lbl_total_profit.setPalette(palette)

        margin = (profit / revenue * 100) if revenue > 0 else 0
        self.ui.lbl_margin.setText(f"% {margin:.1f}")

    def fetch_current_costs(self):
        self.güncel_alis_maliyet_list = {}
        try:
            if hasattr(self.db, 'get_all_products'):
                products = self.db.get_all_products()
                for p in products:
                    barcode = p.get('barcode')
                    cost = p.get('purchase_price', 0) 
                    self.güncel_alis_maliyet_list[barcode] = float(cost)
        except Exception as e:
            print(f"Maliyetler çekilemedi: {e}")

    def get_real_cost(self, item):
        cost = item.get('purchase_price')
        if cost is None:
            barcode = item.get('barcode')
            cost = self.güncel_alis_maliyet_list.get(barcode, 0)
        return float(cost)

    def generate_report(self):
        if not self.db.connected:
            QMessageBox.warning(self, "Hata", "Veritabanı bağlantısı yok!")
            return

        self.fetch_current_costs()

        start_date_q = self.ui.dateEdit_start.date().toPyDate()
        end_date_q = self.ui.dateEdit_end.date().toPyDate()
        start_date = datetime(start_date_q.year, start_date_q.month, start_date_q.day)
        end_date = datetime(end_date_q.year, end_date_q.month, end_date_q.day, 23, 59, 59)

        self.ui.tableWidget_report.setRowCount(0)
        self.ui.tableWidget_report.clearContents()

        try:
            data = self.db.get_sales_report(start_date, end_date)
            self.populate_daily_sales(data, start_date, end_date)
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Rapor hatası: {str(e)}")

    def populate_daily_sales(self, sales_data, start_date, end_date):
        headers = ["Tarih", "İşlem", "Nakit", "K. Kartı", "İade", "Top. Ciro", "Maliyet", "Net Kâr", "Marj %"]
        self.ui.tableWidget_report.setColumnCount(len(headers))
        self.ui.tableWidget_report.setHorizontalHeaderLabels(headers)

        grouped_data = defaultdict(lambda: {
            'count': 0, 
            'revenue': 0.0, 
            'cost': 0.0, 
            'cash': 0.0, 
            'card': 0.0, 
            'refund': 0.0
        })
        
        total_rev = 0
        total_cost = 0

        for sale in sales_data:
            date_val = sale.get('created_at')
            if not date_val: continue
            if isinstance(date_val, str):
                try: date_val = datetime.strptime(date_val, "%Y-%m-%d %H:%M:%S")
                except: continue
            
            day_key = date_val.strftime('%Y-%m-%d')
            
        
            try:
                raw_amount = float(sale.get('total_amount', 0))
            except:
                raw_amount = 0.0

            payment_type = str(sale.get('payment_type', '')).lower()
            
            if raw_amount < 0 or 'iade' in payment_type:
                refund_val = abs(raw_amount)
                grouped_data[day_key]['refund'] += refund_val
                
            
                effect_on_revenue = -refund_val
                grouped_data[day_key]['revenue'] += effect_on_revenue
                total_rev += effect_on_revenue
            
            else:
             
                grouped_data[day_key]['revenue'] += raw_amount
                total_rev += raw_amount
     
                if 'kart' in payment_type or 'card' in payment_type:
                    grouped_data[day_key]['card'] += raw_amount
                else:
         
                    grouped_data[day_key]['cash'] += raw_amount

            cst = 0.0
            items = sale.get('items', [])
            if isinstance(items, list):
                for item in items:
                    try:
                        qty = float(item.get('quantity', 0))
                        unit_cost = self.get_real_cost(item)
                        if raw_amount < 0 or 'iade' in payment_type:
                            cst -= (unit_cost * abs(qty))
                        else:
                            cst += (unit_cost * qty)
                    except:
                        pass

            grouped_data[day_key]['count'] += 1
            grouped_data[day_key]['cost'] += cst
            total_cost += cst

        # Tarih listesini oluştur
        current = start_date
        date_list = []
        while current <= end_date:
            date_list.append(current.strftime('%Y-%m-%d'))
            current += timedelta(days=1)
        date_list.sort(reverse=True)

        row = 0
        for day in date_list:
            stats = grouped_data.get(day, {
                'count': 0, 'revenue': 0.0, 'cost': 0.0, 
                'cash': 0.0, 'card': 0.0, 'refund': 0.0
            })
            
            profit = stats['revenue'] - stats['cost']
            margin = (profit / stats['revenue'] * 100) if stats['revenue'] > 0 else 0

            self.ui.tableWidget_report.insertRow(row)
            self.ui.tableWidget_report.setItem(row, 0, QTableWidgetItem(day))
            self.ui.tableWidget_report.setItem(row, 1, QTableWidgetItem(str(stats['count'])))
            
            self.ui.tableWidget_report.setItem(row, 2, QTableWidgetItem(f"₺ {stats['cash']:.2f}"))
            self.ui.tableWidget_report.setItem(row, 3, QTableWidgetItem(f"₺ {stats['card']:.2f}"))
            
            # İade Sütunu 
            item_refund = QTableWidgetItem(f"₺ {stats['refund']:.2f}")
            item_refund.setForeground(QColor("red"))
            self.ui.tableWidget_report.setItem(row, 4, item_refund)
            
            self.ui.tableWidget_report.setItem(row, 5, QTableWidgetItem(f"₺ {stats['revenue']:.2f}"))
            self.ui.tableWidget_report.setItem(row, 6, QTableWidgetItem(f"₺ {stats['cost']:.2f}"))
            
            # Net Kar
            item_profit = QTableWidgetItem(f"₺ {profit:.2f}")
            if profit >= 0:
                item_profit.setForeground(QColor("darkGreen"))
            else:
                item_profit.setForeground(QColor("red"))
            self.ui.tableWidget_report.setItem(row, 7, item_profit)

            self.ui.tableWidget_report.setItem(row, 8, QTableWidgetItem(f"% {margin:.1f}"))
            row += 1

        self.update_dashboard_cards(total_rev, total_cost, total_rev - total_cost)