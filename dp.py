a="abcd"
b="werabcdt"

ml=0
ll=[]

for i in range(len(a)):
	for j in range(len(b)):
		if a[i]==b[j]:
			d=ml
			while a[i:i+d]==b[j:j+d]:
				ll=a[i:i+d]
				ml=d
				d=d+1
print(ml,ll)
