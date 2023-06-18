#Google Question
#Given an array = [2,5,1,2,3,5,1,2,4]:
#It should return 2

#Given an array = [2,1,1,2,3,5,1,2,4]:
#It should return 1

#Given an array = [2,3,4,5]:
#It should return undefined

# WEll this was a bit too simple.
def firstRecurringCharacter(input):
    empty_array = []
    for i in range(len(input)):
        if input[i] in empty_array:
            return input[i]
        else:
            empty_array.append(input[i])
    return None


#Bonus... What if we had this:
# [2,5,5,2,3,5,1,2,4]
# return 5 because the pairs are before 2,2

print(firstRecurringCharacter([2,5,1,2,3,5,1,2,4]))
print(firstRecurringCharacter([2,1,1,2,3,5,1,2,4]))
print(firstRecurringCharacter([2,5,5,2,3,5,1,2,4]))
