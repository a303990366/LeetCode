class Solution:
    def totalFruit(self, fruits):
        number = 0
        left,right = 0, 0
        if len(set(fruits))<=2:
            return len(fruits)
        while right <= len(fruits):
#             print(left,right)
            tmp=fruits[left:right]
            tmp_num=len(set(tmp))
            if tmp_num<2:
                right+=1
            elif tmp_num>2:
                left+=1
            else:
                number=max(number,(right-left))      
                right+=1
        return number
