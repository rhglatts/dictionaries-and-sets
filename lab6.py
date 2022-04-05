#Rebecca Glatts
#Lab 6

#Task 1: Dictionary
import copy

#(1)
stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2, 1: 'wow', 20 : [3, 4, 5], (1, 
2) : ['hi', 'bye']}
"""No you cannot add [“hi”, “bye”] as a key with  [1, 2] as the value because keys
#cannot be lists
"""

#(2)
favoriteFoods = {"Peg": "burgers", "Cy": "hotdogs", "Bob": "apple pie"}
print(favoriteFoods)
"""
{'Peg': 'burgers', 'Cy': 'hotdogs', 'Bob': 'apple pie'}
"""

#(3)   
fruit = {1 : 'apples', 2 : 'bananas', 3: 'pears', 4: 'grapes'}

#(a)
for item in fruit :
    print(item)

#(b)
for item in fruit.items() :
    print(item)

#(c)
for item in fruit.keys() :
   print(item)

#(d)
for item in fruit.values() :
   print(item)

"""
(a)
1
2 
3 
4

(b)
(1, 'apples')
(2, 'bananas')
(3, 'pears')
(4, 'grapes')

(c) 
1
2
3
4

(d)
apples
bananas
pears
grapes


"""
#(4)
def updateDict ( d, x) :
    d[x] = "new value"
def main () :
    db = {'ted' : 'xxx', 'jan' : 123, 'kay' : '13yy'}
    updateDict(db, 'jan')
    print(db) #any change made to db?

main()

"""
{'ted': 'xxx', 'jan': 'new value', 'kay': 
'13yy'}

Yes, the since each key can only have one value the old value corresponding value "123"
was erased and the new value for "jan" is "new value"
"""

#Task 2
L = [1, 4, 9, 4, 7, 2, 2, 9]

#(1)
temp = copy.deepcopy(L)
S = set(temp)
print("Number of elements in S: ", len(S))
"""
Number of elements in S:  5

"""

#(2)
L.reverse()
FS = frozenset(L)
print("Number of elements in FS: ", len(FS))
"""
Number of elements in FS:  5
"""

#(3)
if (S == FS) :
    print("They are the same")
else:
    print("They are different")
"""
They are the same
"""

#(4)
S1 = {6, 7, 8}
union = S.union(S1)
intersection = S.intersection(S1)
print("Union: ", union)
print("Intersection: ", intersection)
"""
Union:  {1, 2, 4, 6, 7, 8, 9}
Intersection:  {7}
"""

#(5)
S2 = {4, 5, 6, 7, 8, 9}
difference = FS.difference(S2)
symmetric_difference = FS.symmetric_difference(S2)
print("Difference: ", difference)
print("Symmetric difference: ", symmetric_difference)
"""
Difference:  frozenset({1, 2})
Symmetric difference:  frozenset({1, 2, 5, 6, 8})
"""
