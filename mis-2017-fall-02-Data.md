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

## SQL
[2018-09-25](#sql)

### Reading
* ISBB Chapter 4 - data https://bus206.pressbooks.com/chapter/chapter-4-data-and-databases/
* Database design with UML and SQL, 3rd edition: http://www.tomjewett.com/dbdesign
  * Models and languages http://www.tomjewett.com/dbdesign/dbdesign.php?page=models.html
  * Basic structures: classes and schemes http://www.tomjewett.com/dbdesign/dbdesign.php?page=class.php
  * Basic structures: rows and tables http://www.tomjewett.com/dbdesign/dbdesign.php?page=tables.php
  * Basic structure: associations http://www.tomjewett.com/dbdesign/dbdesign.php?page=association.php
  * Discussion: more about keys http://www.tomjewett.com/dbdesign/dbdesign.php?page=keys.php
* Software Carpentry - Databases and SQL http://swcarpentry.github.io/sql-novice-survey/
  * Section 1-6 (Selecting Data, Sorting and Removing Duplicates,
    Filtering, Calculating New Values, Missing Data, and Aggregation).

### Hands-on
You may find the SQLite SQL Reference (http://www.sqlite.org/lang.html) useful in understanding commands.

All the following examples are using the teaching cluster.  Please
change your current directory to a folder to contain these examples
(do not use your home folder).

Get the data from the example
```bash
wget -c https://github.com/swcarpentry/sql-novice-survey/raw/gh-pages/files/survey.db
```

Start SQLite3 with the sample data
```bash
sqlite3 survey.db
```

Use the `.help`, `.exit`, `.tables`, `.schema`, and `.dump` commands.

### Homework

1. Homework 2-2: SQLite3. 
   1. Download and start `sqlite3` as per the above hands-on
   instructions.  Complete the following and copy/paste the session
   into the course assignment similarly named:
	   1. Display the database schema.
	   2. List the columns for the `Site` table.
	   3. Who took samples from site  'DR-1' on '1927-02-10. (use a SQL comment `-- 2-2-3: Your answer` to record your answer)
	   4. Write an SQL statement for the above question.
	   6. Formulate another question to ask the database (use a SQL comment `-- 2-2-6: Your answer` to record your answer)
	   7. Write and SQL statement for the above question.

## Databases
[2018-09-27](#databases)

In this section we will explore relational databases in the context of an example database (https://chinookdatabase.codeplex.com/)

### Reading
 * Some of the examples are taken from http://www.sqlitetutorial.net/

### Hands-On
First create a simple database and use it.
```bash
sqlite3 simple.db
```

```sql
.header ON
CREATE TABLE map (key string PRIMARY KEY, value number);
INSERT INTO map (key,value) VALUES ("One",1),("Two",2);
SELECT * FROM map WHERE key="One";
UPDATE map SET value=100 WHERE key="One";
DELETE FROM map WHERE key="One";
```

Now download, unzip, and run the sample database.
```bash
wget -c http://www.sqlitetutorial.net/download/sqlite-sample-database/?wpdmdl=94 -O chinook.zip
unzip chinook.zip
sqlite3 chinook.db
```

Review the database [**schema**](http://www.sqlitetutorial.net/download/sqlite-sample-database-diagram-with-color/?wpdmdl=98).

Some sample queries:
```sql
SELECT * FROM tracks JOIN genres ON tracks.GenreId=genres.GenreId;
SELECT CustomerId, InvoiceDate, BillingCity FROM invoices;
```

### Homework
1. Homework 2-3: Databases.
   1. Download and load the chinook datbase as described in the notes
      and answer the following questions. Copy and paste the SQL
      session into the course homework assignment.  For written
      questions use the "SQL Comment" syntax (`-- comment`) within
      SQLite.
	  1. Develop a simple question to ask the database.  The question
         must limit the data to a subset of a table or tables.
	  2. Write and execute the SQL for the previous question.
	  3. Develop a more complex question will span at least two tables.
	  4. Write and execute the SQL for the previous question.

### Example 2 - Baseball
The next in-class example is using a baseball statistics database.
 * Baseball Data http://www.seanlahman.com/baseball-archive/statistics/
 * Sqlite3 version of the data https://github.com/jknecht/baseball-archive-sqlite

```bash
wget https://github.com/jknecht/baseball-archive-sqlite/raw/master/lahman2016.sqlite
sqlite3	lahman2016.sqlite
```

Many time you will want to save the query, not just run it in the shell.  To do this save the query in a file and *redirect* the output into the `sqlite3` command and optionally redirect the output to a file.  For the following example:

What did the top 10 season hitters of all time make during that year?
```sql
SELECT 
  Master.playerID, 
  Master.NameLast,
  Master.debut,
  Salaries.YearID,
  Batting.YearID,
  Batting.H
FROM
  Master
JOIN Salaries ON Master.playerID=Salaries.playerID
JOIN Batting ON Master.playerID=Batting.playerID
WHERE
  Salaries.yearID=Batting.yearID
ORDER BY Batting.H DESC, Master.playerID
LIMIT 10;
```

Save the text to a file called `baseball.sql` and run the following command (it takes about 50 seconds to run):
```bash
srun sqlite3 lahman2016.sqlite -header -csv < baseball.sql > baseball.csv
```

Please note the `srun` command runs the `sqlite3` command on a node in
the cluster.  The `-header` and `-csv` make it so the output can be
used by programs such as Excel, R, Julia, Python, etc.  One way to
access the file is to commit it to git and download it from VCS.
There are other tools to access files via either "sftp" or "rsync" but
those methods are left as an exercise for the reader.

## Assessment

Complete the following assessment and push your work to the *mis
assignment repository* on VCS and submit both the last *commit-id* and
the *repository URL* to the class website.

The Module 2 assessment will assess your understanding of data,
databases, and the SQL language and will be an extension of the
in-class and homework assignments.  The assessment is worth 20
assessment points.

This is an assessment as such should be done entirely on your own and
you should treat it as if it where a take home exam.  You may consult
the internet for information but you must not directly or indirectly
solicit third party assistance (classmates or external forums for
example).  Please see the assessment section in the syllabus for
additional requirements.


### References
 * ISBB Chapter 4 - Data (https://bus206.pressbooks.com/chapter/chapter-4/)
 * Relational Databases http://www.tomjewett.com/dbdesign/
 * Software Carpentry - Databases and SQL: http://swcarpentry.github.io/sql-novice-survey/
 * JSON data format and specification: http://www.json.org/
 * Julia https://docs.julialang.org
 * SQL database SQLite: http://www.sqlite.org/ and 
 * SQLite tutorial: http://www.sqlitetutorial.net/
 * Baseball statistics http://www.seanlahman.com/baseball-archive/statistics/, Sqlite3: https://github.com/jknecht/baseball-archive-sqlite
 * Key-Value store Redis: https://redis.io/
