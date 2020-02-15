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
		
		#crear label
		self.label = QLabel("Apagado",self)
		self.label.move(50,50)
		
		#crear primer boton
		button1 = QPushButton("Encendido",self)
		button1.move(100,70)
		button1.clicked.connect(self.on_click)
		#crear segundo boton
		button2 = QPushButton("Apagado",self)
		button2.move(100,120)
		button2.clicked.connect(self.on_click1)
		
		self.show()
	
    @pyqtSlot()	 
	def on_click(self):
	    self.label.setText("Encendido")
	    self.label.adjustSize()
	    
			
     @pyqtSlot()	 
	def on_click1(self):
	    self.label.setText("Apagado")
	    self.label.adjustSize()
	    
	    
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
