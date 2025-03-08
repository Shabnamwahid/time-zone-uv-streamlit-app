import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# Custom CSS for styling
# Custom Styling
st.markdown("""
    <style>
        body {
            background-color: #DFF0D8;
        }
          
        .stApp {
            background-color: #DFF0D8;
        }
        .stButton>button {
            background-color: #008080 !important;
            color: white !important;
            border-radius: 8px;
            padding: 10px;
        }
        .stButton>button:hover {
            background-color: #006666 !important;
        }
        h1, h2, h3 {
           
            color:#008080 !important;
            }
        .stSelectbox, .stTextInput, .stTimeInput {
            background-color: white !important;
            border: 1px solid #008080 !important;
        }
    </style>
""", unsafe_allow_html=True)

# List of available time zones
TIME_ZONES = [
"UTC",
 "Asia/Karachi",       # Pakistan
    "Asia/Kolkata",       # India
    "Asia/Dubai",         # United Arab Emirates
    "Asia/Tokyo",         # Japan
    "Europe/London",      # United Kingdom
    "Europe/Paris",       # France
    "Europe/Berlin",      # Germany
    "America/New_York",   # USA (Eastern Time)
    "Australia/Sydney",   # Australia
    "Africa/Johannesburg", # South Africa
    "Asia/Seoul",  # South Korea
    "Asia/Riyadh",  # Saudi Arabia
    "Asia/Tehran",  # Iran
   "America/Los_Angeles",# USA (Pacific Time)

]
# App Title
st.title("Time Zone App")

# Create a multi-select dropdown for choosing time zones

selected_timezone = st.multiselect("Select Timezones", TIME_ZONES, default=["UTC","Asia/Karachi"])

# Display the selected timezones

st.subheader("Selected Timezones")
for tz in selected_timezone:
# Get  and formet current time for each selected timezone with AM/PM
    current_time = datetime.now(ZoneInfo(tz)).strftime("%y-%m-%d %I:%H:%M:%S %p")
    st.write(f"**{tz}**: {current_time}")

st.subheader("Concvert Time Between Timezones")

current_time =  st.time_input("Current Time", value=datetime.now().time())

from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)

to_tz = st.selectbox(" To Timezone", TIME_ZONES, index=1)

if st.button("Convert Time"):

  dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))

  converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%y-%m-%d %I:%H:%M:%S %p")

  st.success(f"Converted Time to {to_tz}: {converted_time}")


st.markdown("<h5 style='text-align: center;'>Build with ❤️ by Shabnam Wahid</h5>", unsafe_allow_html=True)

