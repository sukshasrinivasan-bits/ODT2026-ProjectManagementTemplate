from applink import AppInventorLink
from machine import Pin, PWM, time_pulse_us
from neopixel import NeoPixel
import time
import random

#App link
app = AppInventorLink()

# Servoss
SERVO_MIN_DUTY = 22 #30 and 120 maybe works #or make servo arm longer
SERVO_MAX_DUTY = 135

servo_pins = [22, 4, 5, 18, 19]
servos = [PWM(Pin(p), freq=50) for p in servo_pins]

servo6 = PWM(Pin(21), freq=50)  # continuous sweep

def set_angle(servo, angle):
    duty = int(SERVO_MIN_DUTY + (angle / 180.0) * (SERVO_MAX_DUTY - SERVO_MIN_DUTY))
    servo.duty(duty)

# continuous servo control
CONT_STOP = 80
CONT_FWD  = 110
CONT_REV  = 50 #if not working change to 50

def set_continuous(speed):
    servo6.duty(speed)

# Initialize servos
for s in servos:
    set_angle(s, 0)

set_continuous(CONT_STOP)

# ultrasonic sensor
trig = Pin(32, Pin.OUT)
echo = Pin(33, Pin.IN)

def get_distance():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    duration = time_pulse_us(echo, 1, 30000)
    if duration < 0:
        return None

    return (duration * 0.0343) / 2

WIN_DISTANCE = 10

# neopixell (my fav)
np = NeoPixel(Pin(13), 16)
current_led = 0

def clear():
    for i in range(16):
        np[i] = (0, 0, 0)

def rotating_red():
    global current_led
    clear()
    np[current_led] = (255, 0, 0)
    np[(current_led - 1) % 16] = (120, 0, 0)
    np[(current_led - 2) % 16] = (40, 0, 0)
    np.write()
    current_led = (current_led + 1) % 16

def celebrate():
    for _ in range(2):
        for i in range(16):
            np[i] = (0, 255, 0)
        np.write()
        time.sleep_ms(200)
        clear()
        np.write()
        time.sleep_ms(200)

    for _ in range(40):
        for i in range(16):
            np[i] = (
                random.randint(0,255),
                random.randint(0,255),
                random.randint(0,255)
            )
        np.write()
        time.sleep_ms(70)

# game state
TRIGGER_ANGLE = 165
RETURN_DELAY  = 1000 #can be in 1000-1500 range

active = [False]*5
return_time = [0]*5

# press queue
press_count = [0]*5

win_latch = False

# stability check variables
stable_count = 0
REQUIRED_STABLE = 3

# servo controls
def trigger_servo(i):
    # optional limit (avoid overload)
    press_count[i] = min(press_count[i] + 1, 5)

# WiFi control
def handle_app_request(params):
    print("App:", params)

    if params.get("servo"):
        try:
            num = int(params.get("servo"))
            if 1 <= num <= 5:
                trigger_servo(num-1)
                return {"status": "Queued " + str(num)}
        except:
            pass

    return {"status": "OK"}

app.start_ap("kmehrawifi", "zxcvbnm78")
app.on_request(handle_app_request)

# continous sweep servo
sweep_forward = True
last_sweep_toggle = 0
SWEEP_INTERVAL = 1000  # ms

# MAIN LOOP
while True:
    now = time.ticks_ms()

    try:
        app.process()
    except:
        pass

    # YAYY U WON!!!
    if not win_latch:
        dist = get_distance()

        if dist is not None and 2 < dist < WIN_DISTANCE:
            stable_count += 1
        else:
            stable_count = 0

        if stable_count >= REQUIRED_STABLE:
            win_latch = True
            set_continuous(CONT_STOP)
            celebrate()
            clear()
            np.write()

    # Neopixel LED animation
    if not win_latch:
        rotating_red()

    # Servo queue system
    for i in range(5):

        # Start movement if idle and queued
        if not active[i] and press_count[i] > 0:
            set_angle(servos[i], TRIGGER_ANGLE)
            active[i] = True
            return_time[i] = time.ticks_add(now, RETURN_DELAY)

        # Finish movement
        if active[i] and time.ticks_diff(return_time[i], now) <= 0:
            set_angle(servos[i], 0)
            servos[i].duty(0)
            active[i] = False
            press_count[i] -= 1

    # Continuous servo
    if not win_latch:
        if time.ticks_diff(now, last_sweep_toggle) > SWEEP_INTERVAL:
            sweep_forward = not sweep_forward
            last_sweep_toggle = now

        if sweep_forward:
            set_continuous(CONT_FWD)
        else:
            set_continuous(CONT_REV)

    time.sleep_ms(20)