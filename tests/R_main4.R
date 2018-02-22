library(rstan)

lin_reg_code = "
functions {
real ext_func4(real x, real a, real b);
}
data {
int<lower=0> n;
real x[n];
real y[n];
}
transformed data {}
parameters {
real a;
real<lower=0> b;
real sigma;
}
transformed parameters {
real mu[n];
for (i in 1:n) {
mu[i] = ext_func4(x[i], a, b);
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
b = 50.0
sigma = 0.1

x = array(seq(0, 1, 0.1))
bs = array(c(b), dim = 11)
y = a*x + bs + rnorm(11, sd = 0.1)

lin_reg_dat = list(n = n, x = x, y = y)

model1 = stan_model(model_code = lin_reg_code, allow_undefined = TRUE, includes = paste0('\n#include "', file.path(getwd(), 'ext_func4.hpp'), '"\n'))
fit = sampling(model1, data = lin_reg_dat,chains=1,iter=500)
print(fit)