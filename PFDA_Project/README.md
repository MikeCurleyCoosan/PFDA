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
* [Author](#60-author)

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

### subdirectories

The following subdirectories are included.

#### ./data

This subdirectory contains two folders, 

- data/daily_data folder which contains the daily data downloaded for a selection of weather stations, as selected when running the project.ipynb notebook.
- data/hourly_data folder which contains the hourly data downloaded for a selection of weather stations, as selected when running the notebook.

It also includes a data/joined_data.csv file which is generated by running the notebook and contains a larger csv file which results from joining all the .csv files contained in the data/daily_data folder. 

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

If you encounter any issues or have any questions about this project please [open an issue](https://github.com/MikeCurleyCoosan/PFDA/
issues) on GitHub. Alternatively you can contact me at G00376456@atu.ie. 

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

If you're interested in contributing code, I would love to have your help! You can [open a pull request](https://github.com/
MikeCurleyCoosan/PFDAt/pulls) on our GitHub repository, which I will endevour to respond to in a timely manner.

----
## 6.0 Author
----

### About Me: 

My name is Michael Curley and I am a student in the Higher Diploma in Data Analytics Course in ATU, Galway Ireland. This project was 
undertaken as part of the Programming for Data Analytics Module undertaken as part of that course of study.

### References


- Reference #1: https://www.ultraboardgames.com/risk/game-rules.php
- Reference #2: https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html
