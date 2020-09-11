class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        n = len(guess)
        A = 0
        arr = [0]*10
        
        for i in range(n):
            if secret[i]==guess[i]:
                A+=1
            else:
                arr[int(secret[i])]+=1
        
        for i in range(n):
            if secret[i]!=guess[i]:
                if arr[int(guess[i])]>0:
                    arr[int(guess[i])]-=1
        
        B = n-A-sum(arr)
        
        
        return "{}A{}B".format(A,B)