def partition_list(a_list):
    partitions = [[a_list]]
    for n in range(1, 2 ** (len(a_list) - 1)):
        partition_set = []
        last_slice = 0
        for m in range(len(a_list) - 1):
            if (2 ** m & n) > 0:
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
