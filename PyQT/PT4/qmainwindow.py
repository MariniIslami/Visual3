# =============== Menggunakan QmainWindow ============================
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow

app = QApplication([])

window = QMainWindow ()
#label = QLabel ("Label", window) # cara  1
label = QLabel (window)           # cara 2
label.setText("Label2")
label.move(200,0)

#button =QPushButton("MyButton", window) # cara 1
button = QPushButton(window)
button.setText("Button1")

window.show()
app.exec_()