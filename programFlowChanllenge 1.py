# for i in ["rajesh", "Vineeth",  "Avula"]:
#     print("what is your last name is it {}".format(i) )
#     res=input("")
#     if res=="yes":
#         print("OK")
#         break
#     else:
#         print("Let me check once again")

ipAddress = input("Please enter the ip address")
numberOfSegments=0
segment=''
segmentNumber = 0
for i in range(0,len(ipAddress)):
    if ipAddress[i] != ".":
        segment = segment + ipAddress[i]
        continue

    else:

        lengthOfSegment = len(segment)
        segmentNumber +=1
        print("length of segment {0} is {1}". format(segmentNumber, lengthOfSegment, segment))
        segment = ''
        numberOfSegments += 1
else :
    lengthOfSegment = len(segment)
    segmentNumber +=1
    print("length of segment {0} is {1}". format(segmentNumber, lengthOfSegment, segment))


print("numberOfSegments in IP address in {0}".format(numberOfSegments + 1))

print(i)





