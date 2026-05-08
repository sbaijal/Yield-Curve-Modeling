'''
CubicSpline.py class to fit a cubic spline to a set of bond yields and maturities.
The main function is cs_interp_fit, which takes in arrays of maturities and bond yields, and returns the fitted cubic spline.
The cs_smooth_fit function fits a smooth cubic spline to the data.
The cs_forward function computes the forward rates implied by the cubic spline.
'''

import numpy as np
from scipy.interpolate import CubicSpline, UnivariateSpline

def cs_interp_fit(maturities, bond_yields):
  cs_interp = CubicSpline(maturities, bond_yields, bc_type='natural')
  return cs_interp

def cs_smooth_fit(maturities, bond_yields, k=3, s=0.08):
  cs_smooth = UnivariateSpline(maturities, bond_yields, k=k, s=s)
  return cs_smooth

def cs_forward(spline, tau, mode='cubic'):
  tau = np.asarray(tau, float)
  if mode == 'cubic':
    return spline(tau) + tau*spline(tau,1)
  else:
    return spline(tau) + tau*spline.derivative()(tau)