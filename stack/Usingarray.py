SIZE = 10
S = [0]*(SIZE+1) #to initialize the list
top = 0

def is_empty():
    if top==0:
        return True
    return False

def is_full():
    if top>SIZE:
        return True
    return False

def push(x):
    global top
    top = top+1
    if is_full():
        print("Stackoverflow")
    else:
        S[top] = x

def pop1():
   
    global top
    if is_empty():
        print("Stackunderflow")
    else:
        top = top-1
        K=S[top+1]
        S[top+1]=0
    return K
def peek():
    global top
    if is_empty():
        print("Stackunderflow")
    else:
        print(S[top])
    
if __name__ == '__main__':
    push(10)
    push(20)
    push(30)
    push(40)
    push(50)
    push(60) 
    push(70)
    push(80)
    push(90)
    push(100)
   
    print(pop1())
    push(14)
    push(1)

    
    print(S[:SIZE+1])
