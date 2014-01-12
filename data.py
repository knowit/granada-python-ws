import codecs
from collections import namedtuple
from os import path

Stop = namedtuple('Stop', ['id', 'name', 'shortname', 'municipality', 'zone', 'x', 'y', 'realtime_database_id'])
Line = namedtuple('Line', ['id', 'name', 'transportation_type'])
LineStop = namedtuple('LineStop', ['line_id', 'stop_id'])

def open_data_file(name):
    return codecs.open(path.join('data', name), mode='rb', encoding='utf-16')

def parse(name, record_type):
    with open_data_file(name) as data_file:
        return [parse_record(record, record_type) for record in data_file]

def parse_record(record, record_type):
    return record_type(*[column.strip() if column != '\0' else None for column in record.split(';')])
