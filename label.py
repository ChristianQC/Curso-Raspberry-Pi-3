import sys
from PyQt5.QtWidgets import QApplication ,QWidget, QLabel,QMainWindow
from PyQt5.QtGui import QIcon

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Curso Rpi4'
        self.left = 100
        self.top = 100
        self.width = 600
        self.height = 300
        self.initUI()
    def initUI(self)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width, self.height)

        label1 = QLabel("Curso",self)
        label1.move(50,50)
       
        label2 = QLabel("RPI4",self)
        label2.move(200,200)

        label3 = QLabel("2020",self)
        label3,move(400,400)

        self.show()

if __name__ == '__main__':
    app= QApplicaction(sys.argv)
    ex = App()
    sys.exit(app.exec_())
