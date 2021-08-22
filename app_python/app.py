from os import getenv
from flask import Flask, render_template
from datetime import datetime
import pytz

TIME_ZONE = 'Europe/Moscow'
DEBUG = getenv('DEBUG')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def page():
    time = datetime.now(tz=pytz.timezone(TIME_ZONE))
    return render_template('index.html', time=time.strftime('%H:%M:%S'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=DEBUG)
