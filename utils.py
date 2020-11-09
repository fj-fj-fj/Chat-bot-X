import builtins
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


if __name__ == '__main__':
    pass