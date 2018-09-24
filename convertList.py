# with user input:

def convert(list_item):
    list_item[-1] = 'and '+str(list_item[-1])
    new_str = ''
    new_str = ', '.join(str(item) for item in list_item)
    return new_str

user_list = input('Hello dear, enter your list to convert it to string: ').split() #convert user input to list
print('your list is: ')
print(user_list)
print('your string is: ')
print(convert(user_list))

# without user input

"""
def convert():
    list_item = ['apples', 'bananas', 'tofu', 'cats']
    list_item[-1] = 'and '+str(list_item[-1])
    new_str = ''
    new_str = ', '.join(str(item) for item in list_item)
    print(new_str)

convert()
"""
