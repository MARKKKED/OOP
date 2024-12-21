class Spiderman:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def describeSpiderman(self):
        print(f'Name: {self.name}, Age: {self.age}')

class Tobey(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name,age)
        self.movieTitle = movieTitle

class Andrew(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name,age)
        self.movieTitle = movieTitle
        
class Tom(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name,age)
        self.movieTitle = movieTitle
        
tobey = Tobey('tobey', 46, 'Spider-Man(2002)')
andrew = Andrew('andrew', 40, 'The Amazing Spider-Man 2(2014)')
tom = Tom('tom', 28, 'Spider-Man: No Way Home(2021)')

print(f"Name: {tobey.name.upper()} \nMovie: {tobey.movieTitle.upper()}")
print(f"\nName: {andrew.name.upper()} \nMovie: {andrew.movieTitle.upper()}")
print(f"\nName: {tom.name.upper()} \nMovie: {tom.movieTitle.upper()}")