import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import QTimer
import ccxt
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtWidgets import QHBoxLayout

price = None


def update_price():
    global price
    progress_bar.setValue(0)
    progress_bar.show()
    try:
        exchange = ccxt.binance()
        price = exchange.fetch_ticker('BTC/USDT')['last']
    except:
        price = "No disponible"
    label.setText("Precio: ${}".format(price))
    progress_bar.setValue(100)
    progress_bar.hide()

app = QApplication(sys.argv)
window = QMainWindow()
h_layout = QHBoxLayout()
label = QLabel("Precio: ${}".format(price))
window.setCentralWidget(label)
label.move(10, 10)
refresh_button = QPushButton("Actualizar precio", window)
h_layout.addWidget(refresh_button)
refresh_button.clicked.connect(update_price)
progress_bar = QProgressBar(window)
progress_bar.setRange(0, 100)
progress_bar.setValue(0)
progress_bar.move(10, 40)
progress_bar.hide()
window.setLayout(h_layout)
window.show()
label.repaint()
update_price()


timer = QTimer()
timer.timeout.connect(update_price)
timer.start(60000)

sys.exit(app.exec_())
