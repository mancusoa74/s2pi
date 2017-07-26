"""
Created on July 26 2017

@author: Antonio Mancuso

@version: 0.1 - July 2017

s2pi is a simple helper function to allow the use Scratch2 Off-line editor to control Raspberry-Pi board
The main goal is to allow a user to control the Raspberry-Pi board from his own computer using the well known Scratch2 environment
Compared to other implementation the main difference is that s2pi helper function does run diorectly on Raspberry-pi board
It requires a simple port forwarding on user's PC
"""

from flask import Flask
import gpiozero
import logging
import log
from gpio_manager import GpioManager
from led_manager import LedManager

#initialize the GPIO manager
gpios = GpioManager()

#initialize the LED manager
leds = LedManager()


#initialize Flask application
app = Flask(__name__)

#initialize logging
log.init(logging.DEBUG)

log.info("Starting s2pi v1.0")

@app.route('/poll')
def poll():
	"""
	A HTTP poll request is sent by Scratch 30 times per second
	This function return the status of the gpios through GpioManager
	"""
	return gpios.poll()
    
@app.route('/reset_all')
def reset_all():
	"""
	A HTTP reset_all request is sent by Scratch anytime a new script is run
	The goal of this request is to reset the board to the initial status
	"""
	log.info("HTTP /reset_all")
	gpios.reset()
	leds.reset()
	log.debug(gpios.gpios)
	log.debug(leds.leds)
	return 'OK'

#GPIO helper
@app.route('/config_gpio/<int:pin>/<string:direction>', methods=['GET'])
def config_gpio(pin, direction):
	"""
	A HTTP config_gpio request is sent by Scratch when the 'Configura Pin Digitale' block is used
	"""
	log.info("HTTP /config_gpio/%i/%s" %(pin, direction))
	gpios.config_gpio(pin, direction)
	log.debug(gpios.gpios)
	return 'OK'

@app.route('/set_gpio/<int:pin>/<string:status>', methods=['GET'])
def set_gpio(pin, status):
	"""
	A HTTP set_gpio request is sent by Scratch when the 'Porta Pin Digitale a' block is used
	"""
	log.info("HTTP /set_gpio/%i/%s" %(pin, status))
	gpios.set_gpio(pin, status)
	return 'OK'


#LED helper
@app.route('/config_led/<int:pin>', methods=['GET'])
def config_led(pin):
	"""
	A HTTP config_led request is sent by Scratch when the 'Collega Led Pin Digitale' block is used
	"""
	log.info("HTTP /config_led/%i" %pin)
	leds.config_led(pin)
	log.debug(leds.leds)
	return 'OK'

@app.route('/set_led/<string:status>/<int:pin>', methods=['GET'])
def set_led(pin, status):
	"""
	A HTTP set_gpio request is sent by Scratch when the 'Porta Pin Digitale a' block is used
	"""
	log.info("HTTP /set_led/%i/%s" %(pin, status))
	leds.set_led(pin, status)
	return 'OK'