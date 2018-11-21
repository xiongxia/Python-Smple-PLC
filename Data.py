import json

class strutUploadCollectData:
    def __init__(self,deviceId,quotaId,value):
        self.deviceId=deviceId
        self.quotaId=quotaId
        self.value=value
    def toString(self):
        data_json=json.dumps(self.__dict__)
        return str(data_json)
