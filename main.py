# ########## Python Beta Level 1 ############
#
# x = 'banana'
# y = 'apple'
# z = 'mango'
#
# print(x,y,z)
#
# ########### multiple variables ##########
#
# x, y, z = 'hamza','asad','ahad'
#
# print(x, y, z)
#
# a = b = c = 'Bismillah', 56 , True
#
# print(a)
#
# print(a,b)
#
# print(a,b,c)
#
# ########## sum ############
#
# num1 = 10
# num2 = 20
#
# num3 = num1+num2
#
# print(num3)
#
# print(num2/num1)
#
# ######### integer division #############
#
# print(num2//num1)
#
# ######### power #############
#
# print(num1**2)
#
# ######### remainder #############
# print(f"num1 = {num1}")
# print(f"num1 = {num1} divide by 3, remainder is following")
# print(num1%3)
#
# print(f"num2 = {num2}")
# print(f"num1 = {num2} divide by 3, remainder is following")
# print(num2%3)
#
# #############################
#
# ####### check type ###############
#
# print(type(198))
#
# print(type(0.198))
#
# print(type("198"))
#
# print(abs(-540))
#
# a = [1,10,9,4,3,5]
# print(sorted(a))
#
# ####################
#
# ####### List ########
#
# myList = [1,2,3,4,5]
#
# a = [1,2,3,4,5]
# anotherList = list(a)
#
# print(anotherList)
#
# diffList = list()
#
# print(type(diffList))
#
# newList = [value for value in range(5)]
# for i in newList:
#     print(i)
# print()
# print(newList[0])
#
# # newList[4] = 5  ##for assigning new value
#
# print(newList)
#
# print(type(newList))
#
# ##### for adding new index and value #########
#
# newList.append(5)
#
# print(newList)
#
# ######## for inserting at a given location ######
#
# newList.insert(0,10)
#
# print(newList)
#
# newList.insert(1,100)
# print(newList)
#
# newList.insert(7,10)
#
# print(newList)
#
# newList.pop()
#
# print(newList)
#
# newList.append(5)
#
# print(newList)
#
# newList.pop(2)
#
# print(newList)
#
# ###############################
#
# ########## Dictionary #############
#
# dictionary = {}
#
# print(type(dictionary))
#
# ## with function
#
# myDictionary = dict()
#
# print(type(myDictionary))
#
# dictionary = {key: value for key, value in [['apple',12],['banana',12 ], ['orange',20]]}
#
# print(dictionary)
#
# print(dictionary['orange'])
#
# print(len(dictionary))
#
# dictionary['banana'] = 14
#
# print(dictionary)
#
# ########## dictionary basic structure #######
#
# veggies = {
#     'potato' : 23,
#     'tomato' : 24,
#     'peach' : 42
# }
#
# print(veggies)
#
# fruits = {
#     'mango' : 230,
#     'apple' : 240,
#     'peach' : 402
# }
#
# fruits.update(veggies)
#
# print(fruits)
#
# fruits.pop('peach')
#
# print(fruits)
#
# ########################
#
# ######### Tupple #############
#
# tupleT = ()
#
# print(type(tupleT))
#
# ### calling with function ###
#
# tupleTT = tuple()
#
# print(type(tupleTT))
#
# tupleT = ("Sadam", "Khan", 12, True)
#
# print(tupleT)
#
# print(tupleT[1])
#
# print(len(tupleT))
#
# ####################
#
# ######### Sets #############
#
# mySet = {14}
#
# print(mySet)
# print(type(mySet))
#
# mySet.add(10)
#
# print(mySet)
#
# print(mySet)
# mySet.add(9)
# print(mySet)
# mySet.add(15)
# print(mySet)
#
# x = {1,2,3,4}
#
# y = {2,4,6,8}
#
# z = {1,3,5,7}
#
#
# print(x.intersection(y))
#
# print(z.intersection(y))
#
# print(y.union(z))
#
# print(x.issubset(y))
#
# print(x.issuperset(y))
#
# print(y.isdisjoint(z))
#
# ########################
#
# ######## Control flow statements #############
#
# num = 10
#
#
# if num % 2 == 0:
#     print("Even number.")
# elif num % 2 == 1:
#     print("Odd number")
# else:
#     print("Neither even nor odd number.")
#
# ########################
#
# ###### Loop ############
#
# for i in range(10):
#     print(i)
#
# for i in range(10):
#     print(i * 5)
#
# names = ['Ali', 'Imran', 'Kamran', 'Mujahid', 'Salamat']
#
# for i in names:
#     print("Mr " + i)
#
# names = ['Ali', 'Imran', 'Kamran', 'Mujahid', 'Salamat']
#
# for i in range(len(names)):       ### (for i in names:) won't work, int needed for indexing not string
#     names[i] = 'Mr. ' + names[i]
#
# print(names)
#
# ########### dictionary loop ###########
#
# fruits = {
#     'apples' :3,
#     'bananas':5,
#     'mangoes':7,
# }
#
# for i, v in fruits.items():
#     print(i, v)
#
# for index, value in fruits.items():
#     print(f'I love to eat {value} {index} everyday.')
#
# ############# enums loop ##########
#
# nums = [10,20,30,40,50,60]
#
# for i, v in enumerate(nums):
#     print(i,v)
#
#
# for index, value in enumerate(nums):
#     print(f'The number {value} is at index {index}.')
#
# ##############################
#
# ######### functions #############
#
# def isEven(num):
#     if num % 2 == 0:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is odd")
#
# isEven(3)
#
# ########## list to function ##########
#
# nums = [10,20,30,40]
#
# def takeList(nums):
#     for i in nums:
#         print(i)
#
# takeList(nums)
#

##################################

####### Error handling #########
#
# def checkType(year):
#     assert type(year) == int, 'Enter an integer value'
#     print('The year type is valid')
#     print('Successful')
#     return True
#
# checkType(2010)
#
# ##### throws error ######
#
# # checkType(2010.1)
#
# ###########################
#
# ########### Reading and Writing Files ###############
#
# data = []
#
# fileObj = open('testFile.txt')
# for d in fileObj:
#     data.append(d)
#
# print(data)
#
# data = []
#
# fileObj = open('testFile.txt')
# for d in fileObj:
#     r = d.strip('\n')
#     data.append(r)
#
# print(data)
#
# write_data = ['alpha','beta','gamma']
#
# with open('GreekLetters.txt', 'w') as fo:
#     for value in write_data:
#         fo.write(value)
#         fo.write('\n')
# fo.close()
#
# append_data = ['zeta','eta','theta']
#
# with open('GreekLetters.txt','a') as fo:
#
#     for value in append_data:
#         fo.write(value)
#         fo.write('\n')
#
# fo.close()
#
# #########################################
#
#
# ##### CSV File #############
#
# observations = []
# count = 0
#
# with open('temperature.CSV','r') as fo:
#     header = fo.__next__()
#     for i in fo:
#         observations.append(i.strip('\n'))
#         count += 1
#
# print(count)
# # print(observations)
#
# ##################################
#
# ############ Classes #############
#
# class Fruit:
#
#     ''' class defined for fruits, to make their objects '''
#
#     def __init__(self, name, nutrients):
#         try:
#             assert type(nutrients) == list
#         except AssertionError:
#             print('Invalid Construction')
#             raise Exception
#         self.name = name
#         self.nutrients = nutrients
#         self.isRipe = False
#
#     def getName(self):
#         return self.name
#
#     def getNutrients(self):
#         for value in self.nutrients:
#             print(value)
#
#     def checkRipeness(self):
#         return self.isRipe
#
#     def makeRipen(self):
#         self.isRipe = True
#
#
#
# apple = Fruit(name = 'Apple', nutrients=['Vit A', 'Vit B', 'Vit C', 'Vit D'])
# banana = Fruit(name = 'Banana', nutrients=['Vit A', 'Vit B', 'Vit C'])
#
# print(banana.getName())
# banana.getNutrients()
# print(banana.checkRipeness())
# banana.makeRipen()
# print(banana.checkRipeness())
# print(apple.getName())
# apple.getNutrients()
# print(apple.checkRipeness())
# apple.makeRipen()
# print(apple.checkRipeness())
#
# ############################
#
# ######### Inheritence #############
#
# class Citrus(Fruit):
#     def __init__(self, name, nutrients):
#         super().__init__(name, nutrients)
#         self.type = 'Citrus'
#         self.characteristic = 'pulpy and juicy'
#
#     def getType(self):
#         return self.type
#
# orange = Citrus(name = 'Orange', nutrients = ['Vit C'])
#
# print(orange.getType())
#
# print(orange.name)
#
# print(orange.checkRipeness())
#
# orange.makeRipen()
#
# print(orange.checkRipeness())
#
# print(orange.characteristic)
#
