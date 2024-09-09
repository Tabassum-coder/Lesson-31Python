class India():

    def capital(self):
        print("New Delhi is capital of India")
    
    def language(self):
        print("language spoken is hindi")

    def typeofcountry(self):
        print("India is developing country")

class USA():
     def capital(self):
        print("Washington D.C is capital of USA")
    
     def language(self):
        print("language spoken is English")

     def typeofcountry(self):
        print("USA is developed country")

Ind=India()
US=USA()

for country in (Ind,US):
    country.capital()
    country.language()
    country.typeofcountry()