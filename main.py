from agent import Agent


def main():
    # define agents
    agent_1 = Agent()
    agent_2 = Agent()
    # keep track of iterations and animals mentioned
    iterations = 0
    num_iterations = 4
    animal_dict = {}
    while iterations < num_iterations:
        # if the first run
        if iterations == 0:
            # agent 1 gets a brand new animal
            agent_1._set_current_animal(agent_1.generate_what_gpt())
            print(
                f"I think the best pet is the {agent_1._get_current_animal()}. {agent_1.generate_why_sentence()}"
            )
            # give agent two some new animal. this is based on agent 1's previous animal
            agent_2._set_current_animal(
                agent_2.generate_what_concept_net(agent_1._get_current_animal())
            )
            print(
                f"Well I think the best pet is the {agent_2._get_current_animal()}. {agent_2.generate_why_sentence_comparison(agent_1._get_current_animal(), agent_2._get_current_animal())}"
            )
        # if not we can just run through
        else:
            # agent 1 gets a brand new animal
            print("AGENT 1\n")
            agent_1._set_current_animal(
                agent_1.generate_what_concept_net(agent_2._get_current_animal())
            )
            print(
                f"How about the {agent_1._get_current_animal()}. {agent_1.generate_why_sentence_comparison(agent_2._get_current_animal, agent_1._get_current_animal)}"
            )
            print("AGENT 2\n")
            # give agent two some new animal. this is based on agent 1's previous animal
            agent_2._set_current_animal(
                agent_2.generate_what_concept_net(agent_1._get_current_animal())
            )
            print(
                f"What about the {agent_2._get_current_animal()}. {agent_2.generate_why_sentence_comparison(agent_1._get_current_animal(), agent_2._get_current_animal())}"
            )
        # iterate
        iterations += 1


if __name__ == "__main__":
    main()