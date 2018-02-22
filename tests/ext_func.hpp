
template <typename T0__, typename T1__, typename T2__>
typename boost::math::tools::promote_args<T0__, T1__, T2__>::type
ext_func1(T0__& x, T1__& a, T2__& b, std::ostream* pstream__) {
  T1__ ans;
  ans = a*x + b;
  return ans;
}


