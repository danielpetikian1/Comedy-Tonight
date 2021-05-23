import random
from gpt_api import (
    get_animal,
    get_single_why,
    get_comparison_why,
    get_insane_comparison_why,
)
from concept_net_api import (
    get_related_to,
    get_animals_from_class,
    get_classes_from_animal,
)


class Agent:
    def __init__(self) -> None:
        self.current_animal = None
        self.animal_dict = {}

    def _get_current_animal(self) -> None:
        return self.current_animal

    def _set_current_animal(self, animal: str) -> None:
        self.current_animal = animal

    def generate_what_gpt(self):
        while True:
            what_animal = get_animal()
            if what_animal is not None:
                if what_animal not in self.animal_dict:
                    return what_animal
                self.animal_dict[what_animal] = what_animal
            continue

    def generate_what_concept_net(self, animal: str) -> str:
        """
        Generates an animal that is similar to the argument animal via concept net
        """
        query = get_classes_from_animal(animal)
        for i in range(len(query)):
            if query[i] is not None:
                # ASSUMES THAT THIS IS GOING TO RETURN SOMETHING
                return random.choice(get_animals_from_class(query))
        # if this does not work, rely on GPT to get the next animal:
        fallback = self.generate_what_gpt()
        print("FALLBACK:", fallback)
        return fallback

    def generate_why_sentence(self) -> str:
        """
        Generate a why sentence based on the current animal
        """
        return get_single_why(self.current_animal)

    def generate_why_sentence_comparison(self, animal_1: str, animal_2: str) -> str:
        return get_comparison_why(animal_1, animal_2)

    def generate_insane_why_sentence_comparison(
        self, animal_1: str, animal_2: str
    ) -> str:
        return get_insane_comparison_why(animal_1, animal_2)
