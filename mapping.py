import kociemba
from clustering import *

my_dict = {
    1: ["Red", "F"],
    2: ["Blue", "U"],
    3: ["Yellow", "R"],
    4: ["Green", "D"],
    5: ["White", "L"],
    6: ["Orange", "B"]
}
# solved = kociemba.solve('DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD')
# order for string to use kociemba: U -> R -> F -> D -> L -> B

#Testing for dictionary
input = [2,2,5,3, 2 ,6,1,6,4, #U
         
         5,4,3,3, 5 ,5,1,2,6, #R

         5,1,2,5, 1 ,4,3,2,6, #F

         4,1,3,3, 3 ,6,6,4,2, #D

         5,5,3,3, 6 ,1,1,6,6, #L

         4,5,1,4, 4 ,1,4,2,2] #B

input_2 = [5, 3, 4, 3, 2, 2, 6, 6, 1, 
           3, 1, 3, 2, 3, 2, 2, 4, 5, 
           2, 3, 6, 1, 1, 4, 1, 3, 4, 
           4, 5, 1, 1, 4, 1, 2, 6, 3, 
           1, 5, 5, 6, 5, 6, 4, 2, 3, 
           5, 5, 6, 4, 6, 4, 2, 5, 6]

string_input2 = ""

for i in input_2:
    string_input2 += (my_dict[i][1])

# answer = kociemba.solve(string_input2)
# print(answer)
# print(type(answer))





