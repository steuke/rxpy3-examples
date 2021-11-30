from examples.rx3_multiple_observers_example import multiple_observers_example
from tests.utils import capture_stdout_as_list

expected_output = """Connecting
emitting 0
modulo3 is emitting item 0, which triggers buffer
buffer emitted: [0]
emitting 1
emitting 2
emitting 3
modulo3 is emitting item 3, which triggers buffer
buffer emitted: [1, 2, 3]
emitting 4
emitting 5
emitting 6
modulo3 is emitting item 6, which triggers buffer
buffer emitted: [4, 5, 6]
emitting 7
emitting 8
emitting 9
modulo3 is emitting item 9, which triggers buffer
buffer emitted: [7, 8, 9]
source completed
modulo3 completed
buffer emitted: []
buffer completed
disposing normally"""


def test_multiple_observers_example():
    # act
    with capture_stdout_as_list() as output:
        multiple_observers_example(items=range(0, 10))

    # assert
    assert str(output) == expected_output
