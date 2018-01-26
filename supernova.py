#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 16:56:24 2018

@author: Alexheib
"""

import pystan
import arrays

lin_reg_code = """
functions {
        real etaf(real a, real omega){
                real s;
                real eta;
                s = ((1-omega)/omega)^(1./3);
                eta = (1/a^4-0.1540*(s/(a^3))+0.4304*(s/a)^2+0.19097*s^3/a+0.066941*s^4);
                eta = eta^(-1./8.);
                eta = eta*2.*(s^3+1)^0.5;
                return eta;
                }
        real Dlstar(real z, real omega){
                real D;
                real x;
                x = 1./(1+z);
                D = (3000.)*(1+z)*(etaf(1, omega)-etaf(x, omega));
                return D;
                }
        real loglikelihood_lpdf(real[] mu, real[] muth, real[,] invC, int n){
                real logL;
                logL = 0.;
                for (i in 1:n){
                        for (j in 1:n){
                                logL = logL + (mu[i] - muth[i])*invC[i, j]*(mu[j] - muth[j]);
                                }
                        }
                logL = logL*-0.5;
                return logL;
                }
}
data {
        int<lower = 0> n;
        real z[n];
        real mu[n];
        real invC[n, n];
}

parameters {
        real h;
        real omega;
}
transformed parameters {
        real muth[n];
        for (i in 1:n){
                muth[i] <- 25. - 5.*log10(h) + 5.*log10(Dlstar(z[i], omega));
                }
}
model {
        target += loglikelihood_lpdf(mu| muth, invC, n);
}
"""

n = 31
z = arrays.z
mu = arrays.mu
invC = arrays.invC

lin_reg_dat = {
            'n': n,
            'z': z,
            'mu': mu,
            'invC': invC
            }

model = pystan.StanModel(model_code=lin_reg_code)
fit = model.sampling(data = lin_reg_dat)

print(fit)
