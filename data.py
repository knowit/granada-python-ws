# coding: utf-8
"""
Terminology:

    csv_line: A line from data/*.csv, structured as
        YYYY-MM-DD, float, float, ..., float
    data_sets: a list of lists of Aapl, Bitcoin and Gold -  [[aapls...], [bitcoins...], [golds...]]
    data_by_date: a dict of key=date, value=[aapl, bitcoin, gold]
    data_type: Aapl, Bitcoin or Gold
    data_parser: a function that reads a csv_line and returns an instance of data_type
"""
from collections import namedtuple, defaultdict, OrderedDict
import datetime
import operator
import itertools
from os import path

Aapl = namedtuple('Aapl', ['date', 'open', 'high', 'low', 'close', 'volume'])
Bitcoin = namedtuple('Bitcoin', ['date', 'open', 'high', 'low', 'close',
                                 'volume_btc', 'volume_usd', 'weighted_price'])
Gold = namedtuple('Gold', ['date', 'usd', 'gbp', 'eur'])
datapoint_fields = ['aapl', 'bitcoin', 'gold']
Datapoint = namedtuple('Datapoint', datapoint_fields)

def to_date(date_str):
    """
    Parses YYYY-MM-DD string into a datetime.date
    """
    pass

def data_parser_for(data_type, csv_line):
    """
    Separate csv_line by commas (,), create a date from the first item and numbers from the remaining items. If any of
    the remaining items are empty, None should be used in their place.

    Can be used to implement aapl, bitcoin and gold

    Returns an instance of data_type initialized with the contents of csv_line
    """
    pass

def aapl(csv_line):
    """
    csv_line: A line from data/NASDAQ_AAPL.csv, structured as
        YYYY-MM-DD, open, high, low, close, volume

    Returns an Aapl initialized with the contents of csv_line
    """
    pass

def bitcoin(csv_line):
    """
    csv_line: A line from data/MTGOXUSD.csv, structured as
        YYYY-MM-DD, open, high, low, close, volume_btc, volume_usd, weighted_price

    Returns an Bitcoin initialized with the contents of csv_line
    """
    pass

def gold(csv_line):
    """
    csv_line: A line from data/GOLD_2.csv, structured as
        YYYY-MM-DD, usd, gbp, eur

    Returns an Gold initialized with the contents of csv_line
    """
    pass

def class_name_of(thing):
    """
    Returns the class name of thing.

    Hint: try dir(thing) in the repl
    """
    pass

def data_point(values):
    """
    Returns a Datapoint from a collection containing one Aapl, one Gold and one Bitcoin in arbitrary order.
    """
    pass

def open_data_file(name):
    """
    Returns an open file handle to the file data/name, for reading
    """
    pass

def consume_header(data_file):
    """
    Read and discard one line from data_file
    """
    pass

def parse(name, data_parser):
    """
    Returns a list of the result of data_parser for each line in the named file
    """
    pass

def group_data_by_date(data_sets):
    """
    data_sets: a list of lists of Aapl, Bitcoin and Gold -  [[aapls...], [bitcoins...], [golds...]]

    Returns a dict of key=date, value=[aapl, bitcoin, gold] for each item in data_sets
    """
    pass

def remove_incomplete_data_points(data_by_date, number_of_data_types=len(datapoint_fields)):
    """
    data_by_date: a dict of key=date, value=[aapl, bitcoin, gold]

    Returns data_by_date with all incomplete Datapoints removed, where a complete Datapoint is one that has a value for all fields
    """
    pass

def order_dictionary_by_date(data_by_date):
    """
    data_by_date: a dict of key=date, value=[aapl, bitcoin, gold]

    Returns an collections.OrderedDict of data_by_date, sorted by date
    """
    pass

def create_data_points_in_date_mapping(data_by_date):
    """
    data_by_date: an OrderedDict of key=date, value=[aapl, bitcoin, gold], ordered by date ascending

    Returns an OrderedDict of (date, Datapoint) ordered by date ascending
    """
    pass


def datapoints(data_sets):
    """
    data_sets: a list of lists of Aapl, Bitcoin and Gold -  [[aapls...], [bitcoins...], [golds...]]

    Groups all items in data_sets by date, removes incomplete groups, orders by date and converts items instances of
    Datapoint

    Returns an OrderedDict of (date, Datapoint) ordered by date ascending
    """
    pass

def fetch_data():
    """
    Read all the dataz
    """
    return datapoints([parse('NASDAQ_AAPL.csv', aapl), parse('MTGOXUSD.csv', bitcoin), parse('GOLD_2.csv', gold)])
