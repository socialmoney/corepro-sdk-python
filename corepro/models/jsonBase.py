__author__ = 'socialmoneydev'

import urllib

class JsonBase(object):

    def __init__(self):
        pass

    @staticmethod
    def escape(val):
        return urllib.quote(val)

    def fromJson(self, json, classDefs):
        if json is not None:
            for k,v in json.items():
                if classDefs is None or k not in classDefs:
                    if k in self.__dict__:
                        self.__dict__[k] = v
                else:
                    ct = classDefs[k]
                    if isinstance(v, list):
                        arr = []
                        for item in v:
                            obj = ct()
                            obj.fromJson(item, None)
                            arr.append(obj)
                        self.__dict__[k] = arr
                    else:
                        obj = ct()
                        obj.fromJson(v, None)
                        self.__dict__[k] = obj
        return self

    def toJson(self):
        d = dict()
        for k,v in self.__dict__:
            if v is not None:
                if isinstance(v, JsonBase):
                    d[k] = v.toJson()
                elif isinstance(v, list):
                    if len(v) > 0:
                        arr = []
                        for item in v:
                            h = item.__dict__
                            arr.append(h)
                        d[k] = arr
                else:
                    d[k] = v
        return d
