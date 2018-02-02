
template <typename T0__, typename T1__, typename T2__>
typename boost::math::tools::promote_args<T0__, T1__, T2__>::type
ext_func(T0__& x, T1__& a, T2__& b, std::ostream* pstream__) {
  T1__ y;
  y = a*x + b;
  return y;
}


