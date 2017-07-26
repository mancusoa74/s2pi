"""
Created on July 26 2017

@author: Antonio Mancuso

@version: 0.1 - July 2017

LedManager provides an abstracted Led device to the user on top of GPIOs level
"""

import log
from gpiozero import LED

class LedManager:
	leds = dict()
	
	def reset(self):
		"""
		Reset the status by cleaning the gpios dictionary
		"""
		log.info("Resetting all LEDs")
		for pin, led in self.leds.items():
			led.off()
		self.leds.clear()
		log.info(self.leds)

	def config_led(self, pin):
		"""
		Create a Led object to provide a user a higer abstraction compared to GPIO
		:param pin: the GPIO pin to configure        
                :return: None
		"""
		self.leds[str(pin)] = LED(pin)
		log.info("Configurazione LED %i  corretta" %pin)

	def set_led(self,pin, status):
		"""
		This function turn a LED on or off or to blink it
		:param pin: the LED to turn on/off
	        :param status: Acceso/Spento/Lampeggio
	        :return: None
		"""
		log.debug(self.leds[str(pin)])
		if status == 'Accendi':
			self.leds[str(pin)].on()
		elif status == 'Spegni':
			self.leds[str(pin)].off()
		elif status == 'Lampeggia':
			self.leds[str(pin)].blink()
		log.info("Impostazione stato [%s] LED %i  corretta" %(status,pin))
