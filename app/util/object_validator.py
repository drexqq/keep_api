class ObjectValidator():
    @staticmethod
    def validate(obj):
        for k, v in obj:
            if not v:
                    return [k, False]
            if isinstance(v, list):
                if k == "coordinate" and len(v) != 2:
                    return [k, False]
                for i in v:
                    if not i:
                        return [k, False]
        return True