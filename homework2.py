def print_params(a=1, b='string', c=True):
    print(a, b, c)


print_params()
print_params(5, 'roma', False)
print_params(5)
print_params(5, 'roma')
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, 'element', False]
values_dict = {'a': 'slon', 'b': True, 'c': 3}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [False, 'Samoyed']
print_params(*values_list_2, 42)