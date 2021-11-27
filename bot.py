# import os
# from dotenv import load_dotenv
from discord.ext import commands
from temp_hum import get_sensor_readings
from sound_detection import activate_detection
import datetime

# get env variables
# load_dotenv()
# TOKEN = os.getenv('BOT_TOKEN')
# GUILD = os.getenv('GUILD')

# while on RaspberryPi - do not use dotenv
TOKEN = 'BOT_TOKEN'
GUILD = 'YOUR_GUILD'

degree_sign = u"\N{DEGREE SIGN}"

bot = commands.Bot(command_prefix='.')


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

    bot.run(TOKEN)


if __name__ == '__main__':
    main()
