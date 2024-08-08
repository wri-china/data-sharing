#!/usr/bin/env python
# coding: utf-8

# ## Packeges

# In[11]:


import numpy as np
import plotly.express as px
#import requests
import pandas as pd
import pylab as plt
import plotly.graph_objects as go   


# ##  Functions 

# In[13]:


#Function Input: Critical Materical want to track，data，Target import country，product code
#Function Output:  Total values ​​for each exporting country, Name fr each exporting country, Product discription
def get_importer_value(CM,all_data_code,country_code,product_code,target_country_name):
    filtered_product = product_code[product_code['description'].str.contains(CM, case=False)]
    filtered_country = country_code[country_code['country_name'].str.contains(target_country_name, case=False)]

    filtered_country_list = list(filtered_country.index)
    filtered_product_list = list(filtered_product.index)

    p_des = list(filtered_product['description'].values)
    
    dff = all_data_code[(all_data_code['product'].isin(filtered_product_list))&(all_data_code['importer'].isin(filtered_country_list))]

    # Group by exporter and sum 'value' 
    exporter_value_sum = dff.groupby('exporter')['value'].sum().drop(filtered_country_list,errors='ignore')
    EVS = exporter_value_sum.sort_values(ascending=False)

    #  'value' as size, and 'exporter' as label 
    sizes = EVS.values
    labels = country_code.loc[EVS.index]['country_name']
    return sizes,labels,p_des


# In[14]:


#Simmilar with previous function but get exporter value 
def get_exporter_value(n3,all_data_code,country_code,product_code,target_country_name):
    
    filtered_product = product_code[product_code['description'].str.contains(n3, case=False)]
    filtered_country = country_code[country_code['country_name'].str.contains(target_country_name, case=False)]

    filtered_country_list = list(filtered_country.index)
    filtered_product_list = list(filtered_product.index)

    p_des = list(filtered_product['description'].values)
    
    dff = all_data_code[(all_data_code['product'].isin(filtered_product_list))&(all_data_code['exporter'].isin(filtered_country_list))]

    # Group by exporter and sum 'value' 
    exporter_value_sum = dff.groupby('importer')['value'].sum().drop(filtered_country_list,errors='ignore')
    EVS = exporter_value_sum.sort_values(ascending=False)

    #  'value' as size, and 'exporter' as label 
    sizes = EVS.values
    labels = country_code.loc[EVS.index]['country_name']
    return sizes,labels,p_des


# In[15]:


def get_exporter_value_list(n3list,all_data_code,country_code,product_code,target_country_name):
    
    filtered_product = product_code[product_code['description'].isin(n3list)]
    filtered_country = country_code[country_code['country_name'].str.contains(target_country_name, case=False)]

    filtered_country_list = list(filtered_country.index)
    filtered_product_list = list(filtered_product.index)

    p_des = list(filtered_product['description'].values)
    
    dff = all_data_code[(all_data_code['product'].isin(filtered_product_list))&(all_data_code['exporter'].isin(filtered_country_list))]

    # Group by exporter and sum 'value' 
    exporter_value_sum = dff.groupby('importer')['value'].sum().drop(filtered_country_list,errors='ignore')
    EVS = exporter_value_sum.sort_values(ascending=False)

    #  'value' as size, and 'exporter' as label 
    sizes = EVS.values
    labels = country_code.loc[EVS.index]['country_name']
    return sizes,labels,p_des


# ### Full Tree diagram

# In[90]:


def all_data_diagram(n3list,all_data_code,country_code,product_code,target_country_name):
    sizes,labels,p_des = get_exporter_value_list(n3list,all_data_code,country_code,product_code,target_country_name)

    df = pd.DataFrame({'country':  labels.values, 'export_value': np.round(sizes,2),'percentage':np.round(100*sizes/sizes.sum(),2)})
    dfx =df
    print('New trio type:', 'Photovoltaic Products','\n Total value of imports:',np.sum(sizes),'thousand USD \n',np.round(sizes[:10],2),'\n',labels[:10].values,'\n','percentage:',np.round(sizes[:10],2)/np.sum(sizes),'\n','oveall percentage:',sum(np.round(sizes[:10],2)/np.sum(sizes)))
    fig = px.treemap(dfx, path=['country'], values='export_value',color='country',
                    color_discrete_sequence = px.colors.sequential.RdBu,
                    hover_data=['percentage'])
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25),
                    title=f"The Proportion of Photovoltaic Related Materials exports from {target_country_name} to Other Countries.")
    fig.update_traces(root_color="lightgrey", texttemplate="%{label}<br>%{value} thousand USD<br>%{customdata[0]}%",
                    textfont=dict(color="white",size=17))
    fig.show()
    fig.write_html("The Proportion of Photovoltaic Related Materials exports from",target_country_name,"to Other Countries.html")
    print('New trio type:', 'Photovoltaic Products','\n Total value of imports:',np.sum(sizes),'thousand USD \n',np.round(sizes[:10],2),'\n',labels[:10].values,'\n','percentage:',np.round(sizes[:10],2)/np.sum(sizes),'\n','oveall percentage:',sum(np.round(sizes[:10],2)/np.sum(sizes)))


# ### Export Tree diagram 

# In[45]:


def export_tree_diagram_preprocess(n3s,all_data_code,country_code,product_code,new_trio,target_country_name):
    DFot = pd.DataFrame()
    for i,n3 in enumerate(n3s):
        sizes,labels,p_des = get_exporter_value(n3,all_data_code,country_code,product_code,target_country_name)
        df_Export_from_china = pd.DataFrame({'country':  labels.values, 'export_value': np.round(sizes,2),'percentage':np.round(100*sizes/sizes.sum(),2)})
        df_Export_from_china['country_from'] = target_country_name
        df_Export_from_china['new_trio_type'] = new_trio[i]
        DFot = pd.concat([DFot,df_Export_from_china],axis = 0)
    return DFot,sizes,labels


# In[44]:


def export_tree_diagram(n3s,all_data_code,country_code,product_code,new_trio,target_country_name):
        export_info = export_tree_diagram_preprocess(n3s,all_data_code,country_code,product_code,new_trio,target_country_name)
        Df_export_from_china = export_info[0]
        sizes = export_info[1]
        labels = export_info[2]
        for n3 in Df_export_from_china['new_trio_type'].unique():
                Df_export_from_china_temp = Df_export_from_china[Df_export_from_china['new_trio_type'] == n3]
                print(' New trio type:', n3,'\n Total value of imports:',np.sum(sizes),'thousand USD \n',np.round(sizes[:10],2),'\n',labels[:10].values,'\n','percentage:',np.round(sizes[:10],2)/np.sum(sizes),'\n','oveall percentage:',sum(np.round(sizes[:10],2)/np.sum(sizes)))

                fig = px.treemap(Df_export_from_china_temp, path=['country'], values='export_value',color='country',
                        color_discrete_sequence = px.colors.sequential.RdBu,
                        hover_data=['percentage'])
                fig.update_layout(margin = dict(t=50, l=25, r=25, b=25),
                        title=f"The Proportion of {n3.capitalize()} exports from {target_country_name} to Other Countries.")
                fig.update_traces(root_color="lightgrey", texttemplate="%{label}<br>%{value} thousand USD<br>%{customdata[0]}%",
                        textfont=dict(color="white",size=16))
                fig.show()
                fig.write_html(f"The Proportion of {n3.capitalize()} exports from {target_country_name} to Other Countries.html")


# ### Export Sankey diagram

# In[51]:


def export_sankey_diagram(n3s,all_data_code,country_code,product_code,new_trio,target_country_name):
    Df_export_from_china = export_tree_diagram_preprocess(n3s,all_data_code,country_code,product_code,new_trio,target_country_name)[0]
    # Assuming DFot is a predefined DataFrame with necessary data
    data2 = Df_export_from_china[Df_export_from_china['export_value'] != 0].reset_index(drop=True)
    data2['export_value'] = data2['export_value'] /1000

    # Assign unique IDs
    target_country_id = 0
    type_ids = {t: i + 1 for i, t in enumerate(data2['new_trio_type'].unique())}
    country_ids = {country: i + len(type_ids) + 1 for i, country in enumerate(data2['country'].unique())}

    # Creating lists of sources, targets, and values
    sources_export = [target_country_id] * len(type_ids) + sum([[type_ids[t]] * len(data2[data2['new_trio_type'] == t]) for t in type_ids], [])
    targets_export = list(type_ids.values()) + sum([[country_ids[c] for c in data2[data2['new_trio_type'] == t]['country']] for t in type_ids], [])
    values_export = [data2[data2['new_trio_type'] == t]['export_value'].sum() for t in type_ids] + data2['export_value'].tolist()
    
    # Nodes colors
    type_colors = ['#FF69B4', '#B87333', '#0047AB']  # Adjust based on actual number of types
    colors = ['red'] + type_colors[:len(type_ids)] + ['grey' for _ in country_ids]

    # Convert HEX colors to RGBA for link colors
    link_colors_rgba =  [
        f"rgba({int(color[1:3], 16)}, {int(color[3:5], 16)}, {int(color[5:7], 16)}, 0.4)" 
        for color in type_colors
    ] + [
        f"rgba({int(tc[1:3], 16)}, {int(tc[3:5], 16)}, {int(tc[5:7], 16)}, 0.4)" 
        for tc in [type_colors[data2['new_trio_type'].unique().tolist().index(data2['new_trio_type'][i])] for i in range(len(data2['country']))]
    ] 
    # Create the Sankey diagram
    fig = go.Figure(data=[go.Sankey(
        valueformat=".0f",
        valuesuffix=" million USD",
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color='black', width=0.5),
            label=[target_country_name] + list(type_ids.keys()) + list(country_ids.keys()),
            color=colors
        ),
        link=dict(
            source=sources_export,
            target=targets_export,
            value=values_export,
            color=link_colors_rgba
        )
    )])

    fig.update_layout(title_text='Sankey Diagram of new trio Exports from 'f'{target_country_name}', font_size=10)
    fig.show()
    fig.write_html(f"Sankey Diagram of new trio Exports from {target_country_name}.html")


# ### Import diagram

# In[59]:


def import_tree_diagram(CriticalMaterials,all_data_code,country_code,product_code,target_country_name):
    DF_import = pd.DataFrame()

    for CM in CriticalMaterials:
        sizes,labels,p_des = get_importer_value(CM,all_data_code,country_code,product_code,target_country_name)
        df_import = pd.DataFrame({'country':  labels.values, 'import_value': np.round(sizes,2),'percentage':np.round(100*sizes/sizes.sum(),2)})
        df_import['country_to'] = target_country_name
        df_import['CM_type'] = f'{CM.capitalize()} Related Materials'
        DF_import = pd.concat([DF_import,df_import],axis = 0)
        print(' Critical materials type:', CM,'\n Total value of imports:',np.sum(sizes),'thousand USD \n',np.round(sizes[:10],2),'\n',labels[:10].values,'\n','percentage:',np.round(sizes[:10],2)/np.sum(sizes),'\n','oveall percentage:',sum(np.round(sizes[:10],2)/np.sum(sizes)))

        fig = px.treemap(df_import, path=['country'], values='import_value',color='country',
                        color_discrete_sequence = px.colors.sequential.RdBu,
                        hover_data=['percentage'])
        fig.update_layout(margin = dict(t=50, l=25, r=25, b=25),
                        title=f"The Proportion of {CM.capitalize()} Related Materials Imports from Countries to {target_country_name}.")
        fig.update_traces(root_color="lightgrey", texttemplate="%{label}<br>%{value} thousand USD<br>%{customdata[0]}%",
                        textfont=dict(color="white",size=15))
        fig.show()
        fig.write_html(f"The Proportion of {CM.capitalize()} Related Materials Imports from Countries to {target_country_name}.html")
    #return DF_import


# In[82]:


def import_sankey_diagram(CriticalMaterials, all_data_code, country_code, product_code, target_country_name):
    DF_import = pd.DataFrame()  # Initialize the DataFrame

    for CM in CriticalMaterials:
        sizes, labels, p_des = get_importer_value(CM, all_data_code, country_code, product_code, target_country_name)
        df_import = pd.DataFrame({
            'country': labels.values, 
            'import_value': np.round(sizes, 2),
            'percentage': np.round(100 * sizes / sizes.sum(), 2)
        })
        df_import['country_to'] = target_country_name
        df_import['CM_type'] = f'{CM.capitalize()} Related Materials'
        DF_import = pd.concat([DF_import, df_import], axis=0)

    data = DF_import[DF_import['import_value'] != 0].reset_index().drop(columns='index')
    data['import_value'] = data['import_value'] / 1000  # Convert to million USD

    # Assign unique IDs to each country and CM_type
    country_ids = {country: i for i, country in enumerate(data['country'].unique())}
    type_ids = {t: i + len(country_ids) for i, t in enumerate(data['CM_type'].unique())}
    china_id = len(country_ids) + len(type_ids)

    # Create source, target, and value lists
    sources = [country_ids[country] for country in data['country']] + \
              [type_ids[t] for t in data.groupby('CM_type')['import_value'].sum().keys()]
    targets = [type_ids[t] for t in data['CM_type']] + \
              [china_id] * len(data['CM_type'].unique())
    values = data['import_value'].tolist() + data.groupby('CM_type')['import_value'].sum().tolist()

    # Define colors
    country_color = '#D3D3D3'
    type_colors = ['#FF69B4', '#B87333', '#0047AB', '#B0B0B0']
    china_color = '#d62728'
    colors = [country_color] * len(country_ids) + type_colors + [china_color]

    # Convert HEX to RGBA string with 50% transparency
    link_colors_rgba = [
        f"rgba({int(tc[1:3], 16)}, {int(tc[3:5], 16)}, {int(tc[5:7], 16)}, 0.4)"
        for tc in [type_colors[data['CM_type'].unique().tolist().index(data['CM_type'][i])] for i in range(len(data['country']))]
    ] + [
        f"rgba({int(color[1:3], 16)}, {int(color[3:5], 16)}, {int(color[5:7], 16)}, 0.4)"
        for color in type_colors
    ]

    # Create Sankey diagram
    fig = go.Figure(data=[go.Sankey(
        valueformat=".0f",
        valuesuffix=" million USD",
        node=dict(
            pad=10,
            thickness=20,
            line=dict(color='black', width=0.5),
            label=list(country_ids.keys()) + list(type_ids.keys()) + [target_country_name],
            color=colors
        ),
        link=dict(
            source=sources,
            target=targets,
            value=values,
            color=link_colors_rgba
        )
    )])

    fig.update_layout(title_text='Sankey Diagram of Critical Materials Imports into ' f'{target_country_name}', font_size=10)
    fig.show()
    fig.write_html("Sankey Diagram of Critical Materials Imports into"f"{target_country_name}"".html")


# ## Example

# In[89]:


#Define Critical Matericals
CriticalMaterials  = ['copper', 'lithium', 'nickel', 'cobalt']
#Define dictionary to translate data columns
data_dict = {
    "t": "year",
    "i": "exporter",
    "j": "importer",
    "k": "product",
    "v": "value",
    "q": "quantity"
}

##Define data file path
dirfolder = 'C:\\Users\\WIN11\\Desktop\\intern\\WRI\\Export_Visuilization\\'
dirp = dirfolder + 'BACI_HS22_V202401/product_codes_HS22_V202401.csv'
dirc = dirfolder + 'BACI_HS22_V202401/country_codes_V202401.csv'
dird = dirfolder + 'BACI_HS22_V202401/BACI_HS22_Y2022_V202401.csv'

##Define target country
target_country_name = 'China'
##Define n3s
n3s = ['Vehicles: with only electric motor for propulsion','Cells and batteries: primary, lithium'] 
##Define new trio needs to track
new_trio = ['Electric vehicles','Lithium-ion batteries','Photovoltaic products']
##Define n3list
n3list = ['Electric generators: photovoltaic DC generators, of an output not exceeding 50W',
 'Electric generators: photovoltaic DC generators, of an output exceeding 50W',
 'Electric generators: (excluding generating sets), photovoltaic AC generators (alternators)',
 'Electrical apparatus: photosensitive semiconductor devices, photovoltaic cells not assembled in modules or made up into panels',
 'Electrical apparatus: photosensitive semiconductor devices, photovoltaic cells assembled in modules or made up into panels',
 'Electrical apparatus: photosensitive semiconductor devices, diodes other than light emitting diodes and photovoltaic cells whether or not assembled in modules or made up into panels',
 ]

#Data process
product_code = pd.read_csv(dirp)
product_code.set_index('code',inplace = True)

country_code = pd.read_csv(dirc)
country_code.set_index('country_code',inplace = True)

all_data_code = pd.read_csv(dird).rename(columns=data_dict)


# ##  Create Diagram

# In[48]:


all_data_diagram(n3list,all_data_code,country_code,product_code,target_country_name)


# In[26]:


export_tree_diagram(n3s,all_data_code,country_code,product_code,new_trio,target_country_name)


# In[84]:


export_sankey_diagram(n3s,all_data_code,country_code,product_code,new_trio,target_country_name)


# In[86]:


import_tree_diagram(CriticalMaterials,all_data_code,country_code,product_code,target_country_name)


# In[88]:


import_sankey_diagram(CriticalMaterials, all_data_code, country_code, product_code, target_country_name)


# In[ ]:




