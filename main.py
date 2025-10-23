# xoop--> Object oriented programming-->Obeyektga yo'naltirilgan programma
# object-->obeyekt-->my_car=Car()
# class-->sinf-->class Car:
# attribute-->Xususiyatlar-->self.color, self.model,self.price,self.birthyear
# method-->drive(), stop(),window(),radio()


сlass Car:
def init(self,brand,model,price,year):
         self.brand=brand
         self.model=model
         self.price=price
         self.year=year
    



my_car = Car("BMW", "M5",120000,2025) #object
your_car=Car("BMW","M3",10000,1326)

class Car:
    def init(self, rusimi,kompaniyasi,narxi):
        self.model = rusimi
        self.brand = kompaniyasi
        self.price = narxi

    def otoldirish(self):
        print(f"{self.model} ishga tushdi!")

    def malumot(self):
        return f"{self.model} mashinasi {self.brand} kompaniyasi tomonida ishlab chiqarilgan va uning narxi {self.price}"
    
    def narxi_in_som(self):
        narx_in_som=self.price*12500
        return narx_in_som


moshinni_nomi=input("Mashinani nomini kiriting: ")
my_car = Car(moshinni_nomi,"Chevrolet",14000)
my_car.otoldirish()
print(my_car.malumot())
print(my_car.narxi_in_som())

my_car2=Car("Jentra","Chevrolet",12000)
my_car2.otoldirish()
print(my_car2.malumot())
print(my_car2.narxi_in_som())