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

# # Create a PWM object on pin 25 (onboard LED of Pico)
# pwm = machine.PWM(machine.Pin(25))
# # Set the PWM freq to 1000 Hz (1 kHz) so brightness changes look smooth
# pwm.freq(1000)


# def ramp(start, stop, step, dwell_ms=6):
#     """
#     Gradually change PWM duty cycle from 'start' to 'stop'
#     in increments of 'step', waiting 'dwell_ms' milliseconds
#     at each step.
#     """
#     for v in range(start, stop, step): # Loop through duty cycle values
#         pwm.duty_u16(v)  # Set LED brightness (0=off, 65535=full on)
#         utime.sleep_ms(dwell_ms)  # Short pause so fade is visible

# # Main loop: fade in, then fade out, continuously
# while True:
#     ramp(0, 65535, 256)  # Fade in: 0 -> full brightness
#     ramp(65535, 0, -256)  # Fade out: full brightness -> 0
