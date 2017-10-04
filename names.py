students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
def names(x):
    for i in range(0,len(x)):
        print x[i]['first_name'], x[i]['last_name']
names(students)
                                            
def name(x):
    for i in x: 
        print i
        if i == 'Students':
#            print "i is == students"
            for j in x[i]:
#                print j
                print j['first_name'], j['last_name']
        elif i == 'Instructors':
#            print "i is == instructors"
            for j in x[i]:
#                print j
                print j['first_name'], j['last_name']
name(users)