#include "int_algo.hpp"

template <typename T0__, typename T1__, typename T2__>
typename boost::math::tools::promote_args<T0__, T1__, T2__>::type
ext_func2(T0__& x, T1__& a, T2__& b, std::ostream* pstream__) {
    T1__ v;
	v=int_exp(0.0,3.0,1000);
    T1__ ans;
    ans = a*x + b + v;
    return ans;
}


