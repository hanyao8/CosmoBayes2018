#include <math.h>

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
	double ans;
	double delta_x = (x_f-x_s) / double(n_steps);
	for (int i = 0; i < n_steps; i=i+1){
		ans = ans + exp( (double(i)+0.5)*delta_x + x_s );
	}
	ans = ans * delta_x;
	return ans;
}