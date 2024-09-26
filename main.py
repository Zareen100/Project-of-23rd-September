binary=list(input("Enter your number:"))
total=0
char=len(binary)
for i in range (char):
    last_elment=binary.pop()
    if last_elment=="1":
        total+=pow(2,i)
print(f'the decimal number is {total}')

