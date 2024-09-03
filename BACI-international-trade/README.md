# BACI: International Trade Database

The [BACI: International Trade Database](http://www.cepii.fr/CEPII/en/bdd_modele/bdd_modele_item.asp?id=37) provides yearly global trade data at a detailed level, including:

- **Year**
- **Exporter**: ISO 3-digit country code
- **Importer**: ISO 3-digit country code
- **Product**: Product category
- **Value**: Value of the trade flow, in thousands current USD
- **Quantity**: Qiantity, in metric tons

## Dataset Versions

This dataset is available in two versions:

### 1. BACI_HS17_V2020401
- **Time Period**: 2017 to 2022
- **Product Source**: [2017](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/supply_chain/BACI_HS17_V202401/BACI_HS17_Y2017_V202401.csv), [2018](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/supply_chain/BACI_HS17_V202401/BACI_HS17_Y2018_V202401.csv), [2019](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/supply_chain/BACI_HS17_V202401/BACI_HS17_Y2019_V202401.csv), [2020](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/supply_chain/BACI_HS17_V202401/BACI_HS17_Y2020_V202401.csv), [2021](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/supply_chain/BACI_HS17_V202401/BACI_HS17_Y2021_V202401.csv), [2022](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/supply_chain/BACI_HS17_V202401/BACI_HS17_Y2022_V202401.csv)
- **Country codes**: [HS17](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/supply_chain/BACI_HS17_V202401/country_codes_V202401.csv)
- **Product codes**: [HS17](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/supply_chain/BACI_HS17_V202401/product_codes_HS17_V202401.csv)

### 2. BACI_HS22_V2020401
- **Time Period**: 2022
- **Product Source**: [2022](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/supply_chain/BACI_HS22_V202401/BACI_HS22_Y2022_V202401.csv)
- **Country codes**: [HS22](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/supply_chain/BACI_HS22_V202401/country_codes_V202401.csv)
- **Product codes**: [HS22](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/supply_chain/BACI_HS22_V202401/product_codes_HS22_V202401.csv)

#### Difference: 
- HS 2022 introduced significant structural changes compared to HS 2017. This includes the reclassification of certain products and the creation of new subheadings to accommodate new products and changes in global trade patterns.
- Many subheadings in HS 2017 were merged, split, or expanded in HS 2022 to reflect the current state of international trade more accurately.
- HS 2022 covers a broader range of products with more detailed classifications. This reflects technological advancements, the emergence of new products, and changes in consumer demand. For instance, HS 2022 includes new classifications for high-tech goods, environmental goods, and health-related products.
- The number of unique product codes increased from 145 in HS 2017 to 370 in HS 2022, indicating more granular classification.

## File Structure

Each folder contains four types of files:

1. **BACI_HS{xx}_Y{YEAR}_V202401.csv**: Represents the dataset itself  
   - `{xx}` indicates the dataset's version.  
   - `{YEAR}` indicates the dataset's year.

2. **country_codes_V2024.csv**: Contains the corresponding country codes for the exporter and importer countries.

3. **product_codes_HS{xx}_V202401.csv**: Contains detailed product information along with its corresponding 6-digit nomenclature in the Harmonized System.

4. **Readme.txt**: Provides detailed information about the dataset.


## A Supply Chain Case Demonstration:  China's New Trio and Critical Materials Visualization

This script visualizes China's new trio and critical minerals supply chain using interactive tree diagrams and sankey diagrams, which effectively represent trade flows at multiple levels.

By running `python3 example.py` or each cell of the `example.ipynb`, user can get the interactive Sankey diagram and Tree diagram as followed:

- View [Sankey diagram](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/supply_chain/Sankey+Diagram+of+Critical+Materials++Imports+into+China.html) of Critical Materials Imports into China
- View [Tree diagram](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/supply_chain/The+Proportion+of+Cobalt+Related+Materials+Imports+from+Countries+to+China.html) of Cabalt Imports into China
