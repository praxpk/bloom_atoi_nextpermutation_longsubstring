# Bloom Filter
The file bloom_filter.py is used for this program. bloom_filter.py generates
1000 bags of 1000 strings each and then creates a bloom filter for each bag.
A word at random is then extracted from any bag and checked to see if the bloom
filter returns the set of bags that contain the word. The program also checks
for false positives. To run this program:
```commandline
python bloom_filter.py
```
When running the program for the first time, a log file called bloom_filter.log
will be generated. The program prints out results and stores them in the
log file too. The file GeneralHashFunctions.py is used by this program
to generate hashes of strings. This file is provided by Arash Partow.

ref: http://www.partow.net/programming/hashfunctions/index.html  

# Atoi
The file atoi.py is used for this program. This program runs in a loop, takes
an input from the user and prints out the integer. It will quit only when 
the user types the word exit. To run this program:
```commandline
python atoi.py
```
This program will generate a log file when run the first time. The log file
stores all the queries asked by the user.

# Next Permutation
The file next_permutation.py gives the 
lexicographically next greater permutation of numbers. This program runs
in a loop, takes a user input of comma separated numbers. The program
then returns the next greater permutation.

```commandline
python next_permutation.py
```
This program will generate a log file when run the first time. The log file
stores all the number lists asked by the user.

# Longest Substring Without Repeating Characters
The file longest_substring.py gives the length of the longest substring
that has no repeating characters. This program uses command line arguments.
Here are a few examples:

```commandline
python longest_substring.py --word abcdef
```
The above command will return the length of the longest substring without
repeating characters for the string abcdef

```commandline
python longest_substring.py --random
```
The above command will generate a string at random and return the length 
of the longest substring without repeating characters for the
randomly generated string.

```commandline
python longest_substring.py --help
```
The above command prints the help section. 

Running the program for the first time will generate a log file.

# Testing
All the programs above are tested in a common file called test_code.py
To run test type the following command:
```commandline
python test_code.py 
```