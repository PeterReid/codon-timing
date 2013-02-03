codon-timing
============

Some people did an experiment in which, for each of many ribosomes, they observed a sequence of base pairs the ribosome translated in a fixed amount of time.
That is, they paused a bunch of ribosomes at the start of RNAs, let it run for N seconds, paused them again, and saw what they had moved over.
They used that to calculate average ribosome speed. 

This script's goal is to use that same data to figure out how long individual codons take to translate. 
The idea is that maybe different codons take different amounts of time to translate.

This makes two assumptions:

* Each codon of the same type takes a constant amount of time to translate.

* The time to translate a sequence of codons is the sum of the times to translate its individual codons.

In cases where one or two base pairs are left over (being a partially translated codon), the extra base pairs are ignored. Since there are quite a few codons that each ribosome did (~70), that should not be too big an error.

The input format is:
   
    # Each line has a time the ribosome took followed by the base pairs 
    # it translated. The leftmost base pair is the first translated.
    
    3.43 AAGCUGCCGUA
    5.34 GGCUAGCUAAGCUGGCAAU


To run (with a sample input file):

    python generate_inputfile.py > sample_inputfile.txt
    python codon_timing.py < sample_inputfile.txt

To run some tests:

    python test.py
   
Depends on numpy.
I used Python 2.7.
