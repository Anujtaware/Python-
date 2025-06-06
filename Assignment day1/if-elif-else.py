
#5)	accept marks from the user. Using if…….elif….  Else,  display whether result is  fail, pass, second class , first class, Distinction etc.
english =int(input("enter english marks"))
maths=int(input("enter maths marks"))
science =int(input("enter science marks"))

sum=english+maths+science
percent=sum/3
print(percent)
if not(english>=35 and maths>=35 and science>=35):
    print("fail")
elif 75>=percent>60:
    print("first class")
elif 60>=percent>50:
    print("second class")
elif 100>= percent >75:
    print("destinction")
else:
    print('pass')