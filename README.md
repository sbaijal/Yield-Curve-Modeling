# Yield-Curve-Modeling

## Overview

The yield curve represents a snapshot of government bond yields across 
all maturities at a given date. In practice, yields are only directly 
observable at a discrete set of maturities — the tenors at which 
benchmark bonds are actively traded. This leaves the curve discontinuous 
by nature, with no direct observation between traded maturities.

The objective of this project is to construct a smooth, continuous curve 
from these discrete observations — enabling reliable yield estimation at 
any maturity on a given date. To this end, we implement and compare two 
established curve construction methodologies: the Nelson-Siegel factor 
model and the Cubic Spline interpolation method. Each approach resolves 
the problem of curve continuity differently, and a comparative study of 
their behaviour, fit, and practical trade-offs forms the core of this 
analysis.

## Yield Curve Fitting Methods

To form a curve from discontinuous points we use two difeerent methodologies :

1. Nelson-Siegel factor model
2. Cubic Spline Interpolation

### 1. Nelson-Siegel Model

The Nelson-Siegel (1987) model represents the yield curve as a linear combination of three *factor loadings*:

$$y(\tau) = \beta_0 + \beta_1 \cdot \frac{1 - e^{-\lambda\tau}}{\lambda\tau} + \beta_2 \cdot \left[\frac{1 - e^{-\lambda\tau}}{\lambda\tau} - e^{-\lambda\tau}\right]$$

#### Fitted Parameters (US Treasury Curve — 2024-09-13)
| Parameter | Value | Interpretation |
|---|---|---|
| **β₀** | 3.618 |The level - Long-run neutral rate |
| **β₁** | 2.0137 |The Slope - Monetary policy stance |
| **β₂** | -0.7415 |The Curvature - Medium-term rate expectations|
| **λ** | 3.2945 |Decay rate — controls where hump peaks (τ* = 1/λ) = 0.3039|

**Fitting strategy:** For each candidate λ on a grid [0.01, 5.0], the loadings are fixed and β₀, β₁, β₂ are estimated via closed-form OLS. The λ that minimises SSE is selected.

### 2. Cubic Spline Model

A natural cubic spline fits a piecewise cubic polynomial through each pair of adjacent knots {τ₁, ..., τₙ}, subject to:
- **Continuity** of y, y', y'' at interior knots  
- **Natural boundary conditions**: y''(τ₁) = y''(τₙ) = 0  

This yields a system of N linear equations solved in closed form — no numerical optimisation required.

**Two variants are implemented:**

| Variant | Description | Use Case |
|---|---|---|
| **Interpolating** | Passes exactly through every observed yield | Exact pricing, CSA discounting |
| **Smoothing** | Penalised spline; trades fit for smoothness | Noisy data |

