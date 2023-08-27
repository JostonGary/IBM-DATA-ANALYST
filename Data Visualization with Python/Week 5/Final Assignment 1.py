Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
csv_file = '/Users/lirui/Desktop/historical_automobile_sales.csv'
df = pd.read_csv(csv_file)
print('CSV file read into dataframe!')
CSV file read into dataframe!
df.describe()
              Year   Recession  ...  unemployment_rate  Automobile_Sales
count   528.000000  528.000000  ...         528.000000        528.000000
mean   2001.500000    0.214015  ...           2.453977       2352.718068
std      12.710467    0.410526  ...           1.119019       1645.321284
min    1980.000000    0.000000  ...           1.000000        102.000000
25%    1990.750000    0.000000  ...           1.600000        793.950000
50%    2001.500000    0.000000  ...           2.300000       2182.600000
75%    2012.250000    0.000000  ...           2.900000       3614.800000
max    2023.000000    1.000000  ...           6.000000      21147.000000

[8 rows x 11 columns]
df.columns
Index(['Date', 'Year', 'Month', 'Recession', 'Consumer_Confidence',
       'Seasonality_Weight', 'Price', 'Advertising_Expenditure', 'Competition',
       'GDP', 'Growth_Rate', 'unemployment_rate', 'Automobile_Sales',
       'Vehicle_Type', 'City'],
      dtype='object')
#create data for plotting

df_line = df.groupby(df['Year'])['Automobile_Sales'].mean()
#create figure

plt.figure(figsize=(10, 6))
Traceback (most recent call last):
  File "<pyshell#7>", line 3, in <module>
    plt.figure(figsize=(10, 6))
NameError: name 'plt' is not defined
plt.figure(figsize=(10, 6))

df_line.plot(kind = 'line')

plt.xlabel('Year')

plt.ylabel('Sales Volume') 

plt.title('Automobile Sales over Time')

plt.show()
SyntaxError: multiple statements found while compiling a single statement
df_line.plot(kind = 'line')
<Axes: xlabel='Year'>
cancel
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    cancel
NameError: name 'cancel' is not defined
plt.figure(figsize=(10, 6))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    plt.figure(figsize=(10, 6))
NameError: name 'plt' is not defined
plt.xlabel('Year')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    plt.xlabel('Year')
NameError: name 'plt' is not defined

============================ RESTART: Shell ============================
import pandas as pd
csv_file = '/Users/lirui/Desktop/historical_automobile_sales.csv'
df = pd.read_csv(csv_file)
print('CSV file read into dataframe!')
CSV file read into dataframe!
df.describe()
              Year   Recession  ...  unemployment_rate  Automobile_Sales
count   528.000000  528.000000  ...         528.000000        528.000000
mean   2001.500000    0.214015  ...           2.453977       2352.718068
std      12.710467    0.410526  ...           1.119019       1645.321284
min    1980.000000    0.000000  ...           1.000000        102.000000
25%    1990.750000    0.000000  ...           1.600000        793.950000
50%    2001.500000    0.000000  ...           2.300000       2182.600000
75%    2012.250000    0.000000  ...           2.900000       3614.800000
max    2023.000000    1.000000  ...           6.000000      21147.000000

[8 rows x 11 columns]
df.columns
Index(['Date', 'Year', 'Month', 'Recession', 'Consumer_Confidence',
       'Seasonality_Weight', 'Price', 'Advertising_Expenditure', 'Competition',
       'GDP', 'Growth_Rate', 'unemployment_rate', 'Automobile_Sales',
       'Vehicle_Type', 'City'],
      dtype='object')
import matplotlib.pyplot as plt
# Read in CSV file 
df = pd.read_csv('/Users/lirui/Desktop/historical_automobile_sales.csv')
# Group by year and calculate average sales
df_line = df.groupby('Year')['Automobile_Sales'].mean().reset_index()
# Create line chart 
plt.figure(figsize=(10, 6))
plt.plot(df_line['Year'], df_line['Automobile_Sales'], marker='o')
SyntaxError: multiple statements found while compiling a single statement
plt.figure(figsize=(10, 6))
<Figure size 2000x1200 with 0 Axes>
plt.plot(df_line['Year'], df_line['Automobile_Sales'], marker='o')
[<matplotlib.lines.Line2D object at 0x140089850>]
plt.xlabel('Year')
Text(0.5, 0, 'Year')
plt.ylabel('Average Sales')
Text(0, 0.5, 'Average Sales')
plt.title('Automobile Sales per Year')
Text(0.5, 1.0, 'Automobile Sales per Year')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
# Read CSV and create df_line as before
# Plot
plt.figure(figsize=(10, 6))
<Figure size 2000x1200 with 0 Axes>
plt.plot(df_line['Year'], df_line['Automobile_Sales'], marker='o')

[<matplotlib.lines.Line2D object at 0x147226290>]
# Set x-axis ticks
years = range(1980, 2024)
plt.xticks(years, rotation=90)
([<matplotlib.axis.XTick object at 0x1471f85d0>, <matplotlib.axis.XTick object at 0x1471f8990>, <matplotlib.axis.XTick object at 0x1427b1cd0>, <matplotlib.axis.XTick object at 0x146b828d0>, <matplotlib.axis.XTick object at 0x146a7d190>, <matplotlib.axis.XTick object at 0x147182450>, <matplotlib.axis.XTick object at 0x142764cd0>, <matplotlib.axis.XTick object at 0x1471f8090>, <matplotlib.axis.XTick object at 0x1471f12d0>, <matplotlib.axis.XTick object at 0x147215110>, <matplotlib.axis.XTick object at 0x14401fc90>, <matplotlib.axis.XTick object at 0x14718c350>, <matplotlib.axis.XTick object at 0x14718e510>, <matplotlib.axis.XTick object at 0x147218750>, <matplotlib.axis.XTick object at 0x14721ab50>, <matplotlib.axis.XTick object at 0x144028c90>, <matplotlib.axis.XTick object at 0x144028490>, <matplotlib.axis.XTick object at 0x14402b550>, <matplotlib.axis.XTick object at 0x144031710>, <matplotlib.axis.XTick object at 0x1440338d0>, <matplotlib.axis.XTick object at 0x144035d10>, <matplotlib.axis.XTick object at 0x1440351d0>, <matplotlib.axis.XTick object at 0x14403c5d0>, <matplotlib.axis.XTick object at 0x14403e690>, <matplotlib.axis.XTick object at 0x144048790>, <matplotlib.axis.XTick object at 0x14404aa10>, <matplotlib.axis.XTick object at 0x144032650>, <matplotlib.axis.XTick object at 0x14404d550>, <matplotlib.axis.XTick object at 0x14404f5d0>, <matplotlib.axis.XTick object at 0x144051750>, <matplotlib.axis.XTick object at 0x1440538d0>, <matplotlib.axis.XTick object at 0x14404da90>, <matplotlib.axis.XTick object at 0x14405e490>, <matplotlib.axis.XTick object at 0x1440644d0>, <matplotlib.axis.XTick object at 0x144066550>, <matplotlib.axis.XTick object at 0x14405e390>, <matplotlib.axis.XTick object at 0x144066750>, <matplotlib.axis.XTick object at 0x144067dd0>, <matplotlib.axis.XTick object at 0x14406ea90>, <matplotlib.axis.XTick object at 0x144076c90>, <matplotlib.axis.XTick object at 0x144075f10>, <matplotlib.axis.XTick object at 0x144075410>, <matplotlib.axis.XTick object at 0x144077bd0>, <matplotlib.axis.XTick object at 0x14406e3d0>], [Text(1980, 0, '1980'), Text(1981, 0, '1981'), Text(1982, 0, '1982'), Text(1983, 0, '1983'), Text(1984, 0, '1984'), Text(1985, 0, '1985'), Text(1986, 0, '1986'), Text(1987, 0, '1987'), Text(1988, 0, '1988'), Text(1989, 0, '1989'), Text(1990, 0, '1990'), Text(1991, 0, '1991'), Text(1992, 0, '1992'), Text(1993, 0, '1993'), Text(1994, 0, '1994'), Text(1995, 0, '1995'), Text(1996, 0, '1996'), Text(1997, 0, '1997'), Text(1998, 0, '1998'), Text(1999, 0, '1999'), Text(2000, 0, '2000'), Text(2001, 0, '2001'), Text(2002, 0, '2002'), Text(2003, 0, '2003'), Text(2004, 0, '2004'), Text(2005, 0, '2005'), Text(2006, 0, '2006'), Text(2007, 0, '2007'), Text(2008, 0, '2008'), Text(2009, 0, '2009'), Text(2010, 0, '2010'), Text(2011, 0, '2011'), Text(2012, 0, '2012'), Text(2013, 0, '2013'), Text(2014, 0, '2014'), Text(2015, 0, '2015'), Text(2016, 0, '2016'), Text(2017, 0, '2017'), Text(2018, 0, '2018'), Text(2019, 0, '2019'), Text(2020, 0, '2020'), Text(2021, 0, '2021'), Text(2022, 0, '2022'), Text(2023, 0, '2023')])
# Annotations
plt.annotate('Recession', xy=(1981, 8.5), xytext=(1983, 8.7), arrowprops=dict(facecolor='black'))
Text(1983, 8.7, 'Recession')
plt.annotate('Recession', xy=(2008, 9.5), xytext=(2010, 9.7), arrowprops=dict(facecolor='black'))
Text(2010, 9.7, 'Recession')
# Labels and title
plt.xlabel('Year')
Text(0.5, 0, 'Year')
plt.ylabel('Average Sales')
Text(0, 0.5, 'Average Sales')
plt.title('Automobile Sales During Recession')
Text(0.5, 1.0, 'Automobile Sales During Recession')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
# Read CSV
df = pd.read_csv('auto_sales.csv')
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    df = pd.read_csv('auto_sales.csv')
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 912, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 577, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 1407, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 1661, in _make_engine
    self.handles = get_handle(
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/io/common.py", line 859, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'auto_sales.csv'
df = pd.read_csv('/Users/lirui/Desktop/historical_automobile_sales.csv')
# Add recession indicator column
df['Recession'] = 0
df.loc[df['Year'].isin([1981, 1982, 2008, 2009]), 'Recession'] = 1
# Groupby year, vehicle type and get mean sales
df_grouped = df.groupby(['Year', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
df_grouped = df_grouped.set_index('Year')
# Set year as index
# Plot each vehicle type
fig, axs = plt.subplots(3, 1, figsize=(10, 10))
df_grouped.loc[df_grouped['Recession']==0, 'Compact'].plot(ax=axs[0], title='Compact')
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/indexes/base.py", line 3653, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 147, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 176, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7080, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7088, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Recession'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    df_grouped.loc[df_grouped['Recession']==0, 'Compact'].plot(ax=axs[0], title='Compact')
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/frame.py", line 3761, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/indexes/base.py", line 3655, in get_loc
    raise KeyError(key) from err
KeyError: 'Recession'
import pandas as pd
import matplotlib.pyplot as plt
df_Mline = df.groupby(['Year','Vehicle_Type'], as_index=False)['Automobile_Sales'].sum()
df_Mline.set_index('Year', inplace=True)
df_Mline = df_Mline.groupby(['Vehicle_Type'])['Automobile_Sales']
df_Mline.plot(kind='line')
Vehicle_Type
Executivecar       Axes(0.125,0.11;0.775x0.226471)
Mediumfamilycar    Axes(0.125,0.11;0.775x0.226471)
Smallfamiliycar    Axes(0.125,0.11;0.775x0.226471)
Sports             Axes(0.125,0.11;0.775x0.226471)
Supperminicar      Axes(0.125,0.11;0.775x0.226471)
Name: Automobile_Sales, dtype: object
plt.xlabel('Year')
Text(0.5, 161.4444444444444, 'Year')
plt.ylabel('Total Sales Volume')
Text(175.06944444444443, 0.5, 'Total Sales Volume')
plt.title('Sales Trend Vehicle-wise during Recession')
Text(0.5, 1.0, 'Sales Trend Vehicle-wise during Recession')
plt.legend()
<matplotlib.legend.Legend object at 0x145f41a10>
plt.show()
plt.show()
import seaborn as sns
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    import seaborn as sns
ModuleNotFoundError: No module named 'seaborn'
import seaborn as sns
import matplotlib.pyplot as plt
new_df = df.groupby('Recession')['Automobile_Sales'].mean().reset_index()
# Create bar chart 
plt.figure(figsize=(8, 6))
<Figure size 1600x1200 with 0 Axes>
sns.barplot(x='Recession', y='Automobile_Sales', hue='Recession', data=new_df)
<Axes: xlabel='Recession', ylabel='Automobile_Sales'>
plt.xlabel('Recession Period')
Text(0.5, 0, 'Recession Period')
plt.ylabel('Average Sales')
Text(0, 0.5, 'Average Sales')
plt.title('Average Automobile Sales during Recession and Non-Recession')
Text(0.5, 1.0, 'Average Automobile Sales during Recession and Non-Recession')
plt.xticks(ticks=[0, 1], labels=['Non-Recession', 'Recession'])
([<matplotlib.axis.XTick object at 0x1427562d0>, <matplotlib.axis.XTick object at 0x147428510>], [Text(0, 0, 'Non-Recession'), Text(1, 0, 'Recession')])

plt.show()
df['Recession'] = 0
df.loc[df['Year'].isin([1981, 1982, 2008, 2009]), 'Recession'] = 1

# Groupby recession, vehicle type and get mean sales
dd = df.groupby(['Recession','Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
# Create bar chart
plt.figure(figsize=(10, 6))
<Figure size 2000x1200 with 0 Axes>
sns.barplot(x='Recession', y='Automobile_Sales', hue='Vehicle_Type', data=dd)
<Axes: xlabel='Recession', ylabel='Automobile_Sales'>
plt.xticks(ticks=[0, 1], labels=['Non-Recession', 'Recession'])
([<matplotlib.axis.XTick object at 0x1427a9010>, <matplotlib.axis.XTick object at 0x147178510>], [Text(0, 0, 'Non-Recession'), Text(1, 0, 'Recession')])
plt.xlabel('Period')
Text(0.5, 0, 'Period')
plt.ylabel('Average Sales')
Text(0, 0.5, 'Average Sales')
plt.title('Vehicle-Wise Sales during Recession and Non-Recession Period')
Text(0.5, 1.0, 'Vehicle-Wise Sales during Recession and Non-Recession Period')
plt.show()
# Create dataframes 
rec_data = df[df['Recession'] == 1]
non_rec_data = df[df['Recession'] == 0]
# Create figure
fig = plt.figure(figsize=(12, 6))
# Add subplots
ax0 = fig.add_subplot(1, 2, 1)
ax1 = fig.add_subplot(1, 2, 2)
# Plot recession data
sns.lineplot(x='Year', y='GDP', data=rec_data, ax=ax0, label='Recession')
<Axes: xlabel='Year', ylabel='GDP'>
ax0.set_xlabel('Year')
Text(0.5, 0, 'Year')
ax0.set_ylabel('GDP')
Text(0, 0.5, 'GDP')
ax0.set_title('GDP Variation during Recession Period')
Text(0.5, 1.0, 'GDP Variation during Recession Period')
# Plot non-recession data
sns.lineplot(x='Year', y='GDP', data=non_rec_data, ax=ax1, label='Non-Recession')
<Axes: xlabel='Year', ylabel='GDP'>
ax1.set_xlabel('Year')
Text(0.5, 0, 'Year')
ax1.set_ylabel('GDP')
Text(0, 0.5, 'GDP')
ax1.set_title('GDP Variation during Non-Recession Period')
Text(0.5, 1.0, 'GDP Variation during Non-Recession Period')
plt.tight_layout()
plt.show()
# Filter non-recession data
non_rec_data = df[df['Recession'] == 0]
# Size based on seasonality weight 
size = non_rec_data['Seasonality_Weight']
# Create bubble plot
sns.scatterplot(data=non_rec_data, x='Month', y='Automobile_Sales', size=size)
<Axes: xlabel='Month', ylabel='Automobile_Sales'>
plt.xlabel('Month')
Text(0.5, 47.04444444444444, 'Month')
plt.ylabel('Automobile Sales')
Text(40.81944444444443, 0.5, 'Automobile Sales')
plt.title('Seasonality impact on Automobile Sales')
Text(0.5, 1.0, 'Seasonality impact on Automobile Sales')
plt.show()
# Filter recession data
rec_data = df[df['Recession'] == 1]
# Create scatter plot 
plt.scatter(rec_data['Consumer_Confidence'], rec_data['Automobile_Sales'])
<matplotlib.collections.PathCollection object at 0x146c57bd0>
plt.xlabel('Consumer Confidence')
Text(0.5, 47.04444444444444, 'Consumer Confidence')
plt.ylabel('Automobile Sales')
Text(58.44444444444443, 0.5, 'Automobile Sales')
plt.title('Consumer Confidence and Automobile Sales during Recessions')
Text(0.5, 1.0, 'Consumer Confidence and Automobile Sales during Recessions')
plt.show()
# Create scatter plot
plt.scatter(rec_data['Average_Vehicle_Price'], rec_data['Automobile_Sales'])

Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/indexes/base.py", line 3653, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 147, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 176, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7080, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7088, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Average_Vehicle_Price'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#125>", line 2, in <module>
    plt.scatter(rec_data['Average_Vehicle_Price'], rec_data['Automobile_Sales'])
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/frame.py", line 3761, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/indexes/base.py", line 3655, in get_loc
    raise KeyError(key) from err
KeyError: 'Average_Vehicle_Price'
# Filter recession data 
rec_data = df[df['Recession'] == 1]
# Create scatter plot
plt.scatter(rec_data['Average_Vehicle_Price'], rec_data['Automobile_Sales'])
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/indexes/base.py", line 3653, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 147, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 176, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7080, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7088, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Average_Vehicle_Price'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#127>", line 2, in <module>
    plt.scatter(rec_data['Average_Vehicle_Price'], rec_data['Automobile_Sales'])
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/frame.py", line 3761, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/indexes/base.py", line 3655, in get_loc
    raise KeyError(key) from err
KeyError: 'Average_Vehicle_Price'
# Create scatter plot
plt.scatter(rec_data['Price'], rec_data['Automobile_Sales'])
<matplotlib.collections.PathCollection object at 0x1478b1110>
plt.xlabel('Price')
Text(0.5, 47.04444444444444, 'Price')
plt.ylabel('Automobile Sales')
Text(58.44444444444443, 0.5, 'Automobile Sales')
plt.title('Relationship between Price and Sales during Recessions')
Text(0.5, 1.0, 'Relationship between Price and Sales during Recessions')
plt.show()
# Filter data
Rdata = df[df['Recession'] == 1]
NRdata = df[df['Recession'] == 0]
# Get totals 
RAtotal = Rdata['Advertising_Expenditure'].sum()
NRAtotal = NRdata['Advertising_Expenditure'].sum()
# Create pie chart
plt.figure(figsize=(8, 6))
<Figure size 1600x1200 with 0 Axes>
labels = ['Recession', 'Non-Recession']
sizes = [RAtotal, NRAtotal]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
([<matplotlib.patches.Wedge object at 0x1476835d0>, <matplotlib.patches.Wedge object at 0x147680810>], [Text(-0.30576407671806893, 1.0566495773854012, 'Recession'), Text(0.30576407671806904, -1.0566495773854012, 'Non-Recession')], [Text(-0.16678040548258302, 0.5763543149374915, '9.0%'), Text(0.16678040548258308, -0.5763543149374915, '91.0%')])
plt.title('Advertising Expenditure during Recession and Non-Recession')
Text(0.5, 1.0, 'Advertising Expenditure during Recession and Non-Recession')
plt.show()
# Get expenditure by vehicle type
expenditure = Rdata.groupby('Vehicle_Type')['Advertising_Expenditure'].sum()
# Create pie chart 
... plt.figure(figsize=(8, 6))
... 
<Figure size 1600x1200 with 0 Axes>
>>> labels = expenditure.index
>>> sizes = expenditure.values
>>> plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
([<matplotlib.patches.Wedge object at 0x147f08250>, <matplotlib.patches.Wedge object at 0x147f09450>, <matplotlib.patches.Wedge object at 0x147f0ab90>, <matplotlib.patches.Wedge object at 0x147f182d0>], [Text(-1.0424742849848116, 0.35106604100283706, 'Mediumfamilycar'), Text(0.48734263914007236, -0.9861527022099515, 'Smallfamiliycar'), Text(1.0853089640465263, 0.17917715412478274, 'Sports'), Text(0.639319079076174, 0.8951374839259012, 'Supperminicar')], [Text(-0.5686223372644427, 0.19149056781972928, '39.7%'), Text(0.2658232577127667, -0.5379014739327008, '35.3%'), Text(0.5919867076617416, 0.0977329931589724, '5.3%'), Text(0.3487194976779131, 0.48825680941412786, '19.7%')])
>>> plt.title('Share of Each Vehicle Type in Total Advertising Expenditure during Recessions')
Text(0.5, 1.0, 'Share of Each Vehicle Type in Total Advertising Expenditure during Recessions')
>>> plt.show()
>>> # Filter recession data
... data = df[df['Recession'] == 1]
>>> # Create countplot 
... plt.figure(figsize=(10, 6))
<Figure size 2000x1200 with 0 Axes>
>>> sns.countplot(data=data, x='unemployment_rate', hue='Vehicle_Type')
<Axes: xlabel='unemployment_rate', ylabel='count'>
>>> plt.xlabel('Unemployment Rate')
Text(0.5, 0, 'Unemployment Rate')
>>> plt.ylabel('Count')
Text(0, 0.5, 'Count')
>>> plt.title('Effect of Unemployment Rate on Vehicle Type and Sales')
Text(0.5, 1.0, 'Effect of Unemployment Rate on Vehicle Type and Sales')
>>> plt.legend(loc='upper right')
<matplotlib.legend.Legend object at 0x147cfd390>
>>> plt.show()
>>> # Create a map on the hightest sales region/offices of the company during recession period
>>> from pyodide.http import pyfetch
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    from pyodide.http import pyfetch
ModuleNotFoundError: No module named 'pyodide'
>>> from pyodide.http import pyfetch
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    from pyodide.http import pyfetch
ModuleNotFoundError: No module named 'pyodide'
>>> pip install pyodide
... 
SyntaxError: invalid syntax
