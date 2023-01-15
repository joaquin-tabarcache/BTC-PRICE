import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import ccxt

class MainApp(QMainWindow):
    def __init__(self, parent=None, *args):
        super(MainApp, self).__init__(parent=parent)
        self.setFixedSize(300,300)
        self.setWindowTitle("Precio BTC")
        self.price = None
        self.label = QLabel("Precio: ${}".format(self.price))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 20))
        self.label.setStyleSheet("color: #fff; background-color: #424242;")
        self.update_price() # Call the update_price method to set the initial label text

        self.update_button = QPushButton("Actualizar", self)
        self.update_button.clicked.connect(self.update_price)

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
        self.label.setText("Precio: ${}".format(self.price))

if __name__ == "__main__":
    app = QApplication([])
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
