cadbury1 = "milk chocolate"
cadbury2 = "dark chocolate"
cadbury3 = "white chocolate"

cadburymilk = 5
cadburydark = 3
cadburywhite = 8

chocolate1 = {"cadburymilk": 5}
chocolate2 = {"cadburydark": 8}
chocolate3 = {"cadburywhite": 3} 

print(chocolate1, chocolate2, chocolate3)

print(chocolate1)

chocolates = {"cadburymilk": 5, "cadburydark": 8, "cadburywhite": 3}


nameandgender = {"Steve": "Male", "Lia": "Female", "Vin": "Male", "Katie": "Female" }
print(nameandgender)

students = {"Steve": 32, "Lia": 28, "Vin": 45, "Katie": 38}
import pandas
dir(pandas)
print(students)

nameandgendercol = pandas.Series(nameandgender)
print(nameandgendercol)
chocolatescol = pandas.Series(chocolates)
print(chocolatescol)
studentscol = pandas.Series(students)
print(studentscol)

#dataframes
chocolatesdata = [chocolates]
print(chocolates)
chocolatesdataf = pandas.DataFrame(chocolatesdata, index=["quantity"])
print(chocolatesdataf)

studentsdata = [students]
print(studentsdata)
studentsdataf = pandas.DataFrame(studentsdata, index=["age"])
print(studentsdataf)

studentlist = [["Steve", 32, "Male"],["Lia", 28, "Female"],["Vin", 45, "Male"],["Katie", 38, "Female"]]
studentlistdf = pandas.DataFrame(studentlist, columns=["Name", "Age", "Gender"], index=["1", "2", "3", "4"])
print(studentlistdf)

print(students)
print(nameandgender)


studentdf1 = [students, nameandgender]
print(studentdf1)


studentdf2 = pandas.DataFrame(studentdf1, index =["Age", "Gender"])
print(studentdf2)







