def Sarima_model():
    """Placeholder for SARIMA model implementation"""
    print("=" * 80)
    print("SARIMA MODEL")
    print("=" * 80)
    
    df = pd.read_csv('CallCenterData.csv')
    df['month'] = df['month'].apply(lambda x: x[3:])
    month_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    # Convert 'month' to an ordered Categorical
    df['month'] = pd.Categorical(df['month'], categories=month_order, ordered=True)
    #remove outliers and missing values
    # for phone lines where data is missing replace 0 or missing cell values with Nan
    df['#ofphonelines'] = df['#ofphonelines'].replace(0, np.nan)
    #handle missing values by calcuating the average phone line, using the average phone lines where  other records have the same number of channels provisioned, and the same month, and the same year
    
    
    """transform target variables channel and phone lines to ensure that they are stationary, 
    using np.log does not ensure constant mean or variance, but it can help stabilize variance and make the data more normally distributed, 
    which can be beneficial for certain models. However, it does not guarantee that the data will be stationary. To ensure stationarity, you may 
    need to perform additional transformations such as differencing or seasonal decomposition.
    """
    phone_transformed = np.log1p(df['#ofphonelines'])
    channel_transformed = np.log1p(df['#noofchannels'])    

    #split data into train and test sets
    #fit ARIMA model on training data and evaluate on test data

def Sarimax_model():
    """Placeholder for SARIMAX model implementation"""
    print("=" * 80)
    print("SARIMAX MODEL")
    print("=" * 80)
    
    df = pd.read_csv('CallCenterData.csv')
    df['month'] = df['month'].apply(lambda x: x[3:])
    month_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    # Convert 'month' to an ordered Categorical
    df['month'] = pd.Categorical(df['month'], categories=month_order, ordered=True)
    #remove outliers and missing values
    
    #transform target variables channel and phone lines to ensure that they are stationary
    phone_transformed = np.log1p(df['#ofphonelines'])
    channel_transformed = np.log1p(df['#noofchannels'])    
    #split data into train and test sets
    #fit ARIMA model on training data and evaluate on test data

