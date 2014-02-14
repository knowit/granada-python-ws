import io
import matplotlib.pyplot as plt
import data

one_troy_ounce_in_grams = 31.1034768

def plot(points):
    """
    point = (x, y, y1, y2, ... yn)
    """
    fig, ax = plt.subplots(1)
    formatted = list(zip(*points))
    xs = formatted[0]
    for ys in formatted[1:]:
        ax.plot(xs, ys)
    fig.autofmt_xdate()
    return fig

def plot_to_png_IO(fig):
    png_bytes = io.BytesIO()
    fig.savefig(png_bytes, format='png')
    png_bytes.seek(0)
    return png_bytes

def aapl_in_gold(datapoints):
    """
    return: [(date, aapl_price_in_gold), ...]
    """
    def aapl_stock_in_grams_of_gold(datapoint):
        return datapoint.aapl.close / datapoint.gold.usd  * one_troy_ounce_in_grams
    return [(date, aapl_stock_in_grams_of_gold(datapoint)) for date, datapoint in datapoints.items()]

def all_as_usd(datapoints):
    return [(date, datapoint.aapl.close, datapoint.bitcoin.close, datapoint.gold.usd)
            for date, datapoint in datapoints.items()]

def aapl_in_bitcoin(datapoints):
    return [(date, datapoint.bitcoin.close / datapoint.aapl.close ) for date, datapoint in datapoints.items()]
