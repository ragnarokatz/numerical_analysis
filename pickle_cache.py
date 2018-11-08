import os
import pickle
import hashlib


def generate_md5_hash(string):
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    return m.hexdigest()


def cache():
    """
    A function that creates a decorator for caching the results of the decorated function "fn".
    """
    def decorator(fn):  # define a decorator for a function "fn"
        def wrapped(*args, **kwargs):   # define a wrapper that will finally call "fn" with all arguments

            filetag = '_'.join((fn.__name__, ) + args)
            cachefile = f'{generate_md5_hash(filetag)}.pk'

            # if cache exists -> load it and return its content
            if os.path.exists(cachefile):
                with open(cachefile, 'rb') as cachehandle:
                    print(f'using cached result from {cachefile}')
                    return pickle.load(cachehandle)

            # execute the function with all arguments passed
            res = fn(*args, **kwargs)

            # write to cache file
            with open(cachefile, 'wb') as cachehandle:
                print(f'saving result to cache {cachefile}')
                pickle.dump(res, cachehandle)

            return res
        return wrapped
    return decorator   # return "customized" decorator
