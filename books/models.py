from django.db import models


class Book(models.Model):
    
    STATUS_CHOICES = (
        ('C', 'Completed'),
        ('R', 'Reading'),
        ('W', 'WhishList'),
    )
    PRIORITY_CHOICES = (
        ('h', 'high'),
        ('m', 'mid'),
        ('l', 'low'),
    )
    name = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    details = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)
    rating = models.IntegerField(null=True, blank=True)
    
    class Meta:
        ordering = ['due_date', 'name']
        unique_together = ['name', 'author']
    
    def __str__(self):
        return f'{self.name} by {self.author}'
    
    def get_due_date(self):
        if self.due_date:
            return self.due_date
        else:
            return 'Not set yet'



class Blog(models.Model):
    
    STATUS_CHOICES = (
        ('C', 'Completed'),
        ('R', 'Reading'),
        ('W', 'WhishList'),
    )
    PRIORITY_CHOICES = (
        ('h', 'high'),
        ('m', 'mid'),
        ('l', 'low'),
    )
    title = models.CharField(max_length=150)
    link = models.URLField(max_length=300)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    due_date = models.DateField(blank=True, null=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)

    class Meta:
        verbose_name = "Blog/Article"
        verbose_name_plural = "Blog/Articles"
        ordering = ['due_date', 'title']
    
    def __str__(self):
        return f'{self.title}'
    
    def get_due_date(self):
        if self.due_date:
            return self.due_date
        else:
            return 'Not set yet'