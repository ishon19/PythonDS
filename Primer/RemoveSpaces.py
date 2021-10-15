def removeSpacesInBetween(str):
    return " ".join(str.split())


str = "  this      is         a spacy text"
print(removeSpacesInBetween(str))
