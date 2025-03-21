# Problem Statement
# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.

anton = 21
beth = anton + 6
chen = beth + 20
drew = chen + anton
ethan = chen

print("Anton is " + str(anton))
print("Beth is " + str(beth))
print("Chen is " + str(chen))
print("Drew is " + str(drew))
print("Ethan is " + str(ethan))