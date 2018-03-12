
template <typename T1__, typename T2__, typename T3__>
typename boost::math::tools::promote_args<T1__,T2__,T3__>::type
inline var extlinfunc(T1__& argx, T2__& a_var, T3__& b_var, std::ostream* pstream__){
	double a;
	double b;
	
	a = a_var.val();
	b = b_var.val();
	
	double ans;
	
	ans = a*argx + b;
	
	double dans_da = argx;
	double dans_db = 1.0;
	
	return var(new precomp_vv_vari(
		ans,
		a_var.vi_,
		b_var.vi_,
		dans_da,
		dans_db
	));
};