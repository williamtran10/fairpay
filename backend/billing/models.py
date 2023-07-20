from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} {self.cost}"


class Customer(models.Model):
    table_id = models.PositiveIntegerField()
    tip = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.table_id} {self.tip}"


class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['customer_id', 'item_id'], name='unique_customer_item_combination'
            )
        ]

    def __str__(self):
        return f"{self.customer_id} {self.item_id} {self.amount}"
