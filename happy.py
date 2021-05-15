# find all possible contiguous partitions of a list
# eg [1,2,3,4] = [[[1,2,3,4]], [[1],[2,3,4]], [[1],[2,3],[4]], [[1],[2],[3,4]], etc
# think of list slice points as a set of slots
# 1 _ 2 _ 3 _ 4
# number of slice points is len(list) - 1
# a particular partition can be represented as a binary number
# 001 means fill slice first slot 1 x 2 _ 3 _ 4 -> [[1],[2,3,4]]
# 101 means slice first and third slot 1 x 2 _ 3 x 4 -> [[1],[2,3],[4]]
# we can represent this slice set as a decimal number, so 001 = 1, 101=5
# so 2**(len-1) is the number of possible partitions and the range
# 0..2**(len-1) represents each of those partitions
# we iterate over each possible partition by just iterating over the numbers
# we slice the array at each slice point if the bitwise AND of the slot and
# 2**(slot_number)  is non-zero


def partition_list(a_list):
    partitions = [[a_list]]
    for n in range(1, 2 ** (len(a_list) - 1)):
        partition_set = []
        last_slice = 0
        for m in range(len(a_list) - 1):                       # iterate over powers of 2
            if (2 ** m & n) > 0:                               # bitwise compare to slice
                partition_set.append(a_list[last_slice:m + 1])
                last_slice = m + 1
        partition_set.append(a_list[last_slice:])
        partitions.append(partition_set)
    return partitions


def happiness(lists):
    maximum = 0
    minimum = 20000
    for partition in lists:
        partition_happy = 0
        for subarray in partition:
            happy = subarray[0]
            for i in range(1, len(subarray)):
                happy = happy ^ subarray[i]
            partition_happy += happy
        if partition_happy < minimum:
            minimum = partition_happy
        if partition_happy > maximum:
            maximum = partition_happy
    return maximum, minimum


count = int(input())
arrayray = []
for i in range(count):
    arrayray.append(int(input()))

partitions = partition_list(arrayray)
maximum, minimum = happiness(partitions)
print(maximum - minimum)

# problem
# A Stanford researcher has been trying to figure out a new way to measure the happiness of undergraduate students. They surveyed N students and stored their reported happiness levels in an array.
#
# You are given an array of size N with integer values. We want to partition the array into one or more contiguous subarrays. The happiness level of a partition is the sum of the bitwise XOR of the numbers in each subarray. We want to compute the maximum happiness and the minimum happiness possible with this array. Output the difference between these values.
#
# Definitions: A subarray is defined as a contiguous segment of an array. In array: [4, 3, 7, 2, 1] some subarrays are [4, 3, 7] and [7, 2]. [4, 2, 1] is not a subarray.
#
# The bitwise XOR (Exclusive Or), is an operator similar to addition. However, it is performed on each bit of a number. For each bit in a number, the XOR of the two bits are 0, if the arguments are the same, else the XOR is 1. XOR(0,0) = 0 XOR(1,1) = 0 XOR(1,0) = 1 XOR(0,1) = 1
#
# Input
# The first line of input holds a single integer N (1≤N≤10,000). The next N lines each contain a single value vi (1≤vi≤220), which are the values in the array.
#
# Output
# Print, on a single line, an integer representing the difference between the minimum happiness and the maximum happiness attainable.
#
# Examples
# inputCopy
# 4
# 2
# 8
# 12
# 4
# outputCopy
# 24
# inputCopy
# 10
# 489
# 104
# 776
# 546
# 557
# 322
# 37
# 408
# 620
# 620
# outputCopy
# 3846
