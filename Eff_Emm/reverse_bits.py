a = 12345




def reverseBits(n):
    start = 0
    
    
    n = str(n)
    end = len(n)-1
    
    while start < len(n)-1:
        present= n[start]
        after = n[end]
        #print(present)
       
        n = n.replace(n[start], after)
        n = n.replace(n[end], present)
        #n = n.replace()
        
        if start == end:
            break
        start += 1
        end -=1
    print(int(n))
    return int(n)
reverseBits(a)
