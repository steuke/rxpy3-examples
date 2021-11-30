#
# I have written a a short blog-post with some explanation:
# https://blog.ukena.de/posts/2021/11/rxpy3-multiple-using-observers-and-buffer/
#

from typing import Optional, Iterable

from rx import operators, create
from rx.core.typing import Observer, Scheduler, Disposable


def multiple_observers_example(items: Iterable):
    def dequeue(observer: Observer, scheduler: Optional[Scheduler]) -> Disposable:
        for item in items:
            try:
                observer.on_next(item)
            except Exception as e:
                observer.on_error(e)
                return Disposable()
        observer.on_completed()

    observable = create(dequeue).pipe(
        operators.do_action(
            on_next=lambda x: print(f"emitting {x}"),
            on_completed=lambda: print("source completed"),
            on_error=lambda e: print(f"source error {e}"),
        ),
        operators.publish(),
    )
    modulo3 = observable.pipe(operators.filter(lambda x: x % 3 == 0))
    modulo3.subscribe(
        on_next=lambda x: print(f"modulo3 is emitting item {x}, which triggers buffer"),
        on_completed=lambda: print("modulo3 completed"),
        on_error=lambda e: print(f"modulo3 error {e}"),
    )
    buffer = observable.pipe(operators.buffer(modulo3))
    buffer.subscribe(
        on_next=lambda x: print(f"buffer emitted: {x}"),
        on_completed=lambda: print("buffer completed"),
        on_error=lambda e: print(f"buffer error {e}"),
    )
    print("Connecting")
    observable.connect()


if __name__ == "__main__":
    multiple_observers_example(items=range(0, 10))
