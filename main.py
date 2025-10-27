import streamlit as st

st.markdown("""
<style>
html, body, [class*="css"]  {
    color: #ffffff !important;
    background-color: #000000 !important;
}

/* Make DataFrame text readable */
.dataframe, .stDataFrame table, .stDataFrame td, .stDataFrame th {
    color: #ffffff !important;
    background-color: #111111 !important;
}

/* Dropdown & text input */
input, select, textarea {
    color: #ffffff !important;
    background-color: #222222 !important;
}

/* Buttons */
.stButton > button {
    color: white !important;
    background-color: #333333 !important;
    border-radius: 8px;
    border: 1px solid #555 !important;
}
</style>
""", unsafe_allow_html=True)


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

def card(text, color="#1e1e1e"):
    st.markdown(
        f"""
        <div style="
            padding:12px 18px;
            border-radius:12px;
            margin-bottom:10px;
            font-size:16px;
            border:1px solid #444;">
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

        result_text = f"Day: {day}\nTime: {start}:00 - {end}:00\n\n"

        st.markdown("---")
        st.subheader(f"✅ Members free for full slot {start}:00 - {end}:00")

        full_free = check_availability(day, start, end)

        result_text += "Members free for full slot:\n"
        if full_free:
            for m in full_free:
                card(m, "#d1ffd6")
                result_text += f"• {m}\n"
        else:
            card("No one free for the whole slot.", "#ffd1d1")
            result_text += "No one free for the full slot.\n"

        st.markdown("---")
        st.subheader("⏱ Hour-by-Hour Availability\n")

        result_text += "\nHour-by-hour availability:\n"

        current = start
        while current < end:
            next_hour = current + 1
            hour_members = check_availability(day, current, next_hour)

            st.markdown(f"**{current}:00 - {next_hour}:00**")
            result_text += f"\n{current}:00 - {next_hour}:00\n"

            if hour_members:
                for m in hour_members:
                    card(m, "#e8f0ff")
                    result_text += f"   • {m}\n"
            else:
                card("No one free in this hour", "#ffd1d1")
                result_text += "   ❌ No one free\n"

            current += 1

        # ---------------- COPY BUTTON ----------------
        st.markdown("""
        <button onclick="navigator.clipboard.writeText(document.getElementById('result_text').innerText)"
        style="padding:10px 16px; font-size:16px; border-radius:6px; background:#444; color:white; margin-top:10px;">
        📋 Copy Result
        </button>
        """, unsafe_allow_html=True)

        st.markdown(f"<pre id='result_text' style='display:none;'>{result_text}</pre>", unsafe_allow_html=True)

        # ---------------- DOWNLOAD BUTTON ----------------
        st.download_button(
            label="🖨️ Download Result (.txt for Print / PDF)",
            data=result_text,
            file_name=f"{day}_{start}-{end}_availability.txt",
            mime="text/plain"
        )

    except:
        st.error("⚠️ Use format like 9-12")

   

    
