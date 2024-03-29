from basemodel import BaseModel
from attribute import Attribute
from developer import Developer
from game import Game
from perk import Perk
from perkeffect import PerkEffect
from player import Player
from playerattribute import PlayerAttribute
from playerperk import PlayerPerk
from playerresource import PlayerResource
from playerskill import PlayerSkill
from playerskilltrainingplan import PlayerSkillTrainingPlan
from resource import Resource
from skill import Skill
from skilleffect import SkillEffect
from skillgroup import SkillGroup

def model_encode(obj):
    enc = None
    try:
        enc = obj.__json__()
    except:
        enc = None

    if enc:
        return enc

    raise TypeError(repr(obj) + " is not JSON serializable")

def model_encode_verbose(obj):
    enc = None
    try:
        enc = obj.__json_verbose__()
    except Exception, e:
        logging.error(e)
        enc = None

    if enc:
        return enc

    raise TypeError(repr(obj) + " is not JSON serializable")
