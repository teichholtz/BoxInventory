from django.db import models

class Box(models.Model):
    box_number = models.CharField(max_length=30, unique=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['box_number']

    def __str__(self):
        return f'Box {self.box_number}'

    @property
    def item_count(self):
        return self.items.count()

class InventoryItem(models.Model):
    box = models.ForeignKey(Box, related_name='items', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['description']

    def __str__(self):
        return f'{self.description} (Box {self.box.box_number})'
