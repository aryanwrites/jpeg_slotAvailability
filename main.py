import streamlit as st

# -------------------- DATA --------------------
availability = {
    "Shiveshwar & Harshil": {
        "Monday": [(9, 13)],
        "Tuesday": [(9, 10)],
        "Wednesday": [(11, 12), (14, 15), (16, 24)],
        "Thursday": [(14, 15)],
        "Friday": [(14, 24)],
        "Saturday": [(13, 24)]
    },
    "Sionna Katiyar": {
        "Monday": [(9, 10), (15, 24)],
        "Tuesday": [(9, 10), (17, 24)],
        "Wednesday": [(9, 10), (17, 24)],
        "Thursday": [(9, 10), (17, 24)],
        "Friday": [(9, 13), (16, 24)],
        "Saturday": [(11, 24)]
    },
    "Raghav Jaiswal": {
        "Monday": [(12, 13), (15, 17)],
        "Tuesday": [(9, 10), (16, 24)],
        "Wednesday": [(9, 11)],
        "Thursday": [(12, 14)],
        "Friday": [(16, 18)],
        "Saturday": [(12, 24)]
    },
    "Priyavrat Saxena": {
        "Monday": [(9, 10), (14, 15)],
        "Tuesday": [(9, 10)],
        "Wednesday": [(9, 11), (16, 17)],
        "Thursday": [(10, 12)],
        "Friday": [(9, 10), (14, 15)],
        "Saturday": [(9, 10)]
    },
    "Suhani Garg": {
        "Monday": [(16, 24)],
        "Tuesday": [(9, 10)],
        "Wednesday": [(9, 11), (16, 24)],
        "Thursday": [(9, 12)],
        "Friday": [(9, 11)],
        "Saturday": [(13, 24)]
    },
    "Hritvij Acharya": {
        "Monday": [(17, 24)],
        "Tuesday": [(17, 24)],
        "Wednesday": [(16, 24)],
        "Thursday": [(15, 24)],
        "Friday": [(14, 15), (17, 24)],
        "Saturday": []
    },
    "Ekansh / Dhairya / Sheezah": {
        "Monday": [(16, 24)],
        "Tuesday": [(9, 10), (16, 24)],
        "Wednesday": [(9, 10), (17, 24)],
        "Thursday": [(15, 24)],
        "Friday": [(15, 24)],
        "Saturday": [(9, 11), (12, 24)]
    },
    "Kisna Agarwal": {
        "Monday": [(12, 14), (17, 24)],
        "Tuesday": [],
        "Wednesday": [(15, 17), (17, 24)],
        "Thursday": [],
        "Friday": [(16, 17), (17, 24)],
        "Saturday": [(12, 24)]
    },
    "Yashika Narayani": {
        "Monday": [(9, 10), (17, 24)],
        "Tuesday": [(9, 10), (17, 24)],
        "Wednesday": [(9, 10), (17, 24)],
        "Thursday": [(9, 10), (15, 16), (17, 24)],
        "Friday": [(9, 10), (14, 15), (17, 24)],
        "Saturday": [(0, 24)]
    }
}

def check_availability(day, start, end):
    free_members = []

    for name, schedule in availability.items():
        if day in schedule:
            for slot in schedule[day]:
                s, e = slot
                if start >= s and end <= e:
                    free_members.append(name)
                    break

    return free_members

# -------------------- UI --------------------
import streamlit as st

st.set_page_config(page_title="JPEG Availability", page_icon="📸", layout="centered")

def card(text, color):
    st.markdown(
        f"""
        <div style="
            background:{color};
            padding:12px 18px;
            border-radius:12px;
            margin-bottom:8px;
            font-size:16px;
            border:1px solid #dadada;">
            {text}
        </div>
        """,
        unsafe_allow_html=True
    )

st.title("📸 JPEG 1st Year Free Slot Finder")
st.caption("Select a day and time to see who's available (24-hour format)")

day = st.selectbox("Select Day", ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"])
time_range = st.text_input("Enter time slot (e.g., 9-12)")

def check_availability(day, start, end):
    free_members = []
    for name, schedule in availability.items():
        if day in schedule:
            for slot in schedule[day]:
                s, e = slot
                if start >= s and end <= e:
                    free_members.append(name)
                    break
    return free_members

if time_range:
    try:
        start, end = map(int, time_range.split('-'))

        st.markdown("---")
        st.subheader(f"✅ Members free for full slot {start}:00 - {end}:00")

        full_free = check_availability(day, start, end)

        if full_free:
            for m in full_free:
                card(m, "#d1ffd6")  # greenish card
        else:
            card("No one free for the whole slot.", "#ffd1d1")

        st.markdown("---")
        st.subheader("⏱ Hour-by-Hour Availability")

        current = start
        while current < end:
            next_hour = current + 1
            hour_members = check_availability(day, current, next_hour)

            st.markdown(f"**{current}:00 - {next_hour}:00**")
            if hour_members:
                for m in hour_members:
                    card(m, "#e8f0ff")  # light blue card
            else:
                card("No one free in this hour", "#ffd1d1")

            current += 1

    except:
        st.error("⚠️ Use format like 9-12")
