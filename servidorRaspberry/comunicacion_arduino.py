import serial,time

class arduino:
	def __init__(self):
         self.puerto_serie=serial.Serial('/dev/ttyUSB0',9600)
         print("Calibrando motor y servo")
         time.sleep(2)
         calibrado=""
         while(calibrado!="Calibrado"):
             calibrado=calibrado+self.puerto_serie.read();
         time.sleep(1)
         self.puerto_serie.write("OK")
         print("Conectado con arduino")
         time.sleep(3)
	

	def cambiaValores(self,valor_nuevo):
		self.puerto_serie.write(valor_nuevo)
	
	def cierraPuerto(self):
		self.puerto_serie.close()
	
	def abrePuerto(self):
		self.puerto_serie.open()
