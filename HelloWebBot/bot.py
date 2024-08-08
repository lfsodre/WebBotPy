
# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.EDGE
    bot.driver_path = "C:\DRIVER\edgedriver_win64\msedgedriver.exe"
    bot.browse("https://github.com/lfsodre")
    
    # IMPLEMENT YOUR CODE HERE
    ...

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
