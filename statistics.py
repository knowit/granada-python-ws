import io
import matplotlib.pyplot as plt
import data

def plot(args):
    fig, ax = plt.subplots(1)
    ax.plot(*args)
    fig.autofmt_xdate()
    return fig

def plot_to_png_IO(fig):
    png_bytes = io.BytesIO()
    fig.savefig(png_bytes, format='png')
    png_bytes.seek(0)
    return png_bytes

def partition(datapoints):
    """
    returns: (list av datetime, list av aapl, list av bitcoin, list av gold)
    """
    dates = list(datapoints.keys())
    aapls = [datapoint.aapl for datapoint in datapoints.values()]
    bitcoins = [datapoint.bitcoin for datapoint in datapoints.values()]
    golds = [datapoint.gold for datapoint in datapoints.values()]
    return dates, aapls, bitcoins, golds

def plot_partition(datapoints):
    return plot(partition(datapoints)[0:2])
