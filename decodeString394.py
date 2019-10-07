class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def helper(st):
            if not st:
                return ''
            tmp=''
            stack=[]
            i,nums=0,0
            while i<len(st):
                if st[i]=='[':
                    stack.append(i)
                elif st[i]==']':
                    start=stack.pop()
                    if not stack:
                        tmp=tmp+helper(st[start+1:i])*nums
                        i=i+1
                        break
                elif 48<=ord(st[i])<=57 and not stack:
                    nums=nums*10+int(st[i])
                elif not stack:
                    tmp=tmp+st[i]
                i=i+1

            return tmp+helper(st[i:])
        return helper(s)