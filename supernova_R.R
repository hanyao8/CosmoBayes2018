library(rstan)

model_code = "
functions {
real DL_star(real dsarg1, real dsarg2);

real loglikelihood_lpdf(vector mu, vector muth, matrix invC) {
real logL;
logL = ((mu-muth)')*(invC*(mu-muth));
logL = logL*-0.5;
return logL;
}
}
data {
int<lower=0> n;
vector[n] z;
vector[n] mu;
matrix[n,n] invC;
}
transformed data {}
parameters {
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


n = 31

zmu_data = read.table(file.path(getwd(),'data/jla_mub_0.txt'))
Cov_inv = read.table(file.path(getwd(),'data/jla_mub_covinvmatrix.txt'))

z=zmu_data[[1]]
distmod=zmu_data[[2]]

model_dat = list(n = n, z=z, mu=distmod, invC=Cov_inv)

model1 = stan_model(model_code = model_code, allow_undefined = TRUE, includes = paste0('\n#include "', file.path(getwd(), 'SN_ext_func.hpp'), '"\n'))
fit = sampling(model1, data = model_dat,chains=1,iter=200)
print(fit)