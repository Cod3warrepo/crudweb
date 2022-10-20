from django.db import models


class StudentDB(models.Model):
    std_roll_no = models.IntegerField(max_length=10, unique=True)
    std_name = models.CharField(max_length=60)
    std_class = models.CharField(max_length=25)

    def __str__(self):
        return self.std_name
    
# class StoreDB(models.Model):
#     storeID = 
#     storeName = 
#     storeSale = 
    
# migration not done
