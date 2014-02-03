from flask import Flask, send_file
import statistics

app = Flask(__name__)

@app.route("/")
def index():
    return app.send_static_file('index.html')

@app.route("/test-plot")
def plot():
    return send_png_plot(statistics.plot(range(100)))

@app.route("/gold_price")
def gold_price():
    return send_png_plot(statistics.gold_price())

def send_png_plot(plot):
    png_byteio = statistics.plot_to_png_IO(plot)
    return send_file(png_byteio, mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
