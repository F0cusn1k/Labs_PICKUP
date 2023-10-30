import time
from contextlib import contextmanager


class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        res = time.time() - self.start_time
        print('Время выполнения: {}'.format(res))


@contextmanager
def cm_timer_2():
    start_time = time.time()
    yield
    end_time = time.time()
    res = end_time - start_time
    print('Время выполнения: {}'.format(res))


def main():
    with cm_timer_1():
        time.sleep(1.5)

    with cm_timer_2():
        time.sleep(1.5)


if __name__ == '__main__':
    main()
