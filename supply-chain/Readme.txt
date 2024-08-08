Import/Export Critical Materials Visualization using Plotly
This Jupyter Notebook provides code and data for visulizing the flow of Import/Export Critical Materials with Sankey diagrams. Sankey diagrams are effective tools for visualizing the flow of data, resources, or energy between different stages or nodes. This project is written under python 3.9 environment.

Prerequisites
Before running, ensure you have the following packages installed:

plotly
numpy
pandas
matplotlib (for pylab functionality)


Input Data Structure
See the DATA file for details. 

Usage
To use this notebook:
Open the notebook in Jupyter Notebook or JupyterLab.
Ensure you have the necessary data files and libraries installed.
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

License
This project is licensed under the MIT License. See the LICENSE file for details.

Reference
Gaulier, G. and Zignago, S. (2010). BACI: International Trade Database at the Product-Level. The 1994-2007 Version. CEPII Working Paper, N°2010-23.
