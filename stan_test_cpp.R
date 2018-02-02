library(rstan)

cpp_code = "
template <typename T0__, typename T1__, typename T2__>
typename boost::math::tools::promote_args<T0__, T1__, T2__>::type
ext_func(T0__& x, T1__& a, T2__& b, std::ostream* pstream__) {
  //double y;
  //y = a*x + b;
  return a*x+b;
}

"

write(cpp_code, "ext_func.hpp")

lin_reg_code = "
functions {
real ext_func(real x, real a, real b);
}
data {
int<lower=0> n;
real x[n];
real y[n];
}
transformed data {}
parameters {
real a;
real b;
real sigma;
}
transformed parameters {
real mu[n];
for (i in 1:n) {
mu[i] = ext_func(x[i], a, b);
}
}
model {
sigma ~ uniform(0, 10);
y ~ normal(mu, sigma);
}
generated quantities {}
"

n = 11
a = 6
b = 2
sigma = 0.1

x = array(seq(0, 1, 0.1))
bs = array(c(b), dim = 11)
y = a*x + bs + rnorm(11, sd = 0.1)

lin_reg_dat = list(n = n, x = x, y = y)

model1 = stan_model(model_code = lin_reg_code, allow_undefined = TRUE, includes = paste0('\n#include "', file.path(getwd(), 'ext_func.hpp'), '"\n'))
fit = sampling(model1, data = lin_reg_dat)
print(fit)