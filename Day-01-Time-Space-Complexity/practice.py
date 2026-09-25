# Day 1 - Practice

# Try to identify the Time Complexity and Extra Space Complexity
# for each function before checking the answers at the bottom.


# Q1
def question_1(arr):
    return arr[0]


# Q2
def question_2(arr):
    for item in arr:
        print(item)


# Q3
def question_3(arr):
    for i in arr:
        for j in arr:
            print(i, j)


# Q4
def question_4(arr):
    for x in arr:
        print(x)

    for y in arr:
        print(y)


# Q5
def question_5(n):
    i = 1
    while i < n:
        i *= 2


# Q6
def question_6(n):
    result = []
    for i in range(n):
        result.append(i)
    return result


# Q7
def question_7(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)


# Q8
def question_8(n):
    i = n
    while i > 1:
        i //= 2


# ANSWERS
# Q1: Time O(1), Extra Space O(1)
# Q2: Time O(n), Extra Space O(1)
# Q3: Time O(n^2), Extra Space O(1)
# Q4: Time O(n), Extra Space O(1)
# Q5: Time O(log n), Extra Space O(1)
# Q6: Time O(n), Extra Space O(n)
# Q7: Time O(n^3), Extra Space O(1)
# Q8: Time O(log n), Extra Space O(1)
