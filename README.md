# IoT Sensor Dashboard & Robotic Car Controller

A complete IoT system with real-time sensor dashboards and web-based robotic vehicle control.

## Features

### 🌡️ Sensor Dashboard
- **Live Sensor Data**: Temperature, Humidity, Rain, Motion, Smoke/Gas, Distance, Soil Moisture
- **Real-time Updates**: Auto-refreshing every 20 seconds
- **Beautiful Dashboard**: Modern dark theme with animated sparklines
- **Zero Configuration**: No backend required - pure static HTML/CSS/JS

### 🤖 Robot Car Controller
- **Web-based Control**: Control from any device with a browser
- **4-directional Movement**: Forward, Backward, Left, Right
- **Real-time Feedback**: Instant command confirmation and response times
- **Keyboard Support**: Use arrow keys or WASD for control
- **Motor Integration**: Works with Raspberry Pi GPIO pins

## Files

### Dashboards
- `index.html` - Main sensor dashboard (Vercel entry point)
- `sensor_dashboard.html` - Sensor monitoring interface
- `robot_controller.html` - Web interface for robot car control

### Backend Scripts
- `dummy_sensor_sender-2.py` - Generates and sends fake sensor data to ThingSpeak
- `robot_receiver.py` - Runs on the robot, receives commands from ThingSpeak

### Documentation
- `README.md` - This file

## Quick Start

### 1. Sensor Dashboard

#### Deploy to Vercel
1. Push repo to GitHub
2. Go to https://vercel.com
3. Select repository and deploy
4. Access at: `https://your-project.vercel.app/`

#### Or use GitHub Pages
1. Enable Pages in repo settings
2. Access at: `https://your-username.github.io/trial/`

#### Configure Dashboard
1. Open the dashboard
2. Enter **Channel ID** and **Read API Key**
3. Click **CONNECT**
4. Watch live sensor data!

### 2. Robot Car Controller

#### Deploy the Web Interface
- Deploy `robot_controller.html` with the sensor dashboard
- Or access via GitHub Pages: `/robot_controller.html`

#### Setup the Robot Receiver
```bash
# On Raspberry Pi or vehicle controller
python robot_receiver.py
```

#### How It Works
```
Web Browser → Send Command (ThingSpeak) → Robot Receiver Script → Motor Control
```

#### Control the Car
1. Open the web controller
2. Enter your **Write API Key** and **Channel ID**
3. Click **CONNECT CAR**
4. Use buttons or arrow keys to control

**Keyboard Controls:**
- ⬆️ `Arrow Up` or `W` → Move Forward
- ⬇️ `Arrow Down` or `S` → Move Backward
- ⬅️ `Arrow Left` or `A` → Turn Left
- ➡️ `Arrow Right` or `D` → Turn Right
- `Space` → Stop

## ThingSpeak Integration

### Sensor Data (Read)
- **Channel ID**: `3301674`
- **Read API Key**: `8OR6MJ5AN4UGAUWP`
- **Fields**:
  - Field 1: Temperature (°C)
  - Field 2: Humidity (%)
  - Field 3: Rain (0/1)
  - Field 4: Motion (0/1)
  - Field 5: Smoke/Gas (ppm)
  - Field 6: Distance (cm)
  - Field 7: Soil Moisture (%)

### Robot Commands (Write)
- **Write API Key**: Your ThingSpeak Write API Key
- **Field 1**: Command (FORWARD, BACKWARD, LEFT, RIGHT, STOP, TEST)

## Raspberry Pi GPIO Setup

To use with actual motors on Raspberry Pi:

1. Edit `robot_receiver.py`:
   ```python
   USE_GPIO = True  # Enable GPIO control
   ```

2. Configure your GPIO pins:
   ```python
   MOTOR_LEFT_FWD = 17
   MOTOR_LEFT_BWD = 27
   MOTOR_RIGHT_FWD = 22
   MOTOR_RIGHT_BWD = 23
   ```

3. Install RPi.GPIO:
   ```bash
   sudo pip3 install RPi.GPIO
   ```

4. Run with permissions:
   ```bash
   sudo python3 robot_receiver.py
   ```

## Running Locally

### Generate Sensor Data
```bash
python dummy_sensor_sender-2.py
```

### Receive Robot Commands
```bash
python robot_receiver.py
```

### View Web Interfaces
- Open `index.html` in browser for sensor dashboard
- Open `robot_controller.html` for car controller

## Project Architecture

```
┌─────────────────────────────────────┐
│   Web Browser (Dashboard/Control)   │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│      ThingSpeak Cloud API           │
├─────────────────────────────────────┤
│ Read: Sensor Data                   │
│ Write: Robot Commands               │
└──────────────┬──────────────────────┘
               │
      ┌────────┴────────┐
      ▼                 ▼
┌──────────────┐  ┌──────────────┐
│ Sensor       │  │ Raspberry Pi │
│ Sender (Py)  │  │ Receiver(Py) │
└──────────────┘  └──────────────┘
                        │
                        ▼
                   Motors/Actuators
```

## Technologies

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: ThingSpeak API, Python
- **Hardware**: Raspberry Pi, GPIO Motors
- **Deployment**: Vercel, GitHub Pages
- **Communication**: REST API (HTTPS)

## API Endpoints

**Sensor Data (ThingSpeak):**
```
GET https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds/last.json?api_key={READ_API_KEY}
```

**Send Robot Command:**
```
GET https://api.thingspeak.com/update?api_key={WRITE_API_KEY}&field1={COMMAND}
```

## CORS Proxy

For web deployment, uses AllOrigins CORS proxy:
```
https://api.allorigins.win/raw?url=...
```

## Troubleshooting

**Dashboard 404 Error:**
- Ensure `index.html` is at repository root
- Vercel should auto-serve it

**Robot Not Responding:**
- Check ThingSpeak credentials
- Verify robot receiver script is running
- Check Channel ID and API Key match

**GPIO Not Working:**
- Ensure `USE_GPIO = True` in script
- Run with `sudo` on Raspberry Pi
- Verify pin numbers match your hardware

## Future Enhancements

- [ ] Add camera feed to dashboard
- [ ] Real-time motor speed control (PWM)
- [ ] Robot battery status monitoring
- [ ] GPS location tracking
- [ ] Obstacle detection/avoidance
- [ ] Custom route planning
- [ ] Multi-device sync

## License

MIT

## Author

Arsalaan Khan

## Links

- **GitHub**: https://github.com/arsalaan024/trial
- **ThingSpeak Channel**: https://thingspeak.com/channels/3301674
- **Vercel Dashboard**: https://trial-[your-username].vercel.app/

