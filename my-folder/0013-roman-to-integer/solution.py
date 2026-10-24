class Solution(object):
    def romanToInt(self, s):
        count = 0
        mydict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        for i in range(len(s)):
            current = mydict[s[i]]
            
            if i + 1 < len(s):
                next_num = mydict[s[i + 1]]
                if current < next_num:
                    count -= current
                    
                else:
                    count += current
            else:
                count += current
        return count
