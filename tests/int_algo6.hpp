#include <math.h>
#include <cmath>

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


template <typename T6__, typename T7__>
typename boost::math::tools::promote_args<T6__, T7__>::type
DL_star_integrand(T6__& argz, T7__& param1, std::ostream* pstream){
	T7__ ans1;
	ans1=pow(param1*pow((1+argz),3.0 ) +1 -param1 , -0.5);
	return ans1;
}


template <typename T8__, typename T9__>
typename boost::math::tools::promote_args<T8__, T9__>::type
DL_star_intpart(T8__& x_f, T9__& param1, std::ostream* pstream){
	T9__ ans; 
	double h;
	double x_s;
	int n_steps;
	T9__ z_cur1;
	T9__ z_cur2;
	T9__ z_cur3;
	
	ans = 0.0 ;
	x_s = 0.0;
	n_steps=100;
	h=(x_f-x_s) / double(n_steps);
	for (int i=0; i<n_steps; i=i+1){
		z_cur1 = (x_s+(double(i))*h);
		z_cur2 = (x_s+(double(i)+0.5)*h);		
		z_cur3 = (x_s+(double(i)+1.0)*h);
		ans=ans+ DL_star_integrand( z_cur1, param1,0 )/3.0 + DL_star_integrand( z_cur2, param1,0 )*4.0/3.0 + DL_star_integrand( z_cur3, param1,0 )/3.0;
	}
	ans = ans * h/2;
	return ans;
}

