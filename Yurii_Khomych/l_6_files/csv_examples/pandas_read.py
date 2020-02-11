import pandas

# df = pandas.read_csv('hr_data.csv')
# df = pandas.read_csv('hr_data.csv', index_col='Name')
df = pandas.read_csv('hr_data.csv', parse_dates=['Hire Date'])
type(df['Hire Date'][0])
df = pandas.read_csv(
    "hr_data.csv",
    index_col="Employee",
    parse_dates=["Hired"],
    header=0,
    names=["Employee", "Hired", "Salary", "Sick Days"],
)
print(df)
