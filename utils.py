import traceback
import builtins
import inspect
import msvcrt
import time
import sys


def fwindows(s):
    return s.encode('utf-8','replace').decode('cp1251', 'ignore')


def tinput(caption, timeout=7):
    def echo(c):
        sys.stdout.write(c)
        sys.stdout.flush()        

    echo(caption)

    _input = []
    start = time.monotonic()
    while time.monotonic() - start < timeout:
        if msvcrt.kbhit():
            c = msvcrt.getwch()
            if ord(c) == 13:
                echo('\r\n')
                break
            _input.append(c)
            echo(c)

    if _input:
        return ''.join(_input)


def print(*args, **kwargs):
    builtins.print('\a>\t>\t>\t', *args, **kwargs)


def get_current_fname():
    current_frame = inspect.currentframe()
    previous_frame = current_frame.f_back
    current_name = previous_frame.f_code.co_name
    return current_name


def get_func_name():
    current_frame = inspect.currentframe()
    previous_frame = current_frame.f_back.f_back
    func_bot_name = previous_frame.f_code.co_name
    return func_bot_name


def inspect_func():
    print(inspect.stack())


def f_name():
    return traceback.extract_stack(None, 2)[0][2]

    
if __name__ == '__main__':
    def foo():
        return None, None

    x, *y = foo()
    print(x)
    print(y)


    def ft_join(lst, sep=' '):
        s = '%s' % lst
        ss = ''
        for i in s:
            if i.isdigit():
                ss += i + sep
            else:
                continue

    ft_join([1,2,3])