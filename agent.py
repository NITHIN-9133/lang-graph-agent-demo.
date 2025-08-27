
import yaml

def atlas_client(ability, data):
    return f"[ATLAS executed {ability}]"

def common_client(ability, data):
    return f"[COMMON executed {ability}]"

def run_agent(config, input_data):
    state = input_data.copy()
    logs = []
    for stage in config["stages"]:
        stage_name = stage["name"]
        logs.append(f"▶ Stage: {stage_name} ({stage['mode']})")
        for ability_dict in stage["abilities"]:
            for ability, server in ability_dict.items():
                result = atlas_client(ability, state) if server == "ATLAS" else common_client(ability, state)
                logs.append(f"  - {ability} via {server} → {result}")
                state[ability] = "done"
    return state, logs

if __name__ == "__main__":
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    input_json = {
        "name": "John Doe",
        "email": "john@example.com",
        "query": "I cannot access my account",
        "priority": "high",
        "ticket_id": "T12345"
    }

    final_state, execution_logs = run_agent(config, input_json)

    print("🔹 Execution Logs:")
    for log in execution_logs:
        print(log)

    print("\n✅ Final Payload:", final_state)
