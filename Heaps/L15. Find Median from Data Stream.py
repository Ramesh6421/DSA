# problem linkk(https://leetcode.com/problems/find-median-from-data-stream/)
'''
The median is the middle value in an ordered integer list. If the size of the list is even,
there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

'''


from heapq import heapify,heappush,heappop
class MedianFinder:

    def __init__(self):
        self.maxheap=[]  # left half
        self.minheap=[]  # right half
        heapify(self.maxheap)
        heapify(self.minheap)

    def addNum(self, num: int) -> None:
        L=len(self.maxheap)
        R=len(self.minheap)
        if L==0:
            heappush(self.maxheap,num*-1)
        elif L==R:
            if num<self.minheap[0]:
                heappush(self.maxheap,num*-1)
            else:
                temp=heappop(self.minheap) 
                heappush(self.minheap,num)
                heappush(self.maxheap,temp*-1)
        else:
            if R==0:
                if num>self.maxheap[0]*-1:
                    heappush(self.minheap,num)
                else:
                    temp=heappop(self.maxheap) 
                    heappush(self.maxheap,num*-1)
                    heappush(self.minheap,temp*-1)
            elif num>=self.minheap[0]:
                heappush(self.minheap,num)
            else:
                if num<self.maxheap[0]*-1:
                    temp=heappop(self.maxheap) 
                    heappush(self.maxheap,num*-1)
                    heappush(self.minheap,temp*-1)
                else:
                    heappush(self.minheap,num)


        

    def findMedian(self) -> float:
        L=len(self.maxheap)
        R=len(self.minheap)        
        if L>R:
            return self.maxheap[0]*-1
        else:
            mid=((self.maxheap[0]*-1)+self.minheap[0])/2
            return mid
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
