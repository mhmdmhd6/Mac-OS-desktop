from flask import Flask, render_template, jsonify
import psutil

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def data():
    battery = psutil.sensors_battery()
    return jsonify({
        'battery': f'{battery.percent}%',
        'wifi': 'Connected',
        'bluetooth': 'Enabled'
    })

if __name__ == '__main__':
    app.run(debug=True)
