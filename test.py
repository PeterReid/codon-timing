from codon_timing import codon_number, codon_counts, Transcription, iter_codons, solve, iter_transcriptions
import unittest
import random

class TestCodonNumber(unittest.TestCase):
    def test_sanity(self):
        self.assertEqual(len(codon_number), 64)
        self.assertNotEqual(codon_number['AAA'], codon_number['AUG'])
    
class TestCodonCounts(unittest.TestCase):
    def test_specific(self):
        self.assertEqual(codon_counts('AAAGGGUUU')[codon_number['AAA']], 1)
        self.assertEqual(codon_counts('GCGAAAGGGUUUGCG')[codon_number['GCG']], 2)
    
    def test_ignore_partial(self):
        self.assertEqual(sum(codon_counts('AAAAA')), 1)
        self.assertEqual(sum(codon_counts('AAAUGUAA')), 2)

def random_base():
    return 'AUCG'[random.randint(0,3)]

def random_whole_codons():
    length = random.randint(40, 70)*3
    return ''.join([random_base() for i in range(length)])

def random_transcription(timings):
    bases = random_whole_codons()
    time = 0
    for codon in iter_codons(bases):
        time += timings[codon_number[codon]]
    return Transcription(bases, time)

class TestComplete(unittest.TestCase):
    def test_whole(self):
        timings = [random.uniform(0, 6) for i in range(64)]
        transcriptions = [random_transcription(timings) for i in range(400)]
        result = solve(transcriptions)
        for expected, actual in zip(timings, result):
            self.assertAlmostEqual(expected, actual)

def run_parser(lines):
    return [x for x in iter_transcriptions(lines)]
            
class TestParse(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(run_parser(["4.52 AGUCC \n", "2.3 CCAA"])[0].time, 4.52)

    def test_normal(self):
        self.assertEqual(run_parser(["4.52 AGUCC \n", "2.3 CCAA"])[1].bases, 'CCAA')
          
    def test_invalid(self):
        self.assertRaises(Exception, run_parser, ["This is completed illegal!"])
    
    def test_comment(self):
        self.assertEqual(len(run_parser(["# a comment", "", "7 A"])), 1)
        
if __name__ == '__main__':
    unittest.main()
