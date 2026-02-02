'''
set operation s:-
1) union (A u B)
2) intersection     (A n B)

3) set difference   (A-B)
4) symmetric difference     (A^B)

'''

#Given sets x={1,2,3,4} , y={5,6,7,8,9}  i> X|Y(UNION)     ii> X & Y(INTERSECTION)

x={1,2,3,4}
y={5,6,7,8,9}
print(x|y)               #union operations


A={1,2,3,4,5,6,7,8}
B={0,6,3,4,5,6,7,8}

print(A&B)           #INTER SECTION OPERATIONS.

A={1,2,3,4,5,6,7,8}
B={0,6,3,4,5,6,7,8}
print(A-B)              #set difference (first A and B ALLI common barodanu remove madi A alli iro elements na type madute )


P={2,4,6,8}
Q={4,6,10,12}
print(P^Q)              #symmetric difference is same items na bittu mikiro yalla elements na print madutte



