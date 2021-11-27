# INPUT PIN 7 (GPIO4) / GND 9 / POWER 2

import time
import Adafruit_DHT

# set sensor type and input pin
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4


def get_sensor_readings(tries: int = 4) -> list:
    """Uses RaspberryPi with DTH11 sensor to get humidity and temperature.
    Parameter:

    tries -> number of tries to get data from sensor default = 4

    Returns: list [humidity, temperature] or list [msg, msg] if failed"""

    msg = "Unable to get sensor's readings... \nTry again later."

    while tries > 0:
        try:
            # get the values from serial port
            humidity, temp = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
            break
        except RuntimeError as error:
            print(error.args[0])
            # if error wait 2 sec
            time.sleep(2)
            continue
        tries -= 1
    if tries == 0 or not temp or not humidity:
        return [msg, msg]
    else:
        return [humidity, temp]
