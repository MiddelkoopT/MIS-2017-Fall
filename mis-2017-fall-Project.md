# Project

*IMSE 4410/7410 Management Information Systems Design (MIS)*

Material Copyright 2017 by Timothy Middelkoop.
Source code licensed under the Apache License, Version 2.0. 
Documentation licensed under CC by SA 3.0.

## Overview
The objective of this project is to gain experience with and
demonstrate competency in developing Engineering Workflows and
managing data.  The project will utilize the methods and examples
covered in the class. Using the "1,2,3, Go" system discussed in class
the data is expected to be "3" (benchmark) and the computation is
expected to be "2" (textbook) class.

The project will use the class gitlabs "mis-* git project used
throughout the class and all material must be stored under the
"project" folder.

Students must use a unique data source and register their data source
on the course website discussion section for the project.  See the
"Registering Data" section for more information.


## Registering Data
Every student must have a unique dataset and register it on the course
website in the project thread.  The first student to register their
data in a post can use the data.  Check before and after posting to
see if someone registered the same data source while you were in the
process of posting (this is called a race condition) and if this is
the case you must find a new data source and register the new one.

Register the dataset with the following information:
  1. The name or title of the dataset.
  2. A short description of the data.
  3. The URL of the website.
  4. The URL you plan to retrieve the data from (wget).
  
Please try to find the original source of the data.  You must not use
any datasets used in class. Government websites are good sources of
public data. All data sources must be downloadable via a "wget"
command and be "public" data.  Data already in SQLite format is not
allow.  Text or CSV formats are recommended.


## Project Questions
In the report you must include an "Questions" section that re-states
and answers the following questions:
1. What is the source of your data (website).  Provide a brief
   description of the dataset.
2. State two or more questions that you will ask of the data-set.
3. Describe how the analysis will be conducted/calculated for each of
   the questions.
4. What is the answers to the questions?
5. Are you a graduate or undergraduate student?


## Analysis Process
Use the SLURM scheduler to run the entire analysis in a "sbatch" file
on the Teaching Cluster (TC).  The project must be able to run
multiple project locations (we will checkout your code and run it).

The `sbatch` file should conduct the following steps in the analysis:
1. Download and extract the data from a website.
2. Pre-process the data into an intermediary form.  This should be in
   either a SQLite3 datbase or a JSON document.  Data conversion
   (e.g. string to integer) and filtering must be performed during
   this step. Other intermediary forms are acceptable but must have
   instructor approval prior to use.
3. Perform a simple calculation using a subset of the intermediary
   data (an SQLQuery or a subset of the JSON file).  Graduate students
   should perform more complex analysis over two or more subsets of
   data (multiple images, samples, etc.).
4. Store the results of the calculation in a JSON or other file format.
5. Graduate students must aggregate the multiple calculations and
   results into a single file or graph.

## Alternative Projects
Student who wish to build a website for the data analysis instead of
using the Teaching Cluster are welcome to do so but must contact the
instructor immediately for approval.  Students are also welcome to
propose alternative project forms but must also contact the instructor
immediately for approval.  In both cases the quality of analysis is
expected to be greater than a simple analysis.


## Graduate Students
Graduate students will be expected to analyze the data instead of
performing simple calculations.  Multiple analysis on different
subsets of the data is required and the results must be aggregated as
a final step.


## Constraints and Reminders
1. All commits must be discrete units of work as discussed in class.
2. The data **must** be retrieved from the internet via a script
   utilizing the "wget" command.
3. The data must be public.
4. Test the complete analysis by cloning the project in a new folder
   and running the analysis.


## Grading
The project will be graded on the following areas:
1. The utilization of git to manage the project including properly
   formed commits and commit comments.
2. Documentation of the project with a project level
   "project/ReadMe.md" file written in "gitlabs flavored markdown" to
   describe the files, data, and metadata.  This file should contain
   the references to the data used in the project.
3. Documentation of the project data (metadata) placed in the
   "project/ReadMe.md" file in a "metadata" section.  If this data is
   copied from the website then the URL must be included in the
   document.
4. Answering the "Project Questions" sections.
5. The quality of the pre-processing and analysis.
6. The quality of the code (formatting, comments, coding style etc.).
7. The use of SLURM to manage the Engineering Workflow.


## Submission
Submit the commit-id and URL to your "mis-*" git repository to the
assignment posted on the course website.

