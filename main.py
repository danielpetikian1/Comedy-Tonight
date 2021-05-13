from agent import Agent


def main():
    agent_1 = Agent()
    agent_2 = Agent()
    # keep track of already mentioned animals (todo)
    animal_dict = {}
    print("Comedy Tonight Script Generator v1.0: \n")
    for _ in range(0, 10):
        # check to see if the current animal is not none
        if agent_2.get_current_animal is not None:
            agent_one_animal: str = agent_1.generate_what_sentence()
        else:
            agent_one_animal: str = agent_1.generate_what_sentence(
                agent_2.get_current_animal
            )
        agent_one_why: str = agent_1.generate_why_sentence()
        # print to console
        print(f"{agent_one_animal} - {agent_one_why} \n")
        if agent_1.get_current_animal is not None:
            agent_two_animal: str = agent_2.generate_what_sentence()
        else:
            agent_two_animal: str = agent_2.generate_what_sentence(
                agent_1.get_current_animal
            )
        agent_two_why: str = agent_2.generate_why_sentence()
        # print to console
        print(f"{agent_two_animal} - {agent_two_why} \n")


if __name__ == "__main__":
    main()
