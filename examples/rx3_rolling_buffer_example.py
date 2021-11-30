#
# Accompanying blog-post:
# https://blog.ukena.de/posts/2021/11/rxpy3-sliding-or-rolling-buffer-operator/
#

from typing import Iterable

from rx import operators, from_


def rolling_buffer_example(items: Iterable, buffer_size: int):
    source = from_(items).pipe(
        operators.do_action(
            on_next=lambda single_item: print(f"action before buffering {single_item}"),
            on_completed=lambda: print("source completed"),
            on_error=lambda e: print(f"source error {e}"),
        ),
        operators.buffer_with_count(buffer_size, 1),
        operators.do_action(
            on_next=lambda buffered_items: print(f"action on buffer {buffered_items}"),
            on_completed=lambda: print("buffer completed"),
            on_error=lambda e: print(f"buffer error {e}"),
        ),
    )
    print("Subscribing to source")
    source.subscribe()


if __name__ == "__main__":
    rolling_buffer_example(items=range(0, 6), buffer_size=3)
