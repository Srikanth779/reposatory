class person:
    def __init__(self,name, money, mood, healthRate):
        self.name=name
        self.money=money

        self.healthRate=healthRate

    def sleep(self,hour):
             if(hour==7):
                 return "happy"
             if(hour<7):
                 return "tried"
             return "lazy"

    def eat(self,maels):
         if(maels==3):
             return "%100 hlt"
         if(maels<3):
             return "%75 hlt"
         return "%50 hlt"

    def work(self,hour):
        mood('happy','tried','lazy')
        if(hour==8):
            print(mood[0])
        if(hour>8):
            print(mood[1])
        print(mood[3])



    def healthRate(self,healthRate):

        if(healthRate<0):
            self.self.healthRate=0
        elif(healthRate>100):
            self.self.healthRate=100
        else:
            self.self.healthRate=healthRate

    def buy(self,items):
        if(items==1):
            money=money*0.1


class employee(person):

        def __init__(self,id, car, email, salary,dict_to_work):
            self.id=id
            self.car=car
            self.email=email
            self.salary=salary
            self.dict_to_work=dict_to_work

        def salary(self,salary):
            if (salary<1000):
                self.salary=1000


        def work(self):
            if(hour==7):
                return "happy"
                if(hour<7):
                    return "tried"
                    return "lazy"

        def drive(self,dis,time):
            dis=self.dis
            time=self.time
            f=car(__car)
            volcity=dic/time
            print ("velocity is"+velocity)




        def refuel(self,gasamount):
            gasamount=100


class car:
     def __init__(self,name, fuelRate, velocity):
         self.name=name
         self.fuelRate=fuelRate
         self.velocity=velocity
     def run(self):
         print("my name is"+self.name);
     def stop(self):
         print("my name is"+self.name);
p=person("seham",4000,"happy",5)
xx=person("seham",700,"lazy",8)
emp=employee(1,'bmww','seham','sehamsamy@yahoo.com',22222)
emp2=employee(1,'lanser','seham','sehamsamy@gmail.com',111)
print(p.sleep(5))
print(p.eat(3))
print(p.name)
print(emp.car)
print(emp2.email)
print(p.buy(1))
