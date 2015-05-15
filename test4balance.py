#!/usr/bin/env python
#stolen from hackerrank.com





passing_test = [ 1, 2, 3, 3]
failing_test = [ 1, 2, 3 ]
longer_passing_test = [1, 7, 8, 0, 5, 3]
longer_failing_test = [1, 5, 11, 16]

#quadratic
def balance_point( a_ints ):
    for pos in range(len(a_ints)):
        a_left = a_ints[:pos]
        a_right = a_ints[pos+1:]
        if sum(a_left) == sum(a_right):
            return True
    return False
        #add all the positions to the left of bp 
        #add all the positions to the right of bs
        #if they equal each other true
        
# Still quatratic because we ahve a loop in a loop, but it's half the work
def somewhat_faster_bp(a_ints):
    total = sum(a_ints) 
    for pos in range(len(a_ints)):
        a_left = a_ints[:pos]
        sum2theleft = sum(a_left)
        sum2theright = total - a_ints[pos] - sum2theleft
        if sum2theright == sum2theleft:
            return True
        #total - bp - sum to the left
    return False

# linear
def alarics_faster_bp(a_ints):
    total = sum(a_ints) 
    sum2theleft = 0
    for pos in range(len(a_ints)):
        if pos > 0:
            sum2theleft = sum2theleft + a_ints[pos-1]
        sum2theright = total - a_ints[pos] - sum2theleft
        if sum2theright == sum2theleft:
            return True
        #total - bp - sum to the left
    return False

# linear
def faster_bp(a_ints):
    total = sum(a_ints) 
    sum2theleft = 0
    for val in a_ints:
        sum2theright = total - val - sum2theleft
        if sum2theright == sum2theleft:
            return True
        sum2theleft = sum2theleft + val
    return False

if faster_bp(passing_test):
    print 'faster passing_test Passed!'
else:
    print 'faster passing_test Failed'


if not faster_bp(failing_test):
    print 'faster failing_test Passed!'
else:
    print 'faster failing_test Failed... you suck'

if balance_point(passing_test):
    print 'passing_test Passed!'
else:
    print 'passing_test Failed'


if not balance_point(failing_test):
    print 'failing_test Passed!'
else:
    print 'failing_test Failed... you suck'

if balance_point(longer_passing_test):
    print 'longer_passing_test Passed!'
else:
    print 'longer_passing_test Failed'

if not balance_point(longer_failing_test):
    print 'longer_failing_test Passed!'
else:
    print 'longer_failing_test Failed'

if faster_bp(longer_passing_test):
    print 'faster longer_passing_test Passed!'
else:
    print 'faster longer_passing_test Failed'

if not faster_bp(longer_failing_test):
    print 'faster longer_failing_test Passed!'
else:
    print 'faster longer_failing_test Failed'
