import logging

from django.db import models
from django.db.models.signals import post_save
from growl.models.basemodel import BaseModel
from growl.caches.currency import store_currency_in_cache

logger = logging.getLogger(__name__)

class CurrencyManager(models.Manager):
    pass

class Currency(BaseModel):
    game = models.ForeignKey('Game')
    name = models.CharField(max_length=256)
    description = models.TextField()
    value_min = models.IntegerField(default=0)
    value_max = models.IntegerField(default=-1) # unlimited
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    objects = CurrencyManager()

    class Meta:
        db_table = 'growl_currency'
        app_label = 'growl'

    def __unicode__(self):
        return self.name

    def __json__(self):
        json = {}
        json['id'] = self.id
        json['game_id'] = self.game_id
        json['name'] = self.name
        json['description'] = self.description
        json['value_min'] = self.value_min
        json['value_max'] = self.value_max
        #json['created'] = str(self.created)
        #json['modified'] = str(self.modified)

        return json

def post_save_cache(sender, **kwargs):
    instance = kwargs.get('instance')
    store_currency_in_cache(instance)
    logger.debug('post save!')

post_save.connect(post_save_cache, sender=Currency)