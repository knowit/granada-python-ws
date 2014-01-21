from collections import namedtuple
import datetime
from os import path


Gold = namedtuple('Gold', ['date', 'usd', 'gbp', 'eur'])
Aapl = namedtuple('Aapl', ['date', 'open', 'high', 'low', 'close', 'volume'])
Bitcoin = namedtuple('Bitcoin', ['date', 'open', 'high', 'low', 'close',
                                 'volume_btc', 'volume_usd', 'weighted_price'])
Datapoint = namedtuple('Datapoint', ['date', 'aapl', 'bitcoin', 'gold'])

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

def dates_for_dataset(dataset):
    return [el.date for el in dataset]

def element_for_date(dataset, date):
    for el in dataset:
        if el.date == date:
            return el

def dates_with_complete_datapoints(*datasets):
    dataset_dates = [dates_for_dataset(dataset) for dataset in datasets]
    all_dates = set(sum(dataset_dates, []))
    return [date for date in all_dates if all([date in dates for dates in dataset_dates])]

def datapoints(aapl, bitcoin, gold):
    return [Datapoint(date, element_for_date(aapl, date),
                      element_for_date(bitcoin, date),
                      element_for_date(gold, date))
            for date in dates_with_complete_datapoints(aapl, bitcoin, gold)]

if __name__ == '__main__':
    aapl = parse('NASDAQ_AAPL.csv', Aapl)
    bitcoin = parse('MTGOXUSD.csv', Bitcoin)
    gold = parse('GOLD_2.csv', Gold)
    datas = datapoints(aapl, bitcoin, gold)
    print 'Found {} datapoints'.format(len(datas))
