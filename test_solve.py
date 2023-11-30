import kociemba

my_dict = {
    1: ["Red", "F"],
    2: ["Blue", "U"] ,
    3: ["Green", "D"],
    4: ["Orange", "B"],
    5: ["Yellow", "R"],
    6: ["White", "L"]
}
# solved = kociemba.solve('DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD')

input = [2,2,5,3, 2 ,6,1,6,4, #U
         
         5,4,3,3, 5 ,5,1,2,6, #R

         5,1,2,5, 1 ,4,3,2,6, #F

         4,1,3,3, 3 ,6,6,4,2, #D

         5,5,3,3, 6 ,1,1,6,6, #L

         4,5,1,4, 4 ,1,4,2,2] #B

string_input = ''
for i in input:
    side = my_dict[i][1]
    string_input += side

print(string_input)
# print(solved)

answer = kociemba.solve(string_input)
print(answer)
print(type(answer))

steps = answer.split()
print(steps)
print(len(steps))