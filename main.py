from agent import Agent
import time


def main():
    agent_1 = Agent()
    agent_2 = Agent()
    # keep track of time of execution
    start_time = time.time()
    # keep track of already mentioned animals
    animal_dict = {}
    iterations: int = 0
    print("Comedy Tonight Script Generator v1.1: \n")
    # number of iterations
    while iterations < 4:
        # check to see if the current animal is not none
        temp_agent_one_animal: str = None
        if agent_2.get_current_animal() is not None:
            temp_agent_one_animal = agent_1.generate_what_sentence()
            if temp_agent_one_animal not in animal_dict:
                agent_one_animal: str = temp_agent_one_animal
            else:
                # the animal was in the dict, continue
                continue
        # temp2 is none
        else:
            agent_one_animal: str = agent_1.generate_what_sentence(
                agent_2.get_current_animal()
            )
        # add this to the animal dictionary
        animal_dict[agent_one_animal] = agent_one_animal
        agent_one_why: str = agent_1.generate_why_sentence()
        # print to console
        print("AGENT ONE: ")
        print(f"{agent_one_animal} - {agent_one_why} \n")
        ### NOW FOR AGENT TWO
        temp_agent_two_animal: str = None
        if agent_1.get_current_animal() is not None:
            temp_agent_two_animal = agent_2.generate_what_sentence()
            if temp_agent_two_animal not in animal_dict:
                agent_two_animal: str = temp_agent_two_animal
            else:
                continue
        else:
            agent_two_animal: str = agent_2.generate_what_sentence(
                agent_1.get_current_animal()
            )
        # add this to the animal dictionary
        animal_dict[agent_two_animal] = agent_two_animal
        agent_two_why: str = agent_2.generate_why_sentence()
        # print to console
        print("AGENT TWO: ")
        print(f"{agent_two_animal} - {agent_two_why} \n")
        iterations += 1
    # print the time results
    total_run_time_seconds = time.time() - start_time
    print(f"TOTAL TIME IN SECONDS: {total_run_time_seconds} seconds")
    print(f"TOTAL TIME IN MINUTES: {total_run_time_seconds/60} minutes")


if __name__ == "__main__":
    main()
