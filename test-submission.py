import sys
import os
import subprocess
import signal
import time

from glob import glob

# max time in seconds to wait for the submission to run on an input
TIME_OUT = 2

class TestCode(object):
    
    def __init__(self, executable_file, input_file):
        self.status = "Queued"
        self.exe = executable_file
        self.input_file = input_file
        self.runtime = None
        self.output = None
        self.correct = None

    def run(self):
        try:
            start = time.time()
            if self.exe[-2:] == 'py':
                self.output = subprocess.check_output(
                    'python %s < %s' % (self.exe, self.input_file),
                    shell=True, timeout=TIME_OUT)
            elif self.exe[-5:] == 'class':
                self.output = subprocess.check_output(
                    'java -Xmx2g -Xss256m %s < %s' % (self.exe[:-6],
                    self.input_file), shell=True, timeout=TIME_OUT)
                
            else:
                self.output = subprocess.check_output(
                    './%s < %s' % (self.exe, self.input_file),
                    shell=True, timeout=TIME_OUT)
            end = time.time()
            self.status = 'Ran'
            self.runtime = int(1000*(end - start))
            self.output = self.output.decode('utf-8').strip()
            self.grade()
        except subprocess.TimeoutExpired:
            self.status = "Timeout"

    def grade(self):
        try:
            output_file = open(self.input_file.replace('input', 'output'), 'r')
        except FileNotFoundError:
            return

        correct_output = output_file.read().strip()
        if correct_output == self.output:
            self.status = 'Correct'
        else:
            self.status = 'Incorrect'

    def __str__(self):
        if self.status == 'Correct':
            return '. %s (%i ms)' % (self.input_file, self.runtime)
        elif self.status == 'Incorrect':
            return 'X %s (%i ms)' % (self.input_file, self.runtime)
        elif self.status == 'Ran':
            return '? %s (%i ms)' % (self.input_file, self.runtime)
        elif self.status == 'Timeout':
            return '! %s (>%i ms)' % (self.input_file, 1000*TIME_OUT)

    def __repr__(self):
        if self.status == 'Ran':
            return '<Ran %s on %s in %s ms>' % \
                (self.exe, self.input_file, self.runtime)
        return '<%s: %s on %s>' % (self.status, self.exe, self.input_file)

if __name__ == '__main__':
    f_name = sys.argv[1]
    tests = []
    for input_file in glob('tests/input*'):
        tests.append(TestCode(f_name, input_file))

    print('Running %i tests on %s\n' % (len(tests), f_name))
    print('. | Correct output')
    print('X | Incorrect output')
    print('? | No solution to check against')
    print('! | Timed out\n')

    for test in tests:
        test.run()
        print(test)

    for test in tests:
        if test.status == 'Incorrect':
            print()
            print('Output of %s' % test.input_file)
            print(test.output)



