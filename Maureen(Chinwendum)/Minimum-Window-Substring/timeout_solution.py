import sys
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res=sys.maxsize
        temp={res:''}
        def check_sub(s, t, i, res, temp):
            hold=s
            l,r=i,i
            cell=t
            while r< len(s):
                for idx in range(len(t)):
                    if t[idx] == hold[r]:
                        hold=hold[:r]+'#'+hold[r+1:]
                        t=t[:idx]+'*'+t[idx+1:]
                        # r=r-1
                    if t=='*'*len(t):
                        if len(hold[l:r+1]) != res:
                            temp[len(hold[l:r+1])]=s[l:r+1]
                            length=min(len(s[l:r+1]), res)
                            if res != length:
                                # print('Wacko')
                                # print(temp)
                                del temp[res]
                                # print('WAcko delete')
                                # print(temp)
                                res=length
                            else:
                                # print(temp)
                                del temp[len(hold[l:r+1])]
                                # print('After Delete')
                                # print(temp)
                        t=cell
                        l=r
                r=r+1
            # print(temp)
            return res
        for i in range(len(s)):
            res=min(check_sub(s, t, i, res, temp), res)
        return temp[res]
        