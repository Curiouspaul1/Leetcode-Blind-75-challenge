class Solution:
    def subtractBinary(self, a, b):
        carried = False
        s = ''
        prev = 0
        start  = -1
        res = {'01': '', '10': '1', '11': '0', '00': '0'}
        while a[start] != 'b' and b[start] != 'b':
            i, j = a[start], b[start]
            if carried:
                if i is '1':
                    i = '0'
                    carried = False
                else:
                    i = '1'
                    
            mid = res[f'{i}{j}']
            if mid == '':
                carried = True
                mid = '1'
            s = f'{mid}{s}'             
            
            start -= 1

        
        if a[start] != 'b':
            if carried:
                s = f"{self.subtractBinary(a[:start+1], f'0b1')}{s}"
            rem = ''
            
        return s
        
        
    def addBinary(self, a, b):
        rem  = '0'
        s = ''
        start = -1
        res = {'10': '1', '01': '1', '11': '10', '00': '0'}
        while a[start] != 'b' and b[start] != 'b':
            i, j = a[start], b[start]
            mid = res[f'{i}{j}']
            if rem == '1':
                mid = self.addBinary(f'0b{mid}', f'0b{rem}')
            s = f'{mid[-1]}{s}'
            rem = mid[:] if mid[:-1] else '0'
            
            start -= 1
        
        if a[start] != 'b':
            s = f"{self.addBinary(a[:start+1], f'0b{rem}')}{s}"
            rem = ''
        if b[start] != 'b':
            s = f"{self.addBinary(b[:start+1], f'0b{rem}')}{s}"
            rem = ''
        if rem == '1':
            s = f'{rem}{s}'
        return s        
        
    def getSum(self, a: int, b: int) -> int:
        if a == 0:
            return b
        elif b == 0:
            return a
        bin_a = bin(a)
        bin_b = bin(b)
        if a > 0 and b > 0:
            return (int(f'0b{self.addBinary(bin_a, bin_b)}', 2))
        elif a > 0 and b < 0:
            return int(f'0b{self.subtractBinary(bin_a, bin_b)}', 2)
        elif a < 0 and b > 0:
            return int(f'0b{self.subtractBinary(bin_b, bin_a)}', 2)
        else:
            return (int(f'-0b{self.addBinary(bin_a, bin_b)}', 2))
        # #return sum([a, b])
        
