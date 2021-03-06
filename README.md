## ABOUT

This program uses RaspberryPi and connected sensors to obtain room's temperature, humidity and detects sound/noise (peeks like **claps** or **snaps**).
In addition it allows to control *hue lights* via discord commends.
Those data are accessed through ***Discord*** server/guild of choice with use of **BOT** when user use proper commands.
<br /> 
<br />

## WHAT IS NEEDED

1. RaspberryPi (following project was performed with use of RaspberryPi Zero WH)
2. Sensors:
    - Temperature/Humidity sensor (DHT11) (*[**example 'How to set temperature/humidity sensor'**](https://medium.com/initial-state/how-to-build-a-raspberry-pi-temperature-monitor-8c2f70acaea9)*)
    - Sound/Noise sensor (cheapest 3 pin 5V) (*[**example 'How to set sound/noise sensor'**](https://www.instructables.com/Using-a-sound-sensor-with-a-Raspberry-Pi-to-contro/)*)
3. Discord server/guild with BOT (*[**example 'How to create'**](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/)*)
4. Hue Bridge and light (if control hue lights functionality is considered)
<br />

## INSTALLATION

If your sensors are connected and RaspberryPi is set:
1. In RaspberyPi terminal type:
    - **pip3 install discord**
    - **pip3 install Adafruit_DHT**
    - **pip3 install discord**
    - **pip3 install phue**

2. In *bot.py* set values of:
    - **TOKEN** - Discord BOT token 
    - **GUILD** - Discord guild/server name
    - **BRIDGE_IP** - Your heu bridge ip
<br />

## HOW TO

1. Run ***bot.py***
2. Go to choosen Discord guild/server (where you added BOT)
3. Check all available commands by typing:
    - ***.help*** at Discord chat
4. Try them out !
<br />


## ADDITIONALLY

Phillips hue light is controlled with use of light's name. In order to change that variable go to **hue_control.py**.