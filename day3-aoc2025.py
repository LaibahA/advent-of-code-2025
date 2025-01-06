totalSum = 0 #Total sum
#Read through text while searching for the instructions
with open('aoc2025-d3.txt', 'r') as file:
    text = file.read()
    index = 0
    while index != -1:
        index = text.find("mul(", index) #Find "mul("
        if index != -1:
            index += 4 #we want to skip over "mul("
            factor1 = "" #Left hand of multiplication
            while index != -1 and text[index].isdigit(): #Intake numbers
                factor1 += text[index]
                index += 1
            if len(factor1) <= 3 and index < len(text) and text[index] == ",":
                index+=1 #Skip comma
                factor2 = "" #Right hand of multiplication
                while index != -1 and text[index].isdigit(): #Intake numbers
                    factor2 += text[index]
                    index += 1
                if len(factor2) <= 3 and index < len(text) and text[index] == ")":
                    index += 1 #Skip closing parenthesis
                    if factor1 and factor2 and len(factor1) <= 3 and len(factor2) <=3:
                        totalSum += int(factor1) * int(factor2)

            
print(totalSum)
    

