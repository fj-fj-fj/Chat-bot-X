import traceback
import builtins
import inspect
import msvcrt
import time
import sys


def fwindows():
    """cp1251 -> utf-8"""
    if sys.stdout.encoding == 'cp1251':
        sys.stdout.reconfigure(encoding='utf-8')

def time_input(caption, timeout=7):
    """input() with a lifespan of 5 seconds"""
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
    """formatted output"""
    builtins.print('\n\a\N{Robot Face}\t>>\t>>>\t', *args, **kwargs)

def get_fname():
    current_frame = inspect.currentframe()
    previous_frame = current_frame.f_back
    current_name = previous_frame.f_code.co_name
    return current_name

def i(): print(inspect.stack())

def f_name(): return traceback.extract_stack(None, 2)[0][2]

log = {
    0: '\n:: Связь установить не удалось; response: {}'.rjust(100, '~'),
    1: '\n:: {} function run',
    2: '\n:: маппинг функций и ответа; response: {}\n'.rjust(100, '~')
}

if __name__ == '__main__':
    pass
