from django.db.models import Sum
from django.db.models.query import QuerySet
from django.forms import models


class MyCustomQuerySet(QuerySet):
    def my_custom_method(self, *args, **kwargs):
        # Add custom logic here
        # Use super () to call the original method and then add the code
        # Or override the method entirely
        # Suppose we want to add a method to return the sum of a specific field
        return self.aggregate(total=Sum('my_field'))['total']

class MyModel(models.Model):
    my_field = models.IntegerField()
    # Other fields...
    objects = MyCustomQuerySet.as_manager()

total = MyModel.objects.my_custom_method()