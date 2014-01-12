import codecs
import data

def test_open_stops2_yields_unicode_lines():
    with data.open_data_file('stops2.csv') as data_file:
        assert isinstance(data_file.read(), unicode)

def test_open_stops2():
    with data.open_data_file('stops2.csv'):
        pass

def test_open_lines():
    with data.open_data_file('lines.csv'):
        pass

def test_open_lines_stops():
    with data.open_data_file('lines_stops.csv'):
        pass

def test_parse_stops_yields_list_of_Stops():
    stops = data.parse('stops2.csv', data.Stop)
    assert len(stops) > 0
    for stop in stops:
        assert isinstance(stop, data.Stop)
        for column in stop:
            assert column is None or '\0' not in column
            assert column is None or '\r' not in column
            assert column is None or '\n' not in column


def test_parse_lines_yields_list_of_Lines():
    lines = data.parse('lines.csv', data.Line)
    assert len(lines) > 0
    for line in lines:
        assert isinstance(line, data.Line)
        for column in line:
            assert column is None or '\0' not in column
            assert column is None or '\r' not in column
            assert column is None or '\n' not in column

def test_parse_stops_yields_list_of_Stops():
    linestops = data.parse('lines_stops.csv', data.LineStop)
    assert len(linestops) > 0
    for linestop in linestops:
        assert isinstance(linestop, data.LineStop)
        for column in linestop:
            assert column is None or '\0' not in column
            assert column is None or '\r' not in column
            assert column is None or '\n' not in column
