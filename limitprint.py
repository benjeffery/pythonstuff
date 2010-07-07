import pprint
from itertools import islice

def recursive_limit_seq(o, limit=3, seen=[]):
    if id(o) in seen:
            raise StandardError("Cycle found in object to be converted")

    if any(type(o) == type(typ) for typ in [int(), float(), long(), complex(), str(), unicode(), bool(), None]):
        return o

    if any(type(o) == type(typ) for typ in [list(), tuple(), set(), frozenset()]):
        list_out = []
        
        for item in islice(o,limit):
            list_out.append(recursive_limit_seq(item, limit, [id(o)]+seen))
        return list_out

    elif type(o) == type(dict()):
        dict_out = {}
        for key,item in o.items():
            dict_out[key] = recursive_limit_seq(item, limit, [id(o)]+seen)
        return dict_out

    #We have am object or something else:
    return o

def limitprint(o, limit=3):
    pprint.pprint(recursive_limit_seq(o, limit))
