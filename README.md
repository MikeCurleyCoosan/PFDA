# PFDA

![Banner Image](Images/Programming_for_Data_Analytics.png)


<a target="_blank" href="https://docs.python.org/3/tutorial/index.html">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python"/>
</a>
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
  <img src="https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black" alt="Matplotlib"/>
</a>
<a target="_blank" href="https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/
basic-writing-and-formatting-syntax">
  <img src="https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white" alt="Markdown"/>
</a>
<a target="_blank" href="https://www.latex-project.org/">
  <img src="https://img.shields.io/badge/latex-%23008080.svg?style=for-the-badge&logo=latex&logoColor=white" alt="LaTeX"/>
</a>
<a target="_blank" href="https://code.visualstudio.com/">
  <img src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white" 
alt="Visual Studio Code"/>
</a>
<a target="_blank" href="https://jupyter.org/">
  <img src="https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter Notebook"/>
</a>

-----

_This README has being written with [GitHub's Documentation on README's](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) in mind. You should refer to that 
documentation for more information on writing an appropriate README for visitors to your repository._

_You can find out more about writing in MarkDown in [GitHub Documentation](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)_

---

## Table of Contents.

* [1.0 About this project](#10-about-this-repository)
* [2.0 Use of this project](#20-use-of-this-repository)
  * [2.1 Getting Started](#21-getting-started)
* [3.0 Get Started](#30-get-started)
  * [3.1 To get started follow these instructions](#31-to-get-stated-with-this-project-please-follow-these-steps)
  * [3.2 Using GitHub codespaces](#32-using-github-codespaces-to-complete-the-tasks)
* [4.0 Get Help](#40-get-help)
  * [4.1 Issue Tracker](#41-issue-tracker)
  * [4.2 Contact Us](#42-contact-us)
* [Contribute](#50-contribute)
* [Author](#60-author)

----
## ***1.0 About this repository***
----

This repository contains the assessment tasks and project for the Programming for Data Analytics module as part of the Higher Diploma in Data Analytics, at the Atlantic Technological University (ATU) Galway. 


The repository contains three folders:

- PFDA-assignments
- PFDA-project
- PFDA-mywork


The purpose of each of these folders is explained in more details below.


----
## ***2.0 Use of this repository***
----

This repository has being used to demonstrate the ability to be able to;

1. Programmatically create plots and other visual outputs from data.
2. Design computer algorithms to solve numerical problems.
3. Create software that incorporates and utilises standard numerical libraries.
4. Employ appropriate data structures when programming for data-intensive applications.

This has being done through the completion of a number of assignments which are stored in the `PFDA_assignments` folder. A bigger project has being completed also and this has being stored in the `PFDA_project` folder. Some more details about the assignments and the project are given below.


The four assignments that were completed were as follows.

- **assignment2-weather.ipynb**
  - Using the file given, which is stored as `weatherreadings1.csv` in the `data` folder of this repository create a nice plot of temperature over time.
  - Use the `dryBulbTemperature_Celsius` column.

- **assignment03-pie.ipynb**
  - Create a nice pie chart of the email domains in the csv file at the following [google drive location](https://drive.google.com/uc?id=1AWPf-pJodJKeHsARQK_RHiNsE8fjPCVK&export=download).

- **assignment05_risk.ipynb**
  - Create a program that simulates 1000 individual battle rounds of Risk (3 attacker vs 2 defender) and plots the result.
  - For extra marks create a more complicated version that simulates a full series of rounds for armies of arbitrary sizes, until one 
    side is wiped out and plots the results.
  - Two versions are offered here, one in notebook form and the other contains a series of python classes which have being written
    to complete both tasks as set above. This version has it own folder, the `Risk` folder contained within the `PFDA_assignments` folder, and also contains its own `README.md` file to explain how it works.


- **assignment06_Weather.ipynb**
  - Using the data from this [link](https://cli.fusio.net/cli/climate_data/webdata/hly4935.csv)
  Plot:
    * The temperature
    * The mean temperature each day
    * The mean temperature for each month
    * The wind speed
    * The rolling wind speed (say over 24 hours)
    * The max wind speed for each day
    * The monthly mean of the daily max wind speed


The project directory has a large project which analyses the wind speed around the country with a view to a windfarm. 


### 2.1 Getting Started

To start using this project, simply follow the steps outlined in the [Get Started](#30-get-started) section below. Once you have set 
up the project, you can begin exploring and analyzing the data in this project right away.

----
## 3.0 Get Started
----

### 3.1 To get stated with this project please follow these steps:

1. Clone the repository to your local machine. 

```sh
git clone https://github.com/MikeCurleyCoosan/PFDA.git

```
2. Download and install [Anaconda](https://www.anaconda.com/). Anaconda comes with its own set of pre-installed 
data science packages and tools, making it convenient for beginners to set up their environment quickly. The 
pre-installed packages that are required to work with the project are [Pandas](https://pandas.pydata.org/), 
[NumPy](https://numpy.org/) [Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/index.
html).

3. Download and install [Visual Studio Code](https://code.visualstudio.com/). Visual Studio Code is a code editor 
with support for development operations like debugging, task running, and version control.

4. Download and install the latest version of [Git](https://git-scm.com/). Git is a free and open source version 
control system designed to handle everything from small to very large projects with speed and efficiency.

5. Navigate to the project directory in VS Code.

6. All the assignments are in jupyter notebook format and can be run in Visual Studio Code by clicking the `Run All` button. Ensure that the python3 kernel has been selected before running the file. You may also navigate to the `Risk` directory contained within the `PFDA_assignments` folder, and follow the instruction on the `README.md` contained within to run the more complex version of the risk assignment. 


----
## 4.0 Get Help
----

If you encounter any issues or have questions about the project, there are a couple of resources available to 
help you:

### 4.1 Issue Tracker

Visit our [issue tracker](https://github.com/MikeCurleyCoosan/PFDA/issues) on GitHub to see if your problem has 
already been reported or to report a new issue. Feel free to join any ongoing discussions related to bugs or feature requests.

### 4.2 Contact Us

If you need further assistance or have any other inquiries, you can reach out to me via [email](G00376456@gatu.
ie). I will do my best to respond to your enquiry in a timely manner.
Please don't hesitate to reach out if you need help or have feedback on how the project may be improved.

----
## 5.0 Contribute 
----

Contributions from the community to help improve the project are welcome. Whether you're a developer, data 
scientist, or command line enthusiast, there are several ways you can contribute:

### 5.1 Feature Requests

Have an idea for a new feature or enhancement? Feel free to [open a feature request](https://github.com/MikeCurleyCoosan/PFDA/issues) on our GitHub repository.I value your feedback and are always looking for ways to enhance the project.

----
## 6.0 Author
----

### About Me: 

My name is Michael Curley and I am a student in the `Higher Diploma in Data Analytics` Course in ATU, Galway 
Ireland. This project was undertaken as part of the `Programming for Data Analytics Module` undertaken as part of 
that course of study.