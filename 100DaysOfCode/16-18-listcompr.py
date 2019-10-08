import string
names = ['pybites', 'mike', 'bob', 'julian', 'tim', 'sara', 'guido']
first_half_alphabets =  list(string.ascii_lowercase)[0:13]
second_half_alphabets =  list(string.ascii_lowercase)[13:]
new_names=[]
for name in names:
    if name[0] in first_half_alphabets:
        new_names.append(name.title())
py_names = [name.title() for name in names if name[0] in first_half_alphabets]

s_names = []
s_names= [name.title() for name in names if name[0] in second_half_alphabets]

print(py_names)
print(sorted(s_names))
