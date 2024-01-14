number_of_rooms=int(input())
rooms=[]
free_chairs=0
needed_chairs_in_rooms=[]
num_needed_chairs_in_rooms=[]
for i in range(number_of_rooms):
    current_room=input()
    rooms.append(current_room)
for j in range(len(rooms)):
    string=rooms[i].split(' ')
    chairs_current_room=len(string[0])
    needed_chairs=string[1]
    if chairs_current_room<needed_chairs:
        needed_chairs_in_rooms.append(str(i+1))
        num_needed_chairs_in_rooms.append(str(needed_chairs-chairs_current_room)
        free_chairs=0
    else:
        free_chairs+=chairs_current_room-needed_chairs
if free_chairs==0:
    for k in range(len(needed_chairs_in_rooms)):
