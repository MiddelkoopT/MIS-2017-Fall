# Information Technology - Module 1

*IMSE 4410/7410 Management Information Systems Design (MIS)*

Material Copyright 2017 by Timothy Middelkoop.
Source code licensed under the Apache License, Version 2.0. 
Documentation licensed under CC by SA 3.0.

In Module 1 we cover basic Information Technology (IT) Architecture and IT paradigms.

## Hardware 
[2018-08-28](#hardware)

### Reading
 * ISBB Chapter 2 - Hardware (https://bus206.pressbooks.com/chapter/chapter-2/)
 * What are bytes, characters (ASCII, Unicode, utf-8), files. (https://www.youtube.com/watch?v=MijmeoH9LT4)

### Hands On
 * We will be passing around various pieces of hardware today.
 * Interactive video data-center tour.

### Reference
 * ASCII https://en.wikipedia.org/wiki/ASCII
 * UTF-8/Unicode http://www.fileformat.info/info/charset/UTF-8/list.htm

## Software
*[2018-08-30](#software)*

### Reading
 * ISBB Chapter 3 - Software (https://bus206.pressbooks.com/chapter/chapter-3/)
 * Software Carpentry: Linux Shell (http://swcarpentry.github.io/shell-novice/) sections 1-3

### Hands On
 * We will be exploring the Linux operating system using the Software Carpentry lesson on the Unix Shell (Linux)

### Homework
  This homework will help you prepare for future homework.  A basic ability to work with the Linux shell will be a fundamental skill required in this class.
  
  1. Homework 1-1: Linux Shell
     1. Connect to the teaching cluster `tc.rnet.missour.edu`
     2. Create a series of folders to store and organize your class work, one of which will be for this class.
     3. In the class folder create a folder called 'module-1' and a sub-folder called 'linux-shell'
     4. In the class folder create a file called 'ReadMe.txt' and in and edit some text about this class.
     5. Create an empty file called 'Homework-1-1.txt' in the 'linux-shell' folder that will contain your submission for this homework.
     6. Make sure that your homework is not readable by your classmates (hint: file permissions).
     7. Place your answers to the following questions/tasks in the 'Homework-1-1.txt' file and copy the results into the class assignment for this homework.  Please copy the command (including the prompt) and the result.  You must copy and paste text and not use screen captures (images).
        1. Demonstrate (through the use of commands and their output) that your created the folders and files properly. Do not show 'how' they were created (for example the use of the `mkdir`command), show that they are indeed there.
        2. Show that your class files are not readable by anyone else but you.
        3. Demonstrate the use of the command `grep` on the file 'ReadMe.txt'
        4. Demonstrate the use of a pipe (`|`) with `grep`, `wc` or some other command.
        6. Demonstrate the use of some other command on your files.


## Networking
[2018-09-06](#networking)

### Reading
 * ISBB Chapter 5 - Netwokring https://bus206.pressbooks.com/chapter/chapter-5-networking-and-communication/ 
 * IPv6 Video - https://player.oreilly.com/videos/9781771375269 ("Introduction" and "IPv6 Background And Basics" sections)
   * Please write a number of (what you think are) important questions down as you view it and bring them to class.
   * The "IPv6 Packet and Header" is very dense and do not worry about understanding all the concepts.

### Questions
 * What is an IP address?
 * What is DNS?
 * How does a packet get from the local network to a website.

### References
 * Networking http://intronetworks.cs.luc.edu/current/ComputerNetworks.pdf
 * Ethernet https://en.wikipedia.org/wiki/Ethernet_frame
 * IP https://en.wikipedia.org/wiki/Internet_Protocol and https://en.wikipedia.org/wiki/IPv6


## Community (gitlabs)

### Reading
Read the introduction material and as much as you wish, we will be covering this in depth later but skim through it for interesting and basic material.
 * Software Carpentry Git Lesson http://swcarpentry.github.io/git-novice/ 
 * Pro Git book https://git-scm.com/book/en/v2

### Hands-On 

Go to Mizzou's Gitlabs server at https://vcs.missouri.edu and login using your Pawprint (SSO) and password (use the default LDAP method).

Create a new project called `mis-login-First-Last` where login is your pawprint, for example I would be `mis-middelkoopt-Timothy-Middelkoop`.

Share this project with myself `@middelkoopt` and the TA `@mjxqb`

Create a ssh key by logging into `tc.rnet.missouri.edu` and running the following (make sure to create a strong passphrase):

```
$ cd ~
$ ssh-keygen
$ cat .ssh/id_rsa.pub
```

Copy the public key shown by the `cat .ssh/id_rsa.pub` command, it should look similar to this:

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDuSqEsyPw9gULRil72VHCrpw/+dmKpcPp50rr7YypK95T4US7eiwOqX0VJANKde77MjAy7+rgbjNJDbO6V3VLSJxOlUWS4Vj7wBF1j/u7EUnjdp2mMMHA2zu7sIwbjp+tjt44MYxK1P/RbB1sXwwIOUvxOZjG1uKsO/Xze6GX3l2pxkb+aDiZ+i8JZdnwC9+0ZFwUVBhcXO90IHapz1rppTFO9K1LRJtj/aiSOcD2E0mphLLDD7Z5l9EDK0tijYz/fB2F0lUFlF1isjKAGkW+Uq5CzsMDtfXWG5skaEKMf2ujMDGEenHZ3662tN2XfVc/I6NOGFGZ9QH+jLmV7JhCl middelkoopt@tc-m610-login-node623
```

Go back to gitlabs and add your public ssh-key to your account as follows (the Avatar/Account button is on the top right of the page):

```
"Avatar" -> Settings -> ssh-keys -> Key: paste public key
```

Now go to "Project" website and copy the git URL by doing the following (the "Hamburger" is the icon with three lines on the top left of the page).

"Hamburger" -> Projects -> Your Projects -> select the project to
clone (in this case mis-$USER-$NAME) -> home -> click the clipboard
icon next to the URL, make sure SSH is selected not HTTP.

Now go to your class folder on `tc.rnet.missouri.edu` and clone the repository
```
git clone git@vcs.missouri.edu:middelkoopt/welcome.git
```
where `git@vcs.missouri.edu:middelkoopt/welcome.git` is the pasted from the step before.


### Homework
Using the hands-on instructions and the documentation complete the following homework:

 1. Homework 1-1: gitlabs
    1. Create a repository on https://vcs.missouri.edu called mis-pawprint-first-last as described in the Hands-On section.
    2. Assign "Guest" permissions to `@middelkoopt` and `@mjxqb` to the project
    3. Create a `ReadMe.txt` file and commit it to the repository (note the upper/lower case and spelling).
    4. Clone the repository on `tc.rnet.missouri.edu`
    5. Bonus: Modify the ReadMe.txt on `tc.rnet.missouri.edu` and push it back to `vcs.missouri.edu`.

### References
 * Pro Git book https://git-scm.com/book/en/v2
 * Software Carpentry - Git  http://swcarpentry.github.io/git-novice/
