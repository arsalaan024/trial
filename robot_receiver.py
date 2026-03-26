"""
robot_receiver.py
Receives movement commands from ThingSpeak and controls a robotic car

Usage:
  python robot_receiver.py
  
Commands received from ThingSpeak Field 1:
  - FORWARD  : Move car forward
  - BACKWARD : Move car backward
  - LEFT     : Turn left
  - RIGHT    : Turn right
  - STOP     : Stop the car
  
This script:
1. Reads commands from ThingSpeak every 2 seconds
2. Executes motor control commands
3. Works with Raspberry Pi GPIO pins (motor controllers)
"""

import urllib.request
import urllib.parse
import time
import json
import ssl

# ─── CONFIGURATION ─────────────────────────────────────────────────────────
READ_API_KEY  = "8OR6MJ5AN4UGAUWP"      # Your ThingSpeak Read API Key
CHANNEL_ID    = "3301674"               # Your ThingSpeak Channel ID
THINGSPEAK_URL = "https://api.thingspeak.com"
POLL_INTERVAL = 2                       # Check for commands every 2 seconds

# For Raspberry Pi GPIO Motor Control
USE_GPIO = False  # Set to True if using Raspberry Pi with GPIO
# Example GPIO pins (adjust based on your setup):
# MOTOR_LEFT_FWD = 17
# MOTOR_LEFT_BWD = 27
# MOTOR_RIGHT_FWD = 22
# MOTOR_RIGHT_BWD = 23

# ─────────────────────────────────────────────────────────────────────────────

def get_last_command():
    """Fetch the last command from ThingSpeak"""
    url = f"{THINGSPEAK_URL}/channels/{CHANNEL_ID}/feeds/last.json?api_key={READ_API_KEY}"
    try:
        # Skip SSL verification (workaround for macOS certificate issues)
        ssl_context = ssl._create_unverified_context()
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request, context=ssl_context, timeout=5) as response:
            data = json.loads(response.read().decode())
            # Read from Field 8 for robot commands (Field 1-7 is for sensors)
            command = data.get('field8', '')
            return command.strip() if command else None
    except Exception as e:
        print(f"  ❌ Error fetching command: {e}")
        return None


def execute_command(command):
    """Execute the motor control command"""
    if not command:
        return
    
    command = command.upper().strip()
    
    if command == 'FORWARD':
        motor_forward()
        print(f"  ▶ MOVING FORWARD")
    elif command == 'BACKWARD':
        motor_backward()
        print(f"  ◀ MOVING BACKWARD")
    elif command == 'LEFT':
        motor_left()
        print(f"  ↙ TURNING LEFT")
    elif command == 'RIGHT':
        motor_right()
        print(f"  ↘ TURNING RIGHT")
    elif command == 'STOP':
        motor_stop()
        print(f"  ⏹ STOPPED")
    elif command == 'TEST':
        print(f"  ⚡ TEST MODE - Car is responding!")
    else:
        print(f"  ⚠ Unknown command: {command}")


def motor_forward():
    """Move forward"""
    if USE_GPIO:
        # Replace with your actual GPIO control code
        # GPIO.output(MOTOR_LEFT_FWD, GPIO.HIGH)
        # GPIO.output(MOTOR_RIGHT_FWD, GPIO.HIGH)
        pass
    else:
        # Simulation mode
        pass


def motor_backward():
    """Move backward"""
    if USE_GPIO:
        # GPIO.output(MOTOR_LEFT_BWD, GPIO.HIGH)
        # GPIO.output(MOTOR_RIGHT_BWD, GPIO.HIGH)
        pass


def motor_left():
    """Turn left"""
    if USE_GPIO:
        # GPIO.output(MOTOR_RIGHT_FWD, GPIO.HIGH)
        # GPIO.output(MOTOR_LEFT_BWD, GPIO.HIGH)
        pass


def motor_right():
    """Turn right"""
    if USE_GPIO:
        # GPIO.output(MOTOR_LEFT_FWD, GPIO.HIGH)
        # GPIO.output(MOTOR_RIGHT_BWD, GPIO.HIGH)
        pass


def motor_stop():
    """Stop all motors"""
    if USE_GPIO:
        # GPIO.output(MOTOR_LEFT_FWD, GPIO.LOW)
        # GPIO.output(MOTOR_LEFT_BWD, GPIO.LOW)
        # GPIO.output(MOTOR_RIGHT_FWD, GPIO.LOW)
        # GPIO.output(MOTOR_RIGHT_BWD, GPIO.LOW)
        pass


def setup_gpio():
    """Initialize GPIO pins (Raspberry Pi)"""
    if not USE_GPIO:
        return
    
    try:
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BCM)
        pins = [17, 27, 22, 23]  # Adjust based on your setup
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
        print("✓ GPIO initialized")
    except Exception as e:
        print(f"✗ GPIO setup failed: {e}")


def main():
    """Main loop - continuously poll ThingSpeak for commands"""
    print("=" * 60)
    print("  ROBO CAR COMMAND RECEIVER")
    print("  Listening for commands from ThingSpeak")
    print(f"  Channel ID: {CHANNEL_ID}")
    print(f"  Poll Interval: {POLL_INTERVAL}s")
    print("=" * 60)
    
    setup_gpio()
    
    last_command = None
    tick = 0
    
    try:
        while True:
            tick += 1
            print(f"\n[Poll {tick}] Checking for commands...")
            
            command = get_last_command()
            
            if command and command != last_command:
                # New command received
                print(f"  📨 New Command: {command}")
                execute_command(command)
                last_command = command
            elif command:
                print(f"  ℹ Same command: {command}")
            else:
                print(f"  ⏳ No command yet")
            
            time.sleep(POLL_INTERVAL)
            
    except KeyboardInterrupt:
        print("\n\n⏹ Shutting down...")
        motor_stop()
        if USE_GPIO:
            import RPi.GPIO as GPIO
            GPIO.cleanup()
        print("✓ Safely stopped")


if __name__ == "__main__":
    main()
