import machine
import utime


# ***** Servo sweep *****

# Define which pin the servo is connected to (GPIO15)
SERVO_PIN = 15
# Create a PWM object on that pin
servo = machine.PWM(machine.Pin(SERVO_PIN))
# Standard hobby servos use ~50 Hz PWM (20 ms cycle)
servo.freq(50) 


# Pulse widths in microseconds for min/max angles
MIN_US = 500  # 0.5 ms pulse -> servo at 0 degrees
MAX_US = 2500  # 2.5 ms pulse -> servo at 180 degrees
PERIOD_US = 20000  # 20 ms total period at 50 Hz 

def angle_to_duty_u16(angle):
    """
    Convert an angle (0-180°) into the 16-bit duty cycle value
    expected by MicroPython's PWM (0-65535).
    """
    # Map the angle (0-180) to a pulse width (500-2500 microseconds)
    us = MIN_US + (MAX_US - MIN_US) * angle / 180.0
    # Convert pulse width into fraction of period, then scale to 16-bit range
    duty = int(us / PERIOD_US * 65535)
    # Clamp result to be safe (0-65535)
    return max(0, min(65535, duty))


def write_angle(a):
    """
    Tell the servo to go to a specific angle by setting the PWM duty cycle
    """
    servo.duty_u16(angle_to_duty_u16(a))


# Main loop: sweep back and forth between 0° and 180°
while True:
    # Sweep forward
    for a in range(0, 181, 5):  # 0 -> 180 in steps of 5°
        write_angle(a)  # Move servo to this angle
        utime.sleep_ms(30)  # Wait for servo to move
    # Sweep backward
    for a in range(180, -1, -5):  # 180 -> 0 in steps of 5°
        write_angle(a)
        utime.sleep_ms(30)


# ***** LED fade in/out *****

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
