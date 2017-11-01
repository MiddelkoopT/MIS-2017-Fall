# Code - Module 3

*IMSE 4410/7410 Management Information Systems Design (MIS)*

Material Copyright 2017 by Timothy Middelkoop.
Source code licensed under the Apache License, Version 2.0. 
Documentation licensed under CC by SA 3.0.

In Module 3 we will cover "Code" in information technology systems
including managing source code, programming, and how code is executed
and run in batch systems.  We will be covering the Python and Julia
languages and continue using SQL.  We will also be covering regular
expressions to process and filter data.

## Overview

In class we covered basic HTML and the importance of separating
content (HTML) and rendering (CSS) on web pages.  The website
https://www.w3schools.com/ is an excellent resource for learning and
reviewing HTML and CSS.

During class we covered the "Web Stack" of the Linux Apache MariaDB
PHP (LAMP) stack.  We covered the simple web request and processing,
how AJAX work, and how Internet Scale software works by separating
processing from the web.

In order to access our development server secure shell login (ssh)
into `cs3380.rnet.missouri.edu` with your pawprint and pawprint
password.

In order to prepare your home folder to serve web pages you must allow
access to your home folder by the Apache webserver.  To accomplish this
do the following (only once):

```
chmod +x ~
mkdir ~/public_html
chmod +x ~/public_html
echo test > ~/public_html/test.txt
```

Then point your browser to
`http://cs3380.rnet.missouri.edu/~${PAWPRINT}/test.txt` where
`${PAWPRINT}` is your pawprint ID.  The login and password were given
in class.

### Reading
 * ISBB Chapter 10 - Development (https://bus206.pressbooks.com/chapter/chapter-10/)
 * HTML and CSS tutorial https://www.w3schools.com/

### Homework

This homework will allow you to write a simple web page and develop a
simple PHP dynamic web page.
1. Homework 3-1: HTML
   1. Create a php file called `homework-3-1.php` in your
      `~/public_html` on cs3380 and copy the complete URL
      (`http://cs3380.rnet.missouri.edu/~${PAWPRINT}/homework-3-1.php`) into
      the homework assignment associated with this homework on canvas.
      Copy and paste your final `homework-3-1.php` file into the
      assignment (not the web page). This resulting page should be valid html5.
	  1. On the web page create a top level "Header" with "IMSE 4410"
	  2. Use php to display the current date and time in a "paragraph" tag.
	  3. Create a file in the `public_html` folder called
         `homework-3-1.json` that contains a 3x2 matrix of random
         numbers (make them up).
	  4. Use the `json_decode` function to read the json file (`file_get_contents`) in
         the previous question.
	  5. Display the table using an html table and a `foreach` loop.
	  6. Validate your html code by "show source" in your browser (ctrl-u in chrome and
         most other browsers) and copy and paste it into the `validate
         by input` section of the W3C validation services at
         https://validator.w3.org/#validate_by_input .

## Python

In this section we cover basic Python (version 3) and iteration,
conditions, lists, dictionary manipulation, functions, and classes.
We will be using as a basis for processing data and learning regular
expressions.

### Reading
 * Python Tutorial https://docs.python.org/3/tutorial/
 * Software Carpentry - Python http://swcarpentry.github.io/python-novice-inflammation/
 * Python Regular Expressions https://docs.python.org/3/library/re.html

### Homework
This homework will introduce you to basic Python 3 programming and classes.

1. Homework 3-2: Python Classes
   1. Create a basic Python 3 `Calculator` class as demonstrated in
      class in a file in your class `mis-` repository in the folder
      `homework-3-2` called `caluclator.py`.  Commit this file and
      push the repository to `vcs.rnet.missouri.edu` and post the
      `commit-id` and repository URL in the assignment associated with
      this homework.  The calculator should do the following:
	  1. Add, subtract, multiply, and divide.
	  2. Keep track of the last answer just as most calculators do ("ANS" key).
	  3. Implement a "Memory" and "Memory+" like most calculators.
	  4. Create a calculator instance and demonstrate all the functions of the calculator.
	  5. Create a second calculator instance and display the current memory.

## Security

### Reading
 *  ISBB Chapter 6 - Security (https://bus206.pressbooks.com/chapter/chapter-6/)

## References
 * ISBB Chapter 10 - Development (https://bus206.pressbooks.com/chapter/chapter-10/)
 * HTML and CSS tutorial https://www.w3schools.com/
 * Python Tutorial https://docs.python.org/3/tutorial/
 * Python Reference https://docs.python.org/3/index.html
 * Python Regular Expressions https://docs.python.org/3/library/re.html
 * Software Carpentry - Python: http://swcarpentry.github.io/python-novice-inflammation/
 * SLURM: https://slurm.schedmd.com/
 *  ISBB Chapter 6 - Security (https://bus206.pressbooks.com/chapter/chapter-6/)
 
