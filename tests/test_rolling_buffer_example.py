from examples.rx3_rolling_buffer_example import rolling_buffer_example
from tests.utils import capture_stdout_as_list

expected_output = """Subscribing to source
action before buffering 0
action before buffering 1
action before buffering 2
action on buffer [0, 1, 2]
action before buffering 3
action on buffer [1, 2, 3]
action before buffering 4
action on buffer [2, 3, 4]
action before buffering 5
action on buffer [3, 4, 5]
source completed
action on buffer [4, 5]
action on buffer [5]
buffer completed"""


def test_rolling_buffer():
    # act
    with capture_stdout_as_list() as output:
        rolling_buffer_example(items=range(0, 6), buffer_size=3)

    # assert
    assert str(output) == expected_output
