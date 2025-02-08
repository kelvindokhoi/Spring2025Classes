import os
import pickle

def get_absolute_path(filename):
  current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
  return os.path.join(current_dir, filename)


class Justice:
    def __init__(self,state,yrleft,yrappt,pres,name):
        self.state=state
        self.yrleft=int(yrleft)
        self.yrappt=int(yrappt)
        self.pres=pres
        self.name=name
        *a,=(self.name).split()
        self.lastname=a[1]
        self.firstname=a[0]
    def numYearsServed(self):
        return self.yleft - self.yrappt
    def __str__(self):
        return f"{self.lastname}, {self.firstname} ({self.state}) appointed by {self.pres} in {self.yrappt} served until: {self.yrleft}"
    def __repr__(self):
        return "haha"
    def __lt__(self,other):
        return self.lastname<other.lastname

try:
    infile =open(get_absolute_path("JusticesDict.dat"),'rb')
    JusticesDict=pickle.load(infile)
    infile.close()
except FileNotFoundError:
    print('FNF')
    quit()

try:
    for j in JusticesDict.items():
        print(j)
except Exception as ex:
    print(ex)
    quit()


justiceList=[]
for x in JusticesDict.items():
    b=x[1]
    print(x)
    newjustice = Justice(b['state'],b['yrLeft'],b['yrAppt'],b['pres'],x[0])
    justiceList.append(newjustice)

justiceList.sort()
print(*[x for x in justiceList],sep="\n")