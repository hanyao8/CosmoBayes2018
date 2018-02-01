# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 19:18:47 2018

@author: Choon
"""

import pystan
import numpy as np
import matplotlib.pyplot as plt
import os
import time

n_iters=10

model_code= """
functions {  
    real[] DL_integrand(real z_, real[] y, real[] theta, real[] x_r, int[] x_i) {
        real dDdz[1];
        dDdz[1] = (theta[1]*(1.0+z_)^3.0+1.0-theta[1])^(-1.0/2.0);
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
    real DL0[1];
    real z_0;
    real zsamp[n,1];
}
transformed data {
    real x_r[0];
    int x_i[0];
}
parameters {
    real h;
    real Omega_m;
}
transformed parameters {
    vector[n] mu_th;
    for (i in 1:n) {
        real DLstar;
        real param_array[1];
        param_array[1] = Omega_m;
        DLstar = integrate_ode_rk45(DL_integrand,DL0,0.0,zsamp[i],param_array,x_r,x_i)[1][1];
        DLstar = DLstar * 3000 * (1.0+z[i]);
        mu_th[i] = 25.0 - 5.0*log10(h) + 5.0*log10( DLstar );
        }
}
model {
    Omega_m ~ uniform(0.0,1.0);
    target += loglikelihood_lpdf(mu| mu_th, invC);
}
"""
"""
    real DLstar(real argz,real argo) {
        real Dsol;
        Dsol = integrate_ode_rk45(DL_integrand,DL0,0.0,[argz],[argo],x_r,x_i)[1][1];
        Dsol = Dsol * 3000 * (1.0+argz);
        return Dsol;
        
        }
    
    mu_th[i] = 25.0 - 5.0*log10(h) + 5.0*log10( DLstar(z[i],Omega_m) );
"""

"""
functions {          
    real etaf(real arg_a, real arg_o){
        real s;
        real eta_ans;
        s = ((1-arg_o)/arg_o)^(1./3);
        eta_ans = arg_a^(-4.0);
        eta_ans = eta_ans-0.154*s/(arg_a^3.0); 
        eta_ans = eta_ans+0.4304*(s^2.0)/(arg_a^2.0); 
        eta_ans = eta_ans+0.19097*(s^3.0)/arg_a; 
        eta_ans = eta_ans+0.066941*(s^4.0)  ;
        eta_ans = eta_ans^(-1.0/8.0);
        eta_ans = eta_ans*2.0*( (s^3.0 +1.0)^0.5 );
        return eta_ans;
        }
    
    real DLstar(real argz,real argo){
        return 3000.0*(1.0+argz)*( etaf(1.0,argo)-etaf(1.0/(1.0+argz),argo) );
        }
    
    real loglikelihood_lpdf(vector mu, vector muth, matrix invC){
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
parameters {
    real h;
    real Omega_m;
}
transformed parameters {
    vector[n] mu_th;
    for (i in 1:n) {
        mu_th[i] = 25.0 - 5.0*log10(h) + 5.0*log10( DLstar(z[i],Omega_m) );
        }
}
model {
    Omega_m ~ uniform(0.0,1.0);
    target += loglikelihood_lpdf(mu| mu_th, invC);
}
"""


zmu_data=np.genfromtxt(os.getcwd()+"\\data\\jla_mub_0.txt")

z=zmu_data[:,0]
mu=zmu_data[:,1]
N=len(z)
Cov_inv=np.genfromtxt(os.getcwd()+"\\data\\jla_mub_covinvmatrix.txt")

model_dat = {
            'n' : N,
            'z' : z,
            'mu' : mu,
            'invC' : Cov_inv,
            'DL0' : np.array([0.0]),
            'z_0' : 0.0,
            'zsamp' : np.reshape(z,(31,1))
            }


st=time.time()
model=pystan.StanModel(model_code=model_code)
model_time=time.time()-st

st=time.time()
fit=model.sampling(iter=int(n_iters*2),data=model_dat,chains=1)
fit_time=time.time()-st

print(fit)
fit.plot()
print("StanModel TIME TAKEN: ",model_time)
print("StanModel.sampling TIME TAKEN: ",fit_time)

la=fit.extract(permuted=True)
h_chain=la['h']
O_chain=la['Omega_m']

#autocorrelation

f1=plt.figure()
ax1=f1.add_subplot(111)
f2=plt.figure()
ax2=f2.add_subplot(111)
f3=plt.figure()
ax3=f3.add_subplot(111)
f4=plt.figure()
ax4=f4.add_subplot(111)

"""
N_ACsites=5
h_AC_result=[[] for i in range(0,N_ACsites)]
h_av=np.mean(h_chain)
s_AC_result=[[] for i in range(0,N_ACsites)]
s_av=np.mean(s_chain)
for k in range(0,N_ACsites):
    i=int(k*n_iters/N_ACsites)
    psi_h=[(h_chain[i+j]-h_av)*(h_chain[i]-h_av) for j in range(0,int(n_iters/N_ACsites))]
    h_AC_result[k]=psi_h
    ax1.plot(np.linspace(0,int(n_iters/N_ACsites-1),int(n_iters/N_ACsites)),psi_h)
    psi_s=[(s_chain[i+j]-s_av)*(s_chain[i]-s_av) for j in range(0,int(n_iters/N_ACsites))]
    s_AC_result[k]=psi_s
    ax2.plot(np.linspace(0,int(n_iters/N_ACsites-1),int(n_iters/N_ACsites)),psi_s)

h_AC_result=np.array(h_AC_result)
s_AC_result=np.array(s_AC_result)

h_mean_AC=[np.mean(abs(h_AC_result[i])) for i in range(0,N_ACsites)]
s_mean_AC=[np.mean(abs(s_AC_result[i])) for i in range(0,N_ACsites)]
"""
ax3.hist(h_chain,bins=100)
ax4.hist(O_chain,bins=100)

plt.show()
