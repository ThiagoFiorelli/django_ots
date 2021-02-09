from typing import List
from datetime import datetime
from publish.models import Publish


class PublishController:
    def get_all(self) -> List[Publish]:
        return Publish.objects.all()

    def get_by_id(self, id: int) -> Publish:
        return Publish.objects.filter(id=id).get()

    def create(self, id_pool: int, id_channel: int, initial_date: datetime, 
                final_date: datetime, is_active: bool) -> Publish:
        publish = Publish(id_pool=id_pool, 
                          id_channel=id_channel, 
                          initial_date=initial_date, 
                          final_date=final_date, 
                          is_active=is_active)
        publish.save()
        return publish

    def update(self, id: int, id_pool: int, id_channel: int, initial_date: datetime, 
                final_date: datetime, is_active: bool) -> Publish:
        publish = self.get_by_id(id)
        publish.id_pool = id_pool
        publish.id_channel = id_channel
        publish.initial_date = initial_date
        publish.final_date = final_date
        publish.is_active = is_active
        publish.save()
        return publish

    def delete(self, id: int) -> None:
        publish = self.get_by_id(id)
        publish.delete()