class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda x:(x[0],-x[1]),reverse=True)
        i=1
        while i<len(people):
            tmp=people[i]
            people[people[i][1]+1:i+1]=people[people[i][1]:i]
            people[tmp[1]]=tmp
            i=i+1
        return people