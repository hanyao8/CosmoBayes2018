library(rstan)

lin_reg_code = "
functions {
real ext_func2(real x, real a, real b, real c);
}
data {
int<lower=0> n;
real x[n];
real y[n];
real c;
}
transformed data {}
parameters {
real a;
real b;
real sigma;
}
transformed parameters {
real c_tf = c;
real mu[n];
for (i in 1:n) {
mu[i] = ext_func2(x[i], a, b, c);
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
b = 0
sigma = 0.1

x = array(seq(0, 1, 0.1))
bs = array(c(b), dim = 11)
y = a*x + bs + rnorm(11, sd = 0.1)

lin_reg_dat = list(n = n, x = x, y = y, c=2.5)

model1 = stan_model(model_code = lin_reg_code, allow_undefined = TRUE, includes = paste0('\n#include "', file.path(getwd(), 'ext_func2.hpp'), '"\n'))
fit = sampling(model1, data = lin_reg_dat,chains=1,iter=500)
print(fit)