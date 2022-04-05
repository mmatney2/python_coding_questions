#Question 1

def hello_name(user_name):
    return ("Hello_" + user_name)
print(hello_name('USERNAME'))

#Question 2

def first_odds():
    for numbers in range(1, 100):
        if numbers % 2 == 1:
            print(numbers)
    return numbers
#odds = first_odds()
#print(odds)

#Question 3

def max_num_in_list(a_list):
    """Print max number in the list"""
    return max(a_list)
    
max_in_list = [1,2,3,6,4]
print(max_num_in_list(max_in_list))

#Question 4
def is_leap_year(a_year):
    if (a_year % 4 == 0) and (a_year % 100 != 0):
        a_year = True
    elif (a_year % 400 == 0):
        a_year = True
    else:
        a_year = False
    return a_year
leap_year = is_leap_year(300)
print(leap_year)


#Question 5
def is_consecutive(a_list):
    """list if it's consecutive. If not, don't print"""
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))


new_list = [1,2,3]       
print(is_consecutive(new_list))

print(5//2)

        

