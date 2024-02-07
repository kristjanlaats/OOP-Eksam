class cal():                            
    def __init__(self,a,b):             
        self.a = a
        self.b = b

    def liitmine(self):                
        return self.a + self.b
    #täpsustab pythonile mis on liitmine
    def lahutamine(self):               
        return self.a - self.b
    #täpsustab pythonile mis on lahutamine
    def korrutamine(self):              
        return self.a * self.b
    #täpsustab pythonile mis on korrutamine
    def jagamine(self):                 
        return self.a / self.b
    #täpsustab pythonile mis on jagamine
    def jaak(self):                     
        return self.a % self.b
    #täpsustab pythonile mis on jaagi otsimine
    def ruutjuur(self):                 
        return self.a ** self.b
    #täpsustab pythonile mis on juurimine
    def kas_on_suurem(self):
        return self.a > self.b
    #täpsustab pythonile funktsiooni
    def sorteeri(self):
        return sorted(self.a, self.b)
    def kas_on_väiksem(self):
        return self.a < self.b
    #täpsustab pythonile funktsiooni
a = int(input("Sisesta esimene number: "))
#küsib et kasutaja sisestaks tema esimese arvu millega arvutada
b = int(input("Sisesta teine number: "))
#küsib et kasutaja sisestaks tema teise arvu millega arvutada
kalk = cal(a,b)                         
while True:
    def menu():
        x = ('1. Liitmine \n2. lahutamine\n3. korrutamine\n4. jagamine\n5. Jäägi leidmine\n6. Ruutjuure leidmine.\n7. Kas on suurem \n8.Sorteeri\n9 Kas on väiksem')
        print(x)
    menu()
    valik = int(input('Sisesta üks valikutest: '))
    #küsib et millist funktsiooni sa tahaksid kasutada 
    if valik == 1:
        print("Vastus: ",kalk.liitmine())
        break
    #prindib vastuse kui valiti liitmine
    elif valik == 2:
        print("Vastus: ",kalk.lahutamine())
        break
    #prindib vastuse kui valiti lahutamine
    elif valik == 3:
        print("Vastus: ",kalk.korrutamine())
        break
    #prindib vastuse kui valiti korrutamine
    elif valik == 4:
        print("Vastus: ",kalk.jagamine())
        break
    #prindib vastuse kui valiti jagamine
    elif valik == 5:
        print("Vastus: ",kalk.jaak())
        break
    #prindib vastuse kui valiti Jäägi leidmine
    elif valik == 6:
        print("Vastus: ",kalk.ruutjuur())
        break
    #prindib vastuse kui valiti Ruutjuure leidmine
    elif valik == 0:
        print('Sisesta uuesti üks liitmise operaator')
    elif valik == 7:
        
        print("vastus: ",kalk.kas_on_suurem())
    elif valik == 8:
        
        print("Vastus ",sorted(self.a, self.b))
    elif valik == 9:
        
        print("vastus: ",kalk.kas_on_väiksem())   
    break




