from django.db import models

### class Base ###
class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True

### class Category ###
class Category(Base):
    describe = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Category'
        db_table = 'Category'

    def __str__(self):
        return self.describe   

### Class Product ###
class Product(Base):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    category = models.ForeignKey(Category, related_name='Category', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Product'
        db_table = 'Product'
        ordering = ['category']

    def __str__(self) -> str:
        return self.name

### Class ###
class Evaluetion(Base):
    product = models.ForeignKey(Product, related_name='Product', on_delete=models.CASCADE)
    email = models.EmailField(max_length=50)    
    text = models.TextField()

    class Meta:
        verbose_name = 'Evaluetion'
        db_table = 'Evaluetion'
        unique_together = ['email','product']

    def __str__(self) -> str:
        return self.email
        


