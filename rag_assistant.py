from retrieval import retrieve_guidance

def answer_question(pet_name, pet_type, topic):
    result = retrieve_guidance(topic, pet_type)

    if result:
        guidance = result["guidance"]
        confidence = result["confidence"]

        return (
            f"Recommendation for {pet_name}:\n\n"
            f"{guidance}\n\n"
            f"Confidence Score: {confidence}%\n\n"
            "For medical concerns or personalized care, "
            "please consult a veterinarian."
        )

    return (
        f"I could not find guidance about '{topic}' for a {pet_type}.\n\n"
        "Confidence Score: 0%"
    )