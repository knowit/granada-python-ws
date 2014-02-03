import io
import matplotlib.pyplot as plt
import data

def plot(*args):
    fig, ax = plt.subplots(1)
    ax.scatter(*args, s=5, linewidth=0)
    fig.autofmt_xdate()
    return fig

def plot_to_png_IO(fig):
    png_bytes = io.BytesIO()
    fig.savefig(png_bytes, format='png')
    png_bytes.seek(0)
    return png_bytes

DATAPOINTS = data.fetch_data()

def gold_price():
    dates = list(DATAPOINTS.keys())
    gold_prices = [DATAPOINTS[date].gold.usd for date in dates]
    return plot(dates, gold_prices)
