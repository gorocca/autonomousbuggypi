from comunicacion_arduino import arduino
import socket
import sys
import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT) ## GPIO 18 como salida
GPIO.setup(23, GPIO.OUT) ## GPIO 23 como salida
GPIO.setup(24, GPIO.OUT)
GPIO.output(24, True) ## Enciendo el 24


arduino = arduino() #instanciamos el arduino


print("Lanzando mjpg-streamer")
os.system('/home/pi/mjpg/mjpg-streamer/mjpg_streamer -i "/home/pi/mjpg/mjpg-streamer/input_uvc.so -d /dev/video0 -y" -o "/home/pi/mjpg/mjpg-streamer/output_http.so -w /home/pi/mjpg/mjpg-streamer/www" &')

# Creando el socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Enlace de socket y puerto
server_address = ("192.168.0.1", 10000)
print >>sys.stderr, 'empezando a levantar %s puerto %s' % server_address
sock.bind(server_address)
# Escuchando conexiones entrantes
sock.listen(1)

GPIO.output(23, True) ## Enciendo el 23
GPIO.output(24, False) ## Apago el 24

while True:
    # Esperando conexion
    print >>sys.stderr, 'Esperando para conectarse'
    connection, client_address = sock.accept()

    try:
        print >>sys.stderr, 'concexion desde', client_address
	GPIO.output(18, True) ## Enciendo el 18
        # Recibe los datos en trozos y reetransmite
        while True:
            data = connection.recv(10)
            print >>sys.stderr, 'recibido "%s"' % data
            if data == 'close':
                print >>sys.stderr, 'close recibido, cerrando conexion', client_address
                arduino.cambiaValores("[0,90]")
		GPIO.output(18, False) ## Apago el 18
                break
            elif data == "":
                print >>sys.stderr, 'cerrando conexion no se ha recibido nada', client_address
                arduino.cambiaValores("[0,90]")
		GPIO.output(18, False) ## Apago el 18
                break
            elif data:
                print >>sys.stderr, 'procesando el mensaje'
                arduino.cambiaValores(data)

    finally:
        # Cerrando conexion
        connection.close()
	    GPIO.cleanup() ## Hago una limpieza de los GPIO
