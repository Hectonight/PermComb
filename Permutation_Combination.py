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
    while True:
        val = input(f'{var} = ')
        try:
            if int(val) >= 0:
                return int(val)
            else:
                print(f'Input a positive integer for {var}')
                continue
        except:
            print(f'Input a positive integer for {var}')
            continue


def get_values():  # defining get_values and its parameters
    while True:
        n_val = values('n')
        r_val = values('r')
        if n_val >= r_val:
            return {
                'n': n_val,
                'r': r_val
            }
        else:
            print('n must be greater than r')


choice = ''  # defining choice
perm_choice = ['P', 'p', 'permutation', 'Permutation']  # a list of possible choices for permutation
comb_choice = ['C', 'c', 'combination', 'Combination']  # a list of possible choices for combination

while choice not in perm_choice + comb_choice:  # run this loop until choice equals a value in the combine lists
    choice = input('P or C?\n')  # prints this message and choice will be equal to the user input as a string
    if choice not in perm_choice + comb_choice:  # if choice not equal to value in combined lists
        print('Please choose either P or C')  # prints this messgage

if choice in perm_choice:
    print('P(n,r)')
    var_val = get_values()
    output = permutation(var_val['n'], var_val['r'])
else:
    print('C(n,r)')
    var_val = get_values()
    output = combination(var_val['n'], var_val['r'])

print(output)
