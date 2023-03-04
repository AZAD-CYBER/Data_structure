# class Evaluate:
#     def __init__(self,capacity):
#         self.top=-1
#         self.capacity=capacity
#         self.array=[]
    
#     def isEmpty(self):
#         return True if self.top==-1 else False
    
#     def peek(self):
#         return self.array[-1]
    
#     def pop(self):
#         if not self.isEmpty():
#             self.top-=1
#             return self.array.pop()
#         else:
#             return "$"
    
#     def push(self,op):
#         self.top+=1
#         self.array.append(op)
    
#     def evaluatePostfix(self,exp):
#         for i in exp:
#             if i.isdigit():
#                 self.push(i)
            
#             else:
#                 val1=self.pop()
#                 val2=self.pop()
#                 self.push(str(eval(val2+i+val1)))
        
#         return int(self.pop())

# exp="231*+9-"
# obj=Evaluate(len(exp))
# print("postfix evaluation: %d "%(obj.evaluatePostfix(exp)))

class evalpostfix:
    def __init__(self):
        self.stack=[]
        self.top=-1
    def pop(self):
        if self.top==-1:
            return
        else:
            self.top-=1
            return self.stack.pop()
        
    def push(self,i):
        self.top+=1
        self.stack.append(i)
    
    def centralfunc(self,ab):
        for i in ab:
            try:
                self.push(int(i))
            except ValueError:
                val1=self.pop()
                val2=self.pop()

                switcher={
                    "+":val2+val1,"-":val2-val1,"*":val2*val1,"/":val2/val1,"^":val2**val1
                }
                self.push(switcher.get(i))
        return int(self.pop())
    
str='100 200 + 2 / 5 * 7 +'
strconv=str.split(" ")
obj=evalpostfix()
print(obj.centralfunc(strconv))