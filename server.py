import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
api = 'e1424507559b9824cadf8743620a128e'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        return get_weather(city)



@app.route('/weather', methods=['GET'])
def get_weather(city=None):
    if city is None:
        city = request.args.get('city')

    try:
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric&lang=ru")
        data = r.json()
        return data
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


if __name__ == '__main__':
    app.run(debug=True)