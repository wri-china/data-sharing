import pandas as pd
import matplotlib.pyplot as plt

# Define file path and sheet name
file_path = 'https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/financial_data/financial-data.xlsx'
sheet_name = 'sheet1'

# Read data from the Excel file
df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
# Subset dataframe
sub_df = df[df['表名称'] == '一般公共支出']

# Filter the dataframe for the relevant rows
total_exp_df = sub_df[
    (sub_df['项目一级'].str.contains('总合计')) &
    (sub_df['项目二级'].isna())
]

item_exp_df = sub_df[
    (sub_df['项目一级'].str.contains('节能环保支出')) &
    (sub_df['项目二级'].str.contains('合计'))
]

# Special handling for Guangdong province
total_exp_guangdong = sub_df[
    (sub_df['省份'] == '广东省') &
    (sub_df['项目一级'].str.contains('一般公共预算支出')) &
    (sub_df['项目二级'].str.contains('合计')) &
    (sub_df['项目三级'].isna())
]

item_exp_guangdong = sub_df[
    (sub_df['省份'] == '广东省') &
    (sub_df['项目二级'].str.contains('节能环保支出')) &
    (sub_df['项目三级'].str.contains('合计'))
]

# Merge the special handling rows with the main conditions
total_exp_df = pd.concat([total_exp_df, total_exp_guangdong]).reset_index(drop=True)
item_exp_df = pd.concat([item_exp_df, item_exp_guangdong]).reset_index(drop=True)

# Merge the DataFrames on '省份'
merged_df = pd.merge(total_exp_df, item_exp_df, on='省份', suffixes=('_总支出', '_节能环保支出'))
# Calculate the percentage
merged_df['百分比'] = merged_df['2024年计划数_节能环保支出'] / merged_df['2024年计划数_总支出'] * 100
# Select relevant columns and rename for clarity
data = merged_df[['省份', '2024年计划数_总支出', '2024年计划数_节能环保支出', '百分比']]
data.columns = ['省份', '总支出', '节能环保支出', '百分比']


# Visualization
# Set font to display Chinese characters
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# Create a bar chart
fig, ax = plt.subplots(figsize=(12, 8))
x = list(range(len(data['省份'])))
width = 0.4  # Set bar width

# Plot only the bars for energy conservation and environmental protection expenditure
ax.bar(x, data['节能环保支出'], width, label='节能环保支出')

# Add percentage labels on the bar chart
for i, row in data.iterrows():
    ax.text(i, row['节能环保支出'] + 50000, f'{row["百分比"]:.2f}%', ha='center', va='bottom',
            bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'))

ax.set_xticks([x_i for x_i in x])
ax.set_xticklabels(data['省份'], rotation=45)
ax.set_title('2024年节能环保支出计划数')
ax.set_ylabel('金额(万元)')

# Set y-axis value format
formatter = plt.FuncFormatter(lambda x, _: f'{x:,.0f}')
ax.yaxis.set_major_formatter(formatter)

# Add legend
legend_items = ['节能环保支出', '节能环保支出占一般公共支出的百分比']
legend_colors = ['blue', 'w']  # Set the second rectangle to white fill
legend_boxes = [plt.Rectangle((0, 0), 1, 1, fc=color, ec='black') for color in legend_colors]
ax.legend(legend_boxes, legend_items, loc='upper right', bbox_to_anchor=(0.90, 0.975))

plt.show()
