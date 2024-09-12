from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    profile_pic = models.ImageField(null=True, upload_to='profile_media')

    def __str__(self):
        return f'{str(self.last_name).capitalize()} {str(self.first_name)[0]}.'


class Records(models.Model):
    customer_id = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    service_type = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Record for {self.customer_id} on {self.date}'
