import machine
import utime

pwm = machine.PWM(machine.Pin(25))  # RP2040 onboard LED pin number
pwm.freq(1000)


def ramp(start, stop, step, dwell_ms=6):
    for v in range(start, stop, step):
        pwm.duty_u16(v)
        utime.sleep_ms(dwell_ms)


while True:
    ramp(0, 65535, 256)
    ramp(65535, 0, -256)
    