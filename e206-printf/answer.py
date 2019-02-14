# -*- encoding: utf-8 -*-


def printf(fmt, *args, newline=True):
    print(fmt % args, end='\n' if newline else '')


printf('hello %s', 'world')
printf('%d + %d = %d', 1, 2, 1 + 2)
printf('hello %s and ', 'world', newline=False)
printf('%d + %d = %d', 1, 2, 1 + 2)
