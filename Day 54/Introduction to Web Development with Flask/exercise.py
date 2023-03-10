import time


def speed_calc_decorator(function):
    def wrapper_function():
        current_time = time.time()
        function()
        speed = time.time() - current_time
        print(f"{function.__name__} run speed: {speed}")

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


fast_function()


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


slow_function()
