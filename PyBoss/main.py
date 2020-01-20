"""
In summary, the required conversions are as follows:
1. Name column should be split into separate
   First Name and Last Name columns.
2. DOB data should be re-written into MM/DD/YYYY format.
3. SSN data should be re-written such that the first five numbers
   are hidden from view.
4. State data should be re-written as simple two-letter abbreviations.

Process: 
    Read data from employee_data.csv
    Store columns of data into separate lists
    Zip columns into tuples which will be used to write to a new .csv
"""


#Import OS and CSV libraries for compatibility with .csv files.
import os
import csv
#Import datetime for convenience format conversion w/ strftime()
import datetime


#Variables
#emp_ID: list for Col1 (employee ID)
emp_ID = []
#first_name: list for Col2/P1 (first name)
first_name = []
#last_name: list for Col2/P2 (last name)
last_name = []
#dob: list for Col3 (date of birth)
dob = []
#temp_date: The dob needs to be converted to a datetime object for
# simple conversion with strftime().  This will hold is for that.

#ssn: list for Col4 (social security number)
ssn = []
#state: list for Col5 (state)
state = []

#State abbreviation conversion list from https://gist.github.com/rogerallen/1583593
# Credit Roger Allen (waived copyright)
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Palau': 'PW',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


#Setup input filepath
old_data_path = os.path.join("..","PyBoss","employee_data.csv")

with open(old_data_path, newline='') as old_data:

    #initialize csvreader
    csvreader = csv.reader(old_data, delimiter=",")

    #Skip header row
    header = next(csvreader)

    #Pull data and insert into lists
    for row in csvreader:

        emp_ID.append(row[0])

        #Split the full name and insert the appropriate half into its
        #respective list
        first_name.append(row[1].split(" ")[0])
        last_name.append(row[1].split(" ")[1])

        #Convert DOB date format and store in dob
        temp_date = datetime.datetime.strptime(row[2], "%Y-%m-%d")
        dob.append(temp_date.strftime("%m/%d/%Y"))

        #Hide first 5 digits of SSN (take last 3) and store in "SSN"
        ssn.append("***-**-" + row[3][7:])

        #Convert full state to aabreviation and stor in state
        state.append(us_state_abbrev[row[4]])
        


# Zip data lists into tuple then write to new csv
processed_data = zip(emp_ID, first_name, last_name, dob, ssn, state)

#Set output filepath
output_path = os.path.join("..", "PyBoss", "new_employee_data.csv")

with open(output_path, "w", newline='') as new_data:

    #Initialize csvwriter
    writer = csv.writer(new_data)

    #Add new header row
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    #Write all new data to file
    writer.writerows(processed_data)


