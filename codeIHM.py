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
        self.UART_checkbox.stateChanged.connect(self.UART_state)
        self.perso_button.clicked.connect(self.personalize)
        self.perso_button.clicked.connect(self.personalize)
        self.SPI_checkbox.stateChanged.connect(self.SPI_state)
        self.ANALOG_checkbox.stateChanged.connect(self.Anlog_state)
        self.I2C_checkbox.stateChanged.connect(self.I2C_state)


    def personalize(self):
        print("ok")

    def I2C_state(self):
        print("I2C : " , self.I2C_checkbox.isChecked())
        if(self.I2C_checkbox.isChecked()):
            # self.input_text.append("I2C")
            tsl = TSL2561(debug=True)
            self.input_text.append("I2C : ", tsl.lux())

    def UART_state(self):
        print("UART : " , self.UART_checkbox.isChecked())
        if(self.UART_checkbox.isChecked()):
            self.input_text.append("UART")

    def SPI_state(self):
        print("SPI : " , self.SPI_checkbox.isChecked())
        if(self.SPI_checkbox.isChecked()):
            self.input_text.append("SPI")

    def Anlog_state(self):
        print("ANALOG : " , self.ANALOG_checkbox.isChecked())
        if(self.ANALOG_checkbox.isChecked()):
            self.input_text.append("ANALOG")


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    form = Interface()
    form.show()
    app.exec_()
