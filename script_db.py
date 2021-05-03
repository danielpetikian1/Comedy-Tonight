import json


class ScriptDB:
    # initialize the animals_db JSON file
    # later, this can be renamed to a more general db of more than just animals
    def __init__(self, path: str) -> None:
        # open and process file
        with open(path) as f:
            json_data = json.load(f)
            self.animals = json_data["animals"]

    # boolean checker to see if some attribute is present in some collection
    def _presentInCollection(self, item, collection) -> bool:
        for i in collection:
            if i in item:
                return True
            else:
                # item was not in collection
                return False