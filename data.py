from collections import namedtuple, defaultdict
import datetime
import itertools
from os import path

Gold = namedtuple('Gold', ['date', 'usd', 'gbp', 'eur'])
Aapl = namedtuple('Aapl', ['date', 'open', 'high', 'low', 'close', 'volume'])
Bitcoin = namedtuple('Bitcoin', ['date', 'open', 'high', 'low', 'close',
                                 'volume_btc', 'volume_usd', 'weighted_price'])
Datapoint = namedtuple('Datapoint', ['aapl', 'bitcoin', 'gold'])

def to_datetime(date_str):
    return datetime.datetime(*[int(pt) for pt in date_str.split('-')])

def date_parser_for(tuple_type):
    def init(line):
        date, *values = line.split(',')
        return tuple_type(to_datetime(date), *[float(arg) if arg.strip() else None for arg in values])
    return init

tuple_types = [Aapl, Bitcoin, Gold]
aapl, bitcoin, gold = [date_parser_for(tp) for tp in tuple_types]

def data_point(values):
    def index_of(item):
        return tuple_types.index(item.__class__)
    return Datapoint(*list(sorted(values, key=index_of)))

def open_data_file(name):
    return open(path.join('data', name), mode='r')

def consume_header(data_file):
    data_file.readline()

def parse(name, record_type):
    with open_data_file(name) as data_file:
        consume_header(data_file)
        return [record_type(record) for record in data_file]

def datapoints(*data_sets):
    date_mapping = defaultdict(list)
    for point in itertools.chain(*data_sets):
        date_mapping[point.date].append(point)
    return {date: data_point(values) for date, values in date_mapping.items() if len(values) == len(data_sets)}

def fetch_data():
    return datapoints(parse('NASDAQ_AAPL.csv', aapl), parse('MTGOXUSD.csv', bitcoin), parse('GOLD_2.csv', gold))

if __name__ == '__main__':
    fetch_data()
