# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 20:45:51 2018

@author: Choon
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as so
import os
import io

gft_data=np.genfromtxt(os.getcwd()+"\\SN_nonflat_wmodel_planck_Omegakparam_(priorwidth0.1)_3.csv",delimiter=',')

h_chain=gft_data[1:,1]
Omegam_chain=gft_data[1:,2]
Omegak_chain=gft_data[1:,3]
Omegal_chain=np.ones(len(Omegam_chain))-Omegam_chain-Omegak_chain
w_chain=gft_data[1:,4]

def find_confidence_interval(x, pdf, confidence_level):
    return pdf[pdf > x].sum() - confidence_level

def density_contour(xdata, ydata, nbins_x, nbins_y, ax=None, **contour_kwargs):
    """ Create a density contour plot.
    Parameters
    ----------
    xdata : numpy.ndarray
    ydata : numpy.ndarray
    nbins_x : int
        Number of bins along x dimension
    nbins_y : int
        Number of bins along y dimension
    ax : matplotlib.Axes (optional)
        If supplied, plot the contour to this axis. Otherwise, open a new figure
    contour_kwargs : dict
        kwargs to be passed to pyplot.contour()
    """

    H, xedges, yedges = np.histogram2d(xdata, ydata, bins=(nbins_x,nbins_y), normed=True)
    x_bin_sizes = (xedges[1:] - xedges[:-1]).reshape((1,nbins_x))
    y_bin_sizes = (yedges[1:] - yedges[:-1]).reshape((nbins_y,1))

    pdf = (H*(x_bin_sizes*y_bin_sizes))

    one_sigma = so.brentq(find_confidence_interval, 0., 1., args=(pdf, 0.68))
    two_sigma = so.brentq(find_confidence_interval, 0., 1., args=(pdf, 0.95))
    three_sigma = so.brentq(find_confidence_interval, 0., 1., args=(pdf, 0.99))
    levels = [one_sigma, two_sigma, three_sigma]
    levels.sort()

    print(one_sigma)
    print(levels)

    X, Y = 0.5*(xedges[1:]+xedges[:-1]), 0.5*(yedges[1:]+yedges[:-1])
    Z = pdf.T

    if ax == None:
        contour = plt.contour(X, Y, Z, levels=levels, origin="lower", **contour_kwargs)
        
    else:
        contour = ax.contour(X, Y, Z, levels=levels, origin="lower", **contour_kwargs)

    return contour

"""
def test_density_contour():
    norm = np.random.normal(0., 5., size=(125400, 2))
    density_contour(norm[:,0], norm[:,1], 100, 100)
    print(np.std(norm[:,0]))
    plt.show()
"""

def test_density_contour():
    density_contour(Omegam_chain, Omegal_chain, 100, 100)
    plt.show()

test_density_contour()