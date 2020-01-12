Cache replacement
================================================================
This program can show cache replacement result by the different algorithm in given cache size step by step.

Supported algorithm
----------------
1. LFU(Least Recently Used)
2. LRU（Least Frequently Used）

If there have multiple page can be replacement, using FIFO.

Sample input
------------------------
The sample file is *project3.txt*

Input Format
---------------------------
        1 2 3 4 5 1 5 3 2 4 7 5 3 2 1 5 6 7 5 2 1 6 9 4 2 3 5 1 6 4 7 5 3 1 2 6 4 8 5 1 2 3 4 6 5 2 1 3 2 1 6 4 5 1 2 3 1 2 2 


How to use this program
------------------------
You have to input your:
1.  Input file name (input file should be put in the same directory)
2.  Cache size
3.  Select which algorithm you want to use.

Result
------------------------
Output is just a print of python dictionary.
So it will like this:

By LFU

        2
        {'2': 12, '3': 8, '4': 7, '5': 10, '1': 2}

By LRU

        2
        {'1': 3, '4': 7, '5': 6, '2': 1, '3': 3}

The first number means which page needs to be visit.
In second line, number in '' is the page number, another number is the counter.
Counter can be using times(LFU), or age(LRU)
