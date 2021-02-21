from math import gcd

class Frac:
    # constructor
    def __init__(self, numerator: int, denominator: int):
        gcd_ = gcd(numerator, denominator)
        self.num_ = numerator // gcd_
        self.den_ = denominator // gcd_

    def __str__(self):
        return f'{self.num_} / {self.den_}'


def main():
    f = Frac(20, 8)
    print(f)


if __name__ == '__main__':
    main()