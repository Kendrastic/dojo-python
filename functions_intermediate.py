#Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1
x[1][0] = 15
# 2
students[0]['last_name'] = 'bryant'
#3
sports_directory['soccer'][0] = 'andres'
#4
z['y'] = 20

#Iterate Through a List of Dictionaries



def iterateDictionary(some_list):
    for student in some_list:
        output = ""
        for key in student.keys():
            output += f"{key} - {student[key]}, " 
        print(output[:-2])
        output = ""
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

iterateDictionary(students) 







# #3 Get Values From a List of Dictionaries

def iterateDictionary2(key_name, some_list):
    for element in some_list:
        print(element[key_name])

iterateDictionary2('test', students)

#4 Iterate Through a Dictionary with List Values

def printInfo(some_dict):
    for key in some_dict:
        print(key)
        for i in some_dict[key]:
            print(i)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)


