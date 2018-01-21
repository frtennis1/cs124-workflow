CS 124 Programming Problem Workflow
===================================

## Introduction

My workflow on programming problems used to be painfully inefficient. This repo
grew out of a desire to do better. It consists of a main script that runs tests
as well as some notes on setting up the workflow.

## Setting-up

Put input files to be tested in the `tests/` directory. These can take the form
of `tests/input<whatever you want>.txt`. I generally label them by number, but
short descriptive names are also possible so long as they begin with `input`. If
for an input file, there exists a corresponding output file whose name is the
same except that it begins with `output` instead of `input`, then the script
will check whether the output is correct. Otherwise, the script will not check
correctness.

## Running

To run the tests, run

```
python3 test-submission.py <submission>
```

If the submission is in Python, then `<submission>` is just the Python file. For
Java, it's the generated `class` file. Any executable will also work (such as a
C `.out` file). This prints out something like,

```
Running 2 tests on submission.out

. | Correct output
X | Incorrect output
? | No solution to check against
! | Timed out

X tests/input1.txt (9 ms)
? tests/input2.txt (6 ms)

Output of tests/input1.txt
6
```

Note that the output times are sensitive to the computer being run on, and carry
some overhead from the Python script, thus, they can only be used as rough
estimates.

