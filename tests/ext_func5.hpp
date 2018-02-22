#include "int_algo5.hpp"

template <typename T0__, typename T1__>
typename boost::math::tools::promote_args<T0__, T1__>::type
DL_star(T0__& dsarg1, T1__& dsarg2, std::ostream* pstream__) {
    T1__ ans;
	//ans = a*x + addone4(b,0);
	//ans = a*x + adde4(b,0);
	//ans = a*x + add20e(b,0);
	//ans = a*x + customexp(b,0);
	//ans = int_exp1(dsarg1+dsarg2,0);
	T1__ exparg;
	exparg = dsarg1 + dsarg2;
	ans = int_exp1(exparg,0);
    return ans;
}

 
