Supermarket Optimization
========================

**Algorithm**

This program finds the frequency of co-occurrence of SKUs in a database of
2500 transactions, with a minimum co-occurrence >= 3.

Each transaction is compared with other transactions in a pairwise manner.
Transactions are reduced to sets and their intersections are found.
These intersections are represented as frozen sets and are added to a dictionary
as keys, and their frequencies as values; frequencies are incremented
on each successive matching of the intersection set. After an iteration,
the transaction that was in focus is discarded. As well, the program keeps
track of frozen sets/ intersections to avoid duplication of pairwise comparison.
The returned dictionary is represented as a nested array and sorted by
frequency.

**Dependencies**

Python 2.7 or higher is required to run to the program.

**How to run**

*On a Mac/Linux:*

In a terminal window, navigate to the program directory and run
the ``__init__.py`` file passing the name of the output file as a command line
argument, for example:

python ``__init__.py`` output.txt

The output of the program will be saved in the program root directory. Sample
output is provided in /sample/out.txt

The sigma value of 2 is hard coded into program as a parameter to the
count_overlaps() function. The database file is included in the program
directory.

The duration of program execution is approximately 330 seconds.
