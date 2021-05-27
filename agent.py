import random
from gpt_api import (
    get_animal,
    get_single_why,
    get_comparison_why,
    get_insane_comparison_why,
    random_name_generator,
)
from concept_net_api import (
    get_related_to,
    get_animals_from_class,
    get_classes_from_animal,
)


class Agent:
    def __init__(self) -> None:
        self.name = random_name_generator()
        self.current_animal = None
        self.animal_dict = {}
        self.insane_comparison = False
        self.cn_loop_check = 0

    def _get_name(self) -> str:
        return self.name

    def _get_current_animal(self) -> None:
        return self.current_animal

    def _set_current_animal(self, animal: str) -> None:
        self.current_animal = animal

    def generate_what_gpt(self):
        while True:
            what_animal = "".join(get_animal().strip()).lower()
            if what_animal != None or len(what_animal) >= 5:
                if what_animal not in self.animal_dict:
                    # print("WHAT ANIMAL:", what_animal)
                    return what_animal
                self.animal_dict[what_animal] = what_animal
            continue

    def generate_what_concept_net(self, animal: str) -> str:
        """
        Generates an animal that is similar to the argument animal via concept net
        """
        # print("animal:", animal)
        query = get_classes_from_animal("".join(animal).strip())
        # print(query)
        for i in range(len(query)):
            if query[i] is not None:
                # ASSUMES THAT THIS IS GOING TO RETURN SOMETHING
                if len(get_animals_from_class(query[i])) > 1:
                    concept_net_response: str = random.choice(
                        get_animals_from_class(query[i])
                    )
                    print("CN!")
                    self.insane_comparison = False
                    self.cn_loop_check += 1
                    if self.cn_loop_check > 10:
                        self.cn_loop_check = 0
                        break
                    return concept_net_response.strip()
        # if this does not work, rely on GPT to get the next animal:
        fallback = self.generate_what_gpt()
        # UN-COMMENT THIS TO MAKE MORE CREATIVE - MIGHT BACKFIRE SO USE w/ CAUTION
        # self.insane_comparison = True
        print("GPT!")
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
