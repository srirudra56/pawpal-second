# 🐾 PawPal+ AI Pet Care Assistant

## Original Project (Module 2)

This project extends my **Module 2 PawPal+** object-oriented programming project. The original PawPal+ application helped pet owners organize and schedule pet-care tasks such as walks, feeding, grooming, and other daily activities. It allowed users to create pet-care tasks, detect scheduling conflicts, and generate a daily schedule to help manage their pet's routine.

For this final project, I expanded PawPal+ by integrating **Retrieval-Augmented Generation (RAG)** to provide AI-powered pet-care recommendations using a structured local knowledge base.

---

# Project Summary

PawPal+ AI Pet Care Assistant is a pet-care scheduling and recommendation system that combines traditional scheduling with AI-powered information retrieval. In addition to organizing pet-care tasks, the application can answer pet-care questions by retrieving trusted information from a structured knowledge base before generating recommendations.

The purpose of this project is to demonstrate how Retrieval-Augmented Generation (RAG) can improve AI reliability by retrieving relevant information before producing a response rather than relying solely on a language model's built-in knowledge.

---

# Features

- 🐶 Schedule daily pet-care tasks
- 🐱 Detect scheduling conflicts
- 📅 Generate a daily pet-care schedule
- 🤖 AI-powered pet-care recommendations
- 📖 Retrieval-Augmented Generation (RAG)
- 📂 Local JSON knowledge base
- 🛡️ Input validation and guardrails
- 📊 Confidence scores for recommendations
- 📝 Logging for debugging and reliability
- ✅ Automated unit testing

---

# Architecture Overview

The system consists of several components that work together:

1. The user enters a pet name, species, and pet-care topic through the Streamlit interface.
2. Input validation (guardrails) checks for missing or invalid information.
3. The RAG Assistant sends the request to the Retriever.
4. The Retriever searches the local JSON knowledge base for matching pet-care guidance.
5. The retrieved guidance and confidence score are returned to the RAG Assistant.
6. The application generates a recommendation, adds a veterinary safety disclaimer, logs the request, and displays the result to the user.

The complete Mermaid architecture diagram is included in:

```text
diagrams/architecture.mmd
```

---

# Project Structure

```
pawpal-second/
│
├── app.py
├── pawpal_system.py
├── retrieval.py
├── rag_assistant.py
├── logger_config.py
├── README.md
├── model_card.md
├── requirements.txt
│
├── data/
│   └── pet_care_knowledge.json
│
├── test/
│   └── test_pawpal.py
│
├── diagrams/
│   └── architecture.mmd
│
├── assets/
│
└── logs/
```

---

# Setup Instructions

## Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the application

```bash
python3 -m streamlit run app.py
```

## Run automated tests

```bash
python3 -m pytest
```

---

# Sample Interactions

## Example 1

### Input

```text
Pet Name: Buddy
Species: Dog
Topic: Exercise
```

### Output

```text
Recommendation for Buddy

Regular exercise helps dogs maintain a healthy weight and provides mental stimulation.

Confidence Score: 97%

For medical concerns or personalized care, please consult a veterinarian.
```

---

## Example 2

### Input

```text
Pet Name: Luna
Species: Cat
Topic: Sleep
```

### Output

```text
Recommendation for Luna

Adult cats commonly sleep about 12–16 hours each day, while kittens may sleep up to 20 hours.

Confidence Score: 93%

For medical concerns or personalized care, please consult a veterinarian.
```

---

## Example 3

### Input

```text
Pet Name:
Species: Dog
Topic: Hydration
```

### Output

```text
Warning

Please enter a pet name.
```

---

# Design Decisions

I chose Retrieval-Augmented Generation (RAG) because it allows the application to retrieve information from a structured pet-care knowledge base before generating recommendations. This approach makes responses more consistent, explainable, and easier to maintain than relying only on a language model.

A local JSON file was used as the knowledge base because it is lightweight, simple to update, and appropriate for the project's scope. One trade-off of this design is that retrieval currently uses exact topic matching instead of semantic search or vector embeddings.

---

# Reliability and Testing

The PawPal+ AI Pet Care Assistant includes several mechanisms to improve reliability:

- Automated unit tests verify the core scheduling functionality.
- Confidence scores indicate how confidently the system matched the user's request to the knowledge base.
- Input validation (guardrails) prevents invalid requests from being processed.
- Logging records successful retrievals and application errors for debugging.

## Automated Unit Tests

The project includes five automated tests that validate the original PawPal+ scheduling system.

| Test | Purpose | Result |
|------|---------|--------|
| `test_mark_complete` | Verify tasks are marked complete correctly | ✅ Pass |
| `test_add_task` | Verify new tasks are added successfully | ✅ Pass |
| `test_sort_by_time` | Verify tasks are sorted correctly by time | ✅ Pass |
| `test_daily_task_creates_next_day_task` | Verify recurring daily tasks generate the next day's task | ✅ Pass |
| `test_conflict_detection` | Verify scheduling conflicts are detected | ✅ Pass |

## AI Feature Testing

The Retrieval-Augmented Generation system was tested using multiple pet-care topics and invalid inputs.

| Test Input | Expected Behavior | Result |
|------------|-------------------|--------|
| Dog + Exercise | Retrieve exercise guidance | ✅ Pass |
| Cat + Sleep | Retrieve sleep guidance | ✅ Pass |
| Hydration | Retrieve hydration guidance | ✅ Pass |
| Missing pet name | Display warning | ✅ Pass |
| Unsupported species | Prevent recommendation | ✅ Pass |
| Unknown topic | Display "No guidance found" | ✅ Pass |

## Overall Results

- **5 out of 5 automated unit tests passed successfully.**
- The RAG system consistently retrieved the correct knowledge base entry for supported topics.
- Confidence scores ranging from **92%–100%** improve explainability by indicating retrieval confidence.
- Guardrails successfully prevented invalid requests from causing application errors.
- Logging captures recommendation requests and errors to improve debugging and reliability.

---

# Technologies Used

- Python
- Streamlit
- JSON
- PyTest
- Logging
- Object-Oriented Programming (OOP)
- Retrieval-Augmented Generation (RAG)

---

# Future Improvements

Future enhancements could include:

- Semantic search using embeddings instead of exact keyword matching.
- Support for additional pet species.
- Personalized recommendations based on pet age, breed, and medical history.
- Natural language questions instead of selecting predefined topics.
- Integration with calendar reminders and notifications.

---

# Documentation

Additional documentation included with this project:

- `README.md` — Project overview and setup instructions
- `model_card.md` — Responsible AI reflection, limitations, AI collaboration, and future improvements
- `diagrams/architecture.mmd` — Mermaid system architecture diagram

---

# Conclusion

PawPal+ AI Pet Care Assistant demonstrates how a traditional object-oriented scheduling application can be enhanced with Retrieval-Augmented Generation to provide reliable AI-assisted recommendations. By combining software engineering principles with AI concepts such as retrieval, guardrails, confidence scoring, logging, and automated testing, the project delivers a more intelligent, explainable, and user-friendly pet-care assistant.