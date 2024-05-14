# -*- coding: utf-8 -*-
import rioxarray as rxr
import geopandas as gpd
import pandas as pd
import os
import glob
import xarray as xr
from rasterio.enums import Resampling
import rasterio
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import warnings
warnings.filterwarnings("ignore")

def Resampling_(raster,upscale_factor = 10):

    if raster.rio.crs == None:
        raster.rio.write_crs("epsg:4326", inplace=True)
        
    new_width = raster.rio.width * upscale_factor
    new_height = raster.rio.height * upscale_factor

    raster_upsampled = raster.rio.reproject(
        raster.rio.crs,
        shape = (new_height, new_width),
        resampling = Resampling.bilinear,
    )
    #print(raster.values[(raster.values>=0)&(raster.values<=9999999.)].sum())
    
    
    raster_upsampled.values[(raster_upsampled.values>=0)&(raster_upsampled.values<=9999999.)] = raster.values[(raster.values>=0)&(raster.values<=9999999.)].sum()*raster_upsampled.values[(raster_upsampled.values>=0)&(raster_upsampled.values<=9999999.)]/raster_upsampled.values[(raster_upsampled.values>=0)&(raster_upsampled.values<=9999999.)].sum()
    
    #print(raster_upsampled.values[(raster_upsampled.values>=0)&(raster_upsampled.values<=9999999.)].sum())
    
    return raster_upsampled

def production_history_cal_upsample(dir_distribution,target,production,shp,target_year,upscale_factor=10):
    
    prod = production[production['Crop (full)'] == target]
    
    raster_dir = glob.glob(dir_distribution +'/clip_{0}_*'.format(Province)+prod['Name (code)'].values[0].upper()+'_A.tif')[0]
     
    raster_before = rxr.open_rasterio(raster_dir)
    
    raster_UP = Resampling_(raster_before,upscale_factor)
    
    #########clip base on province's shapefile
    prodUP = raster_UP.rio.clip(shp.geometry.values, shp.crs)

    ######## calibrate dataset base on https://data.stats.gov.cn/easyquery.htm?cn=C01
    overall = prodUP.values[np.where((prodUP.values>=0)&(prodUP.values<=9999999.))].sum()
    
    basevalue = prod[2010].values
    
    prodUP.values[np.where((prodUP.values>=0)&(prodUP.values<=9999999.))] = (prodUP.values[np.where((prodUP.values>=0)&(prodUP.values<=9999999.))]/overall)*basevalue*10000

    # migrating through the years
    Ratio = prod[target_year].values/basevalue

    prodUP.values[np.where((prodUP.values>=0)&(prodUP.values<=9999999.))] = prodUP.values[np.where((prodUP.values>=0)&(prodUP.values<=9999999.))]*Ratio
    
    status = pd.isna(prodUP.values[0].max())

    return prodUP,status

def Plot_dataset(dataset,region,crop,year = 2010):
    # https://docs.xarray.dev/en/stable/generated/xarray.plot.imshow.html
    # Set up a standard map for latlon data for multiple subplots
    fig, geo_axes = plt.subplots(nrows=2, ncols=3, figsize=(8, 6),
                    subplot_kw={'projection': ccrs.PlateCarree()})
    # adjust the spacing between subplots
    fig.subplots_adjust(wspace=0.01, hspace=0.3)
    minx,miny,maxx,maxy = Region.bounds.values[0]
    var_names = list(dataset.data_vars.keys())
    #print(var_names)

    k = 0
    for i in range(0,2):
        for j in range(0,3):
            geo_axes[i][j].set_extent([minx, maxx, miny, maxy])
        
            v = var_names[k]

            im = dataset[v].plot.imshow(ax = geo_axes[i][j], cmap='Greens', 
                 cbar_kwargs={'label': 'Production_'+v+' (t)', 'orientation': 'horizontal', 'shrink': 0.75, 'aspect': 25, 'extend': 'both'})
            im.colorbar.ax.tick_params(labelsize = 9)
        
            # boudary for the province
            region.plot(ax=geo_axes[i][j], facecolor='none', edgecolor='black', linewidth = 0.5)

            # gridline
            gl = geo_axes[i][j].gridlines(draw_labels=True, x_inline=False, y_inline=False, dms=True,
                  linestyle='--', lw=0.5, rotate_labels=False,
                  color='dimgrey', crs=ccrs.PlateCarree())
            gl.xlabel_style = {'fontsize': 7}
            gl.ylabel_style = {'fontsize': 7}
            gl.top_labels = False
            gl.right_labels = False

            geo_axes[i][j].set_title('{0}{1}{2}年产量_{3}'.format(region['省'].values[0], crop, year, v),
                    fontdict = {'family':'SimHei', 'size': 11})

            k = k+1
    return fig

import configparser
if __name__ == "__main__":
    # Load configuration
    config = configparser.ConfigParser()
    config.read("config.ini")

    Province = config.get("regions", "province")
    Crop = config.get("crops", "crop")
    # Crop_list = ["wheat","rice","maize","soybean","sugarcane","tobacco"]
    Year = config.getint("years", "target_year")
    """
    *_A	all technologies together, ie complete crop
    *_I	irrigated portion of crop
    *_H	rainfed high inputs portion of crop
    *_L	rainfed low inputs portion of crop
    *_S	rainfed subsistence portion of crop
    *_R	rainfed portion of crop (= A - I, or H + L + S)
    """

     # Set the directory for output
    dir_output = config.get("directories", "dir_output")
    for i in ['Prod_2010', 'Prod_{0}'.format(Year)]:
        output_directory = os.path.join(dir_output, i)
        os.makedirs(output_directory, exist_ok=True)
    dir_prod2010 = os.path.join(dir_output, 'Prod_2010')
    dir_prodT = os.path.join(dir_output, 'Prod_{0}'.format(Year))

    dir_shp = config.get("directories", "dir_provshp")
    China = gpd.read_file(os.path.join(dir_shp,'China_province.shp'),encoding = 'utf-8')
    Region = China[China['省'] == Province]
    minx,miny,maxx,maxy = Region.bounds.values[0]

    dir_prodxls = config.get("directories", "dir_prodxls")
    Production = pd.read_excel(os.path.join(dir_prodxls,'Annual_price_for_crops_new.xlsx'),"Production_"+Province)
    CropName = Production[Production['Crop (full)'] == Crop]['Name (code)'].values[0].upper()

    dir_global = config.get("directories", "dir_prodtif")
    # Get the production of the crop in 2010
    Prod_A = glob.glob(os.path.join(dir_global, '*_{0}_A.tif'.format(CropName)))
    da_A = rxr.open_rasterio(Prod_A[0])

    resx = abs(da_A.x[0].values-da_A.x[1].values)
    resy = abs(da_A.x[0].values-da_A.x[1].values)

    da_A_Env = da_A.where((da_A.x > minx-2*resx)&(da_A.x<maxx+2*resx)&(da_A.y>miny-2*resy)&(da_A.y<maxy+2*resy),drop=True)
    # Export the production of 2010 to the dir_distribution
    da_A_Env.rio.to_raster(dir_prod2010+'/clip_{0}_'.format(Province)+os.path.basename(Prod_A[0]))
    da_A_Clip = da_A_Env.squeeze().rio.clip(Region.geometry.values, Region.crs)
    dis_A = xr.DataArray(da_A_Clip)
    ds_dis = xr.Dataset()
    ds_dis.update({'A': dis_A})

    # Get the production of the crop in 2020
    Prod_TargetYear_UP,status = production_history_cal_upsample(
        dir_distribution = dir_prod2010,
        target = Crop,
        production = Production,
        shp = Region,
        target_year = Year,
        upscale_factor = 10)
    
    print(status,"False means the data valid, True means the data invalid")

    prod_A_10 = xr.DataArray(Prod_TargetYear_UP.squeeze())
    # Export the production of 2010 to the dir_prodT
    prod_A_10.rio.to_raster(dir_prodT+'/P_A_{0}_{1}_{2}_'.format(Province, Crop,Year)+os.path.basename(Prod_A[0]))
    ds_prod = xr.Dataset()
    ds_prod.update({'A': prod_A_10})

    tech_List = ['I', 'H', 'L', 'S', 'R']
    
    for tech in tech_List:

        Prod_dis_tech = glob.glob(os.path.join(dir_global, '*_{0}_{1}.tif'.format(CropName, tech)))
        data_tech = rxr.open_rasterio(Prod_dis_tech[0])

        resx = abs(data_tech.x[0].values-data_tech.x[1].values)
        resy = abs(data_tech.x[0].values-data_tech.x[1].values)

        dataTechEnv = data_tech.where((data_tech.x > minx-2*resx)&(data_tech.x<maxx+2*resx)&(data_tech.y>miny-2*resy)&(data_tech.y<maxy+2*resy),drop=True)

        dataTechEnv.rio.to_raster(dir_prod2010+'/clip_{0}_'.format(Province)+os.path.basename(Prod_dis_tech[0]))

        # first, clip as the distribution of 2010 and add it to the dataset
        dis_tech = dataTechEnv.squeeze().rio.clip(Region.geometry.values, Region.crs)
        ds_dis.update({'{0}'.format(tech): dis_tech})

        # Then, resample the envlope dataset of 2010 and get the ratio
        dis_tech_up = Resampling_(dataTechEnv,upscale_factor = 10)
        dis_A_up = Resampling_(da_A_Env,upscale_factor = 10)
        dis_tech_ratio = dis_tech_up/dis_A_up

        dis_tech_ratio_clip = dis_tech_ratio.squeeze().rio.clip(Region.geometry.values, Region.crs)

        P_tech = prod_A_10 * dis_tech_ratio_clip
        prod_tech = xr.DataArray(P_tech.squeeze())
        # prod_tech = prod_tech.where(prod_tech < prod_tech.max())
        prod_tech.rio.to_raster(dir_prodT+'/P_{0}_{1}_{2}_{3}_'.format(tech,Province, Crop,Year)+os.path.basename(Prod_dis_tech[0]))

        ds_prod.update({'{0}'.format(tech): prod_tech})

    ds_dis = ds_dis.where(ds_dis >= 0)
    ds_dis = ds_dis.astype(float)
    ds_prod = ds_prod.where(ds_prod >= 0)
    ds_prod = ds_prod.astype(float)

    config={
        "font.family":'serif',
        "mathtext.fontset":'stix',
        "font.serif":['Times New Roman','Simsun'],
        'axes.unicode_minus':False
    }
    plt.rcParams.update(config)

    CropCHN = Production[Production['Crop (full)'] == Crop]['Name in raw data'].values[0]

    Crop_prod2010 = Plot_dataset(dataset = ds_dis,region = Region,crop = CropCHN,year = 2010)
    Crop_prod2010.savefig(dir_prod2010+'/{0}{1}2010年产量.png'.format(Region['省'].values[0],CropCHN),  dpi=330, bbox_inches='tight')

    Crop_prodY = Plot_dataset(dataset = ds_prod,region = Region,crop = CropCHN,year = Year)
    Crop_prodY.savefig(dir_prodT+'/{0}{1}{2}年产量.png'.format(Province.split("省")[0],CropCHN,Year),  dpi=330, bbox_inches='tight')

    plt.close("all")