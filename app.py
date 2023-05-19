# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import RPi.GPIO as io
import time

class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		# setting title
		self.setWindowTitle("PyQt GPIO ")

		# setting geometry
		self.setGeometry(100, 100, 600, 400)
		# setting GPIO
		io.setmode(io.BCM)
        # calling method
		self.UiComponents()

		# showing all the widgets
		self.show()

	# method for widgets
	def UiComponents(self):

		# creating a push button
		button = QPushButton("On Led Verde", self)
		button2 = QPushButton("Off led Verde", self)
		button3 = QPushButton("on Led Azul", self)
		button4 = QPushButton("off led Azul", self)
		button5 = QPushButton("on Led Rojo", self)
		button6= QPushButton("Off Led Rojo", self)
        # setting geometry of button
		button.setGeometry(200, 150, 100, 30)
		button2.setGeometry(300, 150, 100, 30)
		button3.setGeometry(200, 200, 100, 30)
		button4.setGeometry(300, 200, 100, 30)
		button5.setGeometry(200, 250, 100, 30)
		button6.setGeometry(300, 250, 100, 30)
        # adding action to a button
		button.clicked.connect(self.clickme)
		button2.clicked.connect(self.clickme2)
		button3.clicked.connect(self.clickme3)
		button4.clicked.connect(self.clickme4)
		button5.clicked.connect(self.clickme5)
		button6.clicked.connect(self.clickme6)
    # action method
	def clickme(self):
		led1=27
		io.setup(led1, io.OUT)
		# printing pressed
		print("on verde")
		io.output(led1,True)
    # action method
	def clickme2(self):
		led1=27
		io.setup(led1, io.OUT)
		# printing pressed
		print("off verde")
		io.output(led1,False)
	def clickme3(self):
		led2=22
		io.setup(led2, io.OUT)
		# printing pressed
		print("prende led")
		io.output(led2,True)
    # action method
	def clickme4(self):
		led2=22
		io.setup(led2, io.OUT)
		# printing pressed
		print("apaga led")
		io.output(led2,False)
	def clickme5(self):
		led3=17
		io.setup(led3, io.OUT)
		# printing pressed
		print("prende led")
		io.output(led3,True)
    # action method
	def clickme6(self):
		led3=17
		io.setup(led3, io.OUT)
		# printing pressed
		print("apaga led")
		io.output(led3,False)

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
