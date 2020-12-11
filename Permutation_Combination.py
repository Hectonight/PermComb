import math  # importing the math module for the ability to use math.factorial()


def permutation(n: int, r: int):  # defining permutation and its parameters
    numerator = math.factorial(n)  # the numerator which is n!
    denomenator = math.factorial(n - r)  # the denominator which is (n - r)!
    return numerator // denomenator  # returns (numerator // denominator); used // instead of / to return as int


def combination(n: int, r: int):  # defining permutation and its parameters
    numerator = math.factorial(n)  # the numerator which is n!
    denomenator = math.factorial(r) * math.factorial(n - r)  # the denominator which is (n - r)!
    return numerator // denomenator  # returns (numerator // denominator); used // instead of / to return as int


def values(var: str):  # defining values and its parameters
    while True:  # create an infinite loop
        val = input(f'{var} = ')
        try:  # the try function will try to run the code below but it will test the except if there is an error
            if int(val) >= 0:
                return int(val)
            else:  # executes if the if statement above is false
                print(f'Input a positive integer for {var}')  # prints the string and the variable
                continue  # continues to the next iteration of the loop
        except ValueError:  # executes if there is an ValueError in the try function
            print(f'Input a positive integer for {var}')  # prints the string and the variable
            continue  # continues to the next iteration of the loop


def get_values():  # defining get_values and its parameters
    while True:  # create an infite loop
        n_val = values('n')  # n_val is equal to the output of values with attribute var equal to 'n'
        r_val = values('r')  # r_val is equal to the output of values with attribute var equal to 'r'
        if n_val >= r_val:
            return {  # returning this dictionary as the output; start of dictionary
                'n': n_val,  # creates key 'n' with value n_val
                'r': r_val  # creates key 'r' with value r_val
            }  # end of dictionary
        else:  # executes if the if statement above is false
            print('n must be greater than r')


choice = ''  # defining choice
perm_choice = ['P', 'p', 'permutation', 'Permutation']  # a list of possible choices for permutation
comb_choice = ['C', 'c', 'combination', 'Combination']  # a list of possible choices for combination

while choice not in perm_choice + comb_choice:  # run this loop until choice equals a value in the combine lists
    choice = input('P or C?\n')  # prints this message and choice will be equal to the user input as a string
    if choice not in perm_choice + comb_choice:  # if choice not equal to value in combined lists
        print('Please choose either P or C')  # prints this messgage

if choice in perm_choice:  # testing if choice is permutation
    print('P(n,r)')  # prints ths message
    var_val = get_values()  # var_val is equal to the output of the function get_values()
    output = permutation(var_val['n'], var_val['r'])
    # output is equal to the output of the function permutation with attribute n being the key 'n' in the dictionary
    # var_val and atrribute r being the value of
    # key 'r' in the dictionary
else:  # executes if the if statement above is false
    print('C(n,r)')  # prints ths message
    var_val = get_values()  # var_val is equal to the output of the function get_values()
    output = combination(var_val['n'], var_val['r'])
    # output is equal to the output of the function permutation with attribute n being the key 'n' in the dictionary
    # var_val and atrribute r being the value of
    # key 'r' in the dictionary

print(output)  # prints the variable output
