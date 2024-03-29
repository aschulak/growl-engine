import logging

from growl.api.exception import GrowlException
from growl.api.player import get_player
from growl.api.skill import get_skill
from growl.api.playerskill import create_player_skill
from growl.api.playerskill import get_player_skill
from growl.api.playerskilltrainingplan import create_player_skill_training_plan
from growl.api.playerskilltrainingplan import get_player_skill_training_plan
from growl.api.playerskilltrainingplan import delete_player_skill_training_plan

logger = logging.getLogger(__name__)

def inject_skill(game, player, skill):
    # check for existing player skill
    player_skill = get_player_skill(player.id, skill.id)
    if player_skill:
        raise GrowlException('Skill already injected')

    logger.debug('creating new player skill')
    player_skill = create_player_skill(game, player, skill, level=0)
    return player_skill

def train_skill(game, player, skill):
    player_skill = get_player_skill(player.id, skill.id)

    # check if player_skill is injected
    if not player_skill:
        raise GrowlException('Skill not injected')

    # check if player_skill is maxed out
    if player_skill.level == skill.level_max:
        raise GrowlException('Skill at max level')

    # TODO check for skill requirements

    # check if there is already a plan
    player_skill_training_plan = get_player_skill_training_plan(player.id)
    if player_skill_training_plan:
        raise GrowlException('Training plan exists')

    player_skill_training_plan = create_player_skill_training_plan(game, player, skill)
    return player_skill_training_plan

def cancel_train_skill(game, player):
    # check if there is already a plan
    player_skill_training_plan = get_player_skill_training_plan(player.id)

    if not player_skill_training_plan:
        raise GrowlException('No training plan')

    delete_player_skill_training_plan(player_skill_training_plan)

