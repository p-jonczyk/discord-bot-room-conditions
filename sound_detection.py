# INPUT PIN 18 (GPIO24) / GND 20 / POWER 4
import time
import RPi.GPIO as GPIO


# broadcome
GPIO.setmode(GPIO.BCM)
# input pin
pin = 24
# setup input
GPIO.setup(pin, GPIO.IN)


def activate_detection(timeout: int = 10000) -> str:
    """Active sound detection

    Parameter: 
    timeout: duration of detection default 10 sec
             (value in milisec)
    """
    msg = 'Sound detected in the room !'
    no_sound_msg = "No sound detected in the room."

    # waiting for edge cases for seted time
    response = GPIO.wait_for_edge(pin, GPIO.RISING, timeout=timeout)
    if response:
        return msg
    elif response is None:
        return no_sound_msg


if __name__ == '__main__':
    print(activate_detection())
