#Collect data from text file, process and put into array
#Sort the array in ascending order from left to right of values

total_calories = 0    #to count total calories each elf carry.
with open('input.txt') as file:
  data = [i for i in file.read().strip().split("\n")]
 
array_of_calories = []
num_of_elf = 0
total_calories = 0

for item in data:
   if item == "":
       array_of_calories.append(total_calories) 
       total_calories = 0
       num_of_elf = num_of_elf + 1
       
   else:
       num = int(item)
       total_calories = total_calories + num

array_of_calories.append(total_calories) 
total_calories = 0

#bubblesort - biggest number to the right 
i = 0


while i < num_of_elf:
    j = 0   #this is the reset for j
    while j < num_of_elf:   #(4)
             # traverse the array from 0 to num_of_elf
            # Swap bigger number to the right
            
            if array_of_calories[j] > array_of_calories[j+1]:
                tem_storage = array_of_calories[j]
                array_of_calories[j] = array_of_calories[j+1] 
                array_of_calories[j+1] = tem_storage
                print("j inside for loop",j)
                j = j + 1
            else:
                j = j + 1

    i = i + 1  #This is to move the i

answer = array_of_calories[num_of_elf] + array_of_calories[num_of_elf-1] + array_of_calories[num_of_elf-2] 

ans = array_of_calories[num_of_elf]

print("anser_part_1 is",ans)
print("answer_part_2 is", answer)