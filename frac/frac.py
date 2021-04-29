#!/usr/bin/python3
"""Fraction class module"""

from math import gcd


def lcm(a_num, b_num):
    """Compute the lowest common multiple of a and b"""
    return a_num * b_num // gcd(a_num, b_num)


class Frac:
    """Fraction class implementation"""
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

    def norm(self):
        """
        norm(self) -> void
        """
        gcd_ = gcd(self.den_, self.num_)

        self.den_ //= gcd_
        self.num_ //= gcd_

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
        self.den_ = lcm_

        self.norm()

        return self

    def __add__(self, other):
        tmp = self.__copy__()

        tmp += other

        return tmp

    def __neg__(self):
        return Frac(-self.num_, self.den_)

    def __isub__(self, other):
        self.__iadd__(-other)

        return self

    def __sub__(self, other):
        tmp = self.__copy__()

        tmp -= other

        return tmp

    def __imul__(self, other):
        self.num_ *= other.num_
        self.den_ *= other.den_

        self.norm()

        return self

    def __mul__(self, other):
        tmp = self.__copy__()

        tmp *= other

        return tmp

    def __float__(self):
        return float(self.num_) / self.den_

    def __itruediv__(self, other):
        self.num_ *= other.den_
        self.den_ *= other.num_

        self.norm()

        return self

    def __truediv__(self, other):
        tmp = self.__copy__()

        tmp /= other

        return tmp
