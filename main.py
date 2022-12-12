#bubblesort - biggest number to the right 

i = 0
array_of_numbers = [4,9,2,1]
number_of_items_in_array = len(array_of_numbers)
number_of_items_in_array = number_of_items_in_array - 1

while i < number_of_items_in_array:
        j = 0   #this is the reset for j
        while j < number_of_items_in_array:
            # traverse the array from 0 to 8 
            # Swap bigger number to the right
            if array_of_numbers[j] > array_of_numbers[j+1]:
                print("i is now", i,"j is now", j)
                print("index of j is bigger than index of j+1", array_of_numbers[j], array_of_numbers[j+1])
                tem_storage = array_of_numbers[j]
                print("store index of array_of_numbers[j] the bigger number into tem_storage", tem_storage)
                array_of_numbers[j] = array_of_numbers[j+1]
                print("store index of array_of_numbers[j+1] into array_of_numbers[j]", array_of_numbers[j], array_of_numbers[j+1]) 
                array_of_numbers[j+1] = tem_storage
                print("store index of array_of_numbers[j+1] into index of array_of_numbers[j]", array_of_numbers[j+1], array_of_numbers[j]) 
                print("array of numbers is now", array_of_numbers)
                print("")
                print("increase j by 1 from", j, "to", j+1) 
                j = j + 1
            else:
                j = j + 1

        i = i + 1  #This is to move the i