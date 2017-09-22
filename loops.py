number = "923,366,567,839,462"
cleanNumber= ''

for i in range(0,len(number)):
    if number[i] in "0123456789":
        #print(number[i],end="") # to remove new line line for every iteration.
        cleanNumber = cleanNumber + number[i]
    print(cleanNumber)


# for i in range(0,len(number)):
#     if number[i] in "0123456789":
#         print(number[i])
#
# list = ["egg","Bacon","Sausage"]
# for i in list:
#     if i =="egg":
#         continue
#     print(i)
#
#
#
#
