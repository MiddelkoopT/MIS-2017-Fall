# Data - Module 2

*IMSE 4410/7410 Management Information Systems Design (MIS)*

Material Copyright 2017 by Timothy Middelkoop.
Source code licensed under the Apache License, Version 2.0. 
Documentation licensed under CC by SA 3.0.

In Module 2 we will cover "data" in information technology systems and the different ways representing, managing, and using this data.

## Data
[2018-09-18](#data)

In order to collect, process, and analyze data we must first store and represent it in a computing and storage system.  Most data can be represented by the following fundamental data types (this is a loose definition):

 * Byte: an opaque 8-bit value. Often represented in hex.  Example `0xFF 0xFE`
 * Integer: A whole number (Int32, Int64). Example: `42`
 * Float: A floating point number (an estimate), (Float32, Float64).  Often represented in IEEE 754 format. Example `3.14e1`
 * String: Human readable text.  Often encoded as UTF-8. Example `"世界"`
 * Boolean: True or False
 * Array: An indexed collection of values. Index starts at 0 ('C' format) or 1 (Fortran format).  Example: `[ 100, 200, 300]`
 * Associative Array: A collection of key/value pairs.  Accessed via the key.  Example `{"Apple": 1, "Banana":2}`
 * Date and Time: Seconds since January 1, 1970. Often displayed in ISO 8610. Example: `2017-09-19T08:00Z`
 * Object.  A collection named attributes with values.
 * NULL: The absence of a value.

The data transfer format we will be using this semester
is [JSON](http://www.json.org/).  Example:
```JSON
{
	"Apple": 1,
	"Banana": 2,
	"Carrot": [100, 200, 300]
}
```

### Reading
 * ISBB Chapter 4 - Data (https://bus206.pressbooks.com/chapter/chapter-4/)
 * JSON data format and specification: http://www.json.org/
 * Julia https://docs.julialang.org

### Hands On

[Julia](https://docs.julialang.org) is an Open Source
scientific/engineering language loosely based on Matlab but
dramatically faster and built to take advantage of multiple core and
multiple node systems (HPC).

Log in to the teaching cluster for the following hands-on exercise.

First, Create a new file called `data.json` and place the above JSON
example in it.  Run the following test to ensure the data is formatted
correctly.

```bash
jq . data.json
```

Load the Julia module and launch Julia on a compute node (if the
`srun` command fails just run `julia`).

```bash
module load module load julia/julia-0.5.0
srun --pty julia
```

The first time we use JSON in Julia we must first install the
package. This command may take some time to run.  Only run once.

```Julia
Pkg.add("JSON")
```

Load the package for use (every time we use Julia) and load the JSON file.
```Julia
import JSON
d=JSON.parsefile("data.json")
```

This should show the parsed JSON data (same information, different representation).

Add "Apples and Banana's"
```Julia
d["Apple"]+d["Banana"]
```

To exit Julia either press the `control-d` key or run the exit function.
```Julia
exit()
```

### Homework
1. Homework 2-1: JSON and Julia:
   1. In your class repository create a folder called `homework-2-1` and place all the files here.
   2. In this folder create a `example1.json` file with **valid** JSON that represents some data.  For example (but you cannot use this one) a sample from a weather station.
   3. Load this data into Julia and do some simple calculations on it.  Feel free to read the Julia manual for advanced commands.
   4. Commit and push your work (the JSON file) to Gitlabs.
   5. Copy the calculations and the results into the Canvas assignment for this homework (text, not screen-shots).
   6. Copy the `commit-id` and the repository URL into the Canvas assignment.


### References
 * ISBB Chapter 4 - Data (https://bus206.pressbooks.com/chapter/chapter-4/)
 * Relational Databases http://www.tomjewett.com/dbdesign/
 * Software Carpentry - Databases and SQL: http://swcarpentry.github.io/sql-novice-survey/
 * JSON data format and specification: http://www.json.org/
 * Julia https://docs.julialang.org
 * SQL database SQLite: http://www.sqlite.org/ and 
 * Key-Value store Redis: https://redis.io/
