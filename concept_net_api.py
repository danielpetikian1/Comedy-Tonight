import requests
import random

def main():
    """
    Used for testing the API
    """
    # print the animals that are related to this thing
    print(get_related_to("donkey"))
    # call this if we need to categorize the current animal
    print(get_classes_from_animal("cat"))
    # call this if we need to find some new animal
    #print(get_animals_from_class(get_classes_from_animal("donkey")[2]))

    print(get_related_to("horse"))
    # call this if we need to categorize the current animal
    print(get_classes_from_animal("horse"))
    # call this if we need to find some new animal
    print(get_animals_from_class(get_classes_from_animal("horse")[0]))
    print(get_class_of_object('pizza'))
    print(get_object_from_class('dessert',[]))


def get_related_to(arg: str) -> list:
    """
    Given some animal, return animals that are related. This usually returns more specific animals.
    """
    lower_arg = arg.lower()
    response = requests.get(
        f"http://api.conceptnet.io/query?end=/c/en/{lower_arg}&rel=/r/IsA&limit=1000"
    )
    obj = response.json()
    animals = [edge["start"]["label"] for edge in obj["edges"]]
    return animals


def get_animals_from_class(cls: str) -> list:
    """
    Given some class, return the animals that belong to this class
    """
    lower_type = cls.lower()
    response = requests.get(
        f"http://api.conceptnet.io/query?end=/c/en/{lower_type}/n/wn/animal&rel=/r/IsA&limit=1000"
    )
    obj = response.json()
    animals = [edge["start"]["label"] for edge in obj["edges"]]
    return animals


def get_classes_from_animal(animal: str) -> list:
    """
    Given some animal, return the types
    """
    lower_type = animal.lower()
    response = requests.get(
        f"http://api.conceptnet.io/query?start=/c/en/{lower_type}/n/wn/animal&rel=/r/IsA&limit=1000"
    )
    obj = response.json()
    animals = [edge["end"]["label"] for edge in obj["edges"]]
    return animals

def get_class_of_object(object: str):
    obj = object.lower()
    objsearch = obj.replace(' ','_') 
    response = requests.get(f"http://api.conceptnet.io/c/en/{objsearch}?rel=/r/IsA&limit=1000")

    

    file = response.json()
    
    edges = list(filter(lambda edge: not(edge['surfaceText'] == None) and ("[[" + obj + "]] is related to " in edge['surfaceText'] or \
    "[[" + obj + "]] is a type of " in edge['surfaceText']),
     file['edges']))
    print(edges)
    classes = [(edge['end']['label'], edge['end']['sense_label']) for edge in edges]
    weights = [edge['weight'] for edge in edges]
    print(classes)
    print(weights)
    clss = classes[weights.index(max(weights))]

    while (clss  == obj):
        weights.pop(weights.index(max(weights)))
        classes.pop(weights.index(max(weights)))
        clss = classes[weights.index(max(weights))]

    if clss[0:2] == "a ":
        clss = clss[2:]
    elif clss[0:3] == "an ":
        clss  = clss[3:]
    return clss

def get_object_from_class(clss: str, lstofsaid: list):
    domain = clss.lower()
    file = requests.get(f"http://api.conceptnet.io/c/en/{domain.replace(' ','_')}?rel=/r/IsA&limit=1000")

    file = file.json()
    str1 = "is related to " +  "[[" + domain + "]]"
    str2 = "is a type of " +  "[[" + domain + "]]"
    
    edges = list(filter(lambda edge: not(edge['surfaceText'] == None) and not(edge['start']['label'] in lstofsaid) and (str1  in edge['surfaceText'] or \
    str2 in edge['surfaceText']), file['edges']))
    lstofobjects = list(map(lambda edge: edge['start']['label'], edges))
    object_to_return = random.choice(lstofobjects)
    lstofsaid.append(object_to_return)
    return object_to_return

if __name__ == "__main__":
    main()