from django.db import models


class Book(models.Model):
    STATUS_CHOICES = (
        ('C', 'Completed'),
        ('R', 'Reading'),
        ('W', 'WhishList'),
    )
    name = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    details = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    rating = models.IntegerField(null=True, blank=True)
    
    class Meta:
        ordering = ['due_date', 'name']
    
    def __str__(self):
        return f'{self.name} by {self.author}'
    
    def get_due_date(self):
        if self.due_date:
            return self.due_date
        else:
            return 'Not set yet'
    
