library(rstan)

model_code = "
functions {
real extlinfunc(real arg_x, real par_a, real par_b);

real intlinfunc(real argx, real para, real parb){
  real ans;
  ans = para*argx + parb;
  return ans;
}
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
mu[i] = extlinfunc(x[i], a, b);
}

}
model {

sigma ~ uniform(0, 10);
y ~ normal(mu, sigma);
}
generated quantities {
real result;
result=1.5;
}
"


n = 11
a = 6.0
b = 0.0
sigma = 0.1

x = array(seq(0, 1, 0.1))
bs = array(c(b), dim = 11)
y = a*x + bs + rnorm(11, sd = 0.1)

#zmu_data = read.table(file.path(getwd(),'data/jla_mub_0.txt'))
#Cov_inv = read.table(file.path(getwd(),'data/jla_mub_covinvmatrix.txt'))

#z=zmu_data[[1]]
#distmod=zmu_data[[2]]

#model_dat = list(n = n, z=z, mu=distmod, invC=Cov_inv)
model_dat = list(n=n,x=x,y=y)

model1 = stan_model(model_code = model_code, allow_undefined = TRUE, includes = paste0('\n#include "', file.path(getwd(), 'precomp_ext_func3.hpp'), '"\n'))
fit = sampling(model1, data = model_dat,chains=1,iter=200)
print(fit)