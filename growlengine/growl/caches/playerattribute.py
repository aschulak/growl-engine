import logging
from django.core.cache import cache

logger = logging.getLogger(__name__)

# forever
CACHE_TIMEOUT = None

def get_player_attribute_from_cache(player_attribute_id):
    key = _player_attribute_cache_key(player_attribute_id)
    player_attribute = cache.get(key)
    if not player_attribute:
        logger.debug('cache: player_attribute not found: ' + player_attribute_id)
    return player_attribute

def store_player_attribute_in_cache(player_attribute):
    key = _player_attribute_cache_key(player_attribute.id)
    cache.set(key, player_attribute, CACHE_TIMEOUT)
    logger.debug('cache: stored player_attribute: ' + str(player_attribute))

def delete_player_attribute_from_cache(player_attribute_id):
    key = _player_attribute_cache_key(player_attribute_id)
    cache.delete(key)

###
### PRIVATE
###

def _player_attribute_cache_key(player_attribute_id):
    return 'growl' + ':' + 'PlayerAttribute:' + str(player_attribute_id)