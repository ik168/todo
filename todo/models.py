from django.db import models
from django.utils import timezone

# Create your models here.


class Todo(models.Model):

    task = models.CharField(max_length=1000)
    # created_time = models.DateTimeField('created')
    # updated_time = models.DateTimeField('updated')

    def __repr__(self):
        class_name = self.__class__.__name__
        properties = ('{0} = {1}'.format(k, v) for k, v in self.__dict__.items())
        return '<{0}: \n  {1}\n>'.format(class_name, '\n  '.join(properties))



