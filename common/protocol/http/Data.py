import json

class strutUploadCollectData:
    def __init__(self,name,value):
        self.name=name
        self.value=value
    def toString(self):
        data_json=json.dumps(self.__dict__)
        return str(data_json)
