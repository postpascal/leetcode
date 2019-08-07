class Solution:
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		left=[]
		l=['[','{','(']
		map_dic={'[':0,']':0,'(':1,')':1,'{':2,'}':2}
		
		for i in s:
			if i in l:
				left.append(i)
			else:
				if left==[] or map_dic[i]!=map_dic[left[-1]]:
					return False
				left.pop()
		
		return not bool(left)
			
					
		