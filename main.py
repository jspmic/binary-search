import sys

#Iterative Solution
#def binsearch(li: list, target: int) -> int:
#    #li must be a sorted list
#    li = sorted(li)

#    start,end = 0, len(li)-1
#    middle = (start+end)//2
#    while start<end:
#        if li[middle] < target:
#            start = middle+1
#        elif li[middle] > target:
#            end = middle-1
#        else: break
#        middle = (start+end)//2
#    return middle

#Recursive Solution
def binsearch(li:list,targ:int) -> int:
    def _binsearch(li:list,target:int,l:int,r:int):
        if len(li)==1:
            if li[0]==target: return l
        else:
            m = (l+r)//2
            if li[m]==target: return m
            elif li[m]>target:
                return _binsearch(li,target,l,m-1)
            else: return _binsearch(li,target,m+1,r)
    return _binsearch(li,targ,0,len(li)-1)


if __name__=='__main__':
    title = "\nEXAMPLE OF THIS BINARY SEARCH IMPLEMENTATION\n"
    print(title,"-"*(len(title)-2), "\n")
    print("1st: [1,2,4,6,8,19,32], target=19")
    print("Index of target: ",binsearch([1,2,4,6,8,19,32], 19))
    print("\n2nd: [1,2,8,10,15,24,40], target = 15")
    print("Index of target: ",binsearch([1,2,8,10,15,24,40], 15))
    print("\n3rd: [1,2,19,31,34,48,66], target = 66")
    print("Index of target: ",binsearch([1,2,19,31,34,48,66], 66))
    sys.exit(0)

