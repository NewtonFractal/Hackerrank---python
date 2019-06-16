def weirdness(n):
    if n % 2 == 0 and 1<n<6:
        print("not Weird")
    elif n % 2 == 0 and 5<n<21:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")
    else:
        print("Weird")

weirdness(14)