# Project

## **by Michael Curley**

![Wind](./images/windpark.png)


<div>
<a target="_blank" href="https://docs.python.org/3/tutorial/index.html">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python"/> </a>
<a target="_blank" href="https://www.anaconda.com/">
  <img src="https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white" alt="Anaconda"/>
</a>
<a target="_blank" href="https://numpy.org/devdocs/index.html">
  <img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"/>
</a>
<a target="_blank" href="https://pypi.org/project/pandas/">
  <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
</a>
<a target="_blank" href="https://matplotlib.org/">
  <img src="https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black" 
alt="Matplotlib"/>
</a>
<a target="_blank" href="https://docs.github.com/en/get-started/writing-on-github/
getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax">
  <img src="https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white" alt="Markdown"/>
</a>
<a target="_blank" href="https://www.latex-project.org/">
  <img src="https://img.shields.io/badge/latex-%23008080.svg?style=for-the-badge&logo=latex&logoColor=white" alt="LaTeX"/>
</a>
<a target="_blank" href="https://code.visualstudio.com/">
  <img src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white" alt="Visual Studio Code"/>
</a>
<a target="_blank" href="https://jupyter.org/">
  <img src="https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter 
Notebook"/>
</a>
</div>

-----

_This README has being written with [GitHub's Documentation on README's](https://docs.github.com/en/repositories/
managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) in mind. You should refer to that 
documentation for more information on writing an appropriate README for visitors to your 
repository._

_You can find out more about writing in MarkDown in [GitHub Documentation](https://docs.github.com/en/get-started/writing-on-github/
getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)_

---


## Table of Contents.

* [About this project](#10-about-this-project)
* [Use of this project](#20-use-of-this-project)
  * [2.1 Repository Contents](#21-repository-contents)
* [Get Started](#30-get-started)
* [Get Help](#40-get-help)
  * [4.1 Issue Tracker](#41-issue-tracker)
  * [4.2 Contact Us ](#42-contact-us)
* [Contribute](#50-contribute)
  * [Feature Requests](#51-feature-requests)
  * [Code Contributions](#52-code-contributions)
* [Author](#60-author)
* [References](#70-references)
  * [Websites References](#71-websites)
  * [Book References](#72-books)


## 1.0 About this project

This folder contains the project for the Programming for Data Analytics module, as part of the Higher Diploma in Data Analytics, at the Atlantic Technological University (ATU) Galway for the Year 2024/2025. 

## 2.0 Use of this Project

This project is been used to demonstate learning from the above Module by analysing a dataset/datasets. The project.ipynb notebook contained within this repository examines the suitability of a selection of locations in Ireland for power generation using wind as the source of energy. We will be analysing historical weather data to do this.

The weather data that we are analysing was downloaded from the [Met Éireann Historical Data website](https://www.met.ie/climate/available-data/historical-data). According to this source there are 25 synoptic weather stations recording a range of parameters including wind speed and direction. The notebook will examine this in more details.

### 2.1 Repository Contents:

```sh
/PFDA
├── /PFDA_assignments/               
├── /PFDA_mywork/        
└── /PFDA_Project              # Project folder. You are here!!
│   ├── /data                  # data subdirectory.
│   │   ├── /daily_data/       # daily_data folder 
│   │   ├──   /hourly_data/    # hourly_data folder
│   │   └── joined_data.csv    # joined_data.csv file 
│   ├── /imgages/              # images subdirectory folder
│   ├── /pdf/                  # pdf subdirectory folder 
│   ├── /python/               # python subdirectory folder
│   ├── project.ipynb          # project jupiter notebook
│   ├── README.md              # This file
│   ├── requirements.txt       # requirements.txt file
│   ├── .gitattributes
│   └── .gitignore
```

### Files in this repository.

#### project.ipynb
A Jupyter notebook containing the project submission - an analysis of wind data for a selected set of weather stations downloaded 
from Met Éireann historical website.
Jupyter Notebook is a web-based interactive environment used to create notebook documents that can contain live code, equations, 
visualizations, media and other computational outputs. Jupyter notebooks are often used by programmers and data scientists to 
document, experiment, and demonstrate code-based workflows.

#### requirements.txt
A list of packages from the Python install in the source environment required for the Jupyter notebook, script or program to run. The following command will install the packages in requirements.txt:

```sh
pip install -r requirements.txt

```

### Subdirectories

The following subdirectories are included, with a brief description of the purpose of each given below as well.

#### ./data

This data subdirectory contains two folders, 

- **./data/daily_data** folder which contains the daily data downloaded for a selection of weather stations, as selected when running the project.ipynb notebook.
- **./data/hourly_data** folder which contains the hourly data downloaded for a selection of weather stations, as selected when running the notebook.

It also includes a ./data/joined_data.csv file which is generated by running the notebook and contains a larger csv file which results from joining all the .csv files contained in the data/daily_data folder. 

#### ./images
Contains the image files used in the weather.ipynb notebook. Some of these have being downloaded and some have being generated by running the notebook.

#### ./python

This folder contains a number of custom python classes which have being developed to complete a range of tasks in our project.ipynb notebook. The use and purpose of these classes will be explained within the notebook itself.

#### ./pdf

This folder contains the project brief in .pdf format.


----
## 3.0 Get Started
----

### 3.1 To get stated with this project please follow these steps:

1. Clone the repository to your local machine. 

```sh
git clone https://github.com/MikeCurleyCoosan/PFDA.git

```
2. Download and install [Anaconda](https://www.anaconda.com/). Anaconda comes with its own set of pre-installed data science packages 
and 
tools, making it convenient for beginners to set up their environment quickly. The pre-installed packages that are required to work 
with 
the project are [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/) and [Matplotlib](https://matplotlib.org/).

3. Download and install [Visual Studio Code](https://code.visualstudio.com/). Visual Studio Code is a code editor with support for 
development operations like debugging, task running, and version control.

4. Download and install the latest version of [Git](https://git-scm.com/). Git is a free and open source version control system 
designed 
to handle everything from small to very large projects with speed and efficiency.

5. Navigate to the project directory in VS Code

6. Open up the project.ipynb notebook.

----
## 4.0 Get Help
----

If you encounter any issues or have any questions about this project please [open an issue](https://github.com/MikeCurleyCoosan/PFDA/issues) on GitHub. Alternatively you can contact me at G00376456@atu.ie. 

### 4.1 Issue Tracker

Visit our [issue tracker](https://github.com/MikeCurleyCoosan/PFDA/issues) on GitHub to see if your problem has already been reported 
or to report a new issue. Feel free to join any ongoing discussions related to bugs or feature requests.

### 4.2 Contact Us

If you need further assistance or have any other inquiries, you can reach out to me via [email](G00376456@gatuie). I will do my best 
to respond to your enquiry in a timely manner.
Please don't hesitate to reach out if you need help or have feedback on how the project may be improved.

----
## 5.0 Contribute 
----

Contributions from the community to help improve the project are welcome. Whether you're a developer, data scientist, or game 
enthusiast, there are several ways you can contribute:

### 5.1 Feature Requests

Have an idea for a new feature or enhancement? Feel free to [open a feature request](https://github.com/MikeCurleyCoosan/PFDA/issues) 
on our GitHub repository. I value your feedback and are always looking for ways to enhance the project.

### 5.2 Code Contributions

If you're interested in contributing code, I would love to have your help! You can [open a pull request](https://github.com/MikeCurleyCoosan/PFDAt/pulls) on our GitHub repository, which I will endevour to respond to in a timely manner.

----
## 6.0 Author
----

### About Me: 

My name is Michael Curley and I am a student in the Higher Diploma in Data Analytics Course in ATU, Galway Ireland. This project was 
undertaken as part of the Programming for Data Analytics Module undertaken as part of that course of study.

## 7.0 References

### 7.1 Websites

***
- Reference 1: [Met Eireann historical Data]( https://www.met.ie/climate/available-data/historical-data)
- Reference 2: [Fandom -Wind Turbines]( https://windenergy.fandom.com/wiki/Wind_turbine)
- Reference 3: [Wind farms in Ireland](https://en.wikipedia.org/wiki/List_of_wind_farms_in_the_Republic_of_Ireland)
- Reference 4: [sklearn-linear -LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model)
- Reference 5: [IBM -LinearRegression.html](https://www.ibm.com/topics/linear-regression)
- Reference 6: [Sustainable Energy Authority of Ireland- Renewable energy](https://www.seai.ie/renewable-energy/wind-energy#:~:text=Wind%20energy%20in%20Ireland&text=It%20is%20both%20Ireland%27s%20largest,in%20Ireland%20after%20natural%20gas)
- Reference 7: [Government of Ireland Climate Action Plan 2024](https://www.gov.ie/pdf/?file=https://assets.gov.ie/296414/7a06bae1-4c1c-4cdc-ac36-978e3119362e.pdf#page=null)
- Reference 8: [Regular Expressions - Python Documentation](https://docs.python.org/3/library/re.html)
- Reference 9: [Requests Module - Real Python](https://realpython.com/python-requests/)
- Reference 10: [Zipfile Module - Python Documentation](https://docs.python.org/3/library/zipfile.html)
- Reference 11: [SQL Alchemy module](https://www.sqlalchemy.org/)
- Reference 12: [Git large file storage](https://git-lfs.com/)
- Reference 13: [Javapoint -skip rows while reading csv file](https://www.javatpoint.com/how-to-skip-rows-while-reading-csv-file-using-pandas)
- Reference 14: [W3Schools - Python datetime](https://www.w3schools.com/python/python_datetime.asp)
- Reference 15: [Real Python - Slicing and dicing with .loc[]](https://realpython.com/lessons/slicing-and-dicing-with-loc/)
- Reference 16: [Pandas - Dataframe resampling](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.resample.html)
- Reference 17: [Geeks for Geeks- Dataframe Resampling](https://www.geeksforgeeks.org/python-pandas-dataframe-resample/)
- Reference 18: [Tutorialspoint - Resampling timeseries](https://www.tutorialspoint.com/how-to-resample-time-series-data-in-python)
- Reference 19: [Pandas- Skipinitialspace funtion](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
- Reference 20: [Geeks for Geeks - Strip whitespace from dataframe](https://www.geeksforgeeks.org/pandas-strip-whitespace-from-entire-dataframe/)
- Reference 21: [Random Forest Regressor](https://scikit-learn.org/1.5/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
- Reference 22: [Neural networks - Tensorflow](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.72118&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)
- Reference #23: [Generate Markdown tables](https://www.tablesgenerator.com/markdown_tables)
- Reference #24: [Builtin - Boxplot](https://builtin.com/data-science/boxplot)
- Reference #25: [Align images in markdown](https://davidwells.io/snippets/how-to-align-images-in-markdown)
- Reference #26: [Generate a Markdown Banner](https://banner.godori.dev/)
- Reference #27: [Geeks for geeks - Pandas dataframe correlation](https://www.geeksforgeeks.org/python-pandas-dataframe-corr/)
- Reference #28: [Pearson Correlation co-effiecient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)
- Reference #29: [Python 3 documentation](https://docs.python.org/3/index.html) 
- Reference #30: [Matplotlib documentation](https://matplotlib.org/index.html)   
- Reference #31: [Seaborn documentation](https://seaborn.pydata.org/index.html)  
- Reference #32: [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)  
- Reference #33: [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) 
- Reference #34: [Github Flavoured Markdown](https://github.github.com/gfm/#what-is-github-flavored-markdown-) 

### 7.2 Books

- Reference #1: "An introduction to statistical learning with applications in R" - by Gareth James, Daniela Witten, Trevor Hastie, 
Robert Tibshirani
- Reference #2: [A Whirlwind Tour of Python - Jake VanderPlas available free online](https://jakevdp.github.io/
WhirlwindTourOfPython/)
- Reference #3: "Python for Data Analysis - Data Wrangling with Pandas, NumPy and IPython" - by McKinney, Wes. Python  O'Reilly 
Media.
- Reference #4: [Python Data Science Handbook - Jake VanderPlas -O'Reilly](https://jakevdp.github.io/PythonDataScienceHandbook/)





