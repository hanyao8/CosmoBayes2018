library(rstan)

model_code = "
functions {
real DL_star(real dsarg1, real dsarg2);

real lin_func(real x, real a, real b, real c){
real ans;
ans = a*x + b + c;
return ans;
}

real loglikelihood_lpdf(vector mu, vector muth, matrix invC) {
real logL;
logL = ((mu-muth)')*(invC*(mu-muth));
logL = logL*-0.5;
return logL;
}
}
data {
int<lower=0> n;
real x[n];
real y[n];
vector[n] z;
vector[n] mu;
matrix[n,n] invC;
}
transformed data {}
parameters {
real a;
real b;
real sigma;
real h;
real Omega_m;
}
transformed parameters {
vector[n] mu_th;
for (i in 1:n){
  mu_th[i] =  25.0 - 5.0*log10(h) + 5.0*log10(DL_star(z[i],Omega_m));
}

}
model {

target += loglikelihood_lpdf(mu| mu_th, invC);
}
generated quantities {}
"

#sigma ~ uniform(0, 10);
#y ~ normal(linexp, sigma);

#real linexp[n];
#for (i in 1:n) {
#  linexp[i] = lin_func(x[i], a, 0.0, DL_star(0.3,b));
#}


n = 31
a = 6
b = 50.0
sigma = 0.1

x = array(seq(0, 1, 1/(n-1)))
bs = array(c(b), dim = n)
y = a*x + bs + rnorm(n, sd = 0.1)

zmu_data = read.table(file.path(getwd(),'data/jla_mub_0.txt'))
Cov_inv = read.table(file.path(getwd(),'data/jla_mub_covinvmatrix.txt'))

z=zmu_data[[1]]
distmod=zmu_data[[2]]

model_dat = list(n = n, x = x, y = y, z=z, mu=distmod, invC=Cov_inv)

model1 = stan_model(model_code = model_code, allow_undefined = TRUE, includes = paste0('\n#include "', file.path(getwd(), 'ext_func6.hpp'), '"\n'))
fit = sampling(model1, data = model_dat,chains=1,iter=200)
print(fit)