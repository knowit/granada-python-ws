from collections import namedtuple
import datetime
from os import path


Gold = namedtuple('Gold', ['date', 'usd', 'gbp', 'eur'])
Aapl = namedtuple('Aapl', ['date', 'open', 'high', 'low', 'close', 'volume'])
Bitcoin = namedtuple('Bitcoin', ['date', 'open', 'high', 'low', 'close',
                                 'volume_btc', 'volume_usd', 'weighted_price'])

def to_datetime(date_str):
    return datetime.datetime.strptime(date_str, "%Y-%m-%d")

def transform_types(*args):
    return [to_datetime(args[0])] + [float(arg) if arg else None for arg in args[1:]]

def open_data_file(name):
    return open(path.join('data', name), mode='r')

def parse(name, record_type):
    with open_data_file(name) as data_file:
        data_file.readline()
        return [parse_record(record, record_type) for record in data_file]

def parse_record(record, record_type):
    return record_type(*transform_types(*[column.strip() if column.strip() != '' else None
                                          for column in record.split(',')]))
