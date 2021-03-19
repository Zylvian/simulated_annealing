
import logging
import time


def log_time(func):
    def logitmayne(*args, **kwargs):
        t = time.time()
        x = func(*args, **kwargs)
        print(((time.time()-t)*1000))
        return x

    return logitmayne