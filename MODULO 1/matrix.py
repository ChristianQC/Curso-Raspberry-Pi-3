from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.legacy import show_message
from luma.core.legacy.font import proportional, CP437_FONT

serial = spi(port = 0 , device = 0 ,gpio = noop())
device = max7219(serial,width=8,height=8)
show_message(device, "H",fill="white", font = proportional(CP437_FONT))
