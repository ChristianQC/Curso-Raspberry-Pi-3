import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QSlider
from PyQt5.QtCore import Qt

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        
        mySlyder = QSlider(Qt.Horizontal,self)
        mySlyder.setMaximun(254)
        mySlyder.setMinimun(0)
		mySlyder.setGeometry(30,40,200,30)
        mySlyder.valueChanged[int].connect(self.changedValue)
        
        self.setGeometry(50,50,320,200)
        self.setWindowTitle("Curso RPI4")
        self.show()
    def changeValue(self,value):
        print(value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
