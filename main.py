from flask import Flask
from flask.templating import render_template
from agent import Agent

app = Flask(__name__)

# add as the root route
@app.route("/")
def index():
    name_data, data, data_length = run_program()
    # render the template and pass in the parameters
    return render_template(
        "index.html", name_data=name_data, data=data, data_length=data_length
    )


def run_program():
    # define agents
    agent_1 = Agent()
    agent_2 = Agent()
    # agent_pos % 2 == 1? This is agent one
    # agent_pos % 2 == 0? This is agent one
    name_data = {
        "agent_1_name": agent_1._get_name(),
        "agent_2_name": agent_2._get_name(),
    }
    # keep track of iterations and animals mentioned
    iterations = 0
    num_iterations = 3
    # define data
    data = [] * num_iterations
    # animal dictionary
    animal_dict = {}
    while iterations < num_iterations:
        # if the first 
        data.insert(iterations, [])
        if iterations == 0:
            # all of the while loops check for instances where the animal that has been brought up exists in the dict
            # and, if it does, just continue
            while True:
                # agent 1 gets a brand new animal. do the dictionary checks for all of these
                agent_1._set_current_animal(agent_1.generate_what_gpt())
                agent_one_animal = agent_1._get_current_animal()
                # print(agent_one_animal, "IS THE ANIMAL")
                if agent_one_animal not in animal_dict:
                    # add what and why
                    data[iterations].append(
                        f"I think the best pet is the {agent_one_animal}"
                    )
                    data[iterations].append(f"{agent_1.generate_why_sentence()}")
                    animal_dict[agent_one_animal] = agent_one_animal
                    break
                else:
                    continue
            while True:
                # give agent two some new animal. this is based on agent 1's previous animal
                agent_2._set_current_animal(
                    agent_2.generate_what_concept_net(agent_1._get_current_animal())
                )
                agent_two_animal = agent_2._get_current_animal()
                if agent_two_animal not in animal_dict:
                    if agent_2.insane_comparison:
                        # add what and insane why
                        data[iterations].append(
                            f"Well I think the best pet is the {agent_two_animal}"
                        )
                        data[iterations].append(
                            f"{agent_2.generate_insane_why_sentence_comparison(agent_1._get_current_animal(), agent_2._get_current_animal())}"
                        )
                    else:
                        # add what and why
                        data[iterations].append(
                            f"Well I think the best pet is the {agent_two_animal}"
                        )
                        data[iterations].append(
                            f"{agent_2.generate_why_sentence_comparison(agent_1._get_current_animal(), agent_2._get_current_animal())}"
                        )
                    animal_dict[agent_two_animal] = agent_two_animal
                    break
                else:
                    continue
        # if not we can just run through
        else:
            while True:
                # agent 1 gets a brand new animal
                # print("AGENT 1\n")
                agent_1._set_current_animal(
                    agent_1.generate_what_concept_net(agent_2._get_current_animal())
                )
                agent_one_animal = agent_1._get_current_animal()
                if agent_one_animal not in animal_dict:
                    if agent_1.insane_comparison:
                        # add what and insane why
                        data[iterations].append(f"How about the {agent_one_animal}")
                        data[iterations].append(
                            f"{agent_1.generate_insane_why_sentence_comparison(agent_2._get_current_animal(), agent_1._get_current_animal())}"
                        )
                    else:
                        # add what and why
                        data[iterations].append(f"How about the {agent_one_animal}")
                        data[iterations].append(
                            f"{agent_1.generate_why_sentence_comparison(agent_2._get_current_animal(), agent_1._get_current_animal())}"
                        )
                    animal_dict[agent_one_animal] = agent_one_animal
                    break
                else:
                    continue
            while True:
                agent_2._set_current_animal(
                    agent_2.generate_what_concept_net(agent_1._get_current_animal())
                )
                agent_two_animal = agent_2._get_current_animal()
                # print("AGENT 2\n")
                # give agent two some new animal. this is based on agent 1's previous animal
                if agent_two_animal not in animal_dict:
                    if agent_2.insane_comparison:
                        # add what and insane why
                        data[iterations].append(f"How about the {agent_two_animal}")
                        data[iterations].append(
                            f"{agent_2.generate_insane_why_sentence_comparison(agent_1._get_current_animal(), agent_2._get_current_animal())}"
                        )
                    else:
                        # add what and why
                        data[iterations].append(f"How about the {agent_two_animal}")
                        data[iterations].append(
                            f"{agent_2.generate_why_sentence_comparison(agent_1._get_current_animal(), agent_2._get_current_animal())}"
                        )
                    animal_dict[agent_two_animal] = agent_two_animal
                    break
                else:
                    continue
        # iterate
        iterations += 1
    return name_data, data, num_iterations


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)