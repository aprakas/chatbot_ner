from django.core.cache import caches
cached_ml = caches['redis_ml']
cached_ml_dest = caches['redis_ml_dest']


def set_cache_ml(variable_name, variable_value, expiry_time=172800):
    """
    Stores the cache data in a cache
    """
    return cached_ml.set(variable_name, variable_value, expiry_time)


def get_cache_ml(variable_name):
    """
    Gets the data from the cache
    if data is not present then it will return None
    :return:
    """
    response = cached_ml.get(variable_name)
    return response


def set_cache_ml_dest(variable_name, variable_value, expiry_time=172800):
    """
    Stores the cache data in a cache
    """
    return cached_ml_dest.set(variable_name, variable_value, expiry_time)