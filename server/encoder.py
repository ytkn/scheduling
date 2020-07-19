import json
import numpy


def default_method(item):
    if isinstance(item, object) and hasattr(item, '__dict__'):
        return item.__dict__
    else:
        raise TypeError


class NdArrayEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.integer):
            return int(obj)
        elif isinstance(obj, numpy.floating):
            return float(obj)
        elif isinstance(obj, numpy.ndarray):
            return obj.tolist()
        else:
            return super(NdArrayEncoder, self).default(obj)
