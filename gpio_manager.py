"""
Created on July 26 2017

@author: Antonio Mancuso

@version: 0.1 - July 2017

GpioManager manages the status and the interaction with the Raspberry-Pi GPIOs
"""

import log
import gpiozero

class GpioManager:
	gpios = dict()
	
	def reset(self):
		"""
		Reset the status by cleaning the gpios dictionary
		"""
		log.info("Resetting all GPIOs")
		for pin, gpio in self.gpios.items():
			gpio['gpio'].close()
			del self.gpios[pin]

	def config_gpio(self, pin, direction):
		"""
		Based on the direction instanciate a specific DigitalDevice obect for the given pin
		:param pin: the GPIO pin to configure
	        :param direction: the direction of the pin Ingresso/Uscita
	        :return: None
		"""
		if direction == "Uscita":
			self.gpios[str(pin)] = {'gpio': gpiozero.DigitalOutputDevice(pin, active_high=True, initial_value=False), 'direction': 'OUT'}        
		elif direction == "Ingresso":
			self.gpios[str(pin)] = {'gpio': gpiozero.DigitalInputDevice(pin, pull_up=True, bounce_time=0.1), 'direction': 'IN'}
		log.info("Configurazione GPIO %i [%s] corretta" %(pin, direction))

	def set_gpio(self,pin, status):
		"""
		This function guarantees that only pin which are configured as Output/Uscita can be set to a logical level by the user
		:param pin: the GPIO pin to configure
       		:param status: the logical level of the pin Alto/Basso
	        :return: None
		"""
		log.debug(self.gpios[str(pin)]['direction'])
		log.debug(self.gpios[str(pin)])
		if self.gpios[str(pin)]['direction'] == 'OUT':
			if status == 'Alto':
				self.gpios[str(pin)]['gpio'].on()
			elif status == 'Basso':
				self.gpios[str(pin)]['gpio'].off()
			log.info("Impostato GPIO %i [Uscita] a %s" %(pin, status))
		else:
			log.error("Impossibile impostare GPIO %i [Ingresso] a %s" %(pin, status))

	def poll(self):
		"""
		Report the status of each Input/Ingresso pin
		"""
		poll_reply = 'OK\n'

		for pin, gpio in self.gpios.items():
			if gpio['direction'] == 'IN':
				value = gpio['gpio'].value
				poll_reply = poll_reply + "get_gpio/" + str(pin) + " " + str(value).lower() + "\n"
		return poll_reply


