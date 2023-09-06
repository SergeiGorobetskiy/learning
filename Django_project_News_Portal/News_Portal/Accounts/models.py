# from django.contrib.auth.models import User
#
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)
#     name = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)
#     address = models.CharField(max_length=200, null=True)
#
#     def __str__(self):
#         return self.name