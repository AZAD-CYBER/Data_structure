
# def tower(people):
#     if(people==1):
#         return (50)
#     else:
#         return people*(50)+tower(people-2)

# print("Total weight: ",tower(5))


# import turtle

# my_turtle = turtle.Turtle()
# my_win = turtle.Screen()
# my_win.setup(500,500)

# def draw_spiral(my_turtle, line_len):
#     if line_len <=0:             # works till length is greater than 0
#         return
#     else:
#         my_turtle.forward(line_len)
#         my_turtle.right(90)
#         draw_spiral(my_turtle,line_len-10)   # recursive call

# draw_spiral(my_turtle,160)

# #Write the logic to take the turtle to its destination
# #Refer the statements given above to draw the pattern

# #Provide different values and test your program
# destination="south"

# def tower_of_hanoi(n, source,destination,temp):
#     if(n==1):
#         disk=source.pop(0) #Removes the element in specified position
#         destination.insert(0,disk) #Inserts the given element in specified position
#         return
#     tower_of_hanoi(n-1, source, temp, destination)
#     disk=source.pop(0)
#     destination.insert(0,disk)
#     tower_of_hanoi(n-1, temp, destination, source)
#     return

# source=["red","white","green"]
# destination=[]
# temp=[]
# tower_of_hanoi(3, source, destination, temp)
# print("Source:",source)
# print("Destination:",destination)


# def TowerOfHanoi(n,source,dest,middle):
#     if(n<1):
#         print("NOT POSSIBLE")
#         return
#     if (n==1):
#         print("MOVE DISK {} FROM {} TO {}".format(n,source,dest))
#         return
    
#     TowerOfHanoi(n-1,source,middle,dest)
#     print("MOVE DISK {} FROM {} TO {}".format(n,source,dest))
#     TowerOfHanoi(n-1,middle,dest,source)

# n=int(input("ENTER THE NUMBER OF DISK"))
# TowerOfHanoi(n,"A","C","B")








