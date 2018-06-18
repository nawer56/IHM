import sys
from PyQt4 import QtGui
import interface
from tsl2561 import TSL2561
# import Adafruit_BBIO.PWM as PWM


#Default period 10Khz
def managePWM(period=100000, duty=5 ):
    duty = duty *(period/100)
    print("period: " , period)
    print("duty: " , duty)
    #PWM.start("P9_14", duty, period, 0)
    write_pwm(period, duty)


def init_pwm():
    file = open("/sys/devices/bone_capemgr.9/slots", "w")
    if file is None:
        print("Cape not found")
    file.write("am33xx_pwm")
    file.flush()
    file.write("bone_pwm_P9_14")
    file.close()

def write_pwm(period,duty):
    #init_pwm()
    pol = open("/sys/devices/ocp.3//pwm_test_P9_14.14/polarity","w")
    dut = open("/sys/devices/ocp.3//pwm_test_P9_14.14/duty","w")
    per = open("/sys/devices/ocp.3//pwm_test_P9_14.14/period","w")
    pol.write("0")
    pol.close()
    dut.write(str(duty))
    dut.close()
    per.write(str(period))
    per.close()

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
        self.pota.valueChanged.connect(self.PWM_generator)


    def personalize(self):
        print("ok")

    def PWM_generator(self):
        print(self.pota.value())
	    duty = int(self.pota.value()*10)
        managePWM(duty=duty)

    def plotWindow(self)
        self.qwtPlot.setXaxis("PWM_generator")
        self.qwtPlot.addLegend()


    def I2C_state(self):
        print("I2C : " , self.I2C_checkbox.isChecked())
        if(self.I2C_checkbox.isChecked()):
            # self.input_text.append("I2C")
            tsl = TSL2561(debug=True)
            self.input_text.append("I2C : " + str(tsl.lux()))

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
    PWM.stop("P9_14")
    PWM.cleanup()
