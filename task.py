import requests
res=requests.get('https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences')
js=res.json()
paid_confereces=js['paid']

for conferences in paid_confereces:
    for attribute, detail in conferences.items():
        print(attribute,":", detail)

    print("\n")

res_list = [i for n, i in enumerate(paid_confereces) if i in paid_confereces[n + 1:]] 

print (" duplicates value :" + str(res_list)) 

#conferences hold on same date
sem_dup=[]
for i in range(0,len(paid_confereces)-1):
   for j in range(1,len(paid_confereces)-1):
       if paid_confereces[i]==paid_confereces[j]:
           sem_dup.append(paid_confereces[i])
print(sem_dup)

