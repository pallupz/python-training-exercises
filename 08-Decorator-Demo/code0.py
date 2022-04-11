import time

def time_this(func):
    print(f'---> runnning {func.__name__}')
    start = time.time()
    func()
    print(f'---> completed {func.__name__} in {time.time() - start}')


@time_this
def sleeper_func():
    print(f'sleeping for 2')
    time.sleep(2)


time_this(sleeper_func)