Supermarket Optimization
========================

**Algorithm**

This program finds the frequency of co-occurrence of product IDs in a database of
25000 transactions, with a minimum co-occurrence >= 3.

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

*On a Linux/ Mac:*
In a terminal window, navigate to the program directory and run
the run.py file passing the name of an output file as a command line
argument, for example:

> python run.py output.txt

The output of the program is saved in the program root directory as comma
separated values in the following order: ``item set size (N), co-occurrence
frequency, item 1 id, item 2 id, …. item N id``. The output is sorted by
frequency. Expected program output is provided in /sample/out.txt.

The lower limit of co-occurrence frequency is set by the sigma parameter of
the count_overlaps function. The sigma value of 2 is passed to this
function as an argument when it is called.

The database file is included in the program root directory and is loaded when
the prepare_data function is called.

**Testing**

The program can be tested on a small test dataset by running:

>python test.py
