#include "int_algo.hpp"

template <typename T0__, typename T1__>
typename boost::math::tools::promote_args<T0__, T1__>::type
DL_star(T0__& a, T1__& b, std::ostream* pstream__) {
    T1__ ans;
	double z_end;
	z_end = a + 0.0;
	double omega_m;
	omega_m = b + 0.0;
	ans=DL_star_intpart(0.0,z_end,1000,omega_m);
    ans = ans *(1+z_end)*3000.0;
    return ans;
}


