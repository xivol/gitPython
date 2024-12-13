import sys

import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)
a = QMainWindow()
a.show()
sys.exit(app.exec())