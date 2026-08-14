Student = {
    "name" : "Vamsi",
    "college" : "IIIT Kottayam",
    "CGPA" : 9.44,
    "Language" : "C++",
    "LC Problems" : 413,
    "CC Rating" : 1461
}
print("--------Intial Values---------")
for key,value in Student.items():
    print(f"{key} : {value}")
Student['CC Rating'] = 1500
print()
print("--------Final Values---------")
for key,value in Student.items():
    print(f"{key} : {value}")