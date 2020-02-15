import sys
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):
 
	def __init__(self):
		super().__init__()
		self.title = 'Curso RPi4'
		self.left = 200
		self.top = 200
		self.width = 600
		self.height = 300
		self.initUI()
	 
	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		#crear boton
		button = QPushButton("Alerta",self)
		button.move(100,70)
		button.clicked.connect(self.on_click)
		self.show()
	
	@pyqtSlot()	 
	def on_click(self):
	    print("Se presiono")	
 
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
