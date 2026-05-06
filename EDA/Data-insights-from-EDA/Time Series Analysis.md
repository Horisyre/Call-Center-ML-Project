# Using time series analysis to determine which model would suit a yearly forecast model

Seasonal decomposition of the monthly channel provisioning data suggests the presence of some recurring seasonal behaviour, with visual indications of repetition across annual cycles. However, quantitative decomposition metrics indicate that both the seasonal and trend components explain only a relatively small proportion of the total variance, while the residual component accounts for the majority of variability in the series.

This suggests that the time series is dominated primarily by irregular or stochastic fluctuations rather than strong deterministic trend or seasonal structure. Although some repeating annual patterns may be visually observable, the measured seasonal strength is comparatively weak, indicating that the seasonal component is not sufficiently dominant relative to the residual variation.

Furthermore, the trend component does not appear stable across time and does not exhibit a clear long-term directional movement. This may indicate either weak underlying trend behaviour or instability in the decomposition structure.

Additional diagnostics, including autocorrelation analysis, seasonal subseries plots and spectral or frequency-domain methods, are therefore required before concluding whether the series contains statistically significant annual or multiple seasonal patterns suitable for forecasting.

## Additionally

-In the call centre environment, the number of channels provisioned is influenced by both internal seasonal patterns and external drivers such as operational changes and customer demand fluctuations. Unobserved drivers not explicitly captured in the dataset may still be present in the underlying system and can influence the observed seasonal patterns. For example, certain months exhibit zero phone calls provisioned, which may correspond to atypical operational conditions. These periods could indicate the presence of external or system-related factors—such as infrastructure changes, outages or process disruptions—that are not explicitly captured in the dataset. Other external factors may be customer behaviour, environmental changes, etc.  

-As a result, these events may influence the observed number of channels provisioned and contribute to irregularities in the time series structure.
Given that the data does not conform well to a single, stable seasonal structure, traditional single-seasonality forecasting models may be insufficient.
Instead, the problem is better suited to either:

-Multi-seasonal forecasting models, which can capture overlapping seasonal patterns (e.g. weekly, monthly, and yearly effects), or
Single-seasonal models with exogenous variables, which account for external drivers affecting the target variable.

## Supporting evidence

-Visual evidence can be found in images folder, in addition computed ranges in strenghts of residual, seasonality and trend are as follow:
    -period = 1 (Monthy): Seasonal strength: nan, Trend strength: 1.0 , Residual proportion: 0.0
    -period = 3: Seasonal strength: 0.02213985556823994, Trend strength: 0.2803107636668899 , Residual proportion: 0.7092682163279878
    -period = 4: Seasonal strength: 0.07706876624540315, Trend strength: 0.21293685655360206 , Residual proportion: 0.7332849550596667
    -period = 6(Semi Annually): Seasonal strength: 0.07706876624540315, Trend strength: 0.21293685655360206 , Residual proportion: 0.7332849550596667
    -periods = 12(Annually): Seasonal strength: 0.12512122597124276, Trend strength: 0.04298750514883565 , Residual proportion: 0.8354414731422368

    -Value Stengths : 
        -Low (~0.1–0.3) Model explains most structure (good decomposition)
        -Moderate (~0.3–0.6) Some unexplained structure remains
        -High (~0.6–1.0) Strong unexplained dynamics (missing factors / poor model fit)

## Autocorrelation analysis

-In additon to this I have also performed autocorrelation analysis:

    -The Autocorrelation Function (ACF) measures the linear correlation between the current value of the time series and its past values at different lags.
    In this specific dataset, most autocorrelation values after lag 0 are weak (close to zero) and mostly fall within the confidence band (the blue shaded area). This indicates very little significant linear autocorrelation in the data. 
    -Note that the autocorrelation at lag 0 is always exactly 1.0, as a series is perfectly correlated with itself.

-