import machine
import utime


# Servo sweep

SERVO_PIN = 15
servo = machine.PWM(machine.Pin(SERVO_PIN))
servo.freq(50) # 50 Hz


# servo's min/max:
MIN_US = 500  # 0.5 ms
MAX_US = 2500  # 2.5 ms
PERIOD_US = 20000  # 20 ms at 50 Hz

def angle_to_duty_u16(angle):
    us = MIN_US + (MAX_US - MIN_US) * angle / 180.0
    duty = int(us / PERIOD_US * 65535)
    return max(0, min(65535, duty))


def write_angle(a):
    servo.duty_u16(angle_to_duty_u16(a))


while True:
    for a in range(0, 181, 5):
        write_angle(a)
        utime.sleep_ms(30)
    for a in range(180, -1, -5):
        write_angle(a)
        utime.sleep_ms(30)


# LED fade in/out

# pwm = machine.PWM(machine.Pin(25))  # RP2040 onboard LED pin number
# pwm.freq(1000)


# def ramp(start, stop, step, dwell_ms=6):
#     for v in range(start, stop, step):
#         pwm.duty_u16(v)
#         utime.sleep_ms(dwell_ms)


# while True:
#     ramp(0, 65535, 256)
#     ramp(65535, 0, -256)
