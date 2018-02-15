#include <math.h>
#include <cmath>

addone(double x){
    double ans;
    ans = x + 1.0;
    return ans;
}

addtwo(double x){
    double ans;
    ans = x + 2.0;
    return ans;
}

adde(double x){
	double ans;
	ans = x + exp(1.0);
	return ans;
}

add10e(double x){
	double ans;
	ans = x + 10.0*exp(1.0);
	return ans;
}

int_exp(double x_s, double x_f, int n_steps){
	double ans=0.0;
	double delta_x = (x_f-x_s) / double(n_steps);
	for (int i = 0; i < n_steps; i=i+1){
		ans = ans + exp( (double(i)+0.5)*delta_x + x_s );
	}
	ans = ans * delta_x;
	return ans;
}

DL_star_integrand(double x, double param){
	double ans1;
	ans1=pow(param*pow((1+x),3.0 ) +1 -param , -0.5);
	return ans1;
}

DL_star_intpart(double x_s, double x_f, int n_steps, double param1){
	double ans; 
	ans = 0.0 ;
	double h;
	h=(x_f-x_s) / double(n_steps);
	for (int i=0; i<n_steps; i=i+1){
		ans=ans+ DL_star_integrand((x_s+(double(i))*h) , param1 )/3.0 + DL_star_integrand((x_s+(double(i)+0.5)*h) , param1 )*4.0/3.0 + DL_star_integrand((x_s+(double(i)+1.0)*h) , param1 )/3.0;
	}
	ans = ans * h/2;
	return ans;
}