s1 = [1, 'A', 11, 'c', 'f1', 'm1']
s2 = [2, 'B', 12, 'c', 'f2', 'm2']
s3 = [3, 'C', 10, 'b', 'f3', 'm3']

hashTable = [None for _ in range(101)]

def insert(s):
    rollNo = s[0]
    hashTable[rollNo] = s[1:]
    return

def search(s):
    rollNo = s[0]

    if hashTable[rollNo] is None:
        return False
    
    return hashTable[rollNo]

def delete(s):
    rollNo = s[0]

    hashTable[rollNo] = None
    return

insert(s1)
insert(s2)
insert(s3)
print(hashTable)
print(search(s2))
print(search(s3))

delete(s1)

print(search(s1))