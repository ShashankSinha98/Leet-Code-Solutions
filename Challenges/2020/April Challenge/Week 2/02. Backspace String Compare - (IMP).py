class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        s_ptr = len(S)-1
        t_ptr = len(T)-1

        s_skips = 0
        t_skips = 0

        while s_ptr>=0 or t_ptr>=0:

            while s_ptr>=0:
                if S[s_ptr]=='#':
                    s_skips += 1
                    s_ptr -=1
                elif s_skips > 0:
                    s_ptr -= 1
                    s_skips -= 1
                else:
                    break

            while t_ptr>=0:
                if T[t_ptr]=='#':
                    t_skips += 1
                    t_ptr -=1
                elif t_skips > 0:
                    t_ptr -= 1
                    t_skips -= 1
                else:
                    break

            if s_ptr>=0 and t_ptr>=0 and S[s_ptr] != T[t_ptr]:
                return False

            if (s_ptr>=0) != (t_ptr>=0):
                return False
        
            s_ptr -= 1
            t_ptr -= 1

        return True






S = "ab#c"
T = "ad#c"
print(Solution().backspaceCompare(S,T))
