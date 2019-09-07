# class Solution:
#     def mySqrt(self, x):
#         if x<1:
#             return 0
#         a=2
#         while a*a<=x:
#             n=a*a
#             if n*n>x:
#                 a=a+1
#             else:
#                 a=n

#         return a-1

class Solution:
    def mySqrt(self, x):
        n=2
        while True:
            if n*n<=x and (n+1)*(n+1)>x:
                return n
            z=(x-n*n)/(2*n)+n
            n=int(z)


a=Solution()
print(a.mySqrt(0))