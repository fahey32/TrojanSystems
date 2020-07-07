from django.db import models
from django.contrib.auth.models import User


# Inventory Model with fields
class partslist(models.Model):
    partnumber = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=20)
    stockonhand = models.IntegerField(blank=True)
    minimumstock = models.IntegerField(blank=True)
    reorderqtys = models.IntegerField(blank=True)
    boxsize = models.IntegerField(blank=True)
    leadtime = models.CharField(max_length=50)
    weight = models.IntegerField(blank=True)

    def __str__(self):
        return 'Part : {0} ' \
               'Description : {1} ' \
               'Location : {2} ' \
               'S.O.H : {3}' \
            .format(self.partnumber,
                    self.description,
                    self.location,
                    self.stockonhand)


class suppliers(models.Model):
    supplier = models.CharField(max_length=50)
    phonenumber = models.IntegerField(blank=True)
    address = models.CharField(max_length=200)
    customeraccountnumber = models.CharField(max_length=50)

    def __str__(self):
        return self.supplier

# lookup for many to many relationship between parts and suppliers
class partsuppliers(models.Model):
    partsupplier = models.ForeignKey(suppliers, on_delete=models.CASCADE)
    partnumber = models.ForeignKey(partslist, on_delete=models.CASCADE)
    preferred = models.BooleanField(default=False)

# class part_comments(models.Model):
#     timestamp = models.DateTimeField(auto_now_add=True)
#     author = models.ForeignKey(User, on_delete=models.PROTECT)
#     part = models.ForeignKey(partslist, on_delete=models.PROTECT)
#     comment = models.TextField()