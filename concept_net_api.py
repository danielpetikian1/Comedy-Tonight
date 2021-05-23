import requests


def main():
    """
    Used for testing the API
    """
    # print the animals that are related to this thing
    print(get_related_to("donkey"))
    # call this if we need to categorize the current animal
    print(get_classes_from_animal("cat"))
    # call this if we need to find some new animal
    print(get_animals_from_class(get_classes_from_animal("donkey")[2]))

    print(get_related_to("horse"))
    # call this if we need to categorize the current animal
    print(get_classes_from_animal("horse"))
    # call this if we need to find some new animal
    print(get_animals_from_class(get_classes_from_animal("horse")[0]))


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


if __name__ == "__main__":
    main()