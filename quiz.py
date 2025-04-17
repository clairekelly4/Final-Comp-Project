import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Group Project Matcher (Responses)").sheet1
records = sheet.get_all_records()
df = pd.DataFrame(records)
print(df.head())

#We plan to create an algorithm that takes the results from the google form/spreadsheet. For the quiz, we ask questions that gauge the personality, work styles, and preferences of team members.
#For certain questions, members who choose similar numbers for these questions will be more likely to be put in the same group, and for some questions, people put numbers on different ends of the range will be placed together.
#For example, for students who like to be leaders/dominant personalities, they should be paired with students who prefer to be followers/more passive. For students who prefer to finish projects in one sitting, they should be paired with students who prefer that over splitting it into parts over time.
#to create this code:
#1. the data needs to be cleaned to handle if there are any missing or inconsistent entries
#2. represent each student as a vector
#3. define a compatibility metric, such as distance between the vectors of students
#4. itertaively assigns students to groups that maximizes their compatability
#5. format the grouping results into a readable format
#6. check for edge cases, like same information between participants, or ties in the algorithm
