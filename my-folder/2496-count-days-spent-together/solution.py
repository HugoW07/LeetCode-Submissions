days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def day_of_year(date):       
            parts = date.split("-")
            month = int(parts[0])
            day = int(parts[1])

            before = sum(days_in_month[:month - 1])
            
            return before + day

class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):  
        
        a_start = day_of_year(arriveAlice)
        a_stop = day_of_year(leaveAlice)
        b_start = day_of_year(arriveBob)
        b_stop = day_of_year(leaveBob)

        start = max(a_start, b_start)
        end = min (a_stop, b_stop)
        
        return max(0, end - start + 1)
        
