print(5-4)

print(5/4)

#to print only numerical or int value 
print(5/4)

a=12
print("my age is:",a)
print("my age is ",a,"years old")

x=12
y="abcd"
print(x,y)

#slicing = to print any particular of a variable 
z= "Ssalini" #it start from 0 like s = 0 , h = 1, a= 2 and so on 
print(z[2:5]) #2 is from where it start print and last 5 is befoire that it print in this a = 2 and n = 5 so it print 
print(z[2:]) #if to end nothing to write in last 
print(z[:4]) # if to start from starting nothing to write in start 
print(z[-4:-2]) # negative start from last e.g i=0, n=1, i=2 and so on 


# to convert into uppercase and lowercase
a="abcde"
print(a.upper())
b="ABC"
print(a.lower())

#to replace any thing
print(b.replace("B","G"))


#to write two variable together
print(a+b)
print(a+""+b)
print(a+ " "+b)
print(a+ "_"+b)
print(a," ",b)

#formating = if you add the content of the other type inside the string 
a=23
print("my age is",a,"years")
print(f"my age is{a}years") 
b= 12
print(f"calculate{a+b}")
print(f"this is folting value {a:2f}")

#captilization = this capitalize the first letter of the string
txt=" hello world"
x = txt.capitalize()
print(x)

#center = this will centre the string with given width
x= txt.center(38)
print(x)

#count = this will count the number of accurrance of a substring on the given string

a="abcdeeee"
x = a.count("e")
print(x)


y = a.islower()
print(y)
b="abcdEEee"
y = b.islower()
print(y)
