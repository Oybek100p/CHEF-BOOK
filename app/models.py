from django.db import models

class Chef(models.Model):
    Choice_prof = [
        ('Milliy oshpazlik','Milliy oshpazlik'),
        ('Shirinlik' , 'Shirinlik'),
        ('Salat','Salat'),
    ]
    full_name = models.CharField(max_length=150)    
    mutaxassislik = models.CharField(choices=Choice_prof)
    tajriba = models.IntegerField()
    bio = models.TextField()
    email = models.EmailField( max_length=150 )
    telefon = models.IntegerField()

    def __str__(self):
        return f"{self.full_name} {self.mutaxassislik} {self.tajriba}"
    

class Category(models.Model):
    kategoriya = models.CharField(max_length=65)
    tavsif = models.TextField()

    def __str__(self):
        return f"{self.kategoriya} "


    
class Recipe(models.Model):
    nomi = models.CharField(max_length=120)
    tavsif = models.TextField(default="tavsif yo'q")
    ingredientlar = models.TextField()
    kategoriya = models.ForeignKey(Category, on_delete=models.CASCADE)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    yaratilgan = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nomi} {self.kategoriya} {self.chef} {self.yaratilgan}"
    
class Main(models.Model):
    matn = models.CharField(max_length=100)

    def __str__(self):
        return self.matn

    



# Create your models here.
