import random
from test import random_transcription
from codon_timing import nth_codon

timings = [random.uniform(0, 6) for i in range(64)]
transcriptions = [random_transcription(timings) for i in range(400)]

print('# Auto-generated input file. This is not real data.')
print('# The following timings were used to generate this:')
print('#')
for (i, timing) in enumerate(timings):
    print('# %s: %f' % (nth_codon(i), timing))
print('')

for i in range(400):
    t = random_transcription(timings)
    print('%f %s' % (t.time, t.bases))
