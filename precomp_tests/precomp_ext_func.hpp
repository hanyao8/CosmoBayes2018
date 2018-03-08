
inline var extlinfunc (double argx, const var& a_var, const var& b_var, std::ostream* pstream){
	double a = a_var.val();
	double b = b_var.val();
	
	double ans;
	
	ans = a*argx + b;
	
	double dans_da = argx,
			dans_db = 1.0;
	
	return var(new precomp_vv_vari(
		ans,
		a_var.vi_,
		b_var.vi_,
		dans_da,
		dans_db
	));
}