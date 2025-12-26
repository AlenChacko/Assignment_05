# original list
original_list=[1,2,3,4,5,6,7,8,9,10]
extract_limit=5

# extracting first 5 elments
def extract_list(lst,lim):
    return lst[0:lim]

# reversing the extracted list
def reverse_list(lst):
   return lst[::-1]

# calling the list extracting function and passing orginal list and limit
extracted_list=extract_list(original_list,extract_limit)

# calling extracted list reversing function and passing extracted list
reversed_list=reverse_list(extracted_list)

# printing values
print(f"Original list:{original_list}")
print(f"Extracted first five elements:{extracted_list}")
print(f"Reversed extracted elements:{reversed_list}")
