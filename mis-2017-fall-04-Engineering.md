# Engineering - Module 4

*IMSE 4410/7410 Management Information Systems Design (MIS)*

Material Copyright 2017 by Timothy Middelkoop.
Source code licensed under the Apache License, Version 2.0. 
Documentation licensed under CC by SA 3.0.

In Module 4 we will cover engineering data and workflows.  Engineering
workflows perform analysis of engineering data without human
interaction.

## Platforms

There are many "platforms" to run Engineering Workflows, Scientific
Workflows, and even "Pipelines."  The platform used in this class is
the "Batch Scheduled Computing Cluster" and is the basis of most large
scientific software.  The SLURM scheduler (https://slurm.schedmd.com/)
is responsible for managing jobs.  This platform is similar to many
others used, including the cloud.  What we learn in this class is a
"cluster native" development, just like *internet scale* companies
today utilize "cloud native" development and the practice of DevOps.

### Homework
1. Homework 4-1: Platforms
   1. Briefly describe the following "* as a service" acronyms and
      give an example: IaaS, PaaS, and SaaS.
   2. Briefly discuss "serverless" (cloud) technology.
   3. Briefly discuss what DevOps means to you.

### Reading
 * ISBB Chapter 8 - Business Processes (https://bus206.pressbooks.com/chapter/chapter-9)
 * Cloud Native: 
   * https://www.oreilly.com/learning/the-cloud-native-application
   * https://www.oreilly.com/ideas/the-evolution-of-devops
 * Cloud Security: 
   * https://www.oreilly.com/ideas/why-cloud-native-enterprise-security-matters
   * https://www.theregister.co.uk/2017/11/01/how_to_secure_a_softwaredriven_technology_stack_in_a_cloud_of_moving_parts/
 * Data Governance: https://www.oreilly.com/ideas/developing-a-successful-data-governance-strategy


## Engineering Workflows

### Overview

Even before a workflow is created there are important prerequisites.

1. A problem statement.  What business or engineering question are you trying to answer.
2. A description of the system.  Detailed information about the system
   that the question derives its information.
3. Actual data.  Access to the full raw data.  A subset in an
spreadsheet does not count.  The way in which the data is to be
extracted in used must also be in place (access to the database for
instance).
4. Metadata.  A proper description of the actual data fields and the
data relations is required.

Once the these requirements have been met, then a workflow can be
developed. A workflow in general consists of the following steps:

1. Data ingestion (1,2,3, Go data) (Input)
   * Test Data
   * Generated Data
   * Benchmark Problems
   * Real Data
2. Data pre-processing
   * Data format conversion
   * Data filtering (subset)
   * Data cleaning (matching events, outliers etc.)
   * Data transformation (arc based to node based)
   * Data pre-processing and storage (preparation for analysis)
3. Analysis and Experimental Control
   * Plan and generate jobs (experiments, analysis parameters etc).
   * Prepare data and jobs (marshal data)
   * Monitor job progress
4. Computation
   1. SLRUM runs the jobs on the cluster
   2. Job get's input for computation
   3. Job runs computation (Julia)
   4. Job collects and writes data
5. Results Collection
   * Collect and verify data (feasibility and structure/format).
   * Transform and filter for analysis
   * Comparison with *known good solutions* for verification
6. Analysis and Analytics (Output)
   * Statistics (R)
   * Visualization 
   * Report generation

These steps utilize the following components:

1. An information management system, a git repository to manage the
entire workflow including smaller data and known good solutions.
2. A data management system such as a database (SQLite3).
3. A job management system (a cluster with SLURM).
2. Data visualization.

### Reading
 * Scientific Workflows: http://www.pnl.gov/computing/technologies/sci_workflow.stm

## Analysis Software

### R

The [R language](https://www.r-project.org/) is used extensively in
industry and academia and is an open source alternative to many
expensive statistical software packages.  R utilizes a shell like the
rest of the tools covered in this course and allows for easy
automation for statistical analysis tasks.

To run R you must first load the module, then run it on the cluster
```
module load R/R-3.2.3 
srun --pty R
```

In R you can quit by running `quit(save='no')` or by pressing `control-d`.

Students that are running MobaXterm can display graphs (this may be
slow over wireless or from home).  To test this in the R shell run the
following:

```R 
plot(1) 
```

To write a plot to a PNG file (supported by most browsers) adapt the example below

```R
png(filename = "Rplot%03d.png")
d <- read.csv("http://www.cyclismo.org/tutorial/R/_static/simple.csv",header=TRUE)
plot(velocity~mass,d)
dev.off()
```

To view the file you can either use a "sftp" client or commit it to
the git repository.  MobaXterm has a built in sftp client (sftp tab on
side) and there is an excellent open source sftp client for windows
WinSCP (https://winscp.net).  ChromeOS (Chomebooks) can use the SFTP
button/client in the secure shell app used in this class that allows
access to the files via the built-in file browser.

#### Reading
 * Introduction to R and Statistics for IMSE 4410
   * https://github.com/MiddelkoopT/Stats-2016-Spring/blob/master/stats-2016-00-Introduction.Rmd (R markdown)
   * https://github.com/MiddelkoopT/Stats-2016-Spring/blob/master/stats-2016-00-Introduction.pdf (pdf)


### Julia

[Julia](https://julialang.org) is an emerging Open Source language similar to Matlab.  It has
better performance and supports multi-core and multi-node parallelism.
Vectorization of code to increase performance is not required.

To run Julia on a single node with a single core, run the following:
```
module load julia/julia-0.5.0
srun --pty julia
```

To run 4 cores and 10GB or RAM use
```
module load julia/julia-0.5.0
srun --pty --mem=10G -c 4 julia -p 4
```

An example calculation can be found in the in class Module
4 [compute.jl](inclass/module-4/compute.jl).

See the Julia examples in Module 2 and the Julia docs
(https://docs.julialang.org) for basic and advanced use.

## Application Programmer Interface (API)

API's are the backbone of connected applications and Internet Scale
applications.  One of the most simplest API protocols is HTTP REST
utilizing JSON.  This protocol uses the same protocol as a web server
and encodes the API as set of URL endpoints surrounded by
documentation. We will be using the GitLabs API
(https://docs.gitlab.com/ee/api/) in this example.


The Linux command `curl` is similar to `wget` but is used to collect
data from web servers and pass it to a pipe. The following example
demonstrates how the this process works.

First, a simple example to demonstrate the REST process.  First we get
a JSON file from a URL.

```
curl -k -s https://vcs.missouri.edu/middelkoopt/mis-api/raw/master/simple.json
```

Note the `-s` switch is the "silence" option to remove extra message.
The `-k` switch is a workaround due to some issues with certificates.

Use the `jq` program to get the `name` attribute.
```
curl -k -s https://vcs.missouri.edu/middelkoopt/mis-api/raw/master/simple.json |jq .name
```

Lets get the project information for the https://vcs.missouri.edu/middelkoopt/mis-api project.

Now for a longer example.  Note the use of the API variable to easily
change endpoint.  Also note that it is typical to include a version number.

This lists the public projects on the server (API at https://docs.gitlab.com/ee/api/projects.html)

```
API="https://vcs.missouri.edu/api/v4"
curl -sk $API/projects |jq .
```

Information is included in the URL as well as in how the data is
presented to the server.  This next example will get the project
information for project 926.

```
curl -sk $API/projects/926 |jq .
```

And we can also just get a portion of the data.
```
curl -sk $API/projects/926 |jq .description
```

For a more in depth see the [gitlabs-api.sh](inclass/module-4/gitlabs-api.sh) example for module 4.


## References
 * ISBB Chapter 8 - Business Processes (https://bus206.pressbooks.com/chapter/chapter-9)
 * Cloud Native:
   * https://www.oreilly.com/learning/the-cloud-native-application
   * https://www.oreilly.com/ideas/the-evolution-of-devops
 * R tutorial http://www.cyclismo.org/tutorial/R/
 * Software Carpentry R module http://swcarpentry.github.io/r-novice-inflammation/
 * R language introduction https://cran.r-project.org/doc/manuals/R-intro.html
 * Julia Docs https://docs.julialang.org 
