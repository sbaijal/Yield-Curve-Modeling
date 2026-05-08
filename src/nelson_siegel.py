'''
Nelson_siegel.py class to fit the Nelson-Siegel model to a set of bond yields and maturities.
The main function is fit_ns, which takes in arrays of maturities and bond yields, and returns the fitted parameters (b0, b1, b2, lam) along with RMSE and MAE of the fit.
The ns_loadings function computes the three factor loadings for the Nelson-Siegel model based on the input maturities and lambda parameter.
The ns_yields function calculates the fitted yields for given parameters and maturities, while the ns_forward function computes the forward rates implied by the Nelson-Siegel parameters.
The fit_ns function performs a grid search over possible lambda values to find the best fit to the observed bond yields, using least squares to solve for the beta parameters at each lambda.
'''
import numpy as np
from scipy.linalg import lstsq

def ns_loadings(tau, lam):
  tau = np.asarray(tau, float)
  lt = tau*lam
  safe = np.where(lt==0,1e-12,lt)
  L2 = (1-np.exp(-safe))/safe
  L3 = L2 - np.exp(-safe)
  return np.ones_like(tau), L2, L3

def ns_yields(tau, b0, b1, b2, lam):
  L1, L2, L3 = ns_loadings(tau, lam)
  return b0*L1 + b1*L2 + b2*L3

def ns_forward(tau, b0, b1, b2, lam):
  exp_lt = np.exp(-lam*tau)
  return b0 + b1*exp_lt + b2*(lam*tau)*exp_lt

def fit_ns(maturities, bond_yields, n_lambda=80):
  best_sse, best_parameters= np.inf, None
  
  for lam in np.linspace(0.01, 5.0, n_lambda):
    L1, L2, L3 = ns_loadings(maturities, lam)
    X = np.column_stack([L1, L2, L3])
    betas, _, _, _ = lstsq(X,bond_yields)
    sse = float(np.sum(bond_yields - X @ betas)**2)
    if sse < best_sse:
      best_sse = sse
      best_parameters = (*betas, lam)
  b0, b1, b2, lam = best_parameters
  
  fitted = ns_yields(maturities, b0, b1, b2, lam)
  rmse = np.sqrt(np.mean((bond_yields - fitted)**2))
  mae = np.mean(np.abs(bond_yields - fitted))
  return dict(b0=b0, b1=b1, b2=b2, lam=lam, rmse=rmse, mae=mae)