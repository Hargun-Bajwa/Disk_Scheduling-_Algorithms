from algorithms import FCFS
def scan(arr, current_position, max_cylinders):
    # divide the arr into two small arrays
    # if small to smaller_values_array
    # else to larger_values_array

    #  New array to store the order in which the values must be stored
    order = []

    # initiate both
    smaller_values_array = []
    larger_values_array = []

    # add last cylinder value as it will be used to larger_values_array array
    larger_values_array.append(max_cylinders - 1)
    # make both arrays to have values from original arrays if greater to larger_values_array else to smaller_values_array
    for i in range(len(arr)):
        if arr[i] > current_position:
            larger_values_array.append(arr[i])
        else:
            smaller_values_array.append(arr[i])

    # sort the two arrays
    # smaller_values_array on to be opposite because that is how we are going to access locations of it
    smaller_values_array.sort(reverse=True)
    larger_values_array.sort()
    #  fo till the end doing the requested locations
    for i in range(len(larger_values_array)):
        order.append(larger_values_array[i])
    for i in range(len(smaller_values_array)):
        order.append(smaller_values_array[i])


    # implement FCFS on the ordered array now
    return FCFS.fcfs(order, current_position)

