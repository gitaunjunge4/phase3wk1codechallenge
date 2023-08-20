def postive_numbers(a, b, c):
    positve_count = 0 #initializing the count

    if a > 0:
        positve_count += 1
    if b > 0:
        positve_count += 1
    if c > 0:
        positve_count += 1

    return positve_count == 2
print(postive_numbers(1,2,3))  #false
print(postive_numbers(-1,2,3))  #false
print(postive_numbers(-1,-2,3))  #true
print(postive_numbers(-1,-2,-3))  #false