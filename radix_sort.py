# Radix sort 

# using counting sort to sort the elements in the basis of significant places
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # calculate acumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


# implementation of radix sort
def radixSort(array):
    # get maximum element
    max_element = max(array)

    # apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10
 
 
# function check
values = [170, 45, 75, 90, 802, 24, 2, 66]
 
# function Call
radixSort(values)
 
for i in range(len(values)):
    print(values[i])