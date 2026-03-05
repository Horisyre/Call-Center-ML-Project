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
| Healthcare    | -1.15     | Highly Negatively-skewed;  |
| Telecom       | -1.50     | Highly Negatively-skewed;  |
| Banking       | -1.32     | Highly Negatively right-skewed;  |
| Technology    | -1.33     | Highly Negatively-skewed;  |
| Insurance     | -1.04     | Highly Negatively-skewed;  |
| # Phone Lines | +3.76     | Highly Positively-skewed; |
| # Channels    | -1.44     | Highly Negatively-skewed;  |

---

## 5. Correlations


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