age=23
name = "rajesh avula"
raj = "raju"
print("I am " + str(age)+ " years old ")
print("I am {0} years old".format(age))# replacement
print("there are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}".format(age**2,"January","March","May","july","August","october","December"))
print (raj in name)
print (name[1:7:2]) #name[start:end:step]
print("""
January:{0}
February:{1}
March:{0}
April:{2}
May:{0}
June:{2}
July:{0}
August:{0}
September:{2}
October:{0}
November:{2}
December:{0}""".format(31,28,30))

# to get spacing see the below print

print("""
January:{0:4}
February:{1:4}
March:{0:4}
April:{2:4}
May:{0:4}
June:{2:4}
July:{0:4}
August:{0:4}
September:{2:4}
October:{0:4}
November:{2:4}
December:{0:4}""".format(31,28,30))

print("""
January:{0:>10} 
February:{1:10}
March:{0:4}
April:{2:4}
May:{0:4}
June:{2:4}
July:{0:4}
August:{0:4}
September:{2:4}
October:{0:4}
November:{2:4}
December:{0:4}""".format(31,28,30) )


print("value of pi is {0:.6}".format(22/7))

