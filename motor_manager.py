"""
Created on July 26 2017

@author: Antonio Mancuso

@version: 0.1 - July 2017

MotorManager provides an abstracted Motor device to the user on top of GPIOs level
"""

import log
from gpiozero import Motor
from time import sleep

class MotorManager:
	motors = dict()
	
	def reset(self):
		"""
		Reset the status by cleaning the gpios dictionary
		"""
		log.info("Resetting all MOTORs")
		for name, motor in self.motors.items():
			log.info(name)
			log.debug(motor)
			motor.stop()
		self.motors.clear()
		log.debug(self.motors)

	def config_motor(self, motor, pin1, pin2):
		"""
		Create a Motor object to provide a user a higer abstraction compared to GPIO
		:param motor: the name of the motor
		:param pin1: the GPIO to use to control the motor
		:param pin2: the GPIO to use to control the motor
        :return: None
		"""
		self.motors[motor] = Motor(forward = pin1, backward = pin2)
		self.motors[motor].stop()
		log.info("Configurazione Motore %s  corretta" %motor)

	def start_motor_wait(self, motor, seconds, direction):
		"""
		Start a motor for seconds
		:param motor: the name of the motor
		:param seconds: number of seconds the moto should be on
		:param direction: direction of spinning
        :return: None
		"""
		
		log.info("Avvio motore %s per %i secondi in direzione %s" %(motor, seconds, direction))
		if direction == 'Avanti':
			self.motors[motor].forward()
		elif direction == 'Indietro':
			self.motors[motor].backward()
		sleep(seconds)
		self.motors[motor].stop()

	def start_motor(self, motor, direction):
		"""
		Start a motor
		:param motor: the name of the motor
		:param direction: direction of spinning
        :return: None
		"""
		
		log.info("Avvio motore %s in direzione %s" %(motor, direction))
		if direction == 'Avanti':
			self.motors[motor].forward()
		elif direction == 'Indietro':
			self.motors[motor].backward()
		
	def stop_motor(self, motor):
		"""
		Stop a motor
		:param motor: the name of the motor
        :return: None
		"""
		
		log.info("Stop motore %s" %motor)
		self.motors[motor].stop()
		