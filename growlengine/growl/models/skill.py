import logging

from django.db import models
from django.db.models.signals import post_save
from growl.models.basemodel import BaseModel

logger = logging.getLogger(__name__)

class SkillManager(models.Manager):
    pass

class Skill(BaseModel):
    game = models.ForeignKey('Game')
    name = models.CharField(max_length=256)
    description = models.TextField()
    skill_group = models.ForeignKey('SkillGroup')
    attribute_primary = models.ForeignKey('Attribute', related_name='attribute_primary_set')
    attribute_secondary = models.ForeignKey('Attribute', related_name='attribute_secondary_set')
    skill_points_cost = models.IntegerField(default=250)
    skill_points_cost_level_multiplier = models.IntegerField(default=5)
    skill_points_cost_difficulty_multiplier = models.IntegerField(default=1)
    level_max = models.IntegerField(default=5)
    skill_requirement_primary_id = models.IntegerField(default=-1)
    skill_requirement_primary_level = models.IntegerField(default=-1)
    skill_requirement_secondary_id = models.IntegerField(default=-1)
    skill_requirement_secondary_level = models.IntegerField(default=-1)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)

    # effects
    effect_attribute_change_per_level = models.BooleanField(default=False)
    attribute_change_per_level_value = models.IntegerField(default=0)
    attribute_change_per_level_attribute_id = models.IntegerField(default=-1)

    objects = SkillManager()

    class Meta:
        db_table = 'growl_skill'
        app_label = 'growl'

    def __unicode__(self):
        return self.name

    def __json__(self):
        json = {}
        json['id'] = self.id
        json['game_id'] = self.game_id
        json['name'] = self.name
        json['description'] = self.description
        json['skill_group_id'] = self.skill_group_id
        json['attribute_primary_id'] = self.attribute_primary_id
        json['attribute_secondary_id'] = self.attribute_secondary_id
        json['skill_points_cost'] = self.skill_points_cost
        json['skill_points_cost_level_multiplier'] = self.skill_points_cost_level_multiplier
        json['skill_points_cost_difficulty_multiplier'] = self.skill_points_cost_difficulty_multiplier
        json['level_max'] = self.level_max
        json['skill_requirement_primary_id'] = self.skill_requirement_primary_id
        json['skill_requirement_primary_level'] = self.skill_requirement_primary_level
        json['skill_requirement_secondary_id'] = self.skill_requirement_secondary_id
        json['skill_requirement_secondary_level'] = self.skill_requirement_secondary_level
        # effects
        json['effect_attribute_change_per_level'] = str(self.effect_attribute_change_per_level)
        json['attribute_change_per_level_value'] = self.attribute_change_per_level_value
        json['attribute_change_per_level_attribute_id'] = self.attribute_change_per_level_attribute_id
        #json['created'] = str(self.created)
        #json['modified'] = str(self.modified)

        return json

def post_save_cache(sender, **kwargs):
    instance = kwargs.get('instance')
    logger.debug('post save!')

post_save.connect(post_save_cache, sender=Skill)