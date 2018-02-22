#include <math.h>

template <typename T5__>
typename boost::math::tools::promote_args<T5__>::type
int_exp3(T5__& x_f3, std::ostream* pstream__){
    double x_s3 = 0.0;
	int n_steps3 = 1000;
	T5__ ans3;
		
	double delta_x3 = (x_f3-x_s3) / double(n_steps3);
	for (int i=0; i<n_steps3; i=i+1){
		ans3 = ans3 + exp( (double(i)+0.5)*delta_x3 + x_s3 );
	}
	ans3=ans3*delta_x3;
	//ans = d + 1.0;
    return ans3;
}
