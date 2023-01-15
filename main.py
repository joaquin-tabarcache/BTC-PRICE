import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import ccxt

class MainApp(QMainWindow):
    def __init__(self, parent=None, *args):
        super(MainApp, self).__init__(parent=parent)
        self.setFixedSize(250,300)
        self.setWindowTitle("Precio BTC")
        self.price = None
        self.label = QLabel("BTC: ${}".format(self.price))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Script a", 20))
        self.label.setStyleSheet("color: #fff; background-color: #1f6764; border: none; border-radius: 6px;")
        self.update_price() # Call the update_price method to set the initial label text

        self.update_button = QPushButton("Actualizar", self)
        self.update_button.clicked.connect(self.update_price)
        self.update_button.setFixedSize(280, 40)
        self.update_button.setObjectName("update-button")
        self.update_button.setStyleSheet("background-color: rgba(23, 26, 32, 0.8);  border: none; border-radius: 6px; color: #fff; font-family: SFProText-Regular, Helvetica, Arial, sans-serif; font-size: 15px; height: 36px; line-height: 20px; margin-left: 8px; margin-right: 6px; min-width: 185px; padding: 0 16px 0 16px; color:white;")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.update_button)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.show()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_price)
        self.timer.start(60000) # actualiza cada minuto

    def update_price(self):
        try:
            exchange = ccxt.binance()
            self.price = exchange.fetch_ticker('BTC/USDT')['last']
            print(self.price)
        except Exception as e:
            print(e)
            self.price = "No disponible"
        self.label.setText("BTC: ${}".format(self.price))

if __name__ == "__main__":
    app = QApplication([])
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
