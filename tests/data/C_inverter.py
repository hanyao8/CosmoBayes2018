# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 21:21:45 2018

@author: Choon
"""

import numpy as np
import os
import io
"""
C_data=np.genfromtxt(os.getcwd()+"\\jla_mub_covmatrix.txt")
Cov=C_data.reshape(31,31)
Cov_inv=np.linalg.inv(Cov)

io.open(os.getcwd()+"\\jla_mub_covinvmatrix.txt",'w')
np.savetxt(os.getcwd()+"\\jla_mub_covinvmatrix.txt",Cov_inv)
"""
Cinv_data=np.genfromtxt(os.getcwd()+"\\jla_mub_covinvmatrix.txt")