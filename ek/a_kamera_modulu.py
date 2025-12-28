from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2
from pyzbar.pyzbar import decode
import time

class KameraThread(QThread):
    barcode_scanned = pyqtSignal(str) 
    image_data = pyqtSignal(QImage)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.running = True
        self.camera = cv2.VideoCapture(0) 
        self.last_scanned_barcode = None
        self.last_scan_time = 0

    def run(self):
        print("Kamera Thread'i başlatıldı.")
        
        if not self.camera.isOpened():
            print("HATA: Kamera açılamadı.")
            self.running = False
            return

        while self.running:
            ret, frame = self.camera.read()
            if not ret:
                time.sleep(0.1)
                continue

            decoded_objects = decode(frame)
            
            for obj in decoded_objects:
                barcode_data = obj.data.decode('utf-8')
                
                current_time = time.time()
                if barcode_data == self.last_scanned_barcode and (current_time - self.last_scan_time) < 3: 
                    continue

                (x, y, w, h) = obj.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
                self.barcode_scanned.emit(barcode_data)
                self.last_scanned_barcode = barcode_data
                self.last_scan_time = current_time

            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            
            convert_to_qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            p = convert_to_qt_format.scaled(640, 480, Qt.KeepAspectRatio) 
            self.image_data.emit(p)
            time.sleep(0.01) 

    def stop(self):
        self.running = False
        self.wait()
        if self.camera and self.camera.isOpened():
           self.camera.release()
        cv2.destroyAllWindows()
        print("Kamera Thread'i durduruldu.")