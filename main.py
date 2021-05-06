from script_db import ScriptDB


def main():
    agent_1 = ScriptDB("./data/script_db.json")
    agent_2 = ScriptDB("./data/script_db.json")
    print("Comedy Tonight Script Generator v0.1.0: \n\n")
    # for 10 back in forth messages
    for i in range(0, 10):
        print(
            f"{agent_1.generate_what_sentence()} - {agent_1.generate_why_sentence()} \n"
        )
        print(
            f"{agent_2.generate_what_sentence()} - {agent_2.generate_why_sentence()} \n"
        )


if __name__ == "__main__":
    main()