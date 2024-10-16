import os.path
from datetime import datetime

def save_benchmark(p, t):

    file = 'benchmarks_py.csv'
    if os.path.isfile(file):
        f = open(file, 'a')
        f.write('{},{},{:.20f}\n'.format(p, datetime.today().strftime('%Y-%m-%d'), sum(t.timings) / t.repeat))
        f.close()
    else:
        f = open(file, 'w')
        f.write('Problem,Date,Benchmark\n')
        f.write('{},{},{:.20f}\n'.format(p, datetime.today().strftime('%Y-%m-%d'), sum(t.timings) / t.repeat))
        f.close()
