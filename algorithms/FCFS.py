# In FCFS, the first to arrive is first one to go ,
# Which means get next location
# move to it
# add to total

def fcfs(arr, current_position):
    # Total Movement done.
    movement = 0

    # distance between current position to next position
    distance = 0

    # The next position to move
    next_position = 0

    # loop through the array
    for i in range(len(arr)):
        #  next position will be the next place in array.
        next_position = arr[i]

        # find distance travelled
        distance = abs(next_position - current_position)

        # add it to total movement
        movement += distance

        # make current position of head to be at the accessed location
        current_position = next_position
    return movement
