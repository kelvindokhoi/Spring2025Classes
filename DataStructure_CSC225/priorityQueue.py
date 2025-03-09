# priorityQueue.py

import heapq

class Customer():
    def __init__(self,disabled,fastpass,name):
        self.disabled = disabled
        self.fastpass = fastpass
        self.name = name
    def __str__(self):
        return self.name
    def __lt__(self,other):
        if self.name == 'Todd' and other.name!='Todd':
            return True
        if other.name == 'Todd' and self.name!='Todd':
            return False
        if self.disabled and not other.disable:
            return True
        if not self.disabled and other.disable:
            return False
        if self.fastpass and not other.fastpass:
            return True
        if not self.fastpass and other.fastpass:
            return False
        return self.name <other.name

customers = []
heapq.heapify(customers)
while True:
    try:
        print('1) Add a guest')
        print('2) get next guest in line')
        ans = int(input('Your choice: '))
        if ans==1:
            name=input('name? ')
            disabled = input('Disabled? y/n: ')
            fastpass = input('Fastpass? y/n: ')
            newCustomer = Customer(disabled=='y',fastpass=='y',name)
            heapq.heappush(customers,newCustomer)
        elif ans==2:
            nextCustomer = heapq.heappop(customers)
            print(nextCustomer)

    except Exception as e:
        print(e)
        
