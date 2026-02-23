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