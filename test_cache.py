from time import sleep

from pickle_cache import cache


@cache()
def test_func():
    sleep(3)
    return 'A, B, C'


@cache()
def test_func2(arg1, arg2):
    sleep(3)
    return f'E, D, F, {arg1}, {arg2}'


test_func()
test_func2('what', 'okay')

