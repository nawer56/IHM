import sys
from PyQt4 import QtGui
import interface
import Adafruit_GPIO.I2C as I2C
from tsl2561 import TSL2561
import vxi11


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

	#oscillo command
	self.instr = vxi11.Instrument("172.17.2.170")

	#checkbox function
	self.ANALOG_checkbox.stateChanged.connect(self.AnalogRead)
	self.SPI_checkbox.stateChanged.connect(self.SPI)
	self.UART_checkbox.stateChanged.connect(self.UART)

	#attach function to button
	self.plus_button.clicked.connect(self.plus)
	self.minus_button.clicked.connect(self.minus)
	self.Vmax_button.clicked.connect(self.Vmax)
	self.Vpp_button.clicked.connect(self.Vpp)
	self.stop_button.clicked.connect(self.stop)

	#attach fonction to PWM
        self.pota.valueChanged.connect(self.setDuty)
	self.lineEdit.returnPressed.connect(self.setPeriod)
        self.lire_button.clicked.connect(self.readI2c)
        self.ecrire_button.clicked.connect(self.writeI2c)
	self.nom_registre.editingFinished.connect(self.getRegister)
        self.nom_donnee.editingFinished.connect(self.getData)

	self.period = 0
	self.duty = 0

	f = open("/sys/devices/ocp.3/pwm_test_P9_16.15/polarity","w")
	f.write("0")
	f.close()

	self.trame = I2C.Device(0x20,1)
	self.trame.write8(0x00,0x00)
	
########### I2C  ########

    def getData(self):
	self.data = self.nom_donnee.text()
	print(self.data)

    def getRegister(self):
        self.register = self.nom_registre.text()
	print int(self.register)

    def writeI2c(self):
	print("writeI2c")
	if (self.data != None and self.register != None):
	    print(str(self.data))
	    
            hexa = '0x'
            hexa = hexa + str(self.data)
            self.trame.write8(0x12,int(hexa,16))


    def readI2c(self):
	print("readI2c")
	self.lect = self.res_lect.text()

	hexa = '0x'
        hexa = hexa + str(self.data)
        self.res=self.trame.readU8(int(hexa,16))
	print self.res
	self.input_text.append(str(self.res))

########### OSCILLO COMMAND ########

    def Vmax(self):
	vmax = self.instr.ask(":MEAS:VMAX? CHANnel1 ")
	self.textEdit.append("Vmax " + vmax)	

    def Vpp(self):
        vpp = self.instr.ask(":MEAS:VPP? CHANnel1 ")
        self.textEdit.append("Vpp " + vpp)

    def stop(self):
	self.instr.write(":STOP")

############ AFFICHEUR #################

    def minus(self):
	self.i = self.i - 1
	if self.i == -1:
	    self.i = 15
	self.LCD_command()

    def plus(self):
	self.i = self.i + 1
	if self.i ==16:
	    self.i = 0
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

############# PERSO ##################

    def personalize(self):
        print("ok")

############ PWM ############

    def setDuty(self):

	f = open("/sys/devices/ocp.3/pwm_test_P9_16.15/period","r")
	self.period = f.read()
	f.close()

        self.duty = int(self.period) * int(self.pota.value())/10.0
	self.duty = int(self.duty)

        f = open("/sys/devices/ocp.3/pwm_test_P9_16.15/duty","w")
	f.write(str(self.duty))
	f.close()

    def setPeriod(self):
	self.period = self.lineEdit.text()
	
	f = open("/sys/devices/ocp.3/pwm_test_P9_16.15/period","w")
	f.write(self.period)
        f.close()

	
############# FONCTION PROTOCOL ##########

    def AnalogRead(self):
	f = open("/sys/devices/ocp.3/helper.14/AIN0","r")
	ana = f.read()
	f.close()
	self.input_text.append(ana)

    def I2C(self):
        tsl = TSL2561(debug=True)
        self.input_text.append("I2C : " + str(tsl.lux()))

    def UART(self):
        print("UART : " , self.UART_checkbox.isChecked())
        self.input_text.append("UART")

    def SPI(self):
        print("SPI : " , self.SPI_checkbox.isChecked())
        self.input_text.append("SPI")

############# MAIN #########

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    form = Interface()
    form.show()
    app.exec_()
