# comment if no dotenv
# import os
# from dotenv import load_dotenv

from phue import Bridge
from rgb_to_xy import rgb_to_xy

# get env variables
# comment if no dotenv
# load_dotenv()
# BRIDGE_IP = os.getenv('BRIDGE_IP')

BRIDGE_IP = 'YOU_BRIDGE_IP'


def turn_on_off_event(b, name: str):
    """Turn on or off light
    Parameter:

    b -> bridge

    name -> name of lights"""

    b.connect()
    lights = b.get_light_objects('name')
    # boolen
    if lights[name].on:
        lights[name].on = False
        return 'Light turned off'
    else:
        lights[name].on = True
        return 'Light turned on'


def change_color(b, name: str, color: list):
    """Changes light color

    Parameters:
    b -> bridge

    name -> name of lights

    color -> list of RGB with each value from set <0, 1> """

    b.connect()
    lights = b.get_light_objects('name')

    for value in color:
        if 0 > value or value > 1:
            return 'Invalide color was given... '

    color = rgb_to_xy(color[0], color[1], color[2])

    if lights[name].on:
        lights[name].xy = color
        if color == [1, 0, 0]:
            return 'Light colore changed to red.'
        elif color == [0, 1, 0]:
            return 'Light colore changed to green.'
        elif color == [0, 0, 1]:
            return 'Light colore changed to blue.'
        else:
            return 'Light color changed!'
    else:
        return 'Light is off...'


def change_brightness(b, name: str, brightness: int):
    """Changes light brightness

    Parameters:
    b -> bridge

    name -> name of lights

    brightness -> 0 - 254 """

    b.connect()
    lights = b.get_light_objects('name')

    if 0 > brightness or brightness > 255:
        return 'Invalide brightness was given... '

    if lights[name].on:
        lights[name].brightness = brightness
        return f'Light brightness changed to {brightness}!'
    else:
        return 'Light is off...'


def main():
    b = Bridge(BRIDGE_IP)
    light_name = 'desk'
    # turn_on_off_event(b, light_name)
    color = [0.2, 0.7, 0.5]
    print(change_color(b, light_name, color))
    brightness = 200
    print(change_brightness(b, light_name, brightness))


if __name__ == '__main__':
    main()
