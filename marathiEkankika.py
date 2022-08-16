import streamlit as st
from google.oauth2 import service_account
from gsheetsdb import connect
import pandas as pd

st.write("The display will be improved in the near futre with options")

# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)
conn = connect(credentials=credentials)

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["private_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

# # Print results.
# for row in rows:
#     st.write(f"{row.शीर्षक} is of type :{row.प्रकार}:")

#st.dataframe(rows)[["शीर्षक","लेखक","प्रकाशन साल","प्रकार","पात्रसंख्या (पु)","पात्रसंख्या (स्त्री)","अंक","कालावधी (मिनिटे)","टिप्पणी"]]
#df[["शीर्षक"]]

df = pd.DataFrame(rows)
df[["शीर्षक","लेखक"]]
#df[["शीर्षक","लेखक","प्रकाशन साल","प्रकार","पात्रसंख्या (पु)","पात्रसंख्या (स्त्री)","अंक","कालावधी (मिनिटे)","टिप्पणी"]]
