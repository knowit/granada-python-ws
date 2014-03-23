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

def test_that_aapl_in_gold_returns_expected_structure():
    ounces_per_share = statistics.aapl_in_gold(datapoints)
    assert ounces_per_share
    first_day = ounces_per_share[0]
    expected = datapoints[day0].aapl.close / float(datapoints[day0].gold.usd) * statistics.one_troy_ounce_in_grams
    assert first_day[0] == day0
    assert first_day[1] == expected

def test_that_all_as_usd_returns_4_items():
    all_as_usd = statistics.all_as_usd(datapoints)
    assert len(all_as_usd) == 3
    assert len(all_as_usd[0]) == 4
    first_day = all_as_usd[0]
    assert first_day[0] == day0
    assert first_day[1] == datapoints[day0].aapl.close
    assert first_day[2] == datapoints[day0].bitcoin.close
    assert first_day[3] == datapoints[day0].gold.usd

