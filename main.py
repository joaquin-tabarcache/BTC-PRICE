import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import QTimer
import ccxt
from PyQt5.QtWidgets import QPushButton

price = None

def update_price():
    global price
    try:
        exchange = ccxt.binance()
        price = exchange.fetch_ticker('BTC/USDT')['last']
    except:
        price = "No disponible"
    label.setText("Precio: ${}".format(price))

app = QApplication(sys.argv)
window = QMainWindow()
label = QLabel("Precio: ${}".format(price))
window.setCentralWidget(label)
label.move(10, 10)
refresh_button = QPushButton("Actualizar precio", window)
refresh_button.move(80, -10)
refresh_button.clicked.connect(update_price)
window.show()
label.repaint()
update_price()


timer = QTimer()
timer.timeout.connect(update_price)
timer.start(60000)

sys.exit(app.exec_())
