import sys
from PyQt4 import QtGui
import interface
from tsl2561 import TSL2561

class Interface(QtGui.QMainWindow, interface.Ui_MainWindow):
    def __init__(self, parent=None):
        # access variables, methods etc in the interface.py file
        super(Interface, self).__init__(parent)
        # Sets up layout and widgets that are defined
        self.setupUi(self)
        self.perso_button.clicked.connect(self.personalize)
        # self.perso_button.clicked.connect(self.personalize)
        # self.UART_checkbox.stateChanged.connect(self.state)
        # self.SPI_checkbox.stateChanged.connect(self.state)
        # self.ANALOG_checkbox.stateChanged.connect(self.state)
        self.I2C_checkbox.stateChanged.connect(self.state)

    def personalize(self):
        print("ok")

    def state(self):
        print("I2C : " , self.I2C_checkbox.isChecked())
        tsl = TSL2561(debug=True)
        print(tsl.lux())

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    form = Interface()
    form.show()
    app.exec_()
