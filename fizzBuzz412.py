class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        r=[str(i) for i in range(1,n+1)]
        for i in range(2,n,3):
            r[i]="Fizz"
        for i in range(4,n,5):
            r[i]="Buzz"
        for i in range(14,n,15):
            r[i]="FizzBuzz"
        return r