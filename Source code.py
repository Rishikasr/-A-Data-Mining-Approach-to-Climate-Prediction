#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Load the datasets
country_temps = pd.read_csv('/Users/rishikasrivastava/Downloads/Big data/GlobalLandTemperaturesByCountry.csv')
city_temps = pd.read_csv('/Users/rishikasrivastava/Downloads/Big data/GlobalLandTemperaturesByMajorCity.csv')
state_temps = pd.read_csv('/Users/rishikasrivastava/Downloads/Big data/GlobalLandTemperaturesByState.csv')
global_temps = pd.read_csv('/Users/rishikasrivastava/Downloads/Big data/GlobalTemperatures.csv')

# Display basic information and first few rows of each dataset
datasets = {
    "Global Land Temperatures by Country": country_temps,
    "Global Land Temperatures by Major City": city_temps,
    "Global Land Temperatures by State": state_temps,
    "Global Temperatures": global_temps
}

# Create a summary of each dataset
summary = {name: data.describe() for name, data in datasets.items()}
summary_info = {name: data.info() for name, data in datasets.items()}
summary, summary_info


# In[2]:


# Preprocess the data by handling missing values and standardizing the date format
# Convert 'dt' to datetime format in all datasets and drop rows with missing temperatures

def preprocess_data(df):
    df['dt'] = pd.to_datetime(df['dt'])
    df = df.dropna(subset=['AverageTemperature'])
    return df

country_temps = preprocess_data(country_temps)
city_temps = preprocess_data(city_temps)
state_temps = preprocess_data(state_temps)
global_temps['dt'] = pd.to_datetime(global_temps['dt'])  # Only convert date for global dataset as it has fewer columns

# Show the information after preprocessing to verify
processed_info = {
    "Global Land Temperatures by Country": country_temps.info(),
    "Global Land Temperatures by Major City": city_temps.info(),
    "Global Land Temperatures by State": state_temps.info(),
    "Global Temperatures": global_temps.info()
}
processed_info


# In[5]:


import pandas as pd
import matplotlib.pyplot as plt

# Load your data
# Assuming the data is loaded into DataFrame `global_temps`

# Check columns in the dataframe
print("Columns in the dataframe:", global_temps.columns)

# Function to plot temperature trends safely
def plot_temperature_trends(data, title):
    if 'AverageTemperature' in data.columns:
        plt.figure(figsize=(14, 7))
        plt.plot(data['dt'], data['AverageTemperature'], label='Average Temperature', alpha=0.5)
        plt.title(title)
        plt.xlabel('Year')
        plt.ylabel('Temperature (°C)')
        plt.legend()
        plt.show()
    else:
        print(f"The column 'AverageTemperature' is not present in the dataset for {title}")

# Example usage
plot_temperature_trends(global_temps, "Global Temperature Trends")


# In[6]:


# Display the columns in the DataFrame
print("Columns in the DataFrame:", global_temps.columns)

# Display the first few rows of the DataFrame to see example data
print(global_temps.head())

# Get a summary of the DataFrame
print(global_temps.describe(include='all'))

# Check for missing data in each column
print(global_temps.isnull().sum())


# In[7]:


import matplotlib.pyplot as plt

# Convert 'dt' to datetime for plotting
global_temps['dt'] = pd.to_datetime(global_temps['dt'])

# Plotting Land Average Temperature Trends
plt.figure(figsize=(14, 7))
plt.plot(global_temps['dt'], global_temps['LandAverageTemperature'], label='Land Average Temperature', color='blue', alpha=0.5)
plt.title("Global Land Average Temperature Trends")
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.show()


# In[8]:


import matplotlib.pyplot as plt
import pandas as pd

# Convert 'dt' to datetime for easier handling
global_temps['dt'] = pd.to_datetime(global_temps['dt'])
global_temps['year'] = global_temps['dt'].dt.year
global_temps['month'] = global_temps['dt'].dt.month

# 1. Yearly Average Temperature Trends
yearly_avg_temp = global_temps.groupby('year')['LandAverageTemperature'].mean()
plt.figure(figsize=(14, 7))
plt.plot(yearly_avg_temp.index, yearly_avg_temp, label='Yearly Average Temp', color='green')
plt.title('Yearly Average Land Temperature')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.show()

# 2. Seasonal Patterns
monthly_avg_temp = global_temps.groupby('month')['LandAverageTemperature'].mean()
plt.figure(figsize=(10, 5))
plt.plot(monthly_avg_temp.index, monthly_avg_temp, label='Monthly Average Temp', color='purple')
plt.title('Seasonal Patterns in Land Temperature')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.xticks(range(1, 13))  # Set x-ticks to be the months
plt.legend()
plt.grid(True)
plt.show()

# 3. Temperature Extremes
plt.figure(figsize=(14, 7))
plt.plot(global_temps['dt'], global_temps['LandMaxTemperature'], label='Max Temp', color='red', alpha=0.5)
plt.plot(global_temps['dt'], global_temps['LandMinTemperature'], label='Min Temp', color='blue', alpha=0.5)
plt.title('Maximum and Minimum Land Temperatures')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.show()

# 4. Uncertainty Visualization
plt.figure(figsize=(14, 7))
plt.errorbar(x=yearly_avg_temp.index, y=yearly_avg_temp, yerr=global_temps.groupby('year')['LandAverageTemperatureUncertainty'].mean(), label='Average Temp ± Uncertainty', fmt='-o', color='orange', ecolor='lightgray', elinewidth=3, capsize=0)
plt.title('Yearly Average Temperature with Uncertainty')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:




