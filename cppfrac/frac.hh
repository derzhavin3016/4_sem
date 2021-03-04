#ifndef __FRAC__HH_
#define __FRAC__HH_

#include <iostream>
#include <numeric>

namespace mth
{
  class Frac final
  {
  private:
    int num_{};
    uint den_{};
  public:

    Frac(int num, uint den = 1)
    {
      if (den == 0)
        throw std::runtime_error{"Denomenator equals zero!!"};

      auto gcd = std::gcd(num, den);

      num_ = num / gcd;
      den_ = den / gcd;
    }

    Frac( const Frac &that ) = default;
    Frac &operator =( const Frac &that ) = default;

    std::ostream &dump( std::ostream &ost ) const
    {
      ost << "(" << num_ << " / " << den_ << ")" << std::endl;

      return ost;
    }

    std::istream &input( std::istream &ist )
    {
      ist >> num_ >> den_;

      return ist;
    }

    bool operator <( const Frac &that ) const
    {
      auto pr = lcm_div(that);

      return pr.first * num_ < pr.second * that.num_;
    }

    bool operator >( const Frac &that ) const
    {
      auto pr = lcm_div(that);

      return pr.first * num_ > pr.second * that.num_;
    }

    bool operator <=( const Frac &that ) const
    {
      return !operator >(that);
    }

    bool operator >=( const Frac &that ) const
    {
      return !operator <(that);
    }

    bool operator ==( const Frac &that ) const
    {
      return num_ == that.num_ && den_ == that.den_;
    }

    bool operator !=( const Frac &that ) const
    {
      return !operator ==(that);
    }

    Frac &operator +=( const Frac &that )
    {
      auto pr = lcm_div(that);

      num_ = num_ * pr.first + that.num_ * pr.second;
      den_ = pr.first * den_;

      norm();

      return *this;
    }

    Frac &operator -=( const Frac &that )
    {
      auto pr = lcm_div(that);

      num_ = num_ * pr.first - that.num_ * pr.second;
      den_ = pr.first * den_;

      norm();

      return *this;
    }

    Frac &operator *=( const Frac &that )
    {
      num_ *= that.num_;
      den_ *= that.den_;

      norm();

      return *this;
    }

    Frac &operator /=( const Frac &that )
    {
      if (that.num_ == 0)
        throw std::runtime_error{"Dividing by zero!"};

      num_ *= that.den_;
      den_ *= that.num_;

      norm();

      return *this;
    }

    Frac operator -( void ) const
    {
      return Frac{-num_, den_};
    }

    operator double( void )
    {
      return static_cast<double>(num_) / den_;
    }
private:

    void norm( void )
    {
      auto gcd = std::gcd(num_, den_);

      num_ /= gcd;
      den_ /= gcd;
    }

    std::pair<int, int> lcm_div( const Frac &that ) const
    {
      std::pair<int, int> ipr;
      auto lcm = std::lcm(den_, that.den_);

      ipr.first = lcm / den_;
      ipr.second = lcm / that.den_;

      return ipr;
    }
  };

  Frac operator +( const Frac &lhs, const Frac &rhs )
  {
    Frac sum = lhs;

    sum += rhs;

    return sum;
  }

  Frac operator -( const Frac &lhs, const Frac &rhs )
  {
    Frac sub = lhs;

    sub -= rhs;

    return sub;
  }

  Frac operator *( const Frac &lhs, const Frac &rhs )
  {
    Frac mul = lhs;

    mul *= rhs;

    return mul;
  }

  Frac operator /( const Frac &lhs, const Frac &rhs )
  {
    Frac div = lhs;

    div /= rhs;

    return div;
  }

  std::ostream &operator <<( std::ostream &ost, const Frac &frac )
  {
    return frac.dump(ost);
  }

  std::istream &operator >>( std::istream &ist, Frac &frac )
  {
    return frac.input(ist);
  }
}

#endif /* __FRAC__HH_ */