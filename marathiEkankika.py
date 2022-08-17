import streamlit as st
from google.oauth2 import service_account
from gsheetsdb import connect
import pandas as pd



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

df = pd.DataFrame(rows)
df.अंक = df.अंक.astype('int64')
df.प्रकाशन_साल = df.प्रकाशन_साल.astype('int64')
df.पात्र_पु = df.पात्र_पु.astype('int64')
df.पात्र_स्त्री = df.पात्र_स्त्री.astype('int64')
df.कालावधी_मिनिटे = df.कालावधी_मिनिटे.astype('int64')

st.title("मराठी एकांकिका")
st.sidebar.title("निवडी")

toDisplay = st.sidebar.radio(
	"What would you like to see?",
	["All articles", "By author", "By type"],
	index=0
)

st.write("The display will be improved in the near futre with options")


df[["शीर्षक","लेखक","प्रकार","अंक","प्रकाशन_साल","पात्र_पु","पात्र_स्त्री","कालावधी_मिनिटे"]]