import json

def load_knowledge():
    with open("data/pet_care_knowledge.json", "r", encoding="utf-8") as file:
        return json.load(file)

def retrieve_guidance(topic, pet_type):
    knowledge = load_knowledge()

    topic = topic.lower()
    pet_type = pet_type.lower()

    for item in knowledge:
        if (
            item["topic"].lower() == topic
            and (
                item["pet_type"].lower() == pet_type
                or item["pet_type"].lower() == "all"
            )
        ):
            return item

    return None