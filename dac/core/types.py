
def isInt(prospect):
    if type(prospect) == int:
        return True
    return False

def isBool(prospect):
    if type(prospect) == str:
        if prospect == 'true':
            return True
        if prospect == 'false':
            return True
    if type(prospect) == bool:
        return True
    return False

def isList(prospect):
    if type(prospect) == list:
        return True
    return False

def isString(prospect):
    if type(prospect) == str:
        return True
    return False

def assume_type(inp):
    if isInt(inp):
        return int
    if isBool(inp):
        return bool
    if isList(inp):
        return list
    try:
        int(inp)
        return int
    except ValueError:
        pass

    return str