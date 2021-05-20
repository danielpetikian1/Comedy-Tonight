import requests


def main():
    animal = "lion"
    type = "feline"
    print(get_capable(animal))
    print(get_types_from_animal(animal))
    # gives us verbose list of types of this animal
    print(get_animals_from_type(type))
    # gives us list of new animals
    print(get_related_to(get_animals_from_type(type)[0]))
    # from here can see if something inside of get_related_to(get_animals_from_type(type)[0]) has a 
    # get capable array, and if not, we need to get a new one. If none have it, maybe do a switch to
    # something brand new
    print(get_types_from_animal('elephant'))
    #print(get_stuff_from_loc('forest'))
    #daniels_function('lion')
    #print(get_stuff_from_loc('ocean'))
    print(filter_by(get_stuff_from_loc('forest'), 'animal'))

def get_locations(animal: str):
    '''
    takes an animal and finds where it lives
    '''
    lower_animal = animal.lower()

    response = requests.get(f"http://api.conceptnet.io/query?start=/c/en/{lower_animal}&rel=/r/AtLocation&limit=1000")
    obj = response.json()
    
    locations = [edge["end"]["label"] for edge in obj["edges"]]
    return locations

def get_stuff_from_loc(loc: str):
    lower_loc = loc.lower()

    response = requests.get(f"http://api.conceptnet.io/c/en/{lower_loc}?rel=/r/AtLocation&limit=1000")
    
    obj = response.json()
    #print(obj)
    obj1 = list(filter(lambda x:  x['start']['language'] == 'en' and (x['weight'] > 3 or x['weight'] < 1.5), obj['edges']))
    #print(obj)
    #print(list(filter(lambda x:x.lower().find(lower_loc) == -1 and (len(x.split()) < 3), [edge["start"]["label"] for edge in obj1 ])))
    
    
    #locations = [filter(lambda x: x == lower_loc or x == loc, ])]
    return list(filter(lambda x:x.lower().find(lower_loc) == -1 and (len(x.split()) < 3), [edge["start"]["label"] for edge in obj1]))
    #list(filter(lambda x:x.lower().find(lower_loc) == -1 and (len(x.split()) < 3), [edge["start"]["label"] for edge in obj1 ]))

def get_capable(animal: str) -> list:
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
    capabilities = [edge["start"]["label"] for edge in obj["edges"]]
    return capabilities

def filter_helper(object: str, fltr: str):
    lower_object = object.lower()
    response = requests.get(
        f"http://api.conceptnet.io/c/en/{lower_object}?rel=/r/IsA&limit=1000"
    )
    obj = response.json()
    labels = [fltr in edge['end']['label'].lower() for edge in obj['edges']]
    if True in labels:
        return True
    else: return False

def filter_by(lst: list, fltr: str):
    filtered = filter(lambda x: filter_helper(x, fltr.lower()), lst)
    return list(filtered)

def get_types_from_animal(animal: str) -> list:
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

def daniels_function(animal: str):
    '''
    takes an animal 
        looks is a type of 
            takes 5 related terms
                finds capable of

        looks at 3 locations
    '''
    types = get_types_from_animal(animal)
    print(types)
    print('animals',get_animals_from_type('big_cat'))
    print(get_capable(get_animals_from_type('big_cat')[0]))
    return

def get_animals_from_type(type: str) -> list:
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

def get_related_to(arg: str) -> list:
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
