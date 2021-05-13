import random
from concept_net_api import (
    get_capable,
    get_types_from_animal,
    get_animals_from_type,
    get_related_to,
)


class Agent:
    def __init__(self) -> None:
        self.current_animal = None

    def get_current_animal(self):
        """
        Get the current animal
        """
        return self.current_animal

    def generate_what_sentence(self, animal: str = "") -> str:
        """
        Generate what sentence takes a type and returns a new animal of that type
        Returns an animal of the type animal the first time around
        """
        # if an arg was not provided, it is the first run
        why_exists = False
        while why_exists == False:
            if animal == "":
                # old query = self.current_animal = random.choice(get_related_to(random.choice(get_animals_from_type("bird"))))
                self.current_animal = random.choice(get_related_to("bird"))
                if self.check_if_why_exits() == True:
                    why_exists = True
                    # return the current animal
                    self.get_current_animal()
                # if not, just do it again
                continue

            # if the first run
            else:
                # get the type of the previous animal
                self.current_animal = random.choice(get_types_from_animal(animal))
                if self.check_if_why_exits() == True:
                    why_exists = True
                    # return the current animal
                    self.get_current_animal()
                # if not, continue
                continue

    def generate_why_sentence(self) -> str:
        """
        Generate a why sentence based on the current animal
        """
        current_animal = self.current_animal
        why_sentence_choices = get_capable(current_animal)
        if len(why_sentence_choices) > 0:
            why_sentence: str = random.choice(why_sentence_choices)
        else:
            why_sentence = "No reason found!"
        return why_sentence

    def check_if_why_exits(self) -> bool:
        """
        Check and see if this animal has some corresponding why sentence
        If it does, return true, else false
        """
        current_animal = self.current_animal
        why_sentence_choices = get_capable(current_animal)
        if len(why_sentence_choices) > 0:
            return True
        return False
