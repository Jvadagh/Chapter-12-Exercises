"""11. Wrap the following code in a try statement to defend against any exceptions it can raise. Do not use
a catch-all handler.
"""
lst = [0, 0, 0, 0]

try:
    with open('data.txt', 'r') as f:
        count = 0
        for line in f.readlines():
            try:
                lst[count] = int(line)
                count += 1
            except ValueError:
                print('cant be a String : ', line)
            except IndexError:
                print('lines numbers > list length')

except FileNotFoundError:
    print("can not create a file with 'r' ")
    file = open('data.txt', 'w')
    file.close()

    with open('data.txt', 'r') as f:
        count = 0
        for line in f.readlines():
            try:
                lst[count] = int(line)
                count += 1
            except ValueError:
                print('cant be a String : ', line)
            except IndexError:
                print('lines numbers > list length')

print(lst)
