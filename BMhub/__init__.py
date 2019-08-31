from flask import *
from flask import render_template
app = Flask(__name__)

@app.route('/')
def load_html():
    return render_template("index.html")

@app.route('/weather', methods=['POST', 'GET'])
def load_weather():
    return render_template("weather.html")

@app.route('/hub', methods=['POST', 'GET'])
def load_hub():
    return render_template("hub.html")
@app.route("/cshcal", methods=['POST', 'GET'])
def load_cshCal():
    return render_template("cshcal.html")
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
