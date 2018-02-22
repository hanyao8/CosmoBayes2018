#include <math.h>

template <typename T4__>
typename boost::math::tools::promote_args<T4__>::type
addone4(T4__& d, std::ostream* pstream__){
    T4__ ans;
    ans = d + 1.0;
    return ans;
}

template <typename T5__>
typename boost::math::tools::promote_args<T5__>::type
adde4(T5__& e, std::ostream* pstream__){
    T5__ ans;
    ans = e + exp(1.0);
    return ans;
}

template <typename T5__>
typename boost::math::tools::promote_args<T5__>::type
add20e(T5__& arg1, std::ostream* pstream__){
    T5__ ans;
    ans = arg1 + 20.0*exp(1.0);
    return ans;
}

template <typename T5__>
typename boost::math::tools::promote_args<T5__>::type
customexp(T5__& arg1, std::ostream* pstream__){
    T5__ ans;
	//T5__ arg1_doub;
	//arg1_doub = arg1 + 0.0;
    ans = exp(arg1+0.0);
    return ans;
}


template <typename T5__>
typename boost::math::tools::promote_args<T5__>::type
int_exp1(T5__& arg1, std::ostream* pstream__){
	T5__ ans;
	ans = 0.0;
	double x_st = 0.0;
	int N_steps = 1000;
	double N_steps_doub = 1000.0;
	T5__ delta_x;
	delta_x = (arg1-x_st)/N_steps_doub;
	for (int i=0; i<N_steps; i=i+1){
		ans = ans + exp( (double(i)+0.5 )*delta_x + x_st);
	}
    ans = ans * delta_x;
	//ans = x + 20.0*exp(1.0);
    return ans;
}

