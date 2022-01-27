class Solution:
    def findMedianSortedArrays(self,nums1, nums2):
        tmp=self.merge_two_list(nums1,nums2)
        return self.find_median(tmp)
    def merge_two_list(self,l1,l2):
        tmp_list=[]
        t1,t2=1,1
        for i in range((len(l1)+len(l2))):
            if t1>len(l1):
                return tmp_list+l2[(t2-1):]
            if t2>len(l2):
                return tmp_list+l1[(t1-1):]
            if l1[(t1-1)]<=l2[(t2-1)]:
                tmp_list.append(l1[(t1-1)])
                t1+=1
            else:
                tmp_list.append(l2[(t2-1)])
                t2+=1
    def find_median(self,num_list):
        length=len(num_list)
        t=int(length/2)
        if length%2==0:
            return (num_list[t-1]+num_list[t])/2
        else:
            return num_list[t]
