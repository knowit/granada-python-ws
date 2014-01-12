# coding: utf-8
import simpleplot

import mock

def test_that_plot_separates_points_correctly():
    fig_mock, ax_mock = mock.Mock(), mock.Mock()
    with mock.patch('simpleplot.plt.subplots', return_value=(fig_mock, ax_mock)):
        fig = simpleplot.plot([[1, 2, 3], [2, 1, 2]])
        xs = [1, 2]
        y1s = [2, 3]
        y2s = [3, 2]
        ax_mock.plot.mock_calls == [mock.call(xs, y1s), mock.call(xs, y2s)]
        assert fig is fig_mock
