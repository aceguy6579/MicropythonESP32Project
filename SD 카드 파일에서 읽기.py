# SD카드의 데이터를 읽는 방법을 알아보자

import machine, sdcard, os
from machine import SPI, Pin

spi = SPI(2, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
sd = sdcard.SDCard(spi, Pin(4))

os.mount(sd, "/sd")

file_name="/sd/text.txt"

f=open(file_name)
read_txt=f.read()
print(read_txt)
f.close()

os.umount("/sd")