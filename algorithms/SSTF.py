import numpy as np


def sstf(arr, current_position):
    # Variable to store movement
    movement = 0
    # making a temp array beause dont want to mess original array
    temp=arr.copy()
    # loop through the array
    for i in range(len(arr)):

        array = np.asarray(temp)
        near_value_index = (np.abs(array - current_position)).argmin()
        next_position = array[near_value_index]

        # Check whether it is to the right or to the left.

        # if to the right meaning next near location is greater than correct
        if current_position > next_position:
            distance = current_position - next_position
            movement = movement + distance
            current_position = next_position

        # if to the left meaning next near location is smaller than correct
        if current_position < next_position:
            distance = next_position - current_position
            movement = movement + distance
            current_position = next_position

        # if same location is repeating just make no changes and proceed to remove it
        if current_position == next_position:
            current_position = next_position

        # remove the position which is already been accessed and repeat it for the next values
        temp.remove(next_position)
    return movement

