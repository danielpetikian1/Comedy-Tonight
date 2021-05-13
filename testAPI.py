import requests


def main():
    animal = "butterfly"
    type = "lepidopterous_insect"
    print(get_capable(animal))
    print(get_types_from_animal(animal))
    # gives us verbose list of types of this animal
    print(get_animals_from_type(type))
    # gives us list of new animals
    print(get_related_to(get_animals_from_type(type)[0]))
    # from here can see if something inside of get_related_to(get_animals_from_type(type)[0]) has a 
    # get capable array, and if not, we need to get a new one. If none have it, maybe do a switch to
    # something brand new


def get_capable(animal: str):
    """
    function takes in the name of the animal as a string and gives back a list of strings in the form of "can ____"
    """
    lower_animal = animal.lower()
    # GET request sent to the API, specify the query, animal name, and relation (capable of)
    response = requests.get(
        f"http://api.conceptnet.io/query?start=/c/en/{lower_animal}&rel=/r/CapableOf&limit=1000"
    )
    obj = response.json()
    # Looping though the edges
    capabilities = [edge["end"]["label"] for edge in obj["edges"]]
    return capabilities


def get_types_from_animal(animal: str):
    """
    Given an animal, return types
    """
    lower_animal = animal.lower()
    types = []
    response = requests.get(
        f"http://api.conceptnet.io/query?start=/c/en/{lower_animal}/n/wn/animal&rel=/r/IsA&limit=1000"
    )
    obj = response.json()
    types = [edge["end"]["label"] for edge in obj["edges"]]
    return types


def get_animals_from_type(type: str):
    """
    Given some animal, return the types
    """
    lower_type = type.lower()
    response = requests.get(
        f"http://api.conceptnet.io/query?start=/c/en/{lower_type}/n/wn/animal&rel=/r/IsA&limit=1000"
    )
    obj = response.json()
    animals = [edge["end"]["label"] for edge in obj["edges"]]
    return animals

def get_related_to(arg: str):
    """
    Given some animal, return animals that are related
    """
    lower_arg = arg.lower()
    response = requests.get(
        f"http://api.conceptnet.io/query?end=/c/en/{lower_arg}&rel=/r/IsA&limit=1000"
    )
    obj = response.json()
    animals = [edge["start"]["label"] for edge in obj["edges"]]
    return animals


if __name__ == "__main__":
    main()
