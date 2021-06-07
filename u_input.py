def isint(x):
    isint = True
    try:
        int(x)
    except:
        isint = False
    finally:
        return isint


def boolean(output_true=None, output_false=None, question=None):
    """
    output_true : the option for returning True
    output_false : the option for returning False
    question : The text added before the input
    """
    i = ''
    # if blank setting variables to defaults up defaults
    if output_true is None:
        output_true = 'y'
    if output_false is None:
        output_false = 'n'
    if question is None:
        question = ()
    # printing the requested question if it exists
    else:
        print(question)
    # getting user input and verifying that it is valid
    while i not in [output_true, output_false]:
        i = input(f'({output_true}/{output_false})_?')
    # sorting
    if i == output_true:
        return True
    elif i == output_false:
        return False


def number_only(*question):
    i = ''
    while not i.isdigit():
        i = input(f'{str(*question)}_?')
    return int(i)


def alpha_only(*question):
    i = '1'
    while not i.isalpha():
        i = input(f'{str(*question)}_?')
    return i


def int_only(*question):
    i = ''
    loop = True
    while not isint(i):
        i = input(f'{str(*question)}_?')
    return int(i)
