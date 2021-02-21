#!/usr/bin/python3

import frac


def main():
    f = frac.Frac(2, 5)
    a = frac.copy(f)

    c = a + f
    print(c)
    c += frac.Frac(1, 1)
    print(f)
    print(a)
    print(c)


if __name__ == '__main__':
    main()