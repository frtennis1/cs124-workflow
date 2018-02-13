import random

size = 10
minNum = 1
maxNum = 100

#################################################
## Generate your test cases by creating random numbers 
## This one generates list of 'size' length from minNum to maxNum
#################################################
def generate_data(size, minNum, maxNum):
    randomNums = []
    for i in range(minNum, maxNum):
        my_randoms.append(random.randrange(minNum, maxNum + 1, 1))

    #or do this without a loop
    randomNums = random.sample(xrange(minNum, maxNum + 1), size)

    return randomNums

#################################################
## Implement your function in do_something, 
## that takes in input list and outputs the result
#################################################

#this one adds 1 to every element of the list
def do_something(inputList):
    result = []
    for i in inputList:
        result.append(inputList[i] + 1)

    return result

#################################################
## Put them together
#################################################
def test_function(size, minNum, maxNum):
    sample_input = generate_data(size, minNum, maxNum)
    return do_something(sample_input)

#read input, say it was a list of ints
inputs = int(raw_input())
input_list = inputs.split()