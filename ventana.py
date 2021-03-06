import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
 
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
		self.show()
 
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
