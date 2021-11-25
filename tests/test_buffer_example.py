from examples.rx3_buffer_example import buffer_example
from tests.utils import capture_stdout_as_list

expected_output = """Subscribing to source
action before buffering 0
action before buffering 1
action before buffering 2
buffer marker 0
action after buffering [0, 1, 2]
action before buffering 3
action before buffering 4
action before buffering 5"""


def test_buffer_example():
    # act
    with capture_stdout_as_list() as output:
        buffer_example()

    # assert
    assert output.to_string() == expected_output
