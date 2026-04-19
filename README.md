# Open Design and Technology  
## Final Project README

> **Project Weight:** 70%  
> **Team Size:** 2 students  
> **Project Duration:** 4 weeks  
> **Class Time Available:** 6 hours per class  
> **Total Time Available:** 48 effort-hours per team  
> **Project Type:** Playful, interactive, technology-based experience

---

# Before you begin

## Fork and rename this repository
After forking this repository, rename it using the format:

`ODT-2026-PULLPIN`

### Example
`ODT-2026-PixelWizards`

Do not keep the default repository name.

---

# How to use this README

This file is your team’s **working project document**.

You must keep updating it throughout the 4-week build period.  
By the final review, this README should clearly show:
- your idea,
- your planning,
- your design decisions,
- your technical process,
- your build progress,
- your testing,
- your failures and changes,
- your final outcome.

## Rules
- Fill every section.
- Do not delete headings.
- If something does not apply, write `Not applicable` and explain why.
- Add images, screenshots, sketches, links, and videos wherever useful.
- Update task status and weekly logs regularly.
- Use this file as evidence of process, not only as a final report.

---

# 1. Team Identity

## 1.1 Studio / Group Name
`[Khushi and Suksha]`

## 1.2 Team Members

| Name | Primary Role | Secondary Role | Strengths Brought to the Project |
|---|---|---|---|
| `[Khushi]` | `[Electronics / App / Fabrication / Mechanics]` | `[making the physical setup and app]` | `[Physical build of the setup and mechanics]` |
| `[Suksha]` | `[Electronics / Coding/ Debugging]` | `[Coding and electronics]` | `[Coding prowess and troubleshooting]` |

## 1.3 Project Title
`[Pull pin game]`

## 1.4 One-Line Pitch
`[A game where you have to drop coins through a maze by testing your reaction time]`

## 1.5 Expanded Project Idea
In 1–2 paragraphs, explain:
- what your project is,
- what kind of playful experience it creates,
- what makes it fun, curious, engaging, strange, satisfying, competitive, or delightful,
- what technologies are involved.

**Response:**  
`[A game with several pins that need to pulled out using a web interface to make a coin/ several coins together go through and obstacle course down the correct shoot into the bucket which holds an ultra sonic sensor. It creates a fun and adrenaline filled game of chance. It is based partially on chance and partially on reflexes, the time sensitivity, and planning.]`

---

# 2. Philosophy Fit

## 2.1 Experience, Not Social Problem
This module does **not** require your project to solve a large social problem.

You are allowed to build:
- toys,
- games,
- interactive objects,
- playful machines,
- kinetic artifacts,
- humorous devices,
- strange but delightful experiences,
- things that are entertaining to use or watch.

## 2.2 What kind of experience are you creating?
Answer the following:
- What is the experience?
- What do you want the player or participant to feel?
- Why would someone want to try it again?

**Response:**  
`[This project creates an interactive, arcade-like experience where players trigger mechanisms to release coins and aim to achieve a winning condition. The experience is fast, responsive, and visually engaging, combining physical movement with light feedback. The player should feel excitement, anticipation, and a sense of control while interacting with the system. The unpredictability of outcomes and the satisfying physical response encourage repeated attempts and playful experimentation.]`

## 2.3 Design Persona
Complete the sentence below:

> We are designing this project as if we are a small creative studio making a **[toy / game / playable object / interactive experience]** for **[children / teens / adults / classmates / exhibition visitors / mixed audience]**.

**Response:**  
`[We are designing this project as if we are a small creative studio making an interactive game for a mixed audience of classmates and exhibition visitors, focusing on creating a playful, engaging, and easy-to-understand experience that invites quick participation and repeat interaction.]`

---

# 3. Inspiration

## 3.1 References
List what inspired the project.

| Source Type | Title / Link | What Inspired You |
|---|---|---|
| `[Toy /App/ Website]` | `[(https://poki.com/en/g/how-to-loot-pin-pull)]` | `[to be filled]` |
| `[Toy / Game]` | `[Coin pusher arcade machines and the idea of using coins, physical reward systems, and repeatable play for engagement]` | `[What did you learn or borrow?]` |
| `[Object]` | `[Servo-based mechanisms]` | `[Using controlled mechanical movement to create precise, repeatable interactions.]` |

## 3.2 Original Twist
What makes your project original?

**Response:**  
`[The project translates a digital pin-pull game into a physical, interactive system using servos, sensors, and real coins. It combines app-based control with tangible mechanics, adding unpredictability through real-world physics and feedback through lights and motion, making the experience more immersive and playful than its digital inspiration.]`

---

# 4. Project Intent

## 4.1 Core Interaction Loop
Describe the main loop of interaction.

Examples:
- press → launch → score → reset
- connect → control → observe → repeat
- turn → trigger → react → repeat
- move object → sensor detects → sound/light response → player reacts

**Response:**  
`[Connect → Select pin (app) → Trigger servo (pull pin) → Coin drops → Ultrasonic sensor detects → light as experience (NeoPixel) → Observe result → Repeat]`

## 4.2 Intended Player / Audience

| Question | Response |
|---|---|
| Who is this for? | `[Students, casual players, and exhibition visitors interested in interactive physical-digital games]` |
| Age range | `[9+]` |
| Solo or multiplayer | `[Primarily solo, but can be played turn-based in groups]` |
| Expected duration of one round | `[2-5 minutes]` |
| What should the player feel? | `[Curiosity, anticipation, and satisfaction through cause-and-effect interaction, along with playful engagement]` |
| Is explanation required before use? | `[Minimal — intuitive interaction, but basic instructions improve experience]` |

## 4.3 Player Journey
Describe exactly how a player will use the project.

1. **Approach:** `[The player encounters a physical setup with multiple pins and a coin collection bucket, accompanied by a mobile interface]`
2. **Start:** `[The player takes the phone contected to the system via Bluetooth using the app.]`
3. **First Action:** `[They press a button on the app to select and trigger a specific pin.]`
4. **Main Interaction:** `[The player continues selecting different pins through the app, experimenting with timing and choice to release coins into the bucket.]`
5. **System Response:** `[Each input triggers a servo that pulls a pin, releasing a coin. The ultrasonic sensor detects the coin drop and the NeoPixel lights respond with dynamic color feedback.]`
6. **Win / Lose / End Condition:** `[A round ends after a fixed number of attempts or time. Success can be defined by the Neopixel flashing celebratory colours.]`
7. **Reset:** `[[Pins are manually reset to their original positions, the bucket is emptied and the game resets, and the system is ready for the next player.]`

## 4.4 Rules of Play
If your project is a game, list the rules clearly.

- `[Press one of the five buttons to trigger a corresponding pin (servo).]`
- `[[Each pin releases coins into the system.]`
- `[Players can press buttons multiple times to influence the outcome.]`
- `[Win: When enough coins reach the target area (detected by the sensor), the game triggers a win response.]`

---

# 5. Definition of Success

## 5.1 Definition of “Playable”
Your project will be considered complete only if these conditions are met.

- [YES] `[App successfully connects to the ESP32 via WiFi]`
- [YES] `[Each button correctly triggers its corresponding servo]`
- [YES] `[Pins release coins reliably without jamming]`
- [YES] `[System detects a win condition using the sensor]`
- [YES] `[Visual feedback (NeoPixel lights) responds to gameplay]`

## 5.2 Minimum Viable Version
What is the smallest version of this project that still delivers the core experience?

**Response:**  
`[The smallest version of the project includes one servo-controlled pin, a basic app with one button to trigger it, and a simple mechanism to release coins. The core experience is achieved if pressing the button causes a visible mechanical action and produces a satisfying, repeatable interaction.]`

## 5.3 Stretch Features
What features are nice to have but not essential?

- `[Lightfeedback from Neopixel]`
- `[Ultrasonic sensor to detect win]`
- `[App instead of physical buttons]`

---

# 6. System Overview

## 6.1 Project Type
Check all that apply.

- [YES] Electronics-based
- [ ] Mechanical
- [YES] Sensor-based
- [YES] App-connected
- [ ] Motorized
- [ ] Sound-based
- [YES] Light-based
- [YES] Screen/UI-based
- [ ] Fabricated structure
- [YES] Game logic based
- [YES] Installation / tabletop experience
- [ ] Other: `[Write here]`

## 6.2 High-Level System Description
Explain how the system works in simple terms.

Include:
- input,
- processing,
- output,
- physical structure,
- app interaction if any.

**Response:**  
`[The system is controlled through a mobile app that acts as the main input, where each button press sends a signal over WiFi to the ESP32. The ESP32 processes these signals and triggers the corresponding servo motors to pull pins and release coins. An ultrasonic sensor continuously monitors the system to detect when enough coins reach the target area, acting as a win condition. Based on this, the system processes whether the game is ongoing or completed. Outputs include the physical movement of servos, coins falling through the structure, and visual feedback through NeoPixel LEDs that animate during gameplay and celebrate when the player wins. The physical structure consists of a frame holding the pins, servo mechanisms, coin pathways, and a collection area, creating a tangible and interactive game controlled digitally through the app.]`

## 6.3 Input / Output Map

| System Part | Type | What It Does |
|---|---|---|
| `[ App Input]` | Input | `[Sends]` |
| `[ESP32 / Controller]` | Processing | `[Receives signals, processes game logic, triggers servos, reads sensor data, and controls LEDs]` |
| `[LServos + NeoPixel LEDs]` | Output | `[Servos pull pins to release coins; LEDs provide visual feedback and animations]` |
| `[Mechanical Assembly]` | Physical Action | `[Pins, threads, and structure guide and release coins into the collection area]` |

---

# 7. Sketches and Visual Planning

## 7.1 Concept Sketch
Add an early sketch of the full idea.

**Insert image below:**  
`[Upload image and link here]`

Example:
```md

```

## 7.2 Labeled Build Sketch
Add a sketch with labels showing:
- structure,
- electronics placement,
- user touch points,
- moving parts,
- output elements.

**Insert image below:**  
`[Upload image and link here]`

## 7.3 Approximate Dimensions

| Dimension | Value |
|---|---|
| Length | `[Write here]` |
| Width | `[Write here]` |
| Height | `[Write here]` |
| Estimated weight | `[Write here]` |

---

# 8. Mechanical Planning

## 8.1 Mechanical Features
Check all that apply.

- [ ] Gears
- [YES] Pulleys
- [ ] Belt drives
- [YES] Linkages
- [ ] Hinges
- [ ] Shafts
- [ ] Springs
- [ ] Bearings
- [ ] Wheels
- [YES] Sliders
- [YES] Levers
- [ ] Not applicable

## 8.2 Mechanical Description
Describe the mechanism and what it is meant to do.

**Response:**  
`[The servo pulls a thread that is wrapped around a fixed axle and wheel that in turn pulls the pin to let the coins fall]`

## 8.3 Motion Planning
If something moves, explain:
- what moves,
- what causes the movement,
- how far it moves,
- how fast it moves,
- what could go wrong.

**Response:**  
The servo arm rotates when triggered, pulling the thread that removes the pin. The motion is about 90 degrees, controlled by the servo’s programmed angle, and occurs over a few seconds for smooth release. The pin moves linearly outward, allowing coins to fall. The speed is moderate to ensure control and avoid jamming. Possible issues include thread slipping, servo not generating enough torque, or the pin getting stuck due to friction or misalignment.

## 8.4 Simulation / CAD / Animation Before Making
If your project includes mechanical motion, document the digital planning before fabrication.

| Tool Used | File / Link | What Was Tested |
|---|---|---|
| `[Fusion 360 / Tinkercad / other]` | `[Link or screenshot]` | `[What did you validate?]` |
| `[Tool]` | `[Link or screenshot]` | `[What did you validate?]` |

## 8.5 Changes After Digital Testing
What changed after the CAD, animation, or simulation stage?

**Response:**  
`[Write here]`

---

# 9. Electronics Planning

## 9.1 Electronics Used

| Component | Quantity | Purpose |
|---|---:|---|
| `[ESP32]` | `1` | `[Main controller]` |
| `[Servo]` | `[6]` | `[control the obstacles of the game]` |
| `[Ultra sonic sensor]` | `[1]` | `[senses the coins falling in the winning slot and sends a signal to the neopixel]` |
| `[Neopixel]` | `[1]` | `[Remains red until it recieves the signal from the ultra sonic and then turns green and after that a gradient in celebration]` |

## 9.2 Wiring Plan
Describe the main electrical connections.

**Response:**  
In concurrence with the code - the wiring of 5 of the sercos will be on GPIOs 22, 4, 5, 18 and 19. The GNDs of these servos will be connected to PSU GND. The 6th servo which is the continous sweep servo will be connected to GPIO 21 and the GND will be connected to PSU GND. PSU GND will be connected to the ESP 32's GND so that both grounds are connected. All red cables of teh servos go to the 5V power unit and the yellow wires go to the GPIO pins while all the black wires of the servos go to GND. Then, the ultrasonic sensor will be connected via jumper cables. TRIG and ECHO will be connected to GPIO pins 32 (Pin.OUT) and 33 (Pin.IN) respectively. GND of the sensor will again go to PSU GND and VCC will go to 5V power. The NeoPixel will be connected to the GPIO pin 13 and the red and black wires will go to power and GND respectively. The placement of these can be toggled/shifted with jumper cables - but this is the essence of the wiring in our project.

## 9.3 Circuit Diagram
Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[Upload image and link here]`

## 9.4 Power Plan

| Question | Response |
|---|---|
| Power source | `[Power Supply Unit - connected to the adapter]` |
| Voltage required | `[5V]` |
| Current concerns | `[There was concern that the current passing through the circuit would not be enough to power 6 servos, the neopixel and the sensor, but that concern was resolved through the trials]` |
| Safety concerns | `[We were concerned that the PSU migth over heat and burn - which did happen once - but then we found out how to manage the current in the circuit well enough that all the components are powered and it is safe to work around.]` |

---

# 10. Software Planning

## 10.1 Software Tools

| Tool / Platform | Purpose |
|---|---|
| `[MicroPython / Arduino / MIT App Inventor / CAD tool / other]` | `[Purpose]` |
| `[Tool]` | `[Purpose]` |
|  Micropython code | Used to create a code to connect ESP32, PSU, servos, neopixel, ultrasonic sensor and record its functions |
| MIT App inventor | Used to make interface for pressing the buttons required to move the pull pins |
| Laser cutting software tool | Used to make the hardware intricate parts by laser cutting acrylic sheets |
| Servo motors (5 of the 6) | Servos have a function of moving an angle of 90 degrees to let the coins pass that path |
| Continous sweep servo (6th servo) | This servo has the function of moving an angle of 125 degrees continously and the player must time the pull of the 4th or the 5th servo accurately to win the game |
| Ultrasonic sensor | The sensor is placed on the platfrom that decides the winner - the second coins fall on that platform the colour changes to green and then multiple celebratory colours |
| Neopixel | The neopixel rotates a red light on the circular strip until the player wins and then it resets |


## 10.2 Software Logic
Describe what the code must do.

Include:
- startup behavior,
- input handling,
- sensor reading,
- decision logic,
- output behavior,
- communication logic,
- reset behavior.

**Response:**  
The startup starts with all the servos excpet the continous sweep servo in rest position. The continous sweep servo moves continously 125 degrees back and forth - this is to increase the difficulty of the game. The neopixel is also on during startup - it powers a red light going round and round the neopixel - it loops until the winner is decided. As shown in the flowchart, the initialization of the app also happens during runtime. Once the app is ready, the buttons correspond to the servos to be moved. The buttons are pressed to make the coins move in the path the player intends. The buttons cannot be pressed more than once - demanding higher awareness and planning from the player. Each time a button is pressed, the corresponding servo moves 90 degrees and pulls the pin attatched to it making the coins fall into a path. The Ultrasonic sensor senses coins as they fall into the path that determines if the player wins the game or not. As soon as the sensor senses coins falling into that path, it makes the neopixel change from red to flash green twice to signal the win and then it transforms into celbratory colors for a while and then resets the game. The reset means that the runtime is over and for the game to be played again, the code needs to be run again.

## 10.3 Code Flowchart
Insert a flowchart showing your code logic.

Suggested sequence:
- start,
- initialize,
- wait for input,
- read input,
- decision,
- trigger output,
- repeat or reset,
- error handling.

This is the algorithm sequence of the code that follows the flowchart:

START
Initialization

1.	Initialize App communication using App Inventor link. 
2.	Define servo duty cycle limits (MIN = 26, MAX = 128). 
3.	Initialize: 
o	5 positional servos 
o	1 continuous servo 
4.	Set all servos to 0° (rest position). 
5.	Stop continuous servo. 
6.	Initialize ultrasonic sensor (TRIG + ECHO pins). 
7.	Initialize NeoPixel LED (16 LEDs). 
8.	Initialize:

-	Game state variables (active, press_count, etc.) 
-	Win detection variables (stable_count, win_latch) 
-	Sweep control variables

Main Loop
Step 1: Process App Input

-	Check for incoming app requests 
- IF request contains servo number (1–5): 
- 	Increment corresponding press_count[i]

Step 2: Win Detection (Ultrasonic Sensor)

- Measure distance using ultrasonic sensor
     IF distance is:
  
-	Valid AND between 2 cm and WIN_DISTANCE
→ Increment stable_count 

     ELSE

→ Reset stable_count = 0 

-	IF stable_count ≥ REQUIRED_STABLE: 
-	Set win_latch = True 
-	Stop continuous servo 
-	Run celebration LED animation 
-	Clear LEDs

Step 3: LED Animation

IF game NOT won: 
- 	Run rotating red LED pattern 

Step 4: Servo Queue System (for 5 servos)

FOR each servo i from 0 to 4:
•	Start Movement 
IF: 
- Servo is NOT active 
	press_count[i] > 0
THEN: 
- 	Move servo to TRIGGER_ANGLE 
-	Mark active[i] = True 
-	Set return_time[i] = now + RETURN_DELAY 

	Return Movement 
IF: 
-	Servo is active 
-	Current time ≥ return_time 
THEN: 
- 	Move servo back to 0° 
- 	Turn off PWM (duty(0)) 
-	Mark active[i] = False 
-	Decrease press_count[i]

Step 5: Continuous Servo Sweep

IF game NOT won: 
-	Every SWEEP_INTERVAL: 
-	Toggle direction

IF forward:
→ Set speed = CONT_FWD 
ELSE:
→ Set speed = CONT_REV

Step 6: Delay

•	Wait 20 ms 
•	Repeat loop

This is the flowchart for the code:

**Insert image below:**  
`[Upload image and link here]`

## 10.4 Pseudocode

```text
Somewhere during the project experimentation, we wanted to experiment with a load cell and map out the wins based on the amount/weight of the coins that landed on the load cell platform - but all our load cell hardware was faulty and due to unvailability of a replacement, we decidede to go ahead with our initial idea of using a ultrasonic sensor to give the win feedback to the player.
- This is the code we are using with the Ultrasonic sensor, the neopixel and all 6 servos:

[
from applink import AppInventorLink
from machine import Pin, PWM, time_pulse_us
from neopixel import NeoPixel
import time
import random

#App link
app = AppInventorLink()

# Servoss
SERVO_MIN_DUTY = 26
SERVO_MAX_DUTY = 128

servo_pins = [22, 4, 5, 18, 19]
servos = [PWM(Pin(p), freq=50) for p in servo_pins]

servo6 = PWM(Pin(21), freq=50)  # continuous sweep

def set_angle(servo, angle):
    duty = int(SERVO_MIN_DUTY + (angle / 180.0) * (SERVO_MAX_DUTY - SERVO_MIN_DUTY))
    servo.duty(duty)

# continuous servo control
CONT_STOP = 77
CONT_FWD  = 90
CONT_REV  = 64

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
TRIGGER_ANGLE = 125
RETURN_DELAY  = 4500

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
]
```

---

# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?
- [YES] Yes
- [ ] No

If yes, complete this section.

## 11.2 Why is the app needed?
Explain what the app adds to the experience.

Examples:
- remote control,
- score tracking,
- mode selection,
- personalization,
- triggering effects,
- displaying data.

**Response:**  
`[Instead of having physical buttons and more wiring, it more convenient to have a different interface that makes the experience neater and better, Remote controlling]`

## 11.3 App Features

| Feature | Purpose |
|---|---|
| `[Buttons]` | `[Buttons pressed to make the servos move to pull the pins]` |

## 11.4 UI Mockup
Insert a sketch or screenshot of the app interface.

**Insert image below:**  
`[Upload image and link here]`

## 11.5 Connect: Join WiFi kmehrawifi

1.Control: Press buttons (Servo 1–5)
2.Play: Servos move, game responds
3.Reset: Win → reset game

---

# 12. Bill of Materials

## 12.1 Full BOM

| Item | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec | Why This Choice? |
|---|---:|---|---|---:|---|---|
| `[ESP32]` | `[1]` | `[Yes]` | `[No]` | `0` | `[Spec]` | `[It powers the arduino set]` |
| `[Servo motor]` | `[6]` | `[Yes]` | `[Yes]` | `[125x5]` | `[Spec]` | `[Servo motors are easy to program and work with]` |
| `[Neopixel]` | `[1]` | `[Yes]` | `[No]` | `0` | `[Spec]` | `[To be used as player feedback by using light for both game startup and win]` |
| `[Ultrasonic sensor]` | `[1]` | `[Yes]` | `[No]` | `0` | `[Spec]` | `[To sense the coins as they fall into the win path]` |
| `[Power supply]` | `[1]` | `[Yes]` | `[No]` | `0` | `[Spec]` | `[Gives additional voltage to the circuit - 5V]` |

## 12.2 Material Justification
Explain why you selected your main materials and components.

Examples:
- Why acrylic instead of cardboard?
- Why MDF instead of 3D print?
- Why servo instead of DC motor?
- Why bearing instead of a plain shaft hole?

**Response:**  
`[Pine wood instead of MDF because it would not hold the continuous movement happening through the game and also the MDF deteriorates with time. Arcylic is transparent and light so it does not put pressure on the servos.]`

## 12.3 Items to Purchase Separately

| Item | Why Needed | Purchase Link | Latest Safe Date to Procure | Status |
|---|---|---|---|---|
| `[Servo motors]` | `[A few of our servos were faulty so we needed to get some extra for the project]` | `[amazon link]` | `[12th April]` | `[Ordered on the 10th, arrivedd on the 19th - but since it was physically also procured, we had 4 extra.]` |
| `[Power supply unit]` | `[The power supply unit had stopped working so it had to be replaced]` | `[Physically procured]` | `[17th April (It went out on the 17th)]` | `[Recieved on the 18th of April, tested and assembled.]` |

## 12.4 Budget Summary

| Budget Item | Estimated Cost |
|---|---:|
| Electronics | `[0]` |
| Mechanical parts | `[0]` |
| Fabrication materials | `[0]` |
| Purchased extras | `[Servos + Power supply = 770+500 = 1270 total]` |
| Contingency | `[already factored]` |
| **Total** | `[1270]` |

## 12.5 Budget Reflection
If your cost is too high, what can be simplified, removed, substituted, or shared?

**Response:**  
`[Although we had expected to do this without having to buy the electronics, we had left room for last minute purchases or fixes - and this came under that. As for the servos, it costed much less than expected - its just the delivery charges that added up. Overall, the cost was shared.]`

---

# 13. Planning the Work

## 13.1 Team Working Agreement
Write how your team will work together.

Include:
- how tasks are divided,
- how decisions are made,
- how progress will be checked,
- what happens if a task is delayed,
- how documentation will be maintained.

**Response:**  
- The tasks were divided as such: Khushi to handle the physical materials and app mechanics, Suksha to handle the working of the code and software debugging.
- The decisions were made smoothly as communication was direct and immediate. Each memeber would keep track of their work and share progress timely with the other to ensure concurrence.
- Progress goals for each week were set and both members focused on completion of those tasks to ensure good time management
- Tasks were done on time. On the cases of hardware failure, we did fall back a couple steps but it helped us understand the process more and the time crunch wasn't as heavily felt as we had planned time for probavle failures too.
- Documentation was maintained throughout the process as tasks were getting done. As for the compilation of sketches, pictures and flowcharts - that happened at the end.

## 13.2 Task Breakdown

| Task ID | Task | Owner | Estimated Hours | Deadline | Dependency | Status |
|---|---|---|---:|---|---|---|
| T1 | `[Finalize concept]` | `[Name]` | `2` | `[Date]` | `None` | `To Do` |
| T2 | `[Complete BOM]` | `[Name]` | `1` | `[Date]` | `T1` | `To Do` |
| T3 | `[Test electronics]` | `[Name]` | `2` | `[Date]` | `T1` | `To Do` |
| T4 | `[Build structure]` | `[Name]` | `4` | `[Date]` | `T1` | `To Do` |
| T5 | `[Write control code]` | `[Name]` | `4` | `[Date]` | `T3` | `To Do` |
| T6 | `[Integrate system]` | `[Name]` | `4` | `[Date]` | `T4, T5` | `To Do` |
| T7 | `[Playtest]` | `[Name]` | `2` | `[Date]` | `T6` | `To Do` |
| T8 | `[Refine and document]` | `[Name]` | `3` | `[Date]` | `T7` | `To Do` |

## 13.3 Responsibility Split

| Area | Main Owner | Support Owner |
|---|---|---|
| Concept and gameplay | `[Khushi and Suksha]` |  |
| Electronics | `[Khushi and Suksha]` |  |
| Coding | `[Suksha]` | `[Khushi]` |
| App | `[Khushi]` | `[Suksha]` |
| Mechanical build | `[Khushi]` | `[Suksha]` |
| Testing | `[Suksha]` | `[Khushi]` |
| Documentation | `[Khushi and Suksha]` |  |

---

# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 — Plan and De-risk
Expected outcomes:
- [YES] Idea finalized
- [YES] Core interaction decided
- [YES] Sketches made
- [YES] BOM completed
- [YES] Purchase needs identified
- [YES] Key uncertainty identified
- [YES] Basic feasibility tested

### Week 2 — Build Subsystems
Expected outcomes:
- [YES] Electronics tests completed
- [YES] CAD / structure planning completed
- [YES] App UI started if needed
- [YES] Mechanical concept tested
- [YES] Main subsystems partially working

### Week 3 — Integrate
Expected outcomes:
- [YES] Physical body built
- [YES] Electronics integrated
- [YES] Code connected to hardware
- [YES] App connected if required
- [YES] First playable version exists

### Week 4 — Refine and Finish
Expected outcomes:
- [YES] Technical bugs reduced
- [ ] Playtesting completed
- [ ] Improvements made
- [ ] Documentation completed
- [ ] Final build ready

## 14.2 Weekly Update Log

| Week | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|
| Week 1 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 2 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 3 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 4 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |

---

# 15. Risks and Unknowns

## 15.1 Risk Register

| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|---|---|---|---|---|---|
| `[Example: Bluetooth disconnects]` | `Technical` | `Medium` | `High` | `[Fallback interaction / simplify connection flow]` | `[Name]` |
| `[Example: Structure breaks during play]` | `Mechanical` | `Medium` | `High` | `[Reinforce joints / change material]` | `[Name]` |
| `[Risk]` | `[Technical / Material / Time / Gameplay]` | `[Low/Medium/High]` | `[Low/Medium/High]` | `[Plan]` | `[Name]` |
| `[Risk]` | `[Type]` | `[Low/Medium/High]` | `[Low/Medium/High]` | `[Plan]` | `[Name]` |

## 15.2 Biggest Unknown Right Now
What is the single biggest uncertainty in your project at this stage?

**Response:**  
`[Write here]`

---

# 16. Testing and Playtesting

## 16.1 Technical Testing Plan

| What Needs Testing | How You Will Test It | Success Condition |
|---|---|---|
| `[Bluetooth connection]` | `[Connect wiring system to the ESP32 and run the code. Connect to WiFi and open the App. The goal is to test the working of the buttons]` | `[If the App opens the correct interface and the buttons make the servos move as intended. DONE]` |
| `[Mechanism movement - servo movement]` | `[Test codes were made for each component, so running them would make us test the servo's function]` | `[If 5 servos move 90 degree and the 6th moves 125 degrees]` |
| `[Sensor behavior]` | `[The sensor is connectd to the neopixel for feedback, so we run the test code for the ultrasonic and neopixel. We drop a coin in the vicinity of the sensor and make it read the signal]` | `[If the signal is picked up, the neopixel light will change from red to green and then mulitple colours as celebration.]` |
| `[App communication]` | `[Coonection to WiFi and button interface working]` | `[If the buttons make the servos move. Same as bluetooth test]` |

## 16.2 Playtesting Plan

| Question | How You Will Check |
|---|---|
| Do players understand what to do? | `[Make them look at the game, and the app and see if they recognize it. If not, and some signifiers to show what is to be done.]` |
| Is the interaction satisfying? | `[See if the players find the gameplay engaging]` |
| Do players want another turn? | `[Make a logic not directly understandable until played so that the player is curious as to how to win.]` |
| Is the challenge balanced? | `[Yes, players feel the game logic makes the challenge balanced]` |
| Is the response clear and immediate? | `[The response of the neopixel makes the feedback loop complete and immediate.]` |

## 16.3 Testing and Debugging Log

| Date | Problem Found | Type | What You Tried | Result | Next Action |
|---|---|---|---|---|---|
| `[Date]` | `[Describe issue]` | `[Technical / Mechanical / UI / Gameplay]` | `[What you did]` | `[Worked / Partly / Failed]` | `[Next step]` |
| `[Date]` | `[Describe issue]` | `[Type]` | `[What you did]` | `[Result]` | `[Next step]` |

## 16.4 Playtesting Notes

| Tester | What They Did | What Confused Them | What They Enjoyed | What You Will Change |
|---|---|---|---|---|
| `[Teammate]` | `[Tested out the workings of the servos and the response mechanism]` | `[Why the servos weren't moving as intended]` | `[The overall flow of the game and the celevrations. They also liked how the game play was]` | `[The servo angles to match the max tension point to pull the pin out]` |
| `[Teammate and peer]` | `[They played the game but noticed the neopixel going off before time]` | `[The neopixel was lighting up without even getting a win signal and resetting the game]` | `[They liked the animation of the LEDs but they needed to come onyl after the game was won - not after some amount of time]` | `[Change in code version]` |

---

# 17. Build Documentation

## 17.1 Fabrication Process
Describe how the project was physically made.

Include:
- cutting,
- 3D printing,
- assembly,
- fastening,
- wiring,
- finishing,
- revisions.

**Response:**  
The base structure was cut from pine wood to provide a sturdy foundation, while details and layered elements were made using coloured and transparent acrylic cut with a laser cutter. 3D printed parts were used for components like servo mounts and pin holders to ensure proper alignment. The system was assembled by fixing the servos onto the wooden frame and attaching threads from the servo arms to the pins.

Fastening was done using adhesives and cable ties to keep all parts secure while still allowing small adjustments. Wiring involved connecting the servos, ultrasonic sensor, and NeoPixel strip to the ESP32 along with an external power supply, with careful routing to avoid interference with moving parts. Finishing included smoothing edges, aligning acrylic layers, and cleaning up the overall build.

Several revisions were made to improve the pin mechanism—adjusting thread tension, servo angles, and alignment to reduce friction and prevent jamming during operation

## 17.2 Build Photos
Add photos throughout the project.

Suggested images:
- early sketch,
- prototype,
- electronics testing,
- mechanism test,
- app screenshot,
- final build.

Example:
```md



```

## 17.3 Version History

| Version | Date | What Changed | Why |
|---|---|---|---|
| `v1` | `[25TH March]` | `[The base line code was made mapping out the functions of the servos and the neopixel]` | `[We were unsure which sensor to use]` |
| `v2` | `[26th March]` | `[The working code had the code of the servos, neopixel and the load cell]` | `[The load cell was faulty, we weren't able to derive the calobration factor or procure a new one]` |
| `v3` | `[2nd April]` | `[Working code with the ultrasonic sensor was written and versions of test codes for components were written]` | `[We zeroed down on using the ultrasonic sensor for the project and started testing the components]` |
| `v4` | `[6th April]` | `[The final code was written after testing and retesting the components]` | `[A few rounds of testign were required to avoid running into faulty equipment]` |
| `v5` | `[17th April]` | `[The final code needed to be have 2 values of the servos changed]` | `[It was changed to match the required angle of rotation on the board after mounting to overcome friction]` |

---

# 18. Final Outcome

## 18.1 Final Description
Describe the final version of your project.

**Response:**  
The final project is an interactive, app-controlled coin-release game that combines digital input with physical mechanics. A mobile app connects to the ESP32 via WiFi, allowing users to press buttons that trigger servo motors. Each servo pulls a pin using a thread-based mechanism, releasing coins into the system. The coins travel through a layered wooden and acrylic structure into a collection area. An ultrasonic sensor detects when enough coins reach the target, triggering a win condition. Throughout gameplay, a NeoPixel ring provides dynamic visual feedback, including continuous animations and a celebratory sequence upon winning. A continuously moving servo adds an additional layer of motion, making the system feel more alive and engaging.

## 18.2 What Works Well
- `[Reliable WiFi communication between the app and ESP32 for real-time control]`
- `[Smooth and responsive servo-triggered pin mechanism for coin release]`
- `[Engaging visual feedback through NeoPixel animations and win celebration]`

## 18.3 What Still Needs Improvement
- `[Point 1]`
- `[Point 2]`
- `[Point 3]`

## 18.4 What Changed From the Original Plan
How did the project change from the initial idea?

**Response:**  
`[We had planned to use a load cell somehere during the experimentation but, that didn't work out and was replaced by an ultrasonic sensor. A few of the placement of the obstacles were changed for accuracy.]`

---

# 19. Reflection

## 19.1 Team Reflection
What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  
The team worked well in dividing tasks between coding, electronics, and mechanical design, which helped progress happen in parallel. We communicated ideas clearly and adapted quickly when something didn’t work. However, integration slowed us down, especially when combining the app, hardware, and mechanics. Time management was generally effective, but more structured testing earlier could have reduced last-minute fixes.

## 19.2 Technical Reflection
What did you learn about:
- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  
`[We learned how to mainuplate, and scaffold these electronics in the way we wanted. We understoof the functionalities of each component and made it suit of needs best by manipulation. While coding, you understand what works and what doesn't. A trial and error method of understanding each element is mostly fun. We leanred how to work with elements we had never worked with before and how to code them to extrat maximum properties. We self-learnt how to create and call functions. We did try calling classes in the code, but we found that a bit redundant. But in hindsight, I think classes would have made the code a bit more sophisticated and organized. The fabricaton process was about combining multiple processes like laser cutting, drilling, acrylic mounting, and wood working to match what we had planned to do. Yes, we did run into difficulties here and there - but we figured a way out of the tension points given the workabilities and constraints of the materials we used. In reflection, we were present and weren't blind to the workings of the code and material integration.]`

## 19.3 Design Reflection
What did you learn about:
- designing for play,
- delight,
- clarity,
- physical interaction,
- player understanding,
- iteration?

**Response:**  
`[We learned that designing for play requires immediate feedback and simple interactions. Delight comes from combining physical movement, lights, and unpredictability. Clarity is important so users understand what each action does without explanation. Physical interaction made the experience more engaging compared to purely digital systems. Iteration was key, as small changes in timing, motion, or layout significantly improved usability and overall experience.]`

## 19.4 If You Had One More Week
What would you improve next?

**Response:**  
`[We learned how to connect and control multiple components like servos, sensors, and LEDs using the ESP32. In coding, we understood how to handle real-time inputs from an app and manage timing without blocking the system. Mechanically, we explored how motion from a servo can be translated into linear movement using threads and pins. In fabrication, precision and alignment were important to avoid jamming. Integration taught us that combining all systems is the most complex part and requires continuous testing and adjustment.]`

---

# 20. Final Submission Checklist

Before submission, confirm that:
- [ ] Team details are complete
- [ ] Project description is complete
- [ ] Inspiration sources are included
- [ ] Player journey is written
- [ ] Sketches are added
- [ ] BOM is complete
- [ ] Purchase list is complete
- [ ] Budget summary is complete
- [ ] Mechanical planning is documented if applicable
- [ ] App planning is documented if applicable
- [ ] Code flowchart is added
- [ ] Task breakdown is complete
- [ ] Weekly logs are updated
- [ ] Risk register is complete
- [ ] Testing log is updated
- [ ] Playtesting notes are included
- [ ] Build photos are included
- [ ] Final reflection is written

---

# 21. Suggested Repository Structure

```text
project-repo/
├── README.md
├── images/
│   ├── concept-sketch.jpg
│   ├── labeled-sketch.jpg
│   ├── circuit-diagram.jpg
│   ├── ui-mockup.jpg
│   ├── prototype-1.jpg
│   └── final-build.jpg
├── code/
│   ├── main.py
│   ├── test_code.py
│   └── notes.md
├── cad/
│   ├── models/
│   └── screenshots/
└── docs/
    ├── references.md
    └── extra-notes.md
```

---

# 22. Instructor Review

## 22.1 Proposal Approval
- [ ] Approved to proceed
- [ ] Approved with changes
- [ ] Rework required before proceeding

**Instructor comments:**  
`[Instructor fills this section]`

## 22.2 Midpoint Review
`[Instructor fills this section]`

## 22.3 Final Review Notes
`[Instructor fills this section]`
