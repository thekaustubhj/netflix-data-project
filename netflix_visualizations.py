#!/usr/bin/env python
# coding: utf-8

# # Introduction
# 
# In this project, you will act as a data visualization developer at Yahoo Finance! You will be helping the "Netflix Stock Profile" team visualize the Netflix stock data. In finance, a _stock profile_ is a series of studies, visualizations, and analyses that dive into different aspects a publicly traded company's data. 
# 
# For the purposes of the project, you will only visualize data for the year of 2017. Specifically, you will be in charge of creating the following visualizations:
# + The distribution of the stock prices for the past year
# + Netflix's earnings and revenue in the last four quarters
# + The actual vs. estimated earnings per share for the four quarters in 2017
# + A comparison of the Netflix Stock price vs the Dow Jones Industrial Average price in 2017 
# 
# Note: We are using the Dow Jones Industrial Average to compare the Netflix stock to the larter stock market. Learn more about why the Dow Jones Industrial Average is a general reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp).
# 
# During this project, you will analyze, prepare, and plot data. Your visualizations will help the financial analysts asses the risk of the Netflix stock.
# 
# After you complete your visualizations, you'll be creating a presentation to share the images with the rest of the Netflix Stock Profile team. Your slides should include:
# 
# - A title slide
# - A list of your visualizations and your role in their creation for the "Stock Profile" team
# - A visualization of the distribution of the stock prices for Netflix in 2017
# - A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary
# - A visualization and a brief summary of their earned versus actual earnings per share
# - A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017
# 
# Financial Data Source: [Yahoo Finance](https://finance.yahoo.com/quote/DATA/)
# 

# ## Step 1
# 
# Let's get our notebook ready for visualizing! Import the modules that you'll be using in this project:
# - `from matplotlib import pyplot as plt`
# - `import pandas as pd`
# - `import seaborn as sns`

# In[1]:


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


# ## Step 2

# Let's load the datasets and inspect them.

# Load **NFLX.csv** into a DataFrame called `netflix_stocks`. Then, quickly inspect the DataFrame using `print()`.
# 
# Hint: Use the `pd.read_csv()`function).
# 
# Note: In the Yahoo Data, `Adj Close` represents the adjusted close price adjusted for both dividends and splits. This means this is the true closing stock price for a given business day.

# In[2]:


netflix_stocks = pd.read_csv('NFLX.csv')
print(netflix_stocks.head())


# Load **DJI.csv** into a DataFrame called `dowjones_stocks`. Then, quickly inspect the DataFrame using `print()`.
# 
# Note: You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). 
# 

# In[3]:


dowjones_stocks = pd.read_csv('DJI.csv')
print(dowjones_stocks.head())


# Load **NFLX_daily_by_quarter.csv** into a DataFrame called `netflix_stocks_quarterly`. Then, quickly inspect the DataFrame using `print()`.
# 

# In[4]:


netflix_stocks_quarterly = pd.read_csv('NFLX_daily_by_quarter.csv')
print(netflix_stocks_quarterly.head())


# ## Step 3

# Let's learn more about our data. The datasets are large and it may be easier to view the entire dataset locally on your computer. Open the CSV files directly from the folder you downloaded for this project.
#  - `NFLX` is the stock ticker symbol for Netflix and `^DJI` is the stock ticker symbol for the Dow Jones industrial Average, which is why the CSV files are named accordingly
#  - In the Yahoo Data, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.
#  - You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). 
#  
# Answer the following questions by inspecting the data in the **NFLX.csv**,**DJI.csv**, and **NFLX_daily_by_quarter.csv** in your computer.

# What year is represented in the data? Look out for the latest and earliest date.

# In[5]:


# 2017


# + Is the data represented by days, weeks, or months? 
# + In which ways are the files different? 
# + What's different about the columns for `netflix_stocks` versus `netflix_stocks_quarterly`?

# In[6]:


# The DJI and NFLX files have data represented for every month, while for the NFLX_daily_by_quarter.csv are daily. 
# The netflix_stocks_quarterly has an additional column to denote whether the row belongs to Q1, Q2, Q3 r Q4 of 2017 


# ## Step 4
# 
# Great! Now that we have spent sometime looking at the data, let's look at the column names of the DataFrame `netflix_stocks` using `.head()`. 

# In[7]:


print(netflix_stocks.head())


# What do you notice? The first two column names are one word each, and the only one that is not is `Adj Close`! 
# 
# The term `Adj Close` is a confusing term if you don't read the Yahoo Documentation. In Yahoo, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.
# 
# This means this is the column with the true closing price, so these data are very important.
# 
# Use Pandas to change the name of of the column to `Adj Close` to `Price` so that it is easier to work with the data. Remember to use `inplace=True`.
# 
# Do this for the Dow Jones and Netflix Quarterly pandas dataframes as well.
# Hint: Use [`.rename()`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html)).
# 

# In[8]:


netflix_stocks.rename(columns = {
    'Adj Close' : 'Price'
}, inplace = True)

dowjones_stocks.rename(columns = {
    'Adj Close' : 'Price'
}, inplace = True)

netflix_stocks_quarterly.rename(columns = {
    'Adj Close' : 'Price'
}, inplace = True)


# Run `netflix_stocks.head()` again to check your column name has changed.

# In[9]:


print(netflix_stocks.head())


# Call `.head()` on the DataFrame `dowjones_stocks` and `netflix_stocks_quarterly`.

# In[10]:


print(dowjones_stocks.head())
print(netflix_stocks_quarterly.head())


# In[11]:


## Step 5
#In this step, we will be visualizing the Netflix quarterly data! 

#We want to get an understanding of the distribution of the Netflix quarterly stock prices for 2017. Specifically, we want to see in which quarter stock prices flucutated the most. We can accomplish this using a violin plot with four violins, one for each business quarter!


#1. Start by creating a variable `ax` and setting it equal to `sns.violinplot()`. This will instantiate a figure and give us access to the axes through the variable name `ax`.
#2. Use `sns.violinplot()` and pass in the following arguments:
#+ The `Quarter` column as the `x` values
#+ The `Price` column as your `y` values
#+ The `netflix_stocks_quarterly` dataframe as your `data`
#3. Improve the readability of the chart by adding a title of the plot. Add `"Distribution of 2017 Netflix Stock Prices by Quarter"` by using `ax.set_title()`
#4. Change your `ylabel` to "Closing Stock Price"
#5. Change your `xlabel` to "Business Quarters in 2017"
#6. Be sure to show your plot!


# In[12]:


sns.set_palette('Pastel1')
fig1 = plt.figure(figsize = (10,7))
fig1ax = plt.subplot(1,1,1)
sns.violinplot(data = netflix_stocks_quarterly, x = 'Quarter', y = 'Price')
fig1ax.set_xticklabels(['Quarter1', 'Quarter2', 'Quarter3', 'Quarter4'])
fig1.savefig('Violinplot_new.png')


# ## Graph Literacy
# - What are your first impressions looking at the visualized data?
# 
# - In what range(s) did most of the prices fall throughout the year?
# 
# - What were the highest and lowest prices? 

# In[13]:


# First impressions : While Q3 showed quite a bit of volatility with  large distribution of prices, the stock price showed an overall upwards movement across all quarters
# the Price range fell between $140 to $200 through the year
# The lowest price was in Q1 and the highest price was in Q4


#  

# ## Step 6
# 
# Next, we will chart the performance of the earnings per share (EPS) by graphing the estimate Yahoo projected for the Quarter compared to the actual earnings for that quarters. We will accomplish this using a scatter chart. 
# 
# 1. Plot the actual EPS by using `x_positions` and `earnings_actual` with the `plt.scatter()` function. Assign `red` as the color.
# 2. Plot the actual EPS by using `x_positions` and `earnings_estimate` with the `plt.scatter()` function. Assign `blue` as the color
# 
# 3. Often, estimates and actual EPS are the same. To account for this, be sure to set your transparency  `alpha=0.5` to allow for visibility pf overlapping datapoint.
# 4. Add a legend by using `plt.legend()` and passing in a list with two strings `["Actual", "Estimate"]`
# 
# 5. Change the `x_ticks` label to reflect each quarter by using `plt.xticks(x_positions, chart_labels)`
# 6. Assing "`"Earnings Per Share in Cents"` as the title of your plot.
# 

# In[14]:


x_positions = [1, 2, 3, 4]
chart_labels = ["1Q2017","2Q2017","3Q2017","4Q2017"]
earnings_actual =[.4, .15,.29,.41]
earnings_estimate = [.37,.15,.32,.41 ]
plt.close('all')

fig2 = plt.figure(figsize = (10,7))
fig2ax = plt.subplot(1,1,1)
plt.scatter(x_positions, earnings_actual, color = 'red', alpha = 0.5)
plt.scatter(x_positions, earnings_estimate, color = 'blue', alpha = 0.5)
plt.legend(['Actual', 'Estimate'])
fig2ax.set_xticks(x_positions)
fig2ax.set_xticklabels(chart_labels)
plt.show()
fig2.savefig('ForecastActuals.png')


# ## Graph Literacy
# 
# + What do the purple dots tell us about the actual and estimate earnings per share in this graph? Hint: In color theory red and blue mix to make purple.
# 

# In[15]:


# the Purple dots tell us that yahoo's forecast EPS exactly matched the actual EPS.


#  

# ## Step 7

# Next, we will visualize the earnings and revenue reported by Netflix by mapping two bars side-by-side. We have visualized a similar chart in the second Matplotlib lesson [Exercise 4](https://www.codecademy.com/courses/learn-matplotlib/lessons/matplotlib-ii/exercises/side-by-side-bars).
# 
# As you may recall, plotting side-by-side bars in Matplotlib requires computing the width of each bar before hand. We have pasted the starter code for that exercise below. 
# 
# 1. Fill in the `n`, `t`, `d`, `w` values for the revenue bars
# 2. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `revenue_by_quarter` data
# 3. Fill in the `n`, `t`, `d`, `w` values for the earnings bars
# 4. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `earnings_by_quarter` data
# 5. Create a legend for your bar chart with the `labels` provided
# 6. Add a descriptive title for your chart with `plt.title()`
# 7. Add labels to each quarter by assigning the position of the ticks through the code provided. Hint:  `plt.xticks(middle_x, quarter_labels)`
# 8. Be sure to show your plot!
# 

# In[16]:


# The metrics below are in billions of dollars
revenue_by_quarter = [2.79, 2.98,3.29,3.7]
earnings_by_quarter = [.0656,.12959,.18552,.29012]
quarter_labels = ["2Q2017","3Q2017","4Q2017", "1Q2018"]

# Revenue
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.8 # Width of each bar

bars1_x = [t*element + w*n for element
             in range(d)]

# Earnings
n = 2  # This is our second dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.8 # Width of each bar
bars2_x = [t*element + w*n for element
             in range(d)]

middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]
labels = ["Revenue", "Earnings"]

fig3 = plt.figure(figsize = (10,7))
fig3ax = plt.subplot(1,1,1)
plt.bar(bars1_x, revenue_by_quarter)
plt.bar(bars2_x, earnings_by_quarter)
plt.legend(labels)
plt.title('Revenue and Earnings by Quarter')
fig3ax.set_xticks(middle_x)
fig3ax.set_xticklabels(quarter_labels)
plt.show()
fig3.savefig('RevenueEarningsbyQuarter.png')


# ## Graph Literacy
# What are your first impressions looking at the visualized data?
# 
# - Does Revenue follow a trend?
# - Do Earnings follow a trend?
# - Roughly, what percentage of the revenue constitutes earnings?

# In[17]:


#Yes, both Revenues and Earnings have been increasing Q on Q however, growth in Earnings
# Earnings as a percentage of revenues can be calculated as a separate list using list comprehension below
margin = [earnings_by_quarter[i]/revenue_by_quarter[i] for i in range(len(earnings_by_quarter))]
print(margin)

# Answer is [0.023512544802867383, 0.04348657718120806, 0.05638905775075988, 0.0784108108108108] which shows that margins have grown from 2.3% to 7.8%
#Plotting the same as a simple to view graph
fig4 = plt.figure(figsize = (10,7))
fig4ax = plt.subplot(1,1,1)
plt.bar(range(len(margin)), margin, color = 'green', alpha = 0.5)
plt.title('Operating Margins by Quarter')
plt.xlabel('Quarter')
plt.ylabel('Margin')
fig4ax.set_xticks(range(len(margin)))
fig4ax.set_xticklabels(quarter_labels)
plt.show()
fig4.savefig('MarginbyQuarter.png')


# ## Step 8
# 
# In this last step, we will compare Netflix stock to the Dow Jones Industrial Average in 2017. We will accomplish this by plotting two line charts side by side in one figure. 
# 
# Since `Price` which is the most relevant data is in the Y axis, let's map our subplots to align vertically side by side.
# - We have set up the code for you on line 1 in the cell below. Complete the figure by passing the following arguments to `plt.subplots()` for the first plot, and tweaking the third argument for the second plot
#     - `1`-- the number of rows for the subplots
#     - `2` -- the number of columns for the subplots
#     - `1` -- the subplot you are modifying
# 
# - Chart the Netflix Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`netflix_stocks['Date'], netflix_stocks['Price']`)
# - Assign "Netflix" as a title to this subplot. Hint: `ax1.set_title()`
# - For each subplot, `set_xlabel` to `"Date"` and `set_ylabel` to `"Stock Price"`
# - Chart the Dow Jones Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`dowjones_stocks['Date'], dowjones_stocks['Price']`)
# - Assign "Dow Jones" as a title to this subplot. Hint: `plt.set_title()`
# - There is some crowding in the Y axis labels, add some space by calling `plt.subplots_adjust(wspace=.5)`
# - Be sure to `.show()` your plots.
# 

# In[18]:


# Left plot Netflix

fig5 = plt.figure(figsize = (15,7))

fig5ax1 = plt.subplot(1, 2, 1)
plt.plot(netflix_stocks['Date'], netflix_stocks['Price'], color = 'blue', marker = '*', alpha = 0.5)
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title ('Netflix')
fig5ax1.set_xticks(range(netflix_stocks['Date'].count()))
fig5ax1.set_xticklabels(netflix_stocks['Date'].values, rotation = 90)

# Right plot Dow Jones
fig5ax2 = plt.subplot(1, 2, 2)
plt.plot(dowjones_stocks['Date'], dowjones_stocks['Price'], color = 'green', marker = 'o', alpha = 0.5)
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title ('Dow Jones')
fig5ax2.set_xticks(range(dowjones_stocks['Date'].count()))
fig5ax2.set_xticklabels(dowjones_stocks['Date'].values, rotation = 90)

plt.subplots_adjust(wspace=.4)
plt.show()
fig5.savefig('NetflixvsDowJonespricevolatility.png')


# - How did Netflix perform relative to Dow Jones Industrial Average in 2017?
# - Which was more volatile?
# - How do the prices of the stocks compare?

# In[19]:


#Netflix grew steeply as compared to Dow Jones, albeit much more volatility on stock price between the May - Jun - Jul period.

# Growth % for Netflix and DJI years can be found out as 

def growth_finder(start, end) : 
    growth = (end-start)*1.0/start
    return growth

netflix_prices = netflix_stocks['Price'].values
netflix_start = netflix_prices[0]
netflix_end = netflix_prices[-1]

print('Netflix growth in 2017 was : ' + str(growth_finder(netflix_start, netflix_end)))

dowjones_prices = dowjones_stocks['Price'].values
dowjones_start = dowjones_prices[0]
dowjones_end = dowjones_prices[-1]

print('DJI growth in 2017 was : ' + str(growth_finder(dowjones_start, dowjones_end)))

growth_comparison = [growth_finder(netflix_start, netflix_end), growth_finder(dowjones_start, dowjones_end)]

fig6 = plt.figure(figsize = (10,7))
fig6ax = plt.subplot(1,1,1)
plt.bar(range(len(growth_comparison)), growth_comparison, color = 'green', alpha = 0.4)
plt.title('Growth Comparisons')
plt.xlabel('Stock')
plt.ylabel('2017 Growth')
fig6ax.set_xticks(range(len(growth_comparison)))
fig6ax.set_xticklabels(['Netflix', 'DJIA'])
plt.show()
fig6.savefig('2017Grwothcomparison.png')


#  

# # Step 9
# 
# It's time to make your presentation! Save each of your visualizations as a png file with `plt.savefig("filename.png")`.
# 
# As you prepare your slides, think about the answers to the graph literacy questions. Embed your observations in the narrative of your slideshow!
# 
# Remember that your slideshow must include:
# - A title slide
# - A list of your visualizations and your role in their creation for the "Stock Profile" team
# - A visualization of the distribution of the stock prices for Netflix in 2017
# - A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary
# - A visualization and a brief summary of their earned versus actual earnings per share
# - A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017
# 

# In[20]:


#Okay


# In[21]:


## Just playing around with different ways of defining subplots

## METHOD 1 : Define figure without specifying how many subplots, Define axis for first subplot, plot it and then move on to the next subplot... 

fig1 = plt.figure() # create the canvas for plotting
ax1 = plt.subplot(2,1,1) 
plt.plot([1,2,3,4],[5,6,7,8])
ax2 = plt.subplot(2,1,2)
plt.plot([3,4,5,6],[5,6,7,8])
fig1.suptitle('Figure1') #Stands for Super Title if the Title needs to be given to the whole figure.
ax1.set_title('AX1')
ax2.set_title('AX2')
plt.subplots_adjust(wspace = 0.5, hspace = 0.5)
fig1.savefig('fig1test.png')

## METHOD 1 : Define figure without specifying how many subplots, Define ALL axes for required subplots, and then plot them sequentially 

fig2 = plt.figure() # create the canvas for plotting
al1 = plt.subplot(2,1,1)
al2 = plt.subplot(2,1,2)
al1.plot([1,2,3,4],[5,6,7,8]) # Note how we are using al1. instead of plt. since we will need to specify which one this is for.
al2.plot([3,4,5,6],[5,6,7,8]) 
fig2.suptitle('Figure2')
al1.set_title('AL1')
al2.set_title('AL2')
plt.subplots_adjust(wspace = 0.5, hspace = 0.5)
fig2.savefig('fig2test.png')

## METHOD 3 : Define figure and all axis together using .subplots

fig3, [[am1,am2],[am3,am4]] = plt.subplots(2,2)
# Notice how the axes have been specified in groups of rows.
am1.plot([1,2,3,4],[5,6,7,8])
am2.plot([1,2,3,4],[9,8,7,6])
am3.plot([1,2,3,4],[9,5,8,7])
am4.plot([1,2,3,4],[1,4,2,5])
fig3.suptitle('Figure1') 
am1.set_title('AM1')
am2.set_title('AM2') 
am3.set_title('AM3') 
am4.set_title('AM4') 
plt.subplots_adjust(wspace = 0.5, hspace = 0.5)
fig3.savefig('fig3test.png')


# In[ ]:




