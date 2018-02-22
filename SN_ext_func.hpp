#include "int_algo.hpp"

template <typename T0__, typename T1__>
typename boost::math::tools::promote_args<T0__, T1__>::type
DL_star(T0__& dsarg1, T1__& dsarg2, std::ostream* pstream__) {
    T1__ ans;

	//ans = a*x + customexp(b,0);
	//ans = int_exp1(dsarg1+dsarg2,0);
	
	//T1__ exparg;
	//exparg = dsarg1 + dsarg2;
	//ans = int_exp1(exparg,0);
    
	
	ans=DL_star_intpart(dsarg1,dsarg2,0);
	ans = ans *(1+dsarg1)*3000.0;	
	
	return ans;
}
