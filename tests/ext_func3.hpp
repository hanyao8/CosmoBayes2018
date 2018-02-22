#include "int_algo3.hpp"

template <typename T0__, typename T1__, typename T2__, typename T3__>
typename boost::math::tools::promote_args<T0__, T1__, T2__, T3__>::type
ext_func3(T0__& x, T1__& a, T2__& b, T3__& c, std::ostream* pstream__) {
    //T1__ v;
	double cdoub;
	cdoub = c +0.0;
	//v=int_exp(0.0,cdoub,1000);
    T1__ ans;
	ans = a*x + int_exp3(b,0);
    //ans = a*x + b + v;
    return ans;
}

 
