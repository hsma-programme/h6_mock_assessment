import streamlit as st
import pandas as pd

xmas_number_ones = pd.read_csv("data/xmas_number_ones.csv")

def get_number_one(year):
    number_1_row = pd.DataFrame(xmas_number_ones[xmas_number_ones["year"] == year])

    if len(number_1_row) == 0:
        return "No Data"
    else:
        return {
            'title': number_1_row['title'].values[0],
            'primary_artist': number_1_row['primary_artist'].values[0],
            'weeks_at_number_one': number_1_row['weeks_at_number_1'].values[0],
            'video': number_1_row['video'].values[0]
        }

st.title("Christmas Number One Searcher")

with st.sidebar:
    user_year_of_birth = st.number_input("Enter your year of birth",
                                         value=1980)

number_one_data = get_number_one(user_year_of_birth)

if number_one_data == "No Data":
    st.warning("No data available for this year. Why not try the year of birth for someone else you know?")
else:
    st.success("Data Found!")

    st.write(f"In {user_year_of_birth} the Christmas Number 1",
               f"was {number_one_data['title']} by {number_one_data['primary_artist']}")

    st.metric(label="Weeks at Number 1", value=number_one_data['weeks_at_number_one'])

    st.video(number_one_data['video'])
