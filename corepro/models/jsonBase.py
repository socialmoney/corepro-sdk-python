__author__ = 'socialmoneydev'
import json

class JsonBase(object):

    def isHashedPayload(self):
        return False

    def __init__(self):
        pass

    def fromJson(self, jsonString, classDefs):
        dct = {}
        if jsonString is not None:
            dct = json.loads(jsonString)
        return self.fromDict(dct, classDefs)

    def fromDict(self, dct, classDefs):
        if dct is not None:
            for k,v in dct.items():
                if classDefs is None or k not in classDefs:
                    if k in self.__dict__:
                        self.__dict__[k] = v
                else:
                    ct = classDefs[k]
                    if isinstance(v, list):
                        arr = []
                        for item in v:
                            obj = ct()
                            obj.fromDict(item, None)
                            arr.append(obj)
                        self.__dict__[k] = arr
                    elif ct().isHashedPayload() == True:
                        d = {}
                        for subkey, subitem in v.items():
                            obj = ct()
                            obj.fromDict(subitem, None)
                            d[subkey] = subitem
                        self.__dict__[k] = d
                    else:
                        obj = ct()
                        obj.fromDict(v, None)
                        self.__dict__[k] = obj
        return self

    def toJson(self):
        dct = self.toDict()
        return json.dumps(dct)

    def toDict(self):
        d = dict()
        for k,v in self.__dict__.items():
            if v is not None:
                if isinstance(v, JsonBase):
                    d[k] = v.toDict()
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
