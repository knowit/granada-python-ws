"""
Terminology:

    point: an n-tuple with one x value and one to n y value(s): (x, y, y1, y2, y3, ... yn)
"""

one_troy_ounce_in_grams = 31.1034768


def aapl_in_gold(datapoints):
    """
    Calculates the amount of gold an aapl stock costs for each date in datapoints
    Returns a list of tuples of (date, aapl stock price in grams of gold)
    """
    def aapl_stock_in_grams_of_gold(datapoint):
        return datapoint.aapl.close / datapoint.gold.usd  * one_troy_ounce_in_grams
    return [(date, aapl_stock_in_grams_of_gold(datapoint)) for date, datapoint in datapoints.items()]

def all_as_usd(datapoints):
    """
    Calculate the value of aapl stock, bitcoin and gold for each date in datapoints
    Returns a list of tuples of (date, aapl stock price, bitcoin price, gold price)
    """
    return [(date, datapoint.aapl.close, datapoint.bitcoin.close, datapoint.gold.usd)
            for date, datapoint in datapoints.items()]

def aapl_in_bitcoin(datapoints):
    """
    Calculate the amount of aapl stock you can get for one bitcoin for each date in datasets
    Returns a list of tuples of (date, aapl stock per bitcoin)
    """
    return [(date, datapoint.bitcoin.close / datapoint.aapl.close ) for date, datapoint in datapoints.items()]
