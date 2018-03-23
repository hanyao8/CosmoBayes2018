# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 19:46:59 2018

@author: Choon
"""

import pystan
import numpy as np
import matplotlib.pyplot as plt

lin_reg_code = """
functions {
    real quad_func(real arg_x, real par_a, real par_b, real par_c){
        real ans;
        ans = par_a*(arg_x^2) + par_b*arg_x + par_c;
        return ans;
    }
}
data {
    int<lower=0> n;
    vector[n] x;
    vector[n] y;
}
transformed data {}
parameters {
    real a;
    real b;
    real c;
    real sigma;
}
transformed parameters {
    vector[n] mu;
    for (i in 1:n) {
        mu[i] = quad_func(x[i],a,b,c);
        }
}
model {
    sigma ~ uniform(0, 20);
    target += -log(sigma) - ((y-mu).*(y-mu))/(2*(sigma^2));
}
generated quantities {

}
"""

#mu[i] = a*(x[i]^2) + b*x[i] + c

#real mu[n]
#y ~ normal(mu, sigma);
#target += -log(sigma) - operator*( operator.*(operator-(y,mu),operator-(y,mu)),1/2/(sigma^2) )
#target += -log(sigma) -((y-mu)*(y-mu))/2/(sigma^2)
#target += -log(sigma) -((y-mu)^2 )/2/(sigma^2)

#line 32 sigma ~ uniform(0, 20) must be the declaration of a prior
#Indeed, it is P(theta)
#y ~ normal(mu, sigma) is the likelihood model i.e. P(y|params)
#The productorial of the distributions defined by the model gives the 
#likelihood function that can be used in Bayes theorm or maximised/sampled over

n = 12
_a = 6
_b = 2
_c = 5
x = np.linspace(0, 1, n)
y = _a*(x**2) + _b*x + _c + np.random.normal(0.0,0.1,n)
#y = _a*x + _b + np.random.randn(n)

lin_reg_dat = {
             'n': n,
             'x': x,
             'y': y
            }

#fit = pystan.stan(model_code=lin_reg_code, data=lin_reg_dat, iter=1000, chains=1)

#Alternative:
model=pystan.StanModel(model_code=lin_reg_code)
fit=model.sampling(iter=1000,data=lin_reg_dat,chains=1)

print(fit)

#a_posterior=fit.extract(permuted=True)['a']

fit.plot()

