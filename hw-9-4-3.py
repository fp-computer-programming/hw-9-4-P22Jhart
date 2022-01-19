def count_e(word):
    num = 0
    for x in word:
        if x == "e":
            num += 1
    
    return num

a = count_e("homeeeeeeeeeework")

print(a)