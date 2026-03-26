# IoT Sensor Dashboard

A real-time IoT sensor data dashboard that displays live sensor readings from ThingSpeak.

## Features

- **Live Sensor Data**: Temperature, Humidity, Rain, Motion, Smoke/Gas, Distance, Soil Moisture
- **Real-time Updates**: Auto-refreshing every 20 seconds
- **Beautiful Dashboard**: Modern dark theme with animated sparklines
- **Zero Configuration**: No backend required - pure static HTML/CSS/JS
- **Responsive Design**: Works on desktop, tablet, and mobile

## Files

- `index.html` - Main dashboard (served at root on Vercel)
- `sensor_dashboard.html` - Alternative entry point
- `dummy_sensor_sender-2.py` - Python script to generate and send fake sensor data to ThingSpeak

## Setup

### 1. Get ThingSpeak Credentials

- **Channel ID**: Your ThingSpeak channel ID
- **Read API Key**: Your ThingSpeak read API key

### 2. Deploy Dashboard

#### Option A: Vercel (Recommended)
1. Push this repo to GitHub
2. Connect to Vercel: https://vercel.com
3. Select this repository and deploy
4. Access at: `https://your-project.vercel.app/`

#### Option B: GitHub Pages
1. Enable GitHub Pages in repository settings
2. Access at: `https://your-username.github.io/trial/`

#### Option C: Local
- Simply open `index.html` in a web browser

### 3. Configure Dashboard

1. Open the deployed dashboard
2. Enter your **Channel ID** and **Read API Key**
3. Click **CONNECT**
4. Watch live sensor data stream in!

## Running the Data Generator

```bash
python dummy_sensor_sender-2.py
```

This sends fake sensor data to ThingSpeak every 20 seconds.

**Note**: Requires:
- Python 3.x
- Valid ThingSpeak API key (OJAQ3E7QFLLYRS5X)
- Internet connection

## Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: ThingSpeak API
- **Deployment**: Vercel / GitHub Pages
- **Data Generation**: Python

## API Integration

The dashboard uses ThingSpeak's REST API with a CORS proxy for cross-origin requests:
- Endpoint: `https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds/last.json`
- CORS Proxy: `https://api.allorigins.win/`

## Sensor Mapping

| Field | Sensor | Unit | Icon |
|-------|--------|------|------|
| 1 | Temperature | °C | 🌡️ |
| 2 | Humidity | % | 💧 |
| 3 | Rain | 0/1 | 🌧️ |
| 4 | Motion | 0/1 | 👤 |
| 5 | Smoke/Gas | ppm | 💨 |
| 6 | Ultrasonic Distance | cm | 📡 |
| 7 | Soil Moisture | % | 🌱 |

## License

MIT

## Author

Arsalaan Khan
