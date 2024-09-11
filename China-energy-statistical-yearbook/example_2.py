import pandas as pd

# Specify the Excel file path
file = 'China-energy-statistical-yearbook/分省能源平衡表(实物量)-2022.xlsx'
# Load the Excel file to get the sheet names
xls = pd.ExcelFile(file)

# Load the factor sheet
factor = pd.read_excel(file, sheet_name='各种能源折标准煤参考系数')
factor = factor[factor['项目'] == '四.终端消费量'].iloc[:, 2:].reset_index(drop=True)

standard = {'province': [], 'total_stand': [], 'elec_stand': [], 'elec_rate': []}
# Loop through all the sheets in the order, except for the last one
for sheet_name in xls.sheet_names[:-1]:
    # Load the current sheet
    df = pd.read_excel(file, sheet_name=sheet_name)
    # Update column names
    df.columns = df.iloc[1, :]
    # Drop header
    df = df.iloc[2:, :].reset_index(drop=True)
    # Subset row
    sub_df = df[df['项目'] == '四.终端消费量'].iloc[:, 2:].reset_index(drop=True).astype(float)
    # Update column names
    sub_df.columns = factor.columns

    total_stand = (sub_df * factor).sum().sum()
    elec_stand = (sub_df * factor).iloc[0, -2]

    # append results
    standard['province'].append(sheet_name.split(' ')[1].split('能')[0])
    standard['total_stand'].append(total_stand)
    standard['elec_stand'].append(elec_stand)
    standard['elec_rate'].append(elec_stand/total_stand)

# Convert dictionary to DataFrame
standard_df = pd.DataFrame(standard)
standard_df.sort_values(by='elec_rate', ascending=False)

# Export to CSV
standard_df.to_csv('electrification_rate_province_2022.csv')
