from flask import Flask, render_template
from datetime import datetime
import pytz
import os

TIME_ZONE = 'Europe/Moscow'
DEBUG = os.getenv('DEBUG')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def page():
    time = datetime.now(tz=pytz.timezone(TIME_ZONE))
    if not os.path.exists("data/visits.txt"):
        os.makedirs("data/")
        f = open("data/visits.txt", 'x')
        f.close()
    with open("data/visits.txt", "a") as f:
        f.truncate()
        f.write(time.strftime('%H:%M:%S') + "\n")
    return render_template('index.html', time=time.strftime('%H:%M:%S'))

@app.route('/visits', methods=['GET'])
def visits():
    with open("data/visits.txt") as f:
        visits = f.readlines()[-1]

    time = datetime.now(tz=pytz.timezone(TIME_ZONE))
    return render_template('index.html', time=visits)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=DEBUG)
