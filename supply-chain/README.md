# The International Trade Dataset Overview
[The International Trade Dataset](http://www.cepii.fr/CEPII/en/bdd_modele/bdd_modele_item.asp?id=37) provides yearly global trade products at a detailed level, including year, exporter, importer, product, value, and quantity. this dataset contains two versions: BACI_HS17_V2020401 and BACI_HS22_V2020401:
As for BACI_HS17_V2020401, it contains the trade dataset from 2017 to 2022.
As for BACI_HS22_V2020401, it contains the trade dataset in 2022.

Difference: The 2017 version includes 145 unique product codes, while the 2022 version includes 370 unique codes. This integration allows for detailed product categorization based on the latest available data. 

In each folder, it contains 4 types of files: BACI_HS{xx}_Y{YEAR}_V202401.csv, country_codes_V2024.csv, product_codes_HS{xx}_V202401.csv and Readme.txt

'BACI_HS{xx}_Y{YEAR}_V202401.csv' represents the dataset itself. 'xx' is the dataset's version, 'YEAR' is the dataset's year. 
'country_codes_V2024.csv' represents the corresponding country of exporter and importer country.
'product_codes_HS{xx}_V202401.csv' represents the detailed product and its corresponding 6-digit nomenclature in Harmonized System
'Readme.txt' gives detailed information about the dataset.

# Case for Supplychain

Wihtin this notebook it visualized China's new trio supplychain with interactive tree diagrams and Sankey diagrams, which effectively represent trade flows at multiple levels.

Target country, Critical Materials, and target products are defined within Example section.

There are five functions to create sankey and tree diagrams. 

By running each function, it will show the diagram within the notebook and save it at the notebook's location. 

There will also be a few lines of key information discribe the diagram print before the diagram. 

all_data_diagram(n3list,all_data_code,country_code,product_code)
    This function draws a tree diagram for all new trio type

export_tree_diagram_preprocess(n3s,all_data_code,country_code,product_code,new_trio,target_country_name):
    This function draws tree diagrams for each new_trio's export situation at target country. 

export_sankey_diagram(n3s,all_data_code,country_code,product_code,new_trio,target_country_name)
    This function draws a Sankey diagram to visualiz the export OD of n3s.

import_tree_diagram(CriticalMaterials,all_data_code,country_code,product_code,target_country_name)
        This function draws tree diagrams for each Critical Marerials's import situation at target country. 

import_sankey_diagram(CriticalMaterials, all_data_code, country_code, product_code, target_country_name)
        This function draws a Sankey diagram to visualiz the import OD of Critical Materials.

## Datasets Download Link

Global Trade Dataset:
https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/Supply_Chain/BACI_HS22_V202401/BACI_HS22_Y2022_V202401.csv

Country Code:
https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/Supply_Chain/BACI_HS22_V202401/country_codes_V202401.csv

Product Code:
https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/Supply_Chain/BACI_HS22_V202401/product_codes_HS22_V202401.csv
