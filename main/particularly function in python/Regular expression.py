''' wir use hier regular expression for spilt string in a python list '''
#Regular expression
import re
my_string = 'ahmad and him father is in Home'
x = re.split('i', my_string)
print(x)

my_string_list = list(['ahmad', 'mariem', 'mohammad'])
for word in my_string_list:
    print(word[0])