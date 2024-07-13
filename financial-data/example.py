import pandas as pd
import matplotlib.pyplot as plt

# Define file path and sheet name
file_path = 'https://raw.githubusercontent.com/wri-china/data-sharing/main/financial-data/financial-data.xlsx'
sheet_name = 'sheet1'

# Read data from the Excel file
df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')

# Define provinces
provinces = ['北京市', '广东省', '河北省', '江苏省', '山东省', '上海市', '四川省', '天津市', '浙江省']

# Filter the dataframe for the relevant rows
total_exp_df = df[
    (df['表名称'].str.contains('一般公共支出')) &
    (df['项目一级'].str.contains('总合计')) &
    (df['项目二级'].isna())
]

item_exp_df = df[
    (df['表名称'].str.contains('一般公共支出')) &
    (df['项目一级'].str.contains('节能环保支出')) &
    (df['项目二级'].str.contains('合计'))
]

# Special handling for Guangdong province
total_exp_guangdong = df[
    (df['省份'] == '广东省') &
    (df['表名称'].str.contains('一般公共支出')) &
    (df['项目一级'].str.contains('一般公共预算支出')) &
    (df['项目二级'].str.contains('合计')) &
    (df['项目三级'].isna())
]

item_exp_guangdong = df[
    (df['省份'] == '广东省') &
    (df['表名称'].str.contains('一般公共支出')) &
    (df['项目二级'].str.contains('节能环保支出')) &
    (df['项目三级'].str.contains('合计'))
]

# Merge the special handling rows with the main conditions
total_exp_df = pd.concat([total_exp_df, total_exp_guangdong])
item_exp_df = pd.concat([item_exp_df, item_exp_guangdong])

# Initialize a DataFrame to store data
data = pd.DataFrame(columns=['省份', '总支出', '节能环保支出', '百分比'])

data['省份'] = total_exp_df['省份'].values
data['总支出'] = total_exp_df['2024年计划数'].values
data['节能环保支出'] = item_exp_df['2024年计划数'].values
data['百分比'] = data['节能环保支出'] / data['总支出'] * 100

# Output the calculated raw data
print("Calculated Raw Data:")
print(data)

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
