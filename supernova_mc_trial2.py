# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:22:22 2018

@author: Choon
"""

#some change
#another change

import pystan
import numpy as np
import matplotlib.pyplot as plt
import os
import time

n_iters=20000

model_code="""
functions {  
    real eta(real arg_a, real arg_s){
        real eta_ans;
        eta_ans = (2*( (arg_s^3 +1)^0.5 )) * ( arg_a^(-4) -0.154*arg_s/(arg_a^3) +0.4304*(arg_s^2)/(arg_a^2) +0.19097*(arg_s^3)/arg_a +0.066941*(arg_s^4)  )^-0.125;
        return eta_ans;
    }
}
data {
    int<lower=0> n;
    vector[n] z;
    vector[n] mu;
    matrix[n,n] C_inv;
}
transformed data {}
parameters {
    real h;
    real s;
}
transformed parameters {
    vector[n] mu_th;
    for (i in 1:n) {
        mu_th[i] = 25 - 5*log(h)/log(10) + 5*log( 3000*(1+z[i])*( eta(1,s)+eta(1/(1+z[i]),s) ) )/log(10);
        }
}
model {
    target += -0.5*( ( (mu-mu_th)' )*(C_inv*(mu-mu_th)) );
}
generated quantities {}
"""

"""
    vector[n] D_L_star;
    for (i in 1:n) {
        D_L_star[i] = 3000*(1+z[i])*( eta(1,s)+eta(1/(1+z[i]),s) );
        }
"""

zmu_data=np.genfromtxt(os.getcwd()+"\\jla_mub_0.txt")
C_data=np.genfromtxt(os.getcwd()+"\\jla_mub_covmatrix.txt")

z=zmu_data[:,0]
mu=zmu_data[:,1]
N=len(z)

Cov=C_data.reshape(N,N)
Cov_inv=np.empty((N,N))
for i in range(0,N):
    for j in range(0,N):
        Cov_inv[i][j]=1/Cov[i][j]

model_dat = {
            'n' : N,
            'z' : z,
            'mu' : mu,
            'C_inv' : Cov_inv,
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
s_chain=la['s']

#autocorrelation

f1=plt.figure()
ax1=f1.add_subplot(111)
f2=plt.figure()
ax2=f2.add_subplot(111)
f3=plt.figure()
ax3=f3.add_subplot(111)
f4=plt.figure()
ax4=f4.add_subplot(111)

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

ax3.hist(h_chain,bins=100)
ax4.hist(s_chain,bins=100)

plt.show()
