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


## References
 * ISBB Chapter 8 - Business Processes (https://bus206.pressbooks.com/chapter/chapter-9)
 * Cloud Native:
   * https://www.oreilly.com/learning/the-cloud-native-application
   * https://www.oreilly.com/ideas/the-evolution-of-devops
