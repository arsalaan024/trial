"""
dummy_sensor_sender.py
Generates fake sensor data and pushes it to ThingSpeak every 20 seconds.
Uses only built-in Python libraries — no pip install needed.

ThingSpeak Field Mapping:
  Field 1 → Temperature (°C)
  Field 2 → Humidity (%)
  Field 3 → Rain (0 = dry, 1 = raining)
  Field 4 → Motion (0 = no motion, 1 = motion detected)
  Field 5 → Smoke / Gas level (ppm)
  Field 6 → Ultrasonic Distance (cm)
  Field 7 → Soil Moisture (%)
"""

import urllib.request
import urllib.parse
import urllib.error
import random
import time
import ssl

# ─── CONFIG ──────────────────────────────────────────────────────────────────
WRITE_API_KEY  = "OJAQ3E7QFLLYRS5X"
CHANNEL_ID     = "3301674"
THINGSPEAK_URL = "https://api.thingspeak.com/update"
INTERVAL_SEC   = 20
# ─────────────────────────────────────────────────────────────────────────────


def generate_sensor_data(tick: int) -> dict:
    # Generate completely random sensor data
    temperature   = round(random.uniform(15, 40), 2)
    humidity      = round(random.uniform(20, 95), 2)
    rain          = random.choice([0, 1])
    motion        = random.choice([0, 1])
    smoke         = round(random.uniform(50, 1000), 1)
    distance      = round(random.uniform(5, 400), 1)
    soil_moisture = round(random.uniform(10, 100), 1)

    return {
        "field1": temperature,
        "field2": humidity,
        "field3": rain,
        "field4": motion,
        "field5": smoke,
        "field6": distance,
        "field7": soil_moisture,
    }


def send_to_thingspeak(data: dict) -> None:
    payload = {"api_key": WRITE_API_KEY, **data}
    try:
        # Skip SSL verification (workaround for macOS certificate issues)
        ssl_context = ssl._create_unverified_context()
        url = THINGSPEAK_URL + "?" + urllib.parse.urlencode(payload)
        
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request, context=ssl_context, timeout=10) as response:
            body = response.read().decode().strip()
            status = response.status
            print(f"  ✅ Sent (HTTP {status}) | Entry ID: {body} | Data: {data}")
            
    except urllib.error.HTTPError as e:
        print(f"  ❌ HTTP Error {e.code}: {e.reason}")
        print(f"     URL: {url}")
        print(f"     Response: {e.read().decode()}")
    except urllib.error.URLError as e:
        print(f"  ❌ Connection Error: {e.reason}")
    except Exception as e:
        print(f"  ❌ Error: {e}")


def main():
    print("=" * 60)
    print("  Dummy Sensor → ThingSpeak Sender")
    print("  No pip install needed — using built-in urllib")
    print(f"  Sending every {INTERVAL_SEC}s. Press Ctrl+C to stop.")
    print("=" * 60)

    tick = 0
    while True:
        data = generate_sensor_data(tick)
        print(f"\n[Tick {tick}]")
        for label, val in zip(
            ["Temp(°C)", "Humidity(%)", "Rain", "Motion", "Smoke(ppm)", "Distance(cm)", "SoilMoist(%)"],
            data.values()
        ):
            print(f"  {label:<16}: {val}")
        send_to_thingspeak(data)
        tick += 1
        time.sleep(INTERVAL_SEC)


if __name__ == "__main__":
    main()
