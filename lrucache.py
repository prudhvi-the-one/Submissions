'''//lru()cache
it will take lrucache'''

n = 10
my_dict = {}

for i in range(n):
    value = input("enter the url: ")
    my_dict[i] = value

del my_dict[next(iter(my_dict))]

found = int(input("enter a key number you want to search: "))

for key, value in my_dict.items():
    if key == found:
        print(key, value)
        break
else:
    print("-1")
