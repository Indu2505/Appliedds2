import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# The below code is used for convert the dataset into h years as columns and one with countries as columns
def ConvertDataset(filepath):
    '''
    The ConvertDataset function uses input parameter filepath to return datasets wuth years as columns and one with countries as columns
    ----------
    filepath : String
        the file location path is given as the input parameter.
    Returns
    -------
    yearDataset : dataframe
        years as the column names dataset
        
    countryDataset : dataframe
        countries as the column names dataset
    '''
    
    #reading the dataset.
    originalDataset = pd.read_csv(filepath)
    
    #dropping the columns with are not required and creating the year dataset.
    yearDataset = originalDataset.drop(columns=['Indicator Code','Country Code'])
    
    #Creating countryDataset
    countryDataset = pd.DataFrame.transpose(yearDataset)
    columnNames = countryDataset.iloc[0].values.tolist()
    countryDataset.columns = columnNames
    countryDataset = countryDataset.iloc[1:]
    return yearDataset, countryDataset

yearDataset , countryDataset = ConvertDataset('climate_change.csv')

indicators = countryDataset.iloc[0].unique()

brics = ['Brazil','Russian Federation','India','China','South Africa']

def compareBarplot(inputdataset ,indicator):
    '''
    the function produces bar plot with countries from brics with different indicators.

    Parameters
    ----------
    inputdataset : dataframe
        countryDataset for plotting the data in form of bar plot
    indicator : list values of index of indicators
        indicator to plot

    '''
    #using temp data variable to store country and its indicators values.
    tempData = []
    indexvalueIndicator = indicator
    
    # looping over the values.
    for i in range(5):
        tempData.append(inputdataset.iloc[: , indexvalueIndicator])
        i = i + 1
        indexvalueIndicator = indexvalueIndicator + 76
    # creating new dataset with the filtered values.
    newdata = pd.DataFrame(tempData)
    newdata = newdata.iloc[:,1:]
    newdata = newdata.transpose()
    #plotting the values
    newdata.iloc[48:55].plot(kind='bar',figsize=(15,8),xlabel='Years',ylabel=indicators[indicator],title=indicators[indicator]+' from 2008 to 2014')
    plt.show()

# plotting population growth values
compareBarplot(countryDataset[brics],4)  # values 4 is obtained from the indicators variable.
#plotting CO2 emission values.
compareBarplot(countryDataset[brics],44) 

def correlationHeatmap(inputdataset,country,indicator):
    '''
    This function is used to plot the heat maps which represents the correlation of the data.

    Parameters
    ----------
    inputdataset : Dataframe
       countryDataset for plotting the data in form of heatmaps
    country :string
        name of the country
    indicator : List
       indicator to plot and correlate

    '''
    
    data = inputdataset[[country]]
    tempData = []
    for i in indicator:
        tempData.append(data.iloc[:,i])
        
    dataN = pd.DataFrame(tempData)
    dataN = dataN.transpose()
    dataN.columns=dataN.iloc[0]
    dataN = dataN[31:60]
    dataN = dataN[1:]
    # Fills the data with null values
    dataN = dataN.fillna(dataN.median())
    
    # produces heatmaps
    ax = sns.heatmap(
        dataN.corr(), 
        vmin=-1, vmax=1, center=0
    )
    plt.title(country + " indicators correlation")
    ax.set_xticklabels(
        ax.get_xticklabels(),
        rotation=45,
        horizontalalignment='right'
    );
    plt.show()
    #print(dataN.corr())

correlationHeatmap(countryDataset, 'India', [4,0,8,44,55])
correlationHeatmap(countryDataset,'South Africa', [4,0,8,44,55])


def datastats(inputdataset,country,indicator):
    '''
    the function produces descriptive stats with countries from brics with different indicators.

    Parameters
    ----------
    inputdataset : Dataframe
       countryDataset for plotting the data in form of heatmaps
    country :string
        name of the country
    indicator : List
       indicator to plot and correlate

    Returns
    -------
    data90 dataframe
        descriptive stats from 1990 to 2000
    data20
        descriptive stats from 2000 to 2010
    data21
        descriptive stats from 2010 to present

    '''
    data = inputdataset[[country]]
    tempData = []
    for i in indicator:
        tempData.append(data.iloc[:,i])
        
    dataN = pd.DataFrame(tempData)
    dataN = dataN.transpose()
    dataN.columns=dataN.iloc[0]
    dataN = dataN[31:60]
    dataN = dataN[1:]
    dataN = dataN.fillna(dataN.median())
    # Splitting the dataset into decades to perform stats.
    # data from 1990 to 2000
    data90 = dataN[:10]
    
    # data from 2000 to 2010
    data20 = dataN[10:20]
    
    #data from 2010 to present
    data21 = dataN[20:]
    return data90.describe(), data20.describe(), data21.describe()

stats1,stats2,stats3 = datastats(countryDataset, 'Brazil', [60])

def comparelineplot(inputdataset ,indicator):
    '''
    the function produces line plot with countries from brics with different indicators.

    Parameters
    ----------
    inputdataset : dataframe
        countryDataset for plotting the data in form of bar plot
   indicator : list of indicators
            indicator to plot
    '''
    tempData = []
    indexvalueIndicator = indicator
    for i in range(5):
        tempData.append(inputdataset.iloc[: , indexvalueIndicator])
        i = i + 1
        indexvalueIndicator = indexvalueIndicator + 76
    newdata = pd.DataFrame(tempData)
    newdata = newdata.iloc[:,1:]
    newdata = newdata.transpose()
    #plotting the Line plots.
    newdata.iloc[48:55].plot(kind='line',figsize=(15,8),xlabel='Years',ylabel=indicators[indicator],title=indicators[indicator]+' from 2008 to 2014')
    plt.show()

comparelineplot(countryDataset[brics],52)
comparelineplot(countryDataset[brics],50)
