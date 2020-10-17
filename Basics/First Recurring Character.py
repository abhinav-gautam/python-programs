# Google Question
# Given an array = [2,5,1,2,3,5,1,2,4]:
# It should return 2
#
# Given an array = [2,1,1,2,3,5,1,2,4]:
# It should return 1
#
# Given an array = [2,3,4,5]:
# It should return undefined


def firstRecurringElement(array):
    dict = {}
    for i in range(len(array)):
        if array[i] in dict.keys():
            return array[i]
        else:
            dict[array[i]] = 1
    return "Not Found"


array = [2,1,3]
print(firstRecurringElement(array))