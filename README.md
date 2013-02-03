codon-timing
============

Some people did an experiment in which, for each of many ribosomes, they observed a sequence of base pairs the ribosome transcribed in a fixed amount of time.
That is, they paused a bunch of ribosomes at the start of RNAs, let it run for N seconds, paused them again, and saw what they had moved over.
They used that to calculate average ribosome speed. 

This script's goal is to use that same data to figure out how long individual codons take to transcribe. 
The idea is that maybe different codons take different amounts of time to transcribe.

This makes two assumptions:

* Each codon takes a constant amount of time to transcribe.

* The time to transcribe a sequence of codons is the sum of the times to transcribe its individual codons.

In cases where one or two base pairs are left over (being a partially transcribed codon), the extra base pairs are ignored. Since there are quite a few codons that each ribosome did (~70), that should not be too big an error.

The input format is:
   
    # Each line has a time the ribosome took followed by the base pairs 
    # it transcribed. The leftmost base pair is the first transcribed.
    
    3.43 AAGCUGCCGUA
    5.34 GGCUAGCUAAGCUGGCAAU


To run (with a sample input file):

    python generate_inputfile.py > sample_inputfile.txt
    python codon_timing.py < sample_inputfile.txt

To run some tests:

    python test.py
   
Depends on numpy.
I used Python 2.7.
