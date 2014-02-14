from collections import namedtuple, defaultdict, OrderedDict
import data
import datetime
import string

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
            assert_is_type_or_None(gold.date, datetime.datetime)
            assert_is_type_or_None(gold.usd, float)
            assert_is_type_or_None(gold.gbp, float)
            assert_is_type_or_None(gold.eur, float)

def test_parse_NASDAQ_AAPL_yields_list_of_Aapl():
    aapls = data.parse('NASDAQ_AAPL.csv', data.aapl)
    assert len(aapls) > 0
    for aapl in aapls:
        assert isinstance(aapl, data.Aapl)
        for column in aapl:
            assert_is_type_or_None(aapl.date, datetime.datetime)
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
            assert_is_type_or_None(bitcoin.date, datetime.datetime)
            assert_is_type_or_None(bitcoin.open, float)
            assert_is_type_or_None(bitcoin.high, float)
            assert_is_type_or_None(bitcoin.low, float)
            assert_is_type_or_None(bitcoin.close, float)
            assert_is_type_or_None(bitcoin.volume_btc, float)
            assert_is_type_or_None(bitcoin.volume_usd, float)
            assert_is_type_or_None(bitcoin.weighted_price, float)

def test_to_datetime():
    date = data.to_datetime('2014-01-31')
    assert isinstance(date, datetime.datetime)
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
