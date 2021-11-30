#
# I have written a short blog-post with some explanation:
# https://blog.ukena.de/posts/2021/11/rxpy3-multiple-using-observers-and-buffer/
#

from time import sleep

from rx import operators, interval


def buffer_example():
    buffer_marker = interval(1.0).pipe(
        operators.do_action(
            on_next=lambda x: print(f"buffer marker {x}"),
            on_completed=lambda: print("buffer marker completed"),
            on_error=lambda e: print(f"buffer marker error {e}"),
        ),
    )

    source = interval(0.3).pipe(
        operators.do_action(
            on_next=lambda single_item: print(f"action before buffering {single_item}"),
            on_completed=lambda: print("source completed"),
            on_error=lambda e: print(f"source error {e}"),
        ),
        operators.buffer(buffer_marker),
        operators.do_action(
            on_next=lambda buffered_items: print(
                f"action after buffering {buffered_items}"
            ),
            on_completed=lambda: print("buffer completed"),
            on_error=lambda e: print(f"buffer error {e}"),
        ),
    )
    print("Subscribing to source")
    source.subscribe()
    sleep(2)


if __name__ == "__main__":
    buffer_example()
