## Import/Export Critical Materials Visualization using Plotly
This project provides a set of tools for visualizing [global trade data](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/Supply_Chain/BACI_HS22_V202401/BACI_HS22_Y2022_V202401.csv) related to critical materials using Plotly. The dataset includes yearly import and export information at the level of year, exporter, importer, and product. The visualizations produced include interactive tree diagrams and Sankey diagrams, which effectively represent trade flows at multiple levels.

### Detailed Trade Data: 

Products are categorized using the Harmonized System 6-digit nomenclature, with values reported in thousand USD and quantities in metric tons.
### Comprehensive Coverage: 

Trade flows are detailed at the year - exporter - importer - product level, providing a granular view of global trade patterns.

## Global Trade Dataset Information

t: year
i: exporter
j: importer
k: product
v: value
q: quantity


## Country Data Integration

After importing the main trade dataset, it is connected with a [country codes dataset](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/Supply_Chain/BACI_HS22_V202401/country_codes_V202401.csv) to replace numeric country codes with corresponding country names. The country code dataset contains information for 238 countries, ensuring broad coverage. 

## Product Data Integration

The trade dataset is also linked with a [product codes dataset](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/Supply_Chain/BACI_HS22_V202401/product_codes_HS22_V202401.csv) to categorize the products involved. The product code dataset has two versions (2017 and 2022). The 2017 version includes 145 unique product codes, while the 2022 version includes 370 unique codes. This integration allows for detailed product categorization based on the latest available data. 

## Usage
### To use this notebook:
Using Example section as an Example to input your data. 

There are five functions to create sankey and tree diagrams. 
Each function will show the diagram within the notebook and save at the desktop. 
There will also be a few lines of key information discribe the diagram print before the diagram. 

all_data_diagram(n3list,all_data_code,country_code,product_code)
    This function draws a tree diagram for all new trio type 
export_tree_diagram_preprocess(n3s,all_data_code,country_code,product_code,new_trio,target_country_name):
    This function draws tree diagrams for each new_trio elements
export_sankey_diagram(n3s,all_data_code,country_code,product_code,new_trio,target_country_name)
    This function draws a Sankey diagram to visualiz the export OD of n3s

