max=0
while True:
    a=int(input('Masukan bilangan N:'))
    if max < a:
        max=a
    if a==0:
        break
print('Bilangan Terbesarnya Adalah',max)