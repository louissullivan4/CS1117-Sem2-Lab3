# ScriptName: functions.py
# Author: Louis Sullivan 119363083

# Q1:
def power():
    return [i * i for i in range(1, 6) if i % 2 == 0]


# Q2:
# def F(s1, s2):
#     r = []
#     for e1 in s1:
#         for e2 in s2:
#             if e1 == e2:
#                 r += [e1]
#                 break
#     return r

def F(s1, s2):
    r = []
    e1 = 0
    e2 = 0
    while e1 < len(s1):
        while e2 < len(s2):
            if s1[e1] == s2[e2]:
                r += [s1[e1]]
                break
            e2 += 1
        e1 += 1
    return r


# Q3:

def reducedFeeEntitlement(d):
    i = 0
    j = []
    for key, values in d.items():
        i = len(values)
        if i < 2:
            j.append(key)
    return j


def commmonModules(d, s1, s2):
    r = []
    for e1 in d[s1]:
        for e2 in d[s2]:
            if e1 == e2:
                r += [e1]
                break
    return r


# Q4:
def iter_factorial(n):
    repeat_number = 1
    while n >= 1:
        repeat_number = repeat_number * n
        n -= 1
    return repeat_number


# Q5:
def fizz():
    i = 0
    while i < 100:
        if i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        elif i % 5 == 0 and i % 3 != 0:
            print("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        i += 1
        print(i)