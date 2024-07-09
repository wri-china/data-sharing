import pandas as pd
import matplotlib.pyplot as plt

# Define file path and sheet name
file_path = 'https://github.com/wri-china/data-sharing/blob/main/financial-data/financial-data.xlsx'
sheet_name = 'sheet1'

# Read data from the Excel file
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Merge columns B, C, D, E
df['合并列'] = df[['表名称', '项目一级', '项目二级', '项目三级']].fillna('').agg(''.join, axis=1)

# Iterate over each province
provinces = ['北京市', '广东省', '河北省', '江苏省', '山东省', '上海市', '四川省', '天津市', '浙江省']

# Initialize dictionary to store data
data = {}

for province in provinces:
    # Filter second condition: "General public expenditure", "Energy conservation and environmental protection expenditure", "Total"
    condition2 = df[
        (df['省份'] == province) &
        df['合并列'].str.contains('一般公共支出') &
        df['合并列'].str.contains('节能环保支出') &
        df['合并列'].str.contains('合计')
    ]

    # Extract 2024 budget figure for the second condition
    row2_value = condition2['2024年计划数'].values[0] if not condition2.empty else 0

    # Filter first condition: "General public expenditure", "Total"
    condition1 = df[
        (df['省份'] == province) &
        df['合并列'].str.contains('一般公共支出') &
        df['合并列'].str.endwith('总合计')
    ]

    # Extract 2024 budget figure for the first condition
    row1_value = condition1['2024年计划数'].values[0] if not condition1.empty else 0

    # Calculate the percentage of energy conservation and environmental protection expenditure to total expenditure
    if row1_value == 0:
        percentage = 0
    else:
        percentage = round(row2_value / row1_value * 100, 2)

    # Store data in the dictionary
    data[province] = [row1_value, row2_value, percentage]

# Output the calculated raw data
print("Calculated Raw Data:")
print(data)

# Set font to display Chinese characters
plt.rcParams['font.sans-serif'] = ['SimHei']  # Set font to SimHei
# Solve the negative sign display issue in the coordinate axis
plt.rcParams['axes.unicode_minus'] = False

# Create a bar chart
fig, ax = plt.subplots(figsize=(12, 8))
x = list(range(len(provinces)))
width = 0.4  # Set bar width

# Plot only the bars for energy conservation and environmental protection expenditure
ax.bar(x, [data[province][1] for province in provinces], width, label='节能环保支出')

# Add percentage labels on the bar chart
for i, p in enumerate(data.values()):
    ax.text(i, p[1] + 50000, f'{p[2]}%', ha='center', va='bottom',
            bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'))

ax.set_xticks([x_i for x_i in x])
ax.set_xticklabels(provinces, rotation=45)
ax.set_title('2024年节能环保支出计划数')
ax.set_ylabel('金额(万元)')

# Set y-axis value format
formatter = '{:,.0f}'.format
ax.yaxis.set_major_formatter(formatter)

# Add legend
legend_items = ['节能环保支出', '节能环保支出占一般公共支出的百分比']
legend_colors = ['blue', 'w']  # Set the second rectangle to white fill
legend_boxes = [plt.Rectangle((0, 0), 1, 1, fc=color, ec='black') for color in legend_colors]
ax.legend(legend_boxes, legend_items, loc='upper right',
          bbox_to_anchor=(0.95, 0.95))

plt.show()
