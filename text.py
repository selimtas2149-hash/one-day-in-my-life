import math
def mergearr(arr1,arr2):
    # here ı think one of the lowest  will be our lowest as well so we have to compare the lowest  one of the lowest is ours again.
    a=0
    b=0
    ans=[]
    
    while a<len(arr1) and  b<len(arr2):
        
        if arr1[a]<arr2[b]:
            # we chacke which wşll be selected
            ans.append(arr1[a])
            a+=1
        elif arr2[b]<arr1[a]:
            # same
            ans.append(arr2[b])
            b+=1
        
        else:
            # for shortenning but this is not necessary 
            
            ans.append(arr1[a])
            ans.append(arr2[b])
            a+=1
            b+=1
    
    
    
    return ans+arr1[a::]+arr2[b::]


def rotate(nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        lens=len(nums)


        return nums[lens-k::]+nums[:lens-k]
    


def moveZeroes(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        
        # we will start from target so we can move thenm oour place more easier
        a=0
        b=0

        while b<len(nums):
            if nums[a]!=0 and nums[b]!=0:
                a+=1
                b+=1
            elif nums[a]==0 and nums[b]==0:
                b+=1
            
            elif nums[a]==0 and  nums[b]!=0:
                nums[a],nums[b]=nums[b],nums[a]
            
            elif nums[a]!=0 and nums[b]==0:
                a+=1


def maxSubArray(nums: List[int]) -> int:
        ourmax=-math.inf
        for i in nums:
            total=0
            for x in nums[i::]:
                total+=x
                ourmax=max(ourmax,total)

        return ourmax
    


from collections import defaultdict


def anagrams(arr):
        
        dicter=defaultdict(list)
        
        for i in arr:
            lister=[0]*26
            for x  in i:
                lister[ord(x)-ord("a")]=x
                
            
            dicter[tuple(lister)].append(i)
                
                
        
        
        ans=[]
        for a,b in dicter.items() :
            ans.append(b)
        
        
        return b
    
