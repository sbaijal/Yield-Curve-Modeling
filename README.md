# Yield-Curve-Modeling

## Overview

The yield curve represents a snapshot of government bond yields across 
all maturities at a given date. In practice, yields are only directly 
observable at a discrete set of maturities — the tenors at which 
benchmark bonds are actively traded. This leaves the curve discontinuous 
by nature, with no direct observation between traded maturities.

The objective of this project is to construct a smooth, continuous curve 
from these discrete observations — enabling reliable yield estimation at 
any maturity on a given date. This project fits a continuous curve through those 
discrete points using two methods — Nelson-Siegel and Cubic Spline 
— and compares how each performs.

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
| **β₀** | 3.618% | The level - Long-run neutral rate |
| **β₁** | 2.0137% | The Slope - Monetary policy stance |
| **β₂** | -0.7415% | The Curvature - Medium-term rate expectations|
| **λ** | 3.2945 | Decay rate — controls where hump peaks (τ* = 1/λ) = 0.3039|

**Fitting strategy:** λ is found by grid search; β₀, β₁, β₂ are solved analytically via OLS at each candidate λ.

### 2. Cubic Spline Model

Two variants are implemented — an interpolating spline that passes 
exactly through every observed yield, and a smoothing spline that 
trades fit for smoothness via a penalty parameter.

**Two variants are implemented:**

| Variant | Description | Use Case |
|---|---|---|
| **Interpolating** | Passes exactly through every observed yield | Exact pricing, CSA discounting |
| **Smoothing** | Penalised spline; trades fit for smoothness | Noisy data |

## Results

Nelson-Siegel fits the curve with ~24bp RMSE using only 4 parameters. 
The interpolating spline fits exactly by construction but produces 
unstable forward rates. The smoothing spline sits between the two.

| Metric        | Nelson-Siegel    | Cubic Spline (Interp) | Cubic Spline (Smooth) |
|---------------|------------------|-----------------------|-----------------------|
| RMSE          | ~24 bp           | ~0 bp                 | ~8.5 bp               |
| MAE           | ~20.73 bp        | ~0 bp                 | ~7.7 bp               |
| Parameters    | 4                | N (one per knot)      | N + penalty           |
| Extrapolation | Converges to β₀  | Diverges beyond data  | Moderate              |
| Forward Rates | Smooth, analytic | Can oscillate         | Smooth                |

Nelson-Siegel is used for all downstream analysis in this project 
given its stable forward rates and forecastable parameter structure.

## Data

US Treasury yields downloaded from FRED. See `data/README.md`
for download instructions.

## How to Run

pip install -r requirements.txt

jupyter notebook notebooks/yield_curve_fitting.ipynb
