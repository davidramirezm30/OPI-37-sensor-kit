# -*- coding: utf-8 -*-
##############################
# Importar librerias
import os
import sys

from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port
##############################

led = port.PA21
vibrador = port.PC7

# Inicializamos el objeto gpio
gpio.init()

# Establecemos el pin asociado al LED como salida digital
gpio.setcfg(led, gpio.OUTPUT)
gpio.setcfg(vibrador, gpio.INPUT)

# Realizar un parpadeo del LED hasta que se reciba la senial del sistema correspondiente a Ctrl+C
try:
 # Mostrar por pantalla
 print ("Presiona CTRL+C para salir")
 
 # Bucle infinito
 while True:
	if gpio.input(port.PC7) == 0:
		#print ("\nVibrandoooo") 							#KY-002
		#print ("\nHay un imán cerca. \n¡ALLAHU AKBAR!") 	#KY-003
		print ("\nHas pulsado el botón") 					#KY-004
		#print ("\nHay un imán cerca. \n¡ALLAHU AKBAR!") 	#KY-005
		gpio.output(led, 1) # Encender LED
		sleep(0.25) # Esperar 250ms
		gpio.output(led, 0) # Apagar LED
		sleep(0.25) # Esperar 250ms

		gpio.output(led, 1) # Encender LED 	
		sleep(0.25) # Esperar 250ms
		gpio.output(led, 0) # Apagar LED
		sleep(0.25) # Esperar 250ms

		sleep(1) # Esperar 1 segundo

# Senial provocada por Ctrl+C
except KeyboardInterrupt:
 # Mostrar por pantalla
 print ("\nFin del programa")
