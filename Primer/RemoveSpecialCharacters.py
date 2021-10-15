import re
from RemoveSpaces import removeSpacesInBetween


def removeSpecialChars(str):
    return removeSpacesInBetween(re.sub('[`~!@#$%^&*()_+}{\\":,.\|;\']', '', str).strip())


str = "This is @ special$%$ chsr ^&^&^&%^&"
print(removeSpecialChars(str))
