import io
import matplotlib.pyplot as plt

def plot(points):
    """
    Plots an iterable of points onto a matplotlib Figure object

    A point is an n-tuple with one x value and one to n y value(s): (x, y, y1, y2, y3, ... yn)
    """
    fig, ax = plt.subplots(1)
    formatted = list(zip(*points))
    xs = formatted[0]
    for ys in formatted[1:]:
        ax.plot(xs, ys)
    fig.autofmt_xdate()
    return fig

def plot_to_png_IO(fig):
    """
    Renders a matplotlib Figure object into a PNG and returns a BytesIO (a stream) containing the PNG
    """
    png_bytes = io.BytesIO()
    fig.savefig(png_bytes, format='png')
    png_bytes.seek(0)
    return png_bytes
