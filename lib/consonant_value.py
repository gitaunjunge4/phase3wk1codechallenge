#python lib/consonant_value.py

# BDD
# Given a lowercase string that has alphabetic characters only and no spaces,
# return the highest value of the consonant substrings.
# Consonants are any letters of the alphabet except "aeiou".We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

# For example, for the word "zodiacs", let's cross out the vowels. We get: "z d cs"

# -- The consonant substrings are: "z", "d" and "cs" and the values are z = 26, d = 4 and cs = 3 + 19 = 22. The highest is 26.

# For the word "strength", solve("strength") = 57.

# The consonant substrings are: "str" and "ngth" with values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. The highest is 57.

#input 
# <welcome
#output
#w-lc-m
#wlcm
#w-23 lc-15 m-13

#zodiacs
#z-d-cs
#z-26 d-4 cs=22

#maxwell
#m-xw-ll
#m-13 xw-47 ll-24

#PSEUDOCODE
#define a function that takes in a string
#map the alphabetical letters with their numbers
#store the vowels as a string in a var
#declare an empty arr
#split the string where there is a vowel
#use for loop to loop through the string 
#check if the character in a string is also in vowel
#append the constant characters to the emptyArr


#CODE
def consonant_value(string):
    cons_values ={
        "b": 2, "c": 3, "d": 4,"f": 6, 
        "g": 7, "h": 8, "j": 10, "k": 11,
        "l": 12,"m": 13, "n": 14, "p": 16,
        "q": 17, "r": 18, "s": 19,"t": 20, 
        "v": 22, "w": 23, "x": 24, "y": 25,
        "z": 26,
    }
    vowels = "aeiou"
    cons_total = 0
    max_value = 0

    for char in string:
        if char not in vowels:
            cons_total += cons_values[char]
            if cons_total > max_value:
                max_value = cons_total
        else:
            cons_total = 0

    return max_value

#tests
print(consonant_value("junior"))
print(consonant_value("welcome"))
print(consonant_value("david"))
print(consonant_value("zodiacs"))
print(consonant_value("maxwell"))


# ["w", "lc", "m"]
# [23, 15, 13]