from audioop import reverse
from pickle import TRUE


d = {'mum':[4,2],'dad':[4,1],'sis':[4,4],'bro':[3,5]}


print(sorted(d.items(), key=lambda kv:(kv[1][0],-kv[1][1]),reverse=True))