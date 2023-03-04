
# class Mobile:
#     def __init__(self):
#         print("hi",id(self))

# ob=Mobile
# ob.a="a"
# print(ob.a)

# class Mobile:
#     def __init__(self,brand,price):
#         print("Inside construction ")
#         self.brand=brand
#         self.price=price

# mob1=Mobile("Apple",20000)
# print(f"Mobile 1 has brand {mob1.brand}{mob1.price}")
# mob2=Mobile("Samsung",300)
# print(f"Mobile 1 has brand {mob2.brand}{mob2.price}")

# class Mobile:
#     def __init__(self,brand,price):
#         print("Inside construction ")
#         self.brand=brand
#         self.price=price
#     def purchase(self):
#         print(f"Mobile 1 has brand {self.brand}{self.price}")
        
# mob1=Mobile("Apple",20000)
# mob1.purchase()
# mob2=Mobile("Samsung",300)
# mob2.purchase()

# class Mobile:
#     def display(self):
#         print("Displaying details")

#     def purchase(self,data):
#         self.display()
#         print("Calculating price",data)
  
# ob=Mobile()
# ob.purchase(1)

                                                   
# class Book:
#     def __init__(self):
#         self.title=None


# my_fav=Book()
# my_fav.title="Head First Programming"
# your_fav=Book()
# your_fav.title="Learn Python the hard way"
# my_fav.title="Learning Python"
# your_fav=Book()
# print("My favorite is",my_fav.title)
# print("Your's is",your_fav.title)
                                                
# a=4
# b=41
# print(id(a),id(b))

# class Mobile:
#     def __init__(self, price, brand):
#         self.price = price
#         self.brand = brand

# mob1=Mobile(1000, "Apple")
# print("Price of mobile 1 :", mob1.price)

# mob2=mob1
# mob2.price=3000

# print("Price of mobile 1 :", mob1.price)
# print("Price of mobile 2 :", mob2.price)


# class Vehicle:
#     def __init__(self):
#         self.mileage=None
#         self.fuel_left=None
    
#     def identify_distance_travelled(self,initial_fuel):
#         distance_travelled=(initial_fuel-self.fuel_left)* self.mileage
#         return distance_travelled
#     def identify_distance_that_can_be_travelled(self):
#         initial_fuel=15
#         distance_travelled=self.identify_distance_travelled(initial_fuel)
#         if self.fuel_left>5:
#             return (initial_fuel-5)*self.mileage- distance_travelled
#         else:
#             return 0
# v1=Vehicle()
# v1.mileage=10
# v1.fuel_left=20
# print(v1.identify_distance_that_can_be_travelled())

# import antigravity


# a={"1":1}
# b={"2":2}
# z={**a,**b}

# print(abs.__doc__)
# print(int.__doc__)
# print(input.__doc__)

# def square(num):
#     '''Return the square value of the input number.

#     The input number must be integer.
#     '''
#     return num ** 2

# print(square(2))
# print(square.__doc__)


# class A:
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return str(self.__dict__)

# ob=A("Azad")
# print(ob)

 ####################################################


# Python3 implementation of QuickSort

# This Function handles sorting part of quick sort
# start and end points to first and last element of
# an array respectively

def partition(start, end, array):
    
    # Initializing pivot's index to start
    pivot_index = start
    pivot = array[pivot_index]
    
    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:
        
        # Increment the start pointer till it finds an
        # element greater than pivot
        while start < len(array) and array[start] <= pivot:
            start += 1
            
        # Decrement the end pointer till it finds an
        # element less than pivot
        while array[end] > pivot:
            end -= 1
        
        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if(start < end):
            array[start], array[end] = array[end], array[start]
    
    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]
    
    # Returning end pointer to divide the array into 2
    return end
    
# The main function that implements QuickSort
def quick_sort(start, end, array):
    
    if (start < end):
        
        # p is partitioning index, array[p]
        # is at right place
        p = partition(start, end, array)
        
        # Sort elements before partition
        # and after partition
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)
        
# Driver code
array = [ 10, 7, 8, 9, 1, 5 ]
quick_sort(0, len(array) - 1, array)

print(f'Sorted array: {array}')
    












