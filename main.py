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


   else:
       num = int(item)
       total_calories += num

print(array_of_calories)

#bubblesort - biggest number to the right 
i = 0

for i < num_of_elf:
        j = 0   #this is the master reset for j
for j < num_of_elf:   #(4)
             # traverse the array from 0 to num_of_elf
            # Swap bigger number to the right

    if array_of_calories[j] > array_of_calories[j+1]:
                tem_storage = array_of_calories[j]
                array_of_calories[j] = array_of_calories[j+1] 
                array_of_calories[j+1] = tem_storage
                j = j + 1
    else
                j = j + 1

#must line a line here to tell Python that this is the end of the FOR loop

           i = i + 1  #This is to move the i

answer = array_of_calories[num_of_elf] + array_of_calories[num_of_elf-1] + array_of_calories[num_of_elf-2] 
print(answer)