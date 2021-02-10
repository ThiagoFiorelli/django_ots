from django.db import models
# from channel.models import Channel
# from pool.models import Pool

class Publish(models.Model):
    # id_pool = models.ForeignKey(Pool, on_delete=models.CASCADE, null=False)
    # id_channel = models.ForeignKey(Channel, on_delete=models.CASCADE, null=False)
    id_pool = models.IntegerField(null=False)
    id_channel = models.IntegerField(null=False)
    initial_date = models.DateTimeField(null=False, blank=False)
    final_date = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=False)
