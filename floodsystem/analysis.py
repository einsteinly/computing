# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 13:57:57 2017

This submodule is created to analysis the station data.

@author: Shengyuan
"""

import numpy as np
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):
    """ computes a least-squares fit of polynomial of degree p to water level data """

    # Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(dates, levels, p)

    # Convert coefficient into a polynomial that can be evaluated
    poly = np.poly1d(p_coeff)
    return poly
