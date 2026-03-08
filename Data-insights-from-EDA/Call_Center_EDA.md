# Call Center Dataset – Exploratory Data Analysis (EDA)

## 1. Introduction
- Dataset description: monthly call volumes by industry, number of phone lines, number of communciation channels
- Purpose: Identify trends, anomalies and insights for forecasting and operational planning

---

## 2. Data Summary
- No missing values were found in the dataset.

- Zero values for the number of phone lines occur over a single year across several months. This may indicate a reporting issue, manual input error, or a temporary shift in communication infrastructure (e.g., use of VoIP or other digital channels).

- Importantly, this is not considered an operational anomaly, since other communication channels remained active during these months and call volumes continued.

---

## 3. General Trend Analysis


---
## 4. Skewness & Kurtosis

| Column        | Skewness | Interpretation |
|---------------|----------|----------------------------|
| Healthcare    | +2.1     | Highly right-skewed; industry with the highest frequency of interactions, showing rapid growth with occasional spikes |
| Telecom       | +1.5     | Highly right-skewed; shows relatively stable growth after Healthcare, with mostly moderate values and occasional spikes |
| Banking       | +1.2     | Highly right-skewed; relatively stable growth with some higher interaction periods |
| Technology    | +1.7     | Highly right-skewed; lower frequency of interactions overall, with emerging growth and some extreme months |
| Insurance     | +1.0     | Moderately right-skewed; generally stable with minor spikes |
| # Phone Lines | -0.3     | Slightly left-skewed; mostly stable, with zero months possibly indicating alternative voice channels |
| # Channels    | +0.8     | Moderately right-skewed; gradual shift toward multi-channel communication |


| Column        | Kurtosis | Interpretation |
|---------------|----------|----------------------------|
| Healthcare    | -1.15     | Light-tailed; platykurtic (somewhat flatter than normal) |
| Banking       | -1.32     | Light-tailed; platykurtic (somewhat flatter than normal)  |
| Technology    | -1.33     | Light-tailed; platykurtic (somewhat flatter than normal)  |
| Insurance     | -1.04     | Light-tailed; platykurtic (flatter than normal) |
| # Phone Lines | +3.76     | Heavy-tailed;  Strongly leptokurtic (Taller peak than normal)|
| # Channels    | -1.44     | Light-tailed; platykurtic (flatter than normal) |

-Conclusion
-Most values are low in the overall range of each field, with occasional high values stretching the distribution to the right(outliers).
-Extremely large values are rare, even more so than in a normal distribution.
-This suggests that the call centre may occasionally experience jumps in monthly interactions, but these spikes are unlikely to be very large.

---

## 5. Correlations

### Correlation Matrix

|                | Healthcare | Telecom | Banking | Technology | Insurance | #ofphonelines | #noofchannels |
|----------------|-----------|---------|---------|------------|-----------|---------------|---------------|
| Healthcare     | 1.00 | 0.98 | 0.99 | 0.94 | 0.40 | 0.48 | -0.07 |
| Telecom        | 0.98 | 1.00 | 0.98 | 0.96 | 0.51 | 0.44 | -0.06 |
| Banking        | 0.99 | 0.98 | 1.00 | 0.94 | 0.39 | 0.46 | -0.06 |
| Technology     | 0.94 | 0.96 | 0.94 | 1.00 | 0.61 | 0.41 | -0.08 |
| Insurance      | 0.40 | 0.51 | 0.39 | 0.61 | 1.00 | 0.06 | -0.05 |
| #ofphonelines  | 0.48 | 0.44 | 0.46 | 0.41 | 0.06 | 1.00 | -0.05 |
| #noofchannels  | -0.07 | -0.06 | -0.06 | -0.08 | -0.05 | -0.05 | 1.00 |

-Healthcare, Telecom, Banking, Technology → extremely high correlations (0.94–0.99)→ these industries move very similarly.

-Insurance → moderate correlation with others (0.39–0.61).

-#ofphonelines → moderate correlation (~0.41–0.48).

-#noofchannels → almost no correlation with the other variables (around -0.05 to -0.08). 

-The number of phone lines and channels may not show meaningful correlations with individual industries because these resources are designed to handle aggregate demand across all industries. As a result, it is more appropriate to analyze their relationship with total industry interactions rather than with each industry separately.

### Total Demand Correlation Matrix

|                  | #ofphonelines | #noofchannels | Total_Interactions |
|------------------|---------------|---------------|------------------|
| #ofphonelines       | 1.00          | -0.05         | 0.47          |
| #noofchannels       | -0.05         | 1.00          | -0.07         |
| Total_Interactions  | 0.47          | -0.07         | 1.00          |

-Here, we see little change in the correlation between the number of channels and total interactions, suggesting that there is no clear linear relationship between how channels are provisioned and the number of interactions each month.

-Similarly, there is little change in the correlation between the number of phone lines and total industry activity, which suggests that no single industry dominates the total number of phone lines provisioned.  

---

## 6. Anomalies & Outliers

- Highlight months with 0 phone lines, unusual high call volume months and how this may affect forecasting

---

## 7. Operational Insights

---

## 8. Recommendations for Forecasting
- How to handle skewed data,outliers,algorithms we could use and models we could use

---

## 9. Conclusion
- Summary of key insights, How we will use this data for forecasting in call center calls