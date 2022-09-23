for num in range(1,21):
    if num == 4 or num == 13:
        print(f"{num} is unlucky")
    elif num % 2 == 0:
        print(f"{num} is even")
    elif num == 7:
        print(f"{num} is lucky")
    else:
        print(f"{num} is odd")
