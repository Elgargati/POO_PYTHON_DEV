from faker import Faker
import csv  

data=[]
faker= Faker()
keys=['name','job','phone','email','country','salary']

def create_fille(file,rows):
    with open(file,'w') as f:
        w = csv.DictWriter(f,fieldnames=keys)
        w.writeheader()
        for row in range(int(rows)):
            list_data = {}
            list_data['name'] = faker.name()
            list_data['job'] = faker.job()
            list_data['phone'] = faker.phone_number()
            list_data['email'] = faker.free_email()
            list_data['country'] = faker.country()
            list_data['salary'] = faker.random_int(min=3000,max=20000)
            data.append(list_data)
        w.writerows(data)

f=input('file name :')
row=input('number of rows')
create_fille(f,row)

