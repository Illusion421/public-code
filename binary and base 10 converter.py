import math
import itertools
import Cython
def binary_to_base10(num):
    print("\n--------------------------------------------")
    print("binary to base 10 / decimal conversion:\n")
    print("binary sequence:" , num)
    num = num[::-1]
    each_bit = []
    answer = []
    each_bit.append(1)

    for i in range(len(num)):
        each_bit.append(each_bit[i]*2)
        if num[i] != "0":
            answer.append(each_bit[i])
            print("current answer: " , answer)
    print("base 10 / decimal value:" , sum(answer))


def base10_to_binary(num):
    print("\n--------------------------------------------")
    print("decimal to binary conversion:\n")

    print("base 10 / decimal value:" , num)
    #str to int conversions
    num = int(num)
    num_to_find = int(num)
    #-------------------------------------------------------

    # finds the numbers that will represent each bit number in the binary sequence (1, 2, 4, 8, 16) etc
    each_bit = []
    each_bit.append(1)
    for i in range(num):
        each_bit.append(each_bit[i]*2)
    print("each bit:" , each_bit[:20])
    #---------------------------------------------------------------------------------

    # finds which numbers add up (from the each_bit list ) to the parameter called num
    # finds the numbers that will be used in log calculations
    numbers_for_log_cal = []
    result  = []
    for i in range(len(each_bit), 0, -1):
        for seq in itertools.combinations(each_bit, i):
            if sum(seq) == num:
                numbers_for_log_cal.append(list(seq))
    print("Numbers for log calculations:" , numbers_for_log_cal)
    #-------------------------------------------------------------------------------

    # finding the values of the logs and using them to find the binary sequence
    log_values = []
    for x in range(len(numbers_for_log_cal)):
        line = numbers_for_log_cal[x]
        for i in range(len(line)):
            value = math.log(line[i] , 2)
            value = int(value)
            # tells me the positions of where the zeros are in the binary sequence
            log_values.append(value)
        print("log values:" , log_values)
    #-------------------------------------------------------------------------------

    #assembling the binary ssequence
    sequence = []
    print("the max value of the log_values is :" , max(log_values))
    for i in range(max(log_values) +1):
        sequence.append(0)
    # need to out the correct elements of the log_values in the right place in the sequence
    for i in range(len(log_values)):
        sequence[log_values[i]] = 1

    # to output the binary sequence as a string and not a list
    str_seq = ''
    for i in range(len(sequence)):
        str_seq += ''.join(str(sequence[i]))
    str_seq = str_seq[::-1]
    print("binary sequence:" , str_seq)

    #-----------------------------------------------------------------------------

# subtracting binary numbers---------------------------------------------------------
def subtracting_binary_nums(num1 , num2):
    print("\nAdding binary numbers:\n")
    output = []
    answer = ''
    nums = []
    amount_of_zeros_to_add= 0
    if len(num1) != len(num2):
        amount_of_zeros_to_add = len(num1) - len(num2)
    for i in range(len(num1)):
        nums.append(num2[i])
        num2 += ''.join(nums[i])
    if amount_of_zeros_to_add > 0:
        nums.insert(0 , "0" * (amount_of_zeros_to_add))
    num2 = ""
    for i in range(len(nums)):
        num2 += ''.join(str(nums[i]))

    print("num1: " , num1)
    print("num2: " , num2)

    for i in range(len(num1)):
        if num1[i] == "1" and num2[i] == "1":
            ans = "0"
            output.append(ans)
        elif num1[i] == "0" and num2[i] == "0":
            ans = "0"
            output.append(ans)
        elif num1[i] == "1" and num2[i] == "0":
            ans = "1"
            output.append(ans)
        elif num1[i] == "0" and num2[i] == "1":
            output[i-1] = 0
            ans = "1"
            output.append(ans)

    for i in range(len(output)):
        answer += ''.join(str(output[i]))

    print("\nAnswer: " , answer)

#adding binary numbers ---------------------------------------------------
def add_binary_nums(num1, num2):
    print("\nAdding binary numbers:\n")

    nums = []
    amount_of_zeros_to_add = 0
    if len(num1) != len(num2):
        amount_of_zeros_to_add = len(num1) - len(num2)
    for i in range(len(num1)):
        nums.append(num2[i])
        num2 += ''.join(nums[i])
    if amount_of_zeros_to_add > 0:
        nums.insert(0 , "0" * (amount_of_zeros_to_add))
    num2 = ""
    for i in range(len(nums)):
        num2 += ''.join(str(nums[i]))

    print("nums1: " , num1)
    print("nums2: " , num2)

    ans = ''
    for i in range(len(num1)):
        if num1[i] == "1" and num2[i] == "1":
            ans += "10"
        elif num1[i] == "0" and num2[i] == "0":
            ans += "0"
        elif num1[i] == "0" and num2[i] == "1" or num2[i]:
            ans += "1"
        elif num1[i] == "1" and num2[i] == "0" or num2[i]:
            ans += "1"
    print("\nAnswer:" , ans)
#---------------------------------------------------------------------------------

#example testcases
# converting binary to base 10
'''
input:
binary_to_base10("10011011")

output:
155
'''

# converting base 10 to binary
'''
input:
base10_to_binary(155)

output:
10011011
'''

# adding binary numbers
'''
input:
add_binary_nums("100110","110101")

output:
10101011
'''

'''
input:
subtracting_binary_nums("111010", "10101")

output:
100101
'''
