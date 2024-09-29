# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 17:57:24 2024

@author: Yuchen.Guo
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 12:25:56 2024

@author: Yuchen.Guo
"""

import geopandas as gpd
from tqdm import tqdm
import os
import glob
import rioxarray as rxr
from rasterio.features import rasterize
import rasterio

def buffer_geometry(geom, distance=1000, resolution=20):
    #### Set your buffer distance
    
    try:
        return geom.buffer(distance, resolution)
    except:
        return geom.buffer(0)
    
    

def rasterize_geodataframe(final_gdf, reference_raster, output_raster_path, crs):
    """
    Rasterizes a GeoDataFrame to match the resolution and extent of a reference raster.

    Parameters:
    final_gdf (GeoDataFrame): The GeoDataFrame to rasterize.
    reference_raster (str): Path to the reference raster file to match properties.
    output_raster_path (str): Path to save the output raster file.
    crs (dict or str): Coordinate reference system to use for the output raster.

    Returns:
    None
    """
    # Load the reference raster
    refer_raster = rxr.open_rasterio(reference_raster)
    
    # Extract raster properties from the reference raster
    transform = refer_raster.rio.transform()
    out_shape = refer_raster.shape[1:]  # (height, width)

    # Rasterize the GeoDataFrame using the reference raster's properties
    out_image = rasterize(
        ((geom, 1) for geom in final_gdf.geometry),
        out_shape=out_shape,
        transform=transform,
        fill=0,  # Background value for the raster
        dtype='uint8'
    )

    # Metadata for the output raster
    out_meta = {
        'driver': 'GTiff',
        'height': out_image.shape[0],
        'width': out_image.shape[1],
        'count': 1,
        'dtype': out_image.dtype,
        'crs': crs,  # Use the CRS provided
        'transform': transform,
    }

    # Save the rasterized GeoDataFrame to a new TIFF file
    with rasterio.open(output_raster_path, 'w', **out_meta) as dest:
        dest.write(out_image, 1)    




def get_final_buffer(gridgpd_op_best_utm,crs,dirout,filename,dis = 1000):
    if os.path.exists(os.path.join(dirout,filename.replace('.shp',f'_buffer_{dis}m.geojson'))):
        final = gpd.read_file(os.path.join(dirout,filename.replace('.shp',f'_buffer_{dis}m.geojson')))
    else:
        gridgpd_op_reproj = gridgpd_op_best_utm.copy()
        tqdm.pandas(desc="Buffering geometries")
        gridgpd_op_reproj['geometry'] = gridgpd_op_reproj['geometry'].progress_apply(lambda geom: buffer_geometry(geom, distance=dis))
        final = gridgpd_op_reproj.to_crs(crs)
        #final.to_file(os.path.join(dirout,filename.replace('.gpkg',f'_buffer_{dis}m.geojson')))
        final.to_file(os.path.join(dirout,filename.replace('.shp',f'_buffer_{dis}m.geojson')))
    return final


dis = 1000  # Set your buffer distance
crs = "EPSG:4326" # set crs

## Replace your output folder
dirout = 'E:/SPAM/grid_available/'
rasterout = os.path.join(dirout, f'grid_{dis}m_raster_gf.tif')

## Replace your target folder of reference raster grid
referdir = r'E:/SPAM/calibration_crop_phy/'
reference_raster = os.path.join(referdir,'Finalcrop_China + Southeast Asia_BANA_2020_physical_area_ha_2020_0.00925926.tif')

## Replace your grid dataset
dirin = r'C:/Users/Yuchen.Guo/OneDrive - World Resources Institute/Desktop/wordbank/gadm404-shp/'
filename = "grid_china_southasian_gf.gpkg"

# To best crs
gridgpd_op = gpd.read_file(os.path.join(dirin,filename))
gridgpd_op_best_utm = gridgpd_op.to_crs(gridgpd_op.estimate_utm_crs())

## vec to raster
final = get_final_buffer(gridgpd_op_best_utm,crs,dirout,filename,dis = dis)   
rasterize_geodataframe(final, reference_raster, rasterout, crs)


