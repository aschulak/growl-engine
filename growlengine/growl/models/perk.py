import logging

from django.db import models
from django.db.models.signals import post_save
from growl.models.basemodel import BaseModel
from growl.caches.perk import store_perk_in_cache

logger = logging.getLogger(__name__)

class PerkManager(models.Manager):
    pass

class Perk(BaseModel):
    game = models.ForeignKey('Game')
    name = models.CharField(max_length=256)
    description = models.TextField()
    choosable = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    objects = PerkManager()

    class Meta:
        db_table = 'growl_perk'
        app_label = 'growl'

    def __unicode__(self):
        return self.name

    def __json__(self):
        json = {}
        json['id'] = self.id
        json['game_id'] = self.game_id
        json['name'] = self.name
        json['description'] = self.description
        json['choosable'] = str(self.choosable)
        try:
            json['perk_effect'] = self.perk_effect
        except:
            pass
        #json['created'] = str(self.created)
        #json['modified'] = str(self.modified)

        return json

def post_save_cache(sender, **kwargs):
    instance = kwargs.get('instance')
    store_perk_in_cache(instance)
    logger.debug('post save!')

post_save.connect(post_save_cache, sender=Perk)