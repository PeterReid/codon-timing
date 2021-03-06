import numpy
import re
import sys

# We need to assign numbers to each of the 64 codons so that we can
# put them in a matrix in an orderly way. This generates the codon that
# corresponds to some index in [0..63]
def nth_codon(n):
    bases = 'AUGC'
    return bases[n%4] + bases[(n//4)%4] + bases[(n//16)%4]

# Codon -> Number lookup
codon_number = dict([nth_codon(n), n] for n in range(64))

# Iterate through codons in a string, ignoring a final partial one
def iter_codons(bases):
    for codon_start_index in range(0, len(bases)-2, 3):
        yield bases[codon_start_index : codon_start_index+3]

# Build an array (of length 64) where the i'th index is how many of the i'th codon there were.
# Partial codons at the end are ignored.
def codon_counts(bases):
    counts = [0]*64
    for codon in iter_codons(bases):
        counts[codon_number[codon]] += 1
    return counts

class Translation:
    # time: how long it took to translate
    # bases: base pairs translated
    def __init__(self, bases, time):
        self.bases = bases
        self.time = time
        
# The central idea here is that we can represent this as a matrix multiplication:
#
#                   # of codons
#                 ________|_______
#               /                 \
#
#            /  | N N N N N N N N |   |T|    |S|
#           |   | N N N N N N N N |   |T|    |S|
# # of runs |   | N N N N N N N N | x |T|  = |S|
#           |   | N N N N N N N N |   |T|    |S|
#            \  | N N N N N N N N |   |T|    |S|
#                                     |T|
#                                     |T|
#                                     |T|
# Where Nij = How many times the j'th type of codon occurs in the i'th run
#       Tj  = Time to translate the j'th type of codon
#       Si  = Time that the i'th run ran for
#
# Each S is the sum of the product of counts with the corresponding times.
#
# N and S are known. T is not. Fortunately, numpy solves that sort of problem,
# finding the lowest-error solution.
def solve(translations):
    count_matrix = []
    timing_vector = []
    for translation in translations:
        timing_vector.append(translation.time)
        count_matrix.append(codon_counts(translation.bases))
    return numpy.linalg.lstsq(count_matrix, timing_vector)[0]

# Turn some lines into some Translations
def iter_translations(lines):
    pattern = re.compile(r'^([\d.]+)\s+([AUCG]*)$')
    
    for (line_no, line) in enumerate(lines):
        line = line.strip()
        if line=='' or line[0] == '#': continue
        
        match = pattern.match(line)
        
        if match:
            try:
                time = float(match.group(1))
                bases = match.group(2)
                yield Translation(bases, time)
            except ValueError:
                raise Exception('Invalid number on line %d' % (line_no+1))
        else:
            raise Exception('Could not parse line %d. Expected "<TIME> <CODONS>", where CODONS is made of AUCG.' % (line_no+1))

if __name__ == '__main__':
    solution_timings = solve(iter_translations(sys.stdin.readlines()))
    for (codon_number, time) in enumerate(solution_timings):
        print('%s %f' % (nth_codon(codon_number), time))
