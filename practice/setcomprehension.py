#create an ouput set which contain only even no 
#discard dublicate value without set comprehension
input_list=[1,2,3,4,4,5,5,6,7,8,7,9,8,9,2,3,4]
output_set=set()

#using loop for constructing output set
for var in input_list:
    if var%2==0:
        output_set.add(var)
print("output set using for loop:", output_set)

#with set comprehension
input_list=[1,2,3,4,4,5,5,6,7,8,7,9,8,9,2,3,4]
set_using_comp={var for var in input_list if var % 2==0}
print("output set using set comprehension:",set_using_comp)