# The International Trade Dataset Overview

## International Trade Dataset

The [International Trade Dataset](http://www.cepii.fr/CEPII/en/bdd_modele/bdd_modele_item.asp?id=37) provides yearly global trade data at a detailed level, including:

- **Year**
- **Exporter**
- **Importer**
- **Product**
- **Value**
- **Quantity**

### Dataset Versions

This dataset is available in two versions:

#### 1. BACI_HS17_V2020401
- **Time Period**: 2017 to 2022
- **Product Source**: [2017](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/supply_chain/BACI_HS17_V202401/BACI_HS17_Y2017_V202401.csv), [2018](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/supply_chain/BACI_HS17_V202401/BACI_HS17_Y2018_V202401.csv), [2019](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/supply_chain/BACI_HS17_V202401/BACI_HS17_Y2019_V202401.csv), [2020](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/supply_chain/BACI_HS17_V202401/BACI_HS17_Y2020_V202401.csv), [2021](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/supply_chain/BACI_HS17_V202401/BACI_HS17_Y2021_V202401.csv), [2022](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/supply_chain/BACI_HS17_V202401/BACI_HS17_Y2022_V202401.csv)
- **Country codes**: [HS17](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/supply_chain/BACI_HS17_V202401/country_codes_V202401.csv)
- **Product codes**: [HS17](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/supply_chain/BACI_HS17_V202401/product_codes_HS17_V202401.csv)

#### 2. BACI_HS22_V2020401
- **Time Period**: 2022
- **Product Source**: [2022](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/supply_chain/BACI_HS22_V202401/BACI_HS22_Y2022_V202401.csv)
- **Country codes**: [HS22](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/supply_chain/BACI_HS22_V202401/country_codes_V202401.csv)
- **Product codes**: [HS22](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/supply_chain/BACI_HS22_V202401/product_codes_HS22_V202401.csv)

##### Difference: The 2017 version includes 145 unique product codes, while the 2022 version includes 370 unique codes. 2022 version have more subdivision from 2017 version which allows for more detailed product categorization based on the latest available data.

### File Structure

Each folder contains four types of files:

1. **`BACI_HS{xx}_Y{YEAR}_V202401.csv`**  
   This file represents the dataset itself.  
   - `{xx}` indicates the dataset's version.  
   - `{YEAR}` indicates the dataset's year.

2. **`country_codes_V2024.csv`**  
   This file contains the corresponding country codes for the exporter and importer countries.

3. **`product_codes_HS{xx}_V202401.csv`**  
   This file contains detailed product information along with its corresponding 6-digit nomenclature in the Harmonized System.

4. **`Readme.txt`**  
   This file provides detailed information about the dataset.

## Supply Chain Case Demonstration:  China's New Trio and CriticalMaterials Visualization

This script visualizes China's new trio supply chain using interactive tree diagrams and Sankey diagrams, which effectively represent trade flows at multiple levels. The target country, critical materials, and target products are defined within the Example section.


### Example to use this notebook
Using `all_data_diagram(n3list, all_data_code, country_code, product_code)` as an example: 
1. Before executing any diagram functions, ensure that you define the following variables in the initial setup cell:

      **`all_data_code, country_code, product_code`**: Provide the absolute or relative path to the CSV data file that contains the critical materials and trade information and define them within the notebook. 

      **`n3list`**: A List of products in product list  are new trio exports. 
2. Once the variables are defined, you can generate the desired visualizations by running the function with all the inputs in the bracket. The diagram will show up in the notbook and save as a html file at notbook's location.


### 1. `all_data_diagram(n3list, all_data_code, country_code, product_code)`
- **Description**: Draws a tree diagram for all new trio types.
- **Parameters**:
  - `n3list`: List of product in product list that is new trio export. 
  - `all_data_code`: Data code for all categories.
  - `country_code`: Country code for filtering data.
  - `product_code`: Product code for filtering data.
  ![fugure1](https://raw.githubusercontent.com/MingchuanMa/test/main/all_data_diagram.png)


### 2.`export_tree_diagram_preprocess(n3s,all_data_code,country_code,product_code,new_trio,target_country_name)`
- **Description**: Draw tree diagrams for each new_trio's export situation at target country. 
- **Parameters**:
   - `n3s`: List of new trio products in product code data.
   - `all_data_code`: Data code for all categories.
   - `country_code`: Country code for filtering data.
   - `product_code`: Product code for filtering data.
   - `new_trio`: New trio product categories.
   - `target_country_name`: Target country name. 
     ![fugure2](https://raw.githubusercontent.com/MingchuanMa/test/main/export_tree_diagram.png)

### 3.`export_sankey_diagram(n3s,all_data_code,country_code,product_code,new_trio,target_country_name)`
   - **Description**： Draws a Sankey diagram for the export OD of new trios.
   - **Parameters**:
   - `n3s`: List of new trio products in product code data.
   - `all_data_code`: Data code for all categories.
   - `country_code`: Country code for filtering data.
   - `product_code`: Product code for filtering data.
   - `new_trio`: New trio product categories.
   - `target_country_name`: Target country name. 
     ![fugure3](https://raw.githubusercontent.com/MingchuanMa/test/main/export_sankey_diagram.png)


### 4.`import_tree_diagram(CriticalMaterials,all_data_code,country_code,product_code,target_country_name)`
   - **Description**: Draw tree diagrams for each Critical Marerials's import situation at target country. 
   - **Parameters**:
   - `CriticalMaterials`: List of Critical Material.
   - `all_data_code`: Data code for all categories.
   - `country_code`: Country code for filtering data.
   - `product_code`: Product code for filtering data.
   - `target_country_name`: Target country name. 
     ![fugure4](https://raw.githubusercontent.com/MingchuanMa/test/main/import_tree_diagram.png)


### 5. `import_sankey_diagram(CriticalMaterials, all_data_code, country_code, product_code, target_country_name)`
   - **Description**: Draws a Sankey diagram to visualiz the import OD of Critical Materials.   
   - **Parameters**:
   - `CriticalMaterials`: List of Critical Material.
   - `all_data_code`: Data code for all categories.
   - `country_code`: Country code for filtering data.
   - `product_code`: Product code for filtering data.
   - `target_country_name`: Target country name. 
     ![fugure5](https://raw.githubusercontent.com/MingchuanMa/test/main/import_sankey_diagram.png)

