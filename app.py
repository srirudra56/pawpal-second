import streamlit as st

from pawpal_system import Owner, Pet, Task, Scheduler
from rag_assistant import answer_question

from datetime import date, time

if "owner" not in st.session_state:
    st.session_state.owner = Owner(
        name="Default Owner",
        email="owner@example.com"
    )

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler()

owner = st.session_state.owner
scheduler = st.session_state.scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add task"):
    new_task = Task(
        task_name=task_title,
        task_type=priority,
        scheduled_date=date.today(),
        scheduled_time=time(9, 0),
        pet_name=pet_name
    )

    warning = scheduler.schedule_task(new_task)

if warning:
    st.warning(warning)
else:
    st.session_state.tasks.append(
        {
            "Pet": pet_name,
            "Task": task_title,
            "Priority": priority,
            "Duration": duration
        }
    )
    st.success("Task added!")

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    todays_tasks = scheduler.view_todays_tasks()

    if todays_tasks:
        st.success("Today's Schedule")

        for task in todays_tasks:
            st.write(
                f"{task.scheduled_time.strftime('%I:%M %p')} - "
                f"{task.pet_name}: {task.task_name}"
            )
    else:
        st.info("No tasks scheduled for today.")
st.divider()

st.subheader("🐾 Pet Care Recommendation Assistant")

st.write(
    "Choose a pet-care topic to receive guidance "
    "from the PawPal knowledge base."
)

care_topic = st.selectbox(
    "Choose a topic",
    [
        "vet visits",
        "exercise",
        "hydration",
        "sleep",
        "playtime"
    ]
)

if st.button("Get care recommendation"):
    if not pet_name.strip():
        st.warning("Enter a pet name.")
    elif species == "other":
        st.warning(
            "The current knowledge base supports dogs and cats only."
        )
    else:
        try:
            response = answer_question(
                pet_name=pet_name,
                pet_type=species,
                topic=care_topic
            )
            st.success(response)
        except FileNotFoundError:
            st.error("The pet-care knowledge base could not be found.")
        except Exception:
            st.error(
                "The recommendation could not be generated. "
                "Please try again."
            )