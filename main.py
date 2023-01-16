import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import ccxt

class MainApp(QMainWindow):
    def __init__(self, parent=None, *args):
        super(MainApp, self).__init__(parent=parent)
        self.setFixedSize(300, 200)
        self.setWindowTitle("CRYPTO PRICE")
        self.price_btc = None
        self.price_eth = None # Agrega esta línea
        self.label_btc = QLabel("BTC: ${}".format(self.price_btc))
        self.label_eth = QLabel("ETH: ${}".format(self.price_eth)) # Agrega esta línea
        self.label_btc.setAlignment(Qt.AlignCenter)
        self.label_eth.setAlignment(Qt.AlignCenter) # Agrega esta línea
        self.label_btc.setFont(QFont("Script a", 20))
        self.label_eth.setFont(QFont("Script a", 20)) # Agrega esta línea
        self.label_btc.setStyleSheet("color: #fff; background-color: #1f6764; border: none; border-radius: 6px;")
        self.label_eth.setStyleSheet("color: #fff; background-color: #1f6764; border: none; border-radius: 6px;") # Agrega esta línea
        layout = QVBoxLayout()
        layout.addWidget(self.label_btc)
        layout.addWidget(self.label_eth)
        
        self.update_button = QPushButton("Actualizar", self)
        self.update_button.clicked.connect(self.update_price)
        layout.addWidget(self.update_button, alignment = Qt.AlignCenter) 
        self.update_button.setFixedSize(280, 40)
        self.update_button.setObjectName("update-button")
        self.update_button.setStyleSheet("background-color: rgba(23, 26, 32, 0.8);  border: none; border-radius: 6px; color: #fff; font-family: SFProText-Regular, Helvetica, Arial, sans-serif; font-size: 15px; height: 36px; line-height: 20px; margin-left: 8px; margin-right: 6px; min-width: 185px; padding: 0 16px 0 16px; color:white;")

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
            self.price_btc = exchange.fetch_ticker('BTC/USDT')['last']
            self.price_eth = exchange.fetch_ticker('ETH/USDT')['last'] 
            print(self.price_btc, self.price_eth)
        except Exception as e:
            print(e)
            self.price_btc = "No disponible"
            self.price_eth = "No disponible" 
        self.label_btc.setText("BTC: ${}".format(self.price_btc))
        self.label_eth.setText("ETH: ${}".format(self.price_eth))

if __name__ == "__main__":
    app = QApplication([])
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
