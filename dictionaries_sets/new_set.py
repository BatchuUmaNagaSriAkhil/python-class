'''
what is a set?

collection of unordered unique elements
-> Unordered
->Unique (never allow duplicates)
why we use?
->fast searching -->O(1)
->duplicates removal

how to create a set?

numbers = {1,2,3,4,5}
print(numbers)
'''

#creation of set
numbers = {1,2,3,4,5}
print(numbers)

numbers = {1,2,2,2,3,4,5}
print(numbers)

num = [1,2,3,3,4,4,5]

unique = set(num)

print(unique)

#checking the mutability

#numbers[0] = 18
#print(numbers)

#set is unordered ---> fixed indexing

numbers.add(18)
print(num)

#1st way --->create

num = {1,2,3,4,5}

#2nd way -->create

s = set([1,2,3,4,5])

#empty set - creation
s = set()
s.add(1)
print(s)

#multiple elements
s.update([2,3,4,5])
print(s)

#removing the element
s.remove(2)
print(s)

#discard:
print(s.discard(10))
print(s)

#pop():Deletes the random element
s.pop()

#clear():gives the boolean value

print(3 in s)

'''
what is hashing?
Hashing will convert data into unique hash values which is stored in hash tables

Python uses:
1.hash tables
2.Hash functions

target = 10
set = {1,2,3,4,10}

unlike linear search
it directly jumps to target or location by the help of hashing technique

search,insert,delete --> O(1)

set operations:

1.Union   |
2.Intersection
3.Difference


'''
a = {1,2,3,4}
b = {5,6,7,8}

print(a|b)
print(a.union(b))

#intersection
print(a & b)
print(a.intersection(b))

#difference
print(a - b)
print(a.difference(b))

#symmetric difference:Elements which are not common
a = {1,2,3}
b = {2,3,4}
print(a ^ b)
print(a.symmetric_difference(b))

#subset and superset

a = {1,2}
b = {1,2,3,4}

print(a.issubset(b))

print(b.issubset(a))

print(b.issuperset(a))

print(a.issuperset(b))

#Frozenset:Immutable version of set
#cannot add 
#cannot del
#cannot update

fs = frozenset([1,2,3,4,5])

print(fs)

'''
Feature          List   Tuple   Dictionary   Set:
Ordered           Yes    Yes       No         No
mutability        Yes     No       Yes        Yes
Allow duplicates  Yes    Yes     keys:no val:allows
Indexing          Yes    Yes       No         No


can I store list inside the set?
1.list
2.dict
3.set


Task:

Create a set with the squares of a number
Convert the list with squares of a number to set
Try to repeat the squares two times
add the multiples of 2 to the same set at a single time
--> seperate the set with 2 diff sets
multiples of 2
squares
now perform all the set operations


'''
squares = {x * x for x in range(1, 6)}
print("Squares set:", squares)

square_list = [1, 4, 9, 16, 25]
square_set = set(square_list)
print("Converted list to set:", square_set)

square_list_repeat = [1, 4, 9, 16, 25, 1, 4, 9, 16, 25]
square_set_repeat = set(square_list_repeat)
print("After repeating squares:", square_set_repeat)

multiples_of_2 = {2, 4, 6, 8, 10}
print("Multiples of 2 set:", multiples_of_2)

print("\nSquares:", squares)
print("Multiples of 2:", multiples_of_2)

print("\nUnion:")
print(squares | multiples_of_2)

print("\nIntersection:")
print(squares & multiples_of_2)

print("\nDifference (Squares - Multiples of 2):")
print(squares - multiples_of_2)

print("\nDifference (Multiples of 2 - Squares):")
print(multiples_of_2 - squares)

print("\nSymmetric Difference:")
print(squares ^ multiples_of_2)
