class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}
        arr=[0]*256
        
        for word in strs:
            arr=[0]*256
            for ch in word:
                arr[ord(ch)]+=1
            
            key = ""
            for i in range(256):
                if arr[i]>0:
                    key+=chr(i)+str(arr[i])
            if key not in d:
                d[key] = [word]
            else:
                d[key].append(word)
        res = []
        
        for key in d:
            res.append(d[key])
        
        return res
                