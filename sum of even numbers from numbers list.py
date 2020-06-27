

#Make a list of all the numbers
numbers=[1,12,14,56,19,77,76]

#Make an empty list for even numbers to be stored later
even_list=[]
#using for loop for each member of the list
for num in numbers:
    if num % 2 == 0: #it means that the remainder after the number divides by 2 is 0
        even_list.append(num) # it will store only the even numbers from number list into the even list
print("This is the sum of all even numbers: ", sum(even_list))




