#python Valiables(INt,Float and Boolean)
studentNumber=70
print(studentNumber)
#Oparetors(Arthemetic)
x=2
y=3
a=x+y
print(a)

# Assignment Oparetors
x+=2 # adding 2 two the value of x(increament)
print(x)
# relational oparetors( relatang two value using different sign)
x<y
# Datatype (int, float,boolean,complex, string,list...)
c=2+3j
print(c)
firstName="mukagasaraba"
secondName="rachel"
country="rwanda"
district="rusizi"
lendMoney= 200,000
payedBack=50,000
currency="rwf"
print(f"Dear {firstName.capitalize()} {secondName.capitalize()} who is {2021-1978} years old from {country.upper()} in {district.title()}.We are extrimly excited to give you your remining {200000-5000} {currency.upper()}.")

# datastrucure using a list(List can contain anything)
foodList=["Bread","Cakes","Meat","Rolls"]
foodList[2] # always index start from zero
print(foodList[0:2])
print(foodList[-3:-1])
foodList.append("Marshmallow") # add value to the bottom of the list
foodList.insert(1,"beans") # insert value to between index specified
foodList.extend(["sweet potatoes","millet "]) # add alist to the bottom of list
foodList.remove("Meat")# removes last item in the list
foodList.sort() # sort items in accending manner
foodList.reverse() #reverse item last became first
print(foodList)
foodList.clear() # delet items in the list
print(foodList)
# usng for loop in list
list=[1,2,3,4,5]
for i in list:
    a=i*2
    print(a)
length = len(list)
print(length)
# make a list from a nother list
a=[[1,2,3],[4,5,6],[7,8,9]]
b=[]
b=[e for sublist in a  for e in sublist]
print(b)


