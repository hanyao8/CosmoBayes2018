library(rstan)
source('Rimporttest.R')

model_code1= "
functions {  
real[] DL_integrand(real z_, real[] y, real[] theta, real[] x_r, int[] x_i) {
real dDdz[1];
dDdz[1] = (theta[1]*(1.0+z_)^3.0+(1-theta[1]-theta[2])*(1.0+z_)^(3*(1+theta[3]))+theta[2]*(1.0+z_)^2.0)^(-0.5);
return dDdz;
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
vector[n] z;
vector[n] mu;
matrix[n,n] invC;
}
transformed data {
real x_r[0];
int x_i[0];
real DL0[1];
real zsamp[n, 1];
DL0[1] = 0.0;
for (i in 1:n) {
zsamp[i, 1] = z[i];
}
}
parameters {
real h;
real Omega_m;
real w;
real Omega_k;
}
transformed parameters {
vector[n] mu_th;
real param_array[3];
param_array[1] = Omega_m;
param_array[2] = Omega_k;
param_array[3] = w;

for (i in 1:n) {
real r;
real DLstar;
r = integrate_ode_rk45(DL_integrand,DL0,0.0,zsamp[i],param_array,x_r,x_i)[1][1];
if (Omega_k > 0.001){
DLstar = 3000.*(1.0 + z[i])*sinh(r*(fabs(Omega_k))^0.5)*(fabs(Omega_k))^-0.5;
}
else if (Omega_k < -0.001){
DLstar = 3000.*(1.0 + z[i])*sin(r*(fabs(Omega_k))^0.5)*(fabs(Omega_k))^-0.5;
}
else {
DLstar = r*3000*(1.0+z[i]);
}
mu_th[i] = 25.0 - 5.0*log10(h) + 5.0*log10( DLstar );
}
}
model {
Omega_m ~ normal(0.316, 0.009);
Omega_k ~ normal(0,0.1);
target += loglikelihood_lpdf(mu| mu_th, invC);
}
"

data1 = list(n = 31, z = zmu_data[,1], mu = zmu_data[,2], invC = Cov_inv)
model1 = stan_model(model_code = model_code1)
fit = sampling(model1, data = data1, chains=4, iter=4000)
print(fit)

f_e=extract(fit)

h_results=f_e$h
Omega_m_results=f_e$Omega_m
w_results=f_e$w
Omega_k_results=f_e$Omega_k

df_results=data.frame(h_results,Omega_m_results,Omega_k_results,w_results)

write.csv(df_results,file="SN_nonflat_wmodel_planck_Omegakparam_(priorwidth0.1)_3.csv")

