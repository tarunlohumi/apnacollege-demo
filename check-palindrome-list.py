

list1 = []

list2 = []

#enter 5 elements for list 1
list1.append(input("enter 1st element for list 1: "))
list1.append(input("enter 2nd element for list 1: "))
list1.append(input("enter 3st element for list 1: "))
list1.append(input("enter 4th element for list 1: "))
list1.append(input("enter 5th element for list 1: "))

#copy list1 into list2
list2 = list1.copy()

#reverse the order of list1
list1.reverse()

if(list1==list2):
    print("It is indeed a palindrome list")
else:
    print("This is not a palindrome list")
