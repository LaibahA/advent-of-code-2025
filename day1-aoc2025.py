import csv

list1 = []
list2 = []
#Reads all the numbers into two lists
with open('aoc2025-d1.txt', 'r') as file:
    for line in file:
        nums = line.split()

        list1.append(int(nums[0]))
        list2.append(int(nums[1]))
        
#Sort both lists
list1.sort()
list2.sort()

#Iterate through lists and compute sum
sum = 0
for i in range(len(list1)):
    distance = abs(list1[i]-list2[i])
    sum+= distance

#This prints the final distance between the pairs of points
print(sum)

#Part 2

#Efficient: Make hashmap, key is unique number, value is amt of times been updated

sum = 0 #Similarity score
count = 0
#Go through each item from list 1
for i1 in list1:
    #For each item in list2, compare it
    for i2 in list2:
        #If its the same, increase count
        if i1 == i2:
            count+=1
    #Add the count times the actual number to the similarity score
    sum += i1*count
    count = 0

#This will print the similarity score
print(sum)
        
    

    
