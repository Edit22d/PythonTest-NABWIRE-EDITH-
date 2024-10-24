# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F
mark= int(input('Enter the mark scored in percentage:\t'))
if mark >= 90 and mark <=100:
    print(' Grade A')
elif mark >=80 and mark <=89:
    print('Grade B')
elif mark >=70 and mark <= 79:
    print('Grade C')
elif mark >= 60 and mark <=69:
    print('Grade D')
elif mark >=40 and mark <= 49:
    print('Grade E') 
else:
      print('Grade F') 
      
      
 