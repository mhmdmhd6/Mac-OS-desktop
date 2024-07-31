from flask import Flask, render_template, jsonify
import psutil

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def data():
    battery = psutil.sensors_battery()
    charging = battery.power_plugged
    time_left = battery.secsleft
    hours = 0
    minutes = 0
    if time_left == psutil.POWER_TIME_UNLIMITED:
        time_left_str = "Unlimited"
    elif time_left == psutil.POWER_TIME_UNKNOWN:
        time_left_str = "Unknown"
    else:
        hours, remainder = divmod(time_left, 3600)
        minutes, seconds = divmod(remainder, 60)

    return jsonify({
        'battery': f'{battery.percent}%',
        'charging': 'Yes' if charging else 'No',
        'time_left': f"{hours} hours, {minutes} minutes" if hours > 0 else f"{minutes} minutes",
        'wifi': 'Connected',
        'bluetooth': 'Enabled'
    })

if __name__ == '__main__':
    app.run(debug=True)
