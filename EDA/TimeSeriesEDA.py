from calendar import month
from unicodedata import decomposition

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn import decomposition
import warnings
from sklearn.model_selection import train_test_split
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
sns.set_style("whitegrid")
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.seasonal import STL
"""Time series specific EDA checking for trend, seasonality and irregularity"""

#--------------------------------seasonality--------------------------------------------
def overall_montly_demand_trends():
    """Monthly Demand and Capacity Trends over all years"""
    df = pd.read_csv('data/CallCenterData.csv')
    df['month'] = df['month'].apply(lambda x: x[3:])
    month_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    # Convert 'month' to an ordered Categorical
    df['month'] = pd.Categorical(df['month'], categories=month_order, ordered=True)
    monthly_summary = df.groupby('month', as_index=False).sum()
    print(monthly_summary)
    
    plt.figure(figsize=(12, 6))
    plt.plot(monthly_summary['month'], monthly_summary['#ofphonelines'], marker='o', label='Total Interactions')
    plt.plot(monthly_summary['month'], monthly_summary['#noofchannels'], marker='o', label='Total Phone Lines Provisioned')
    plt.title('Overall Monthly Demand Across All Years')
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig('monthly_trends.png', dpi=100, bbox_inches='tight')
    plt.show()


def monthly_demand_info():
    """Demand and Capacity Summary by Month"""
    df= pd.read_csv('data/CallCenterData.csv')
    df['month'] = df['month'].apply(lambda x: x[3:])
    # Define the correct month order
    month_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    
    # Convert 'month' to an ordered Categorical
    df['month'] = pd.Categorical(df['month'], categories=month_order, ordered=True)
    fig, ax = plt.subplots(3, 4, figsize=(16, 10))
    ax = ax.flatten()

    for i, month in enumerate(month_order):
        month_data = df[df['month'] == month]
        x = range(1, len(month_data) + 1)
        y = month_data['#noofchannels']
        y2 = month_data['#ofphonelines']
        ax[i].plot(x, y, marker='o')
        ax[i].plot(x, y2, marker='o')
        ax[i].set_title(month)
        ax[i].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


def seasonal_demand_decomposition():
    """
    Performs time series decomposition on the full monthly demand series
    aggregated across all years to analyse trend, seasonality, and residuals.

    This helps visualise:
    - Long-term trend in demand
    - Repeating monthly seasonal patterns (period = 12)
    - Irregular/random fluctuations not explained by trend or seasonality
    """
    data = pd.read_csv('data/CallCenterData.csv')
    time_series =data["#noofchannels"]
    time_series.index = pd.date_range(
        start="2020-01-01",
        periods=len(time_series),
        freq="ME"
    )
    y_log = np.log(time_series)
    result = seasonal_decompose(y_log, model='additive', period=4)
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(12, 10))
    result.observed.plot(ax=ax1, title='Observed')
    result.trend.plot(ax=ax2, title='Trend')
    result.seasonal.plot(ax=ax3, title='Seasonal')
    result.resid.plot(ax=ax4, title='Residual')

    resid = result.resid.dropna()
    seasonal = result.seasonal.dropna()
    trend = result.trend.dropna()

    Fs = 1 - (np.var(resid) / np.var(seasonal + resid))
    Ft = 1 - (np.var(resid) / np.var(trend + resid))
    Fr = np.var(resid) / np.var(y_log.dropna())
    
    print(f"Seasonal strength: {Fs}, Trend strength: {Ft} , Residual proportion: {Fr}")


    plt.tight_layout()
    #plt.show()

def acf_pacf_plots():
    data = pd.read_csv('data/CallCenterData.csv')
    time_series =data["#noofchannels"]
    time_series.index = pd.date_range(
        start="2020-01-01",
        periods=len(time_series),
        freq="ME"
    )
    plot_acf(time_series, lags=50)
    plt.show()

    # PACF plot (helps identify direct dependencies)
    plot_pacf(time_series, lags=50)
    plt.show()

def spectral_analysis():
    data = pd.read_csv('data/CallCenterData.csv')
    time_series =data["#noofchannels"]
    time_series.index = pd.date_range(
        start="2020-01-01",
        periods=len(time_series),
        freq="ME"
    )
    # Remove mean (important)
    x = time_series - time_series.mean()

    # FFT
    fft_vals = np.fft.fft(x)
    freqs = np.fft.fftfreq(len(x))

    # Keep only positive frequencies
    mask = freqs > 0

    plt.plot(freqs[mask], np.abs(fft_vals[mask]))
    plt.xlabel("Frequency")
    plt.ylabel("Amplitude")
    plt.title("Spectral Analysis")
    plt.show()


def stl():
    # STL decomposition (robust to outliers, can handle complex seasonality)
    data = pd.read_csv('data/CallCenterData.csv')
    time_series =data["#noofchannels"]
    time_series.index = pd.date_range(
        start="2020-01-01",
        periods=len(time_series),
        freq="ME"
    )

    stl = STL(time_series, period=5, robust=True)
    result = stl.fit()

    # plot components
    result.plot()
    plt.show()
if __name__ == "__main__":
   stl()