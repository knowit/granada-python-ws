from flask import Flask, send_file
import statistics
import data

app = Flask(__name__)
datapoints = data.fetch_data()

@app.route("/")
def index():
    return app.send_static_file('index.html')

@app.route("/test-plot")
def plot():
    return send_png_plot(statistics.plot(range(100)))

@app.route("/plot-partition")
def plot_partition():
    return send_png_plot(statistics.plot_partition(datapoints))

def send_png_plot(plot):
    png_byteio = statistics.plot_to_png_IO(plot)
    return send_file(png_byteio, mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
