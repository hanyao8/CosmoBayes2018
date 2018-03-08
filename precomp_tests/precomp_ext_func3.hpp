
template <typename T0__, typename T1__, typename T2__>
typename boost::math::tools::promote_args<T0__, T1__, T2__>::type
extlinfunc(T0__& x, T1__& a, T2__& b, std::ostream* pstream__) {
  T1__ ans;
  
  double a_doub;
  double b_doub;
  
  a_doub = a.val();
  b_doub = b.val();
  
  ans = a_doub*x + b_doub;
  return ans;
}


