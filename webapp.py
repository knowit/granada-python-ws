from flask import Flask, send_file
import statistics
import data

app = Flask(__name__)
datapoints = data.fetch_data()

@app.route("/")
def index():
    return app.send_static_file('index.html')

@app.route("/aapl-in-gold")
def aapl_in_gold():
    return send_png_plot(statistics.plot(statistics.aapl_in_gold(datapoints)))

@app.route("/all-as-usd")
def all_as_usd():
    return send_png_plot(statistics.plot(statistics.all_as_usd(datapoints)))

@app.route("/aapl-in-bitcoin")
def aapl_in_bitcoin():
    return send_png_plot(statistics.plot(statistics.aapl_in_bitcoin(datapoints)))

def send_png_plot(plot):
    png_byteio = statistics.plot_to_png_IO(plot)
    return send_file(png_byteio, mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
