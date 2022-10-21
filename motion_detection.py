from machine import Pin
from utime import sleep

# Initializing of PIR-Module
pir = Pin(2, Pin.IN, Pin.PULL_DOWN)

# Initializing of Onboard-LED
led = Pin(25, Pin.OUT, value=0)

# Initializing for Buzzer
# buz = Pin(16, Pin.OUT, value=0)

# wait for PIR default
print('Wait...')
print()
sleep(3)
print('Ready')
print()

# function call at motion detection
def pir_handler(pin):
    # PIR-Sensor-Status read
    pir_value = pir.value()
    if pir_value == 1:
        # trigger alarm
        print('Alarm was triggered')
        alarm()
        # wait for sensor to 'cool down'
        sleep(2)
        print('Snooze')
        print()

def alarm():
    # Text for debugging
    print('Motion detected')
    print()
    # Buzzer on
#     buz.on()
    # LED blink
    for i in range(10):
        led.toggle()
        sleep(0.2)
#     # Buzzer off
#     buz.off()
    led.value(0) #LED off

# Initialize Interrupt for motion detection
pir.irq(trigger=Pin.IRQ_RISING, handler=pir_handler)
