#QtQui QTCore QTWidgets
# ================== Cara 1 ================================
from PyQt5 import QtGui, QtCore, QtWidgets
app = QtWidgeds.QApplication([])
window = QtWidgets.QPushButton("MyButton")
window.show()
app.exec_()
# ================== Cara 2 =================================
from PyQt5.Qtwidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
app = Qapplication([])
window = QtWidgets.QPushButton("MyButton")
window.show()
app.exec_()
# ================= Cara 3 =================================
from PyQt5 import QtWidgets as qtw
app = qtw.QApplication([])
window = QtWidgets.QPushButton("MyButton")
window.show()
app.exec_()
# ================= Cara 4 =================================
from PyQt5.Qtwidgets import QApplication, QPushButton
app = qtw.QApplication([])
window = QtWidgets.QPushButton("MyButton")
window.show()
app.exec_()