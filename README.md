# Final Project | Vegan Snack Recommender
<br>
## Python (Web Scraping, Clustering), Tableau

![photo](https://latestvegannews.com/wp-content/uploads/2019/07/91FFqqXvBhL._SL1500_.jpg)

---------------------------------------------------------------------------------------------------------

### Project goal

With my final project I want to showcase what I have learned during my Data Analytics.


**Objective:** <br>
The goal of this project is to be able to build a function which recommends you more similar vegan snacks according to your taste and current preferences. To do so I am using the clustering algorithm k-means. The clusters are later analyzed 

---------------------------------------------------------------------------------------------------------

### Structure of the repository
This repository contains x folders:<br>
> **Data:** <br>
>> 3 *CSV-files* with the data which was scraped from three websites <br>
>> 1 *CSV-file* with the cleaned data <br>
>> 1 *CSV-file* with the cleaned data <br>

> **Python:**  <br>
>> 3 Jupyter notebooks (*ipynb-file*) for web scraping with data cleaning, analysis, model building <br>
>> 1 Jupyter notebook (*ipynb-file*) with data cleaning, analysis, model building <br>
>> 1 Jupyter notebook (*ipynb-file*) for the model building <br>
>> 1 Jupyter notebook (*ipynb-file*) with the explanatory analysis and first visualizations <br>
>> Python functions (*py-file*) with all self-built functions used for this project <br>
>> 1 *pickle-file* saving information from scaling the data (StandardScaler) <br>

> **Tableau:** <br>
>> *README-file* with screenshots of the visualizations <br>
>> Tableau results (*twb-file*)

---------------------------------------------------------------------------------------------------------

### Project data

> 1232 rows and 14 columns

The data set provides information about:

|Columns | Info | Data type |
|:--- |:---|:---|
| Product name | unique product name | categorical |
| Brand | brand of the product | categorical | 
| Brand (new) | only brands with appear >10 times + 'Others' | categorical |
| Price | in EUR | numerical |
| Weight | in kg | numerical |
| kJ | kilojoule per 100 g | numerical |
| kcal | calories per 100 g | numerical |  
| Fat  | fats (in g / 100 g) | numerical |
| Sat Fat | saturated fats (in g / 100 g) | numerical |
| Carbs | carbohydrates (in g / 100 g) | numerical |
| Sugar | sugar (in g / 100 g) | numerical |
| Protein  |  protein (in g / 100 g) | numerical |
| Product link  | link to product website | categorical |
| Photo link  | link to product photo | categorical |



---------------------------------------------------------------------------------------------------------

### Project workflow

1. **Agile Project Management via Kanban Board**
    - Self-managing my project via Kanban Board (Github *Projects*)
    - Using Kanban Board to save ressources and references

2. **Web Scraping with BeautifulSoup**
    - Creating a database and table within SQL-Workbench
    - Writing the right queries to extract the information we need

3. **Preparing and exploring the data with Python**
    - Cleaning the scraped data and merging it into one dataframe
    - Exploring the data (statistically and visually)
    - Performing data cleaning and data wrangling in Python
  
4.  **Clustering the data with K means algorithm** 
    - Fitting the models
    - Iterating on the models to get more optimized results
  
5. **Presenting the results with Tableau** 
    - Producing documentation to make the project accessible
    - Building engaging presentations
    - Including storytelling to my presentation


---------------------------------------------------------------------------------------------------------


### Project outcome/results

**Business insights** 


! MORE TO COME !


**Clustering model results**




**Future score of work**

Possible future improvements of the model could include:
- increasing the size of the data set by webscraping even more websites
- including more features in the dataframe:
    - snack category (e.g. chocolate, chips, protein bars, etc.)
    - organic (yes/no)
    - allergenes
    - ingredients 
- text analysis of product description/ingredients

---------------------------------------------------------------------------------------------------------
### Modules used for Python analysis

[BeautifulSoup4](https://beautiful-soup-4.readthedocs.io/en/latest/)<br>
[matplotlib.pyplot](https://matplotlib.org/3.1.1/contents.html)<br>
[numpy](https://numpy.org/doc/)<br>
[pandas](https://pandas.pydata.org/)<br>
[pickle](https://docs.python.org/3/library/pickle.html)<br>
[seaborn](https://seaborn.pydata.org/)<br>
[scikitplot](https://pypi.org/project/scikit-plot/)<br>
[scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html)<br>
[sklearn](https://scikit-learn.org/stable/index.html)<br>
[statsmodels](https://www.statsmodels.org/stable/index.html)<br>



