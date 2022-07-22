import network
import time
import ubinascii

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

print(wlan.scan())

# print(wlan.ifconfig())

# mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()

# print("MAC:" + mac)
