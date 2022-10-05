print(" Rules of the game are: ")
print(" 1. there is a secret number already set\n you have 3 attempts to try and the number is within 0-10 ")
secret_number=7
count=0
while count!=3:
    x=int(input("Guess the number: "))
    if x==secret_number:
        print(f'you guessed it correctly!! in {count+1} attempts')
        break
    count+=1
if count>=3:
    print("It's over, You exausted the limit!!!")