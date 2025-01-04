import csv

#This makes sure it's not the same number and that the distance between levels is safe
def conditions(levels):
        for i in range(len(levels) - 1):
            if abs(int(levels[i]) - int(levels[i + 1])) < 1 or abs(int(levels[i]) - int(levels[i + 1])) > 3:
<<<<<<< HEAD
                    return False
=======
                return False
>>>>>>> 0225e51a559a457f932a518201327e88a2735984
        return True
#This makes sure that its only going up or down, not both
def trend(levels):
    increase = True
    decrease = True
<<<<<<< HEAD
=======

>>>>>>> 0225e51a559a457f932a518201327e88a2735984
    for i in range(len(levels) - 1):
        if int(levels[i]) <  int(levels[i+1]):
            decrease = False #its increasing
        elif int(levels[i]) >  int(levels[i+1]):
            increase = False #its decreasing
<<<<<<< HEAD
    return increase or decrease

#Read each line into a list, checking elements of the list as we go
safeFloors = 0
=======
    
    return increase or decrease

#Read each line into a list, checking elements of the list as we go
count = 0
>>>>>>> 0225e51a559a457f932a518201327e88a2735984
with open('aoc2025-d2.txt', 'r') as file:
    for line in file:
        levels = line.split()
        #We want to check both necessities
        t1 = conditions(levels)
        t2 = trend(levels)
        if t1 and t2:
<<<<<<< HEAD
            safeFloors += 1
        else:
            safe = False
            for i in range(len(levels)):
                temp_levels = levels[:i] + levels[i+1:]
                if conditions(temp_levels) and trend(temp_levels):
                        safe = True
            if safe == True:
                    safeFloors += 1
print(safeFloors)
=======
            count += 1
print(count)
>>>>>>> 0225e51a559a457f932a518201327e88a2735984
