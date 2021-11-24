#
# I have written a a short blog-post with some explanation:
# https://blog.ukena.de/posts/2021/11/rxpy3-multiple-using-observers-and-buffer/
#


from time import sleep
from typing import Optional

from rx import operators, create
from rx.core.typing import Observer, Scheduler, Disposable


def multiple_observers_example():
    def dequeue(observer: Observer, scheduler: Optional[Scheduler]) -> Disposable:
        next_item = 0
        while True:
            try:
                next_item += 1
                observer.on_next(next_item)
                sleep(0.3)
            except Exception as e:
                observer.on_error(e)
                return Disposable()

    observable = create(dequeue).pipe(operators.publish())
    skip4 = observable.pipe(operators.filter(lambda x: x % 3 == 0))
    skip4.subscribe(lambda x: print(f"skipped to {x}"))
    buffer = observable.pipe(operators.buffer(skip4))
    buffer.subscribe(lambda x: print(f"processing buffered events {x}"))
    print("Connecting")
    observable.connect()
    while True:
        sleep(10)


if __name__ == "__main__":
    multiple_observers_example()
