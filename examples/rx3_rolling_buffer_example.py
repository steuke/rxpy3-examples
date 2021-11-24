#
# Accompanying blog-post:
# https://blog.ukena.de/posts/2021/11/rxpy3-sliding-or-rolling-buffer-operator/
#

from time import sleep

from rx import operators, interval


def rolling_buffer_example(buffer_size: int):

    source = interval(0.3).pipe(
        operators.do_action(
            on_next=lambda single_item: print(f"action before buffering {single_item}"),
        ),
        operators.buffer_with_count(buffer_size, 1),
        operators.do_action(
            on_next=lambda buffered_items: print(f"action on buffer {buffered_items}"),
        ),
    )
    print("Subscribing to source")
    source.subscribe()
    sleep(2)


if __name__ == "__main__":
    rolling_buffer_example(3)
