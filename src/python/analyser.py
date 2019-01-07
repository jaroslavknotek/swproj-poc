from itertools import groupby
from operator import itemgetter
from functools import reduce

def histogram_of_counts(records):
    mapped = map(lambda rec: (len(rec.text.split()),1), records)
    histo_data = [(k, sum([vv for kk, vv in v])) for k, v in groupby(sorted(mapped), key=itemgetter(0))]

    return  histo_data

