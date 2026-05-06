import calendar
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
from sklearn.model_selection import train_test_split


# Set visualization styles
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
#---------------------------------GENERAL EDA------------------------------------------------
def readHead():
    """Display first few rows of dataset"""
    df = pd.read_csv('data/CallCenterData.csv')
    print("=" * 80)
    print("FIRST 5 ROWS")
    print("=" * 80)
    print(df.head())
    print("\n")

def CheckNan():
    """Check for missing values"""
    df = pd.read_csv('data/CallCenterData.csv')
    print("=" * 80)
    print("MISSING VALUES ANALYSIS")
    print("=" * 80)
    missing = df.isnull().sum()
    missing_percent = (df.isnull().sum() / len(df)) * 100
    missing_df = pd.DataFrame({
        'Missing_Count': missing,
        'Percentage': missing_percent
    })
    print(missing_df)
    print(f"\nTotal missing values: {df.isnull().sum().sum()}")
    print("\n")

def dataset_shape_info():
    """Display dataset shape and info"""
    df = pd.read_csv('data/CallCenterData.csv')
    print("=" * 80)
    print("DATASET SHAPE AND INFO")
    print("=" * 80)
    print(f"Shape: {df.shape}")
    print(f"Total Records: {len(df)}")
    print(f"Total Columns: {len(df.columns)}")
    print("\nData Types:")
    print(df.dtypes)
    print("\nMemory Usage:")
    print(df.memory_usage(deep=True))
    print("\n")

def descriptive_statistics():
    """Display descriptive statistics"""
    df = pd.read_csv('data/CallCenterData.csv')
    df_copy  =df.copy()
    df_copy= df_copy.drop(columns=['month'], errors='ignore') 
    print("=" * 80)
    print("DESCRIPTIVE STATISTICS")
    print("=" * 80)
    print(df_copy.describe())
    print("\nAdditional Statistics:")
    print(f"Skewness:\n{df_copy.skew()}\n")
    print(f"Kurtosis:\n{df_copy.kurtosis()}\n")
    print("\n")

def check_duplicates():
    """Check for duplicate rows"""
    df = pd.read_csv('data/CallCenterData.csv')
    print("=" * 80)
    print("DUPLICATE ROWS ANALYSIS")
    print("=" * 80)
    duplicates = df.duplicated().sum()
    print(f"Total duplicate rows: {duplicates}")
    if duplicates > 0:
        print("\nDuplicate rows:")
        print(df[df.duplicated(keep=False)].sort_values(by=list(df.columns)))
    print("\n")

def unique_values_analysis():
    """Display unique value counts for each column"""
    df = pd.read_csv('data/CallCenterData.csv')
    print("=" * 80)
    print("UNIQUE VALUES ANALYSIS")
    print("=" * 80)
    for col in df.columns:
        unique_count = df[col].nunique()
        print(f"{col}: {unique_count} unique values")
    print("\n")

def categorical_value_counts():
    """Display value counts for categorical columns"""
    df = pd.read_csv('data/CallCenterData.csv')
    print("=" * 80)
    print("CATEGORICAL VALUE COUNTS")
    print("=" * 80)
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        print(f"\n{col}:")
        print(df[col].value_counts())
    print("\n")

def correlation_matrix():
    """Generate and display correlation matrix"""
    df = pd.read_csv('data/CallCenterData.csv')
    print("=" * 80)
    print("CORRELATION MATRIX")
    print("=" * 80)
    numeric_df = df.select_dtypes(include=[np.number])
    if not numeric_df.empty:
        corr_matrix = numeric_df.corr()
        print(corr_matrix)
        
        # Visualize correlation matrix
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, 
                    fmt='.2f', square=True, linewidths=0.5)
        plt.title('Correlation Matrix Heatmap')
        plt.tight_layout()
        plt.savefig('correlation_matrix.png', dpi=100, bbox_inches='tight')
        plt.show()
    else:
        print("No numeric columns found for correlation analysis")
    print("\n")

def Total_demand_correlation_matrix():
    """Total Industry Demand and Capacity Correlation Matrix"""
    df = pd.read_csv('data/CallCenterData.csv')

    df['Total_Interactions'] = df['Healthcare'] + df['Telecom'] + df['Banking'] + df['Technology'] + df['Insurance']
    total_demand_df = df[['#ofphonelines', '#noofchannels', 'Total_Interactions']]
    if not total_demand_df.empty:
        corr_matrix = total_demand_df.corr()
        
        # Visualize correlation matrix
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, 
                    fmt='.2f', square=True, linewidths=0.5)
        plt.title('Total Interactions Correlation Matrix Heatmap')
        plt.tight_layout()
        plt.savefig('correlation_matrix.png', dpi=100, bbox_inches='tight')
        plt.show()
    else:
        print("No numeric columns found for correlation analysis")
    print("\n")

def monthly_variance():
    """Variance of Demand and Capacity by Month"""
    df = pd.read_csv('data/CallCenterData.csv')
    df['month'] = df['month'].apply(lambda x: x[3:])
    month_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    
    # Convert 'month' to an ordered Categorical
    df['month'] = pd.Categorical(df['month'], categories=month_order, ordered=True)
    
    monthly_variance = df.groupby('month').agg({
        '#ofphonelines': 'var',
        '#noofchannels': 'var'
    }).reset_index()
    
    print("=" * 80)
    print("MONTHLY VARIANCE OF DEMAND AND CAPACITY")
    print("=" * 80)
    print(monthly_variance)
    print("\n")


def yearly_demand_trends():
    """Yearly Demand and Capacity Trends"""
    df = pd.read_csv('data/CallCenterData.csv')
    df['month'] = df['month'].apply(lambda x: x[3:])

    years_array = []
    x=1
    for month in df['month']:
        years_array.append(x)
        if month.startswith('Dec'):
            x += 1
    df['year'] = years_array
    
    yearly_summary = df.groupby('year').agg({
        '#ofphonelines': 'sum',           # sum all calls in the year
        '#noofchannels': 'sum'      # sum all phone lines provisioned
    }).reset_index()
    
    plt.figure(figsize=(12, 6))
    plt.plot(yearly_summary['year'], yearly_summary['#ofphonelines'], marker='o', label='Total Phone Lines Provisioned')
    plt.plot(yearly_summary['year'], yearly_summary['#noofchannels'], marker='o', label='Total channels Provisioned')
    plt.title('Yearly Demand and Capacity Trends')
    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig('yearly_trends.png', dpi=100, bbox_inches='tight')
    plt.show()

def phone_lines_box_plot():
    """Distribution of Phone Lines Provisioned by Month"""
    fig = plt.figure(figsize =(10, 7))
    df = pd.read_csv('data/CallCenterData.csv')


    df_copy = df.copy()
    df_copy['month'] = df_copy['month'].apply(lambda x: x[3:])
    
    d = [df[df['month'] == month]['#ofphonelines'] for month in df['month'].unique()]
    plt.boxplot(d,showmeans=True)

    plt.ylabel("Number of Phone Lines Provisioned")
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    plt.xticks(ticks=range(1, len(months)+1), labels=months, rotation=45 )
    plt.show()

def scatter_matrix():
    """Generate pairwise scatter plots"""
    df = pd.read_csv('data/CallCenterData.csv')
    print("=" * 80)
    print("SCATTER MATRIX")
    print("=" * 80)
    numeric_df = df.select_dtypes(include=[np.number])
    
    if len(numeric_df.columns) > 1:
        from pandas.plotting import scatter_matrix
        scatter_matrix(numeric_df, alpha=0.3, figsize=(12, 10))
        plt.tight_layout()
        plt.savefig('scatter_matrix.png', dpi=100, bbox_inches='tight')
        plt.show()
    print("\n")

def outlier_detection():
    """Detect outliers using IQR method"""
    df = pd.read_csv('data/CallCenterData.csv')
    print("=" * 80)
    print("OUTLIER DETECTION (IQR Method)")
    print("=" * 80)
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        print(f"\n{col}:")
        print(f"  Q1: {Q1:.2f}, Q3: {Q3:.2f}, IQR: {IQR:.2f}")
        print(f"  Lower Bound: {lower_bound:.2f}, Upper Bound: {upper_bound:.2f}")
        print(f"  Number of Outliers: {len(outliers)}")
    print("\n")

def statistical_tests():
    """Perform statistical tests"""
    df = pd.read_csv('data/CallCenterData.csv')
    print("=" * 80)
    print("STATISTICAL TESTS")
    print("=" * 80)
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    for col in numeric_cols:
        data = df[col].dropna()
        if len(data) > 2:
            # Normality test (Shapiro-Wilk)
            stat, p_value = stats.shapiro(data[:5000] if len(data) > 5000 else data)
            print(f"\n{col} - Normality Test (Shapiro-Wilk):")
            print(f"  Statistic: {stat:.4f}, P-value: {p_value:.4f}")
            print(f"  Normal: {'Yes' if p_value > 0.05 else 'No'}")
    print("\n")

def pairwise_plots():
    """Create pairwise relationship plots"""
    df = pd.read_csv('data/CallCenterData.csv')
    print("=" * 80)
    print("PAIRWISE PLOTS")
    print("=" * 80)
    numeric_df = df.select_dtypes(include=[np.number])
    
    if len(numeric_df.columns) > 0:
        # Create pairplot if enough numeric columns
        if len(numeric_df.columns) <= 5:
            sns.pairplot(numeric_df, diag_kind='hist')
            plt.savefig('pairplot.png', dpi=100, bbox_inches='tight')
            plt.show()
    print("\n")

def quantile_analysis():
    """Display quantile analysis"""
    df = pd.read_csv('data/CallCenterData.csv')
    print("=" * 80)
    print("QUANTILE ANALYSIS")
    print("=" * 80)
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    quantiles = [0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99]
    for col in numeric_cols:
        print(f"\n{col}:")
        print(df[col].quantile(quantiles))
    print("\n")

if __name__ == "__main__":
   monthly_variance()