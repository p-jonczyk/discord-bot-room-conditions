# comment if no dotenv
# import os
# from dotenv import load_dotenv

from discord.ext import commands
from temp_hum import get_sensor_readings
from sound_detection import activate_detection
import datetime
from hue_control import turn_on_off_event, change_color, change_brightness
from phue import Bridge
import random

# get env variables
# comment if no dotenv
# load_dotenv()
# TOKEN = os.getenv('BOT_TOKEN')
# GUILD = os.getenv('GUILD')
# BRIDGE_IP = os.getenv('BRIDGE_IP')


# while on RaspberryPi - do not use dotenv
TOKEN = 'BOT_TOKEN'
GUILD = 'YOUR_GUILD'
BRIDGE_IP = 'YOU_BRIDGE_IP'


# SET ADDITIONAL
b = Bridge(BRIDGE_IP)
light_name = 'desk'
degree_sign = u"\N{DEGREE SIGN}"

bot = commands.Bot(command_prefix='.')
client = commands.Bot(command_prefix='.', case_insensitive=True)


def main():

    @bot.event
    async def on_ready():
        """If ready prints in consol

        Returns: consol log"""

        print('[INFO] RUNNING ...')
        print(f'[INFO] Server name: {GUILD}')

    @bot.command(name='time', help=' -> Gives current date and time.')
    async def give_data_time(ctx):
        """Gives current date and time"""
        response = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        await ctx.send(response)

    @bot.command(name='temp', help=" -> Gives current room temperature.")
    async def give_temperature(ctx):
        """Gives room temperature after getting commend '!temp' in discord chat.

        Returns: discord chat message"""
        msg = 'It may take a few seconds...'
        await ctx.send(msg)
        sensor_readings = get_sensor_readings()
        response = f"The room's temperature is {sensor_readings[1]}{degree_sign}C"
        await ctx.send(response)

    @bot.command(name='humidity', help=" -> Gives current room humidity.")
    async def give_humidity(ctx):
        """Gives room humidity after getting commend '!hum' in discord chat.

        Returns: discord chat message"""
        msg = 'It may take a few seconds...'
        await ctx.send(msg)
        sensor_readings = get_sensor_readings()
        response = f"The room's humidity is {sensor_readings[0]}%"
        await ctx.send(response)

    @bot.command(name='sound-detection', help=" -> Starts detection of sound in the room for 10sec.")
    async def start_detection(ctx):
        # set timeout of detection
        timeout = 10000
        response = f"Sound detection activated...\nDuration is {timeout//1000}sec..."
        await ctx.send(response)
        response = activate_detection(timeout=timeout)
        await ctx.send(response)

    # LIGHTS

    @bot.command(name='light', help=" -> Turn ON/OFF light")
    async def trun_on_off_light(ctx):
        """Turn ON/OFF lights 

        Returns: discord chat message"""

        light_event = turn_on_off_event(b, light_name)
        response = light_event
        await ctx.send(response)

    @bot.command(name='light-red', help=" -> Change light color to red")
    async def color_red(ctx):
        """Turn change light color to RED 

        Returns: discord chat message"""
        color = [1, 0, 0]
        light_event = change_color(b, light_name, color)
        response = light_event
        await ctx.send(response)

    @bot.command(name='light-green', help=" -> Change light color to green")
    async def color_green(ctx):
        """Turn change light color to green 

        Returns: discord chat message"""
        color = [0, 1, 0]
        light_event = change_color(b, light_name, color)
        response = light_event
        await ctx.send(response)

    @bot.command(name='light-blue', help=" -> Change light color to blue")
    async def color_blue(ctx):
        """Turn change light color to blue 

        Returns: discord chat message"""
        color = [0, 0, 1]
        light_event = change_color(b, light_name, color)
        response = light_event
        await ctx.send(response)

    @bot.command(name='light-color-random', help=" -> Change light color to random")
    async def color_random(ctx):
        """Turn change light color to random 

        Returns: discord chat message"""
        color = [random.uniform(0, 1), random.uniform(
            0, 1), random.uniform(0, 1)]
        light_event = change_color(b, light_name, color)
        response = light_event
        await ctx.send(response)

    @bot.command(name='light-color', help=" -> Change light color to user given value")
    async def color_user(ctx):
        """Turn change light color to user input 

        Returns: discord chat message"""

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        await ctx.send("Give RGB values in form R,G,B (i.e. '0.5,0.7,3')...\nREMEMBER: values has to be from 0 to 1...")
        color_user = await bot.wait_for("message", check=check)
        color_user = color_user.content
        color = color_user.split(',')
        color = [float(x) for x in color]

        light_event = change_color(b, light_name, color)
        response = light_event
        await ctx.send(response)

    @bot.command(name='light-brightness', help=" -> Change light brightness")
    async def brightness(ctx):
        """Change brightness from user input

        Returns: discord chat message"""

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        await ctx.send('Give brightness value form 0 to 255...')
        brightness = await bot.wait_for("message", check=check)
        brightness = brightness.content
        brightness = int(brightness)

        light_event = change_brightness(b, light_name, brightness)
        response = light_event
        await ctx.send(response)

    bot.run(TOKEN)


if __name__ == '__main__':
    main()
