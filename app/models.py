from django.db import models

# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    slug = models.SlugField()
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    

class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/category')

class Group(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='group')
    image = models.ForeignKey('Image', on_delete=models.CASCADE, related_name='group')
    

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    product = models.ForeignKey('Product',on_delete=models.CASCADE, related_name='images')
    

class Comment(models.Model):
    class RatingChoice(models.TextChoices):
        Zero = '0'
        One = 'One'
        Two = 'Two'
        Three = 'Three'
        Four = 'Four'
        Five = 'Five'

    rating = models.CharField(max_length=100, choices=RatingChoice.choices, default=RatingChoice.One.value )
    message = models.TextField()
    file = models.FileField(upload_to='media/comments')
    product = models.ForeignKey('Product', on_delete = models.CASCADE, related_name = 'comments')
    

class Attribute_Key(models.Model):
    key_name = models.CharField(max_length=50)


class Attribute_Value(models.Model):
    value_name = models.CharField(max_length=50)


class Attribute(models.Model):
    key = models.ForeignKey('Attribute_Key', on_delete=models.CASCADE)
    value= models.ForeignKey('Attribute_Value', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

