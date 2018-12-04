#!/usr/bin/python

from datetime import datetime
import sys
import io
import json
import os

import RPi.GPIO as GPIO
import time
import urllib2

from util import Console
from configs import AppConfig

config_path = "/config/hvac_switch.cfg"

Console.WriteLine("")
Console.WriteLine("#######################################################")
Console.WriteLine("#######################################################")
app_config = None

with open(config_path, 'r') as content_file:
    j = json.loads(content_file.read())
    app_config = AppConfig(j)

Console.WriteLine("[{0}] Taking control of gpios",
                  datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
GPIO.setmode(GPIO.BCM)

GPIO.setup(app_config.pin_on, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(app_config.pin_off, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    input_green = GPIO.input(app_config.pin_on)
    if input_green == True:
        Console.WriteLine("[{0}] Button ON Pressed",
                         datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
        urllib2.urlopen(app_config.base_url + "/hvac/on/" + app_config.api_key + "/").read()
        time.sleep(0.2)
    input_black = GPIO.input(app_config.pin_off)
    if input_black == True:
        Console.WriteLine("[{0}] Button OFF Pressed",
                         datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
        urllib2.urlopen(app_config.base_url + "/hvac/off/" + app_config.api_key + "/").read()
        time.sleep(0.2)
