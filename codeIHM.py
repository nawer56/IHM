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

	#RAZ de l'afficheur
	self.i = 0
	self.LCD_command()
	self.lcdNumber.setHexMode()

	#attach function to button
        self.perso_button.clicked.connect(self.personalize)
	self.RUN_button.clicked.connect(self.run)
	self.plus_button.clicked.connect(self.plus)
	self.minus_button.clicked.connect(self.minus)

	#attach fonction to pota
        self.pota.valueChanged.connect(self.PWM_generator)

    def run(self):
	if(self.UART_checkbox.isChecked()):
            self.UART()

        if(self.I2C_checkbox.isChecked()):
            self.I2C()

        if(self.ANALOG_checkbox.isChecked()):
            self.AnalogRead()

        if(self.SPI_checkbox.isChecked()):
            self.SPI()

    def minus(self):
	self.i = self.i - 1
	if self.i == -1:
	    self.i = 15
	print hex(self.i)
	self.LCD_command()

    def plus(self):
	self.i = self.i + 1
	if self.i ==16:
	    self.i = 0
	print hex(self.i)
	self.LCD_command()

    def LCD_command(self):
	self.lcdNumber.display(self.i)

	#code la pin A
	f = open("/sys/class/gpio/gpio30/value","w")
	if self.i not in (1,3,5,7,9,11,13,15):
	    f.write("0")
	else:
	    f.write("1")
	f.close()

	#code la pin B
	f = open("/sys/class/gpio/gpio60/value","w")
	if self.i not in (2,3,6,7,10,11,14,15):
            f.write("0")
        else:
            f.write("1")
        f.close()

        #code la pin C
        f = open("/sys/class/gpio/gpio31/value","w")
        if self.i not in (4,5,6,7,12,13,14,15):
            f.write("0")
        else:
            f.write("1")
        f.close()

        #code la pin D
        f = open("/sys/class/gpio/gpio50/value","w")
        if self.i not in (8,9,10,11,12,13,14,15):
            f.write("0")
        else:
            f.write("1")
        f.close()

    def personalize(self):
        print("ok")

    def PWM_generator(self):
        print(self.pota.value())
	duty = int(self.pota.value()*10)
        managePWM(duty=duty)

    def plotWindow(self):
        self.qwtPlot.setLabel("left","PWM_generator")
        self.qwtPlot.addLegend()

    def AnalogRead(self):
	f = open("/sys/devices/ocp.3/helper.14/AIN0","r")
	ana = f.read()
	f.close()
	self.input_text.append(ana)

    def I2C(self):
        print("I2C : " , self.I2C_checkbox.isChecked())
        tsl = TSL2561(debug=True)
        self.input_text.append("I2C : " + str(tsl.lux()))

    def UART(self):
        print("UART : " , self.UART_checkbox.isChecked())
        self.input_text.append("UART")

    def SPI(self):
        print("SPI : " , self.SPI_checkbox.isChecked())
        self.input_text.append("SPI")

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    form = Interface()
    form.show()
    app.exec_()
