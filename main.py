from algorithms import FCFS, CSCAN, CLOOK
from algorithms import SSTF
from algorithms import SCAN
from algorithms import LOOK

#
# arr = [4512, 120, 1977, 3675, 3890, 2251, 1028, 785, 2001, 4118]
# current_position = 1802
# max_cylinders=5000


cylinders = int(input("Enter size of Disk : "))

current_position = int(input("Enter Current Head Location : "))

arr = []
# number of elements as input
number_of_requests = int(input("Enter number of total requests : "))

# iterating till the range
for i in range(0, number_of_requests):
    requeest_prompt = "Enter your Request Location Number " + str(i+1) +" :"
    request_location = int(input(requeest_prompt))

    arr.append(request_location)

fcfs_distance = FCFS.fcfs(arr, current_position)
sstf_distance =SSTF.sstf(arr, current_position)
scan_distance =SCAN.scan(arr, current_position, cylinders)
look_distance =LOOK.look(arr, current_position)
cscan_distance =CSCAN.cscan(arr, current_position, cylinders)
clook_distance =CLOOK.clook(arr,current_position)

print("Distance for FCFS= ", fcfs_distance)
print("Distance for SSTF= ", sstf_distance)
print("Distance for SCAN= ", scan_distance)
print("Distance for LOOK= ", look_distance)
print("Distance for CSCAN= ", cscan_distance)
print("Distance for CLOOK= ", clook_distance)


