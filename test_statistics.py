from collections import OrderedDict
import datetime

from data import Datapoint, Aapl, Bitcoin, Gold
import statistics

day0 = datetime.datetime(2013, 12, 31)
day1 = datetime.datetime(2014, 1, 1)
day2 = datetime.datetime(2014, 1, 2)
datapoints = OrderedDict([
    (day0, Datapoint(Aapl(day0, 1, 2, 3, 4, 5), Bitcoin(day0, 1, 2, 3, 4, 5, 6, 7), Gold(day0, 1, 2, 3))),
    (day1, Datapoint(Aapl(day1, 1, 2, 3, 4, 5), Bitcoin(day1, 1, 2, 3, 4, 5, 6, 7), Gold(day1, 1, 2, 3))),
    (day2, Datapoint(Aapl(day2, 1, 2, 3, 4, 5), Bitcoin(day2, 1, 2, 3, 4, 5, 6, 7), Gold(day2, 1, 2, 3))),
])

def test_that_partition_returns_sorted_datapoints():
    partitioned = statistics.partition(datapoints)
    assert len(partitioned) == 4

    dates, aapls, bitcoins, golds = partitioned
    assert sorted(dates) == dates

    for part in partitioned:
        assert len(part) == 3

    assert dates[0] == day0
    assert aapls[0] == datapoints[day0].aapl
    assert bitcoins[0] == datapoints[day0].bitcoin
    assert golds[0] == datapoints[day0].gold
