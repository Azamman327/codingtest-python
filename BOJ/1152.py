input_str = input()

new_str = input_str.split(' ')
if new_str[0] == '':
    new_str.pop(0)
if new_str[-1] == '':
    new_str.pop(-1)

print(len(new_str))