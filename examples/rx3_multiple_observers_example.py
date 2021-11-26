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

    observable = create(dequeue).pipe(
        operators.do_action(on_next=lambda x: print(f"emitting {x}")),
        operators.publish(),
    )
    modulo3 = observable.pipe(operators.filter(lambda x: x % 3 == 0))
    modulo3.subscribe(
        lambda x: print(f"modulo3 is emitting item {x}, which triggers buffer")
    )
    buffer = observable.pipe(operators.buffer(modulo3))
    buffer.subscribe(lambda x: print(f"buffer emitted: {x}"))
    print("Connecting")
    observable.connect()


if __name__ == "__main__":
    multiple_observers_example(items=range(0, 10))
