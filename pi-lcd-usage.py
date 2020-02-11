import board
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
import psutil
from gpiozero import CPUTemperature
from math import ceil
from socket import gethostname
from busio import I2C

# Modify this if you have a different sized Character LCD
lcd_columns = 16
lcd_rows = 2

# Initialise I2C bus.
i2c = I2C(board.SCL, board.SDA)

# Initialise the LCD class
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

lcd.clear()

lcd.color = [75, 0, 130]

while True:
    cpu_temp = ceil(CPUTemperature().temperature)
    cpu_usage = ceil(psutil.cpu_percent())
    mem_usage = ceil(psutil.virtual_memory()[2])
    
    lcd.message = "({})\nC:{} M:{} T:{}".format(gethostname(), cpu_usage, mem_usage, cpu_usage)