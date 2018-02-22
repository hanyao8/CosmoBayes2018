#include "int_algo4.hpp"

template <typename T0__, typename T1__, typename T2__>
typename boost::math::tools::promote_args<T0__, T1__, T2__>::type
ext_func4(T0__& x, T1__& a, T2__& b, std::ostream* pstream__) {
    T1__ ans;
	//ans = a*x + addone4(b,0);
	//ans = a*x + adde4(b,0);
	//ans = a*x + add20e(b,0);
	//ans = a*x + customexp(b,0);
	ans = a*x + int_exp1(b,0);
    return ans;
}

 
