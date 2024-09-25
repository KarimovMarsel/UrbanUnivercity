#1.
def print_params (a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
#print_params(1, 2, 3, 4)
print_params(b = 25)
print_params(c = [1,2,3])
#2.
values_list = (1, 'Привет', True)
values_dict = {'a': 12, 'b': 'Hello', 'c': False}
print_params(*values_list)
print_params(**values_dict)
#3.
values_list_2 = [23, 'word']
print_params(*values_list_2, 42)
