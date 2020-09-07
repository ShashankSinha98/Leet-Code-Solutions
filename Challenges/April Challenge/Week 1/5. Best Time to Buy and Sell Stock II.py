class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        
        n = len(arr)
        minima = []
        maxima = []

        mini = True
        for i in range(n):

            if mini:
                if i+1!=n and arr[i]<arr[i+1]:
                    minima.append(i)
                    mini = False
            else:
                if i+1!=n and arr[i]>arr[i+1]:
                    maxima.append(i)
                    mini = True

                if i+1==n:
                    maxima.append(i)
                    
        maxProfit = 0
        if len(minima)==0:
            return 0
        else:
            k = len(minima)
            for i in range(k):
                maxProfit += (arr[maxima[i]]-arr[minima[i]])
            return maxProfit
