import os.path
from datetime import datetime

def save_benchmark(p, t):

    benchmark = (sum(t.timings) / t.repeat) * 10**9 # convert seconds to nanoseconds

    file = 'benchmarks_py.csv'
    if os.path.isfile(file):
        f = open(file, 'a')
        f.write('{},{},{:.20f}\n'.format(p, datetime.today().strftime('%Y-%m-%d'), benchmark))
        f.close()
    else:
        f = open(file, 'w')
        f.write('Problem,Date,Python\n')
        f.write('{},{},{:.20f}\n'.format(p, datetime.today().strftime('%Y-%m-%d'), benchmark))
        f.close()
