class Solution:
    def myPow(self, x: float, n: int) -> float:
        k = abs(n)
        def pls( k):
            if k == 1:
                return x
            temp  =pls( k // 2)
            # print(k, temp)

            if k %2 ==0: return temp * temp 
            else: return temp * temp * x
        if n < 0:
            return 1 / pls( k)
        elif n > 0:
            return pls( k)
        else:
            return 1