#!/usr/bin/python3

from math import gcd
from copy import copy


def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b // gcd(a, b)


class Frac:
    # constructor
    def __init__(self, numerator, denominator):
        gcd_ = gcd(numerator, denominator)
        self.num_ = numerator // gcd_
        self.den_ = denominator // gcd_

    def __copy__(self):
        return Frac(self.num_, self.den_)

    def __str__(self):
        return f'({self.num_} / {self.den_})'

    def __lt__(self, other):
        lcm_ = lcm(self.den_, other.den_)

        self_mult = lcm_ // self.den_
        other_mult = lcm_ // other.den_

        return self_mult * self.num_ < other_mult * other.den_

    def __gt__(self, other):
        lcm_ = lcm(self.den_, other.den_)

        self_mult = lcm_ // self.den_
        other_mult = lcm_ // other.den_

        return self_mult * self.num_ > other_mult * other.den_

    def __le__(self, other):
        return not self.__gt__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __eq__(self, other):
        return self.num_ == other.num_ and self.den_ == other.den_

    def __ne__(self, other):
        return not self.__eq__(other)

    def __iadd__(self, other):
        lcm_ = lcm(self.den_, other.den_)

        self_mult = lcm_ // self.den_
        other_mult = lcm_ // other.den_

        self.num_ = self.num_ * self_mult + other.num_ * other_mult
        self.den_ = self.den_ * self_mult + other.den_ * other_mult

        gcd_ = gcd(self.num_, self.den_)

        self.num_ //= gcd_
        self.den_ //= gcd_

        return self

    def __add__(self, other):
        tmp