import pandas as pd
import matplotlib.pyplot as plt


ene_total = {'year': [], 'energy_total': []}
for year in range(1996, 2023):
    # Load data
    df = pd.read_excel('https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/China_energy_statistical_yearbook/1996-2022%E5%85%A8%E5%9B%BD%E8%83%BD%E6%BA%90%E5%B9%B3%E8%A1%A1%E8%A1%A8-%E6%A0%87%E5%87%86%E9%87%8F.xlsx', sheet_name=str(year))
    # Update column names
    df.columns = df.iloc[3, :]
    # Drop header
    df = df.iloc[4:, :].reset_index(drop=True)
    # Extract values
    ene_total['year'].append(year)
    ene_total['energy_total'].append(float(df.loc[df['项目'].str.contains(r'2\.\s*工\s*业', regex=True), df.columns.str.contains('电热当量')].values.flatten()))


# Plotting
plt.figure(figsize=(10, 6))
plt.plot(ene_total['year'], ene_total['energy_total'], marker='o', linestyle='-', color='b')

# Adding title and labels
plt.title('Energy Total (Calorific Value Calculation)')
plt.xlabel('Year')
plt.ylabel('Energy Total (10,000 tce)')

# Adding grid
plt.grid(True)

# Show the plot
plt.show()
