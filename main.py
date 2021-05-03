from script_db import ScriptDB

def main():
    agent_1 = ScriptDB('./data/script_db.json')
    agent_2 = ScriptDB('./data/script_db.json')

    # for 10 back in forth messages
    for i in range(0, 10):
        print(agent_1.generate_random_animal())
        print(agent_2.generate_random_animal())

if __name__ == "__main__":
    main()