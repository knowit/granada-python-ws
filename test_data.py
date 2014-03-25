# coding: utf-8
from collections import defaultdict, OrderedDict
import data
import datetime
import mock
import io

def test_open_MTGOXUSD():
    with data.open_data_file('MTGOXUSD.csv'):
        pass

def test_open_NASDAQ_AAPL():
    with data.open_data_file('NASDAQ_AAPL.csv'):
        pass

def test_open_GOLD_2():
    with data.open_data_file('GOLD_2.csv'):
        pass

def assert_is_type_or_None(obj, expected_type):
    assert obj is None or isinstance(obj, expected_type)

def test_parse_GOLD_2_yields_list_of_Gold():
    golds = data.parse('GOLD_2.csv', data.gold)
    assert len(golds) > 0
    for gold in golds:
        assert isinstance(gold, data.Gold)
        for column in gold:
            assert_is_type_or_None(gold.date, datetime.date)
            assert_is_type_or_None(gold.usd, float)
            assert_is_type_or_None(gold.gbp, float)
            assert_is_type_or_None(gold.eur, float)

def test_parse_NASDAQ_AAPL_yields_list_of_Aapl():
    aapls = data.parse('NASDAQ_AAPL.csv', data.aapl)
    assert len(aapls) > 0
    for aapl in aapls:
        assert isinstance(aapl, data.Aapl)
        for column in aapl:
            assert_is_type_or_None(aapl.date, datetime.date)
            assert_is_type_or_None(aapl.open, float)
            assert_is_type_or_None(aapl.high, float)
            assert_is_type_or_None(aapl.low, float)
            assert_is_type_or_None(aapl.close, float)
            assert_is_type_or_None(aapl.volume, float)

def test_parse_MTGOXUSD_yields_list_of_Bitcoin():
    bitcoins = data.parse('MTGOXUSD.csv', data.bitcoin)
    assert len(bitcoins) > 0
    for bitcoin in bitcoins:
        assert isinstance(bitcoin, data.Bitcoin)
        for column in bitcoin:
            assert_is_type_or_None(bitcoin.date, datetime.date)
            assert_is_type_or_None(bitcoin.open, float)
            assert_is_type_or_None(bitcoin.high, float)
            assert_is_type_or_None(bitcoin.low, float)
            assert_is_type_or_None(bitcoin.close, float)
            assert_is_type_or_None(bitcoin.volume_btc, float)
            assert_is_type_or_None(bitcoin.volume_usd, float)
            assert_is_type_or_None(bitcoin.weighted_price, float)

def test_to_datetime():
    date = data.to_date('2014-01-31')
    assert isinstance(date, datetime.date)
    assert date.year == 2014
    assert date.month == 1
    assert date.day == 31

data_sets = [[data.Gold(1, 0, 0, 0), data.Gold(8, 0, 0, 0), data.Gold(3, 0, 0, 0), data.Gold(-17, 0, 0, 0)],
             [data.Aapl(1, 0, 0, 0, 0, 0)],
             [data.Bitcoin(1, 1, 2, 3, 4, 5, 6, 7)]]

def test_group_data_by_date_should_yield_defaultdict(): # hint
    assert isinstance(data.group_data_by_date(data_sets), defaultdict)
    assert data.group_data_by_date(data_sets).default_factory == list

def test_group_data_behaves():
    groups = data.group_data_by_date(data_sets)
    assert len(groups) == 4
    assert len(groups[1]) == 3
    assert len(groups[8]) == 1
    group_for_1 = [data_sets[0][0], data_sets[1][0], data_sets[2][0]]
    assert groups[1] == group_for_1

def test_remove_incomplete_data_points():
    groups = data.group_data_by_date(data_sets)
    filtered = data.remove_incomplete_data_points(groups)
    assert len(filtered) == 1
    group_for_1 = [data_sets[0][0], data_sets[1][0], data_sets[2][0]]
    assert filtered[1] == group_for_1

def test_order_dictionary_by_dates_yields_ordered_dict():
    assert isinstance(data.order_dictionary_by_date({}), OrderedDict)

def test_order_dictionary_by_dates_behaves_nicely():
    groups = data.group_data_by_date(data_sets)
    ordered_dict = data.order_dictionary_by_date(groups)
    keys = list(ordered_dict.keys())
    assert keys == list(sorted(keys))

def test_fetches_correct_amount_of_data():
    assert len(data.fetch_data()) == 848

def test_data_point_smart_constructor_is_smart():
    gold = data.Gold(*range(4))
    aapl = data.Aapl(*range(6))
    bitcoin = data.Bitcoin(*range(8))

    data_point = data.data_point([bitcoin, aapl, gold])

    assert data_point.gold == gold
    assert data_point.aapl == aapl
    assert data_point.bitcoin == bitcoin

def test_fetches_datapoints_in_correct_order():
    points = data.fetch_data()
    assert isinstance(points, OrderedDict)
    keys = list(points.keys())
    assert keys == list(sorted(keys))

def test_data_parser_for():
    csv_line = '2399-07-12,7,1597,13,229, ,,4.7'
    thing = data.data_parser_for(lambda *args: tuple(args), csv_line)
    assert thing == (datetime.date(2399, 7, 12), 7.0, 1597.0, 13.0, 229.0, None, None, 4.7)

def test_class_name_of():
    assert data.class_name_of(('tuppel',)) == 'tuple'
    assert data.class_name_of(data_sets[0][0]) == 'Gold'

def test_parse():
    not_a_file = mock.Mock()
    csv = """Date, Prime, Prime, Prime, Prime, Nothing, Nothing, FourPointSeven
2399-07-12,7,1597,13,229, ,,4.7
    """
    stream = io.StringIO(csv)
    with mock.patch('data.open_data_file', return_value=stream) as open_data_file:
        data_set = data.parse('A StringIO', lambda args: args)

        open_data_file.assert_called_with('A StringIO')
        assert data_set == ['2399-07-12,7,1597,13,229, ,,4.7']

def test_open_data_file():
    sentinel = object()
    with mock.patch('builtins.open', return_value=sentinel) as mock_open:
        assert data.open_data_file('file name') is sentinel
        mock_open.assert_called_with('data/file name', mode='r')

