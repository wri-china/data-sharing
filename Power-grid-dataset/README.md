
#  Power Grid Dataset Overview 

## Project Description

This project focuses on creating a medium-voltage grid dataset with a 1000m buffer, stored in the `grid_1000m_raster_gf.tif` file. The code `vector2raster.py` is used to generate this dataset from various input sources, providing a spatial representation of predicted and existing power grids.

### Files and Dataset

- **grid_1000m_raster_gf.tif**: This is the final raster dataset representing the medium-voltage grid with a 1000m buffer.

- **grid.gpkg**: Vectorized dataset predicting the distribution of the transmission line network, including existing OpenStreetMap transmission lines tagged under the 'source' column.
  - **Source**: [Gridfinder](https://gridfinder.rdrn.me/) columns `gf` represent medium-voltage

- **reference_crop_dataset**: This folder contains reference datasets used in the generation of the grid. A key file is `Finalcrop_China+Southeast_Asia_BANA_2020_physical_area_ha_2020_0.00925926.tif`, representing a crop dataset across China and Southeast Asia.
  - **Reference Dataset Folder**: [Link](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/Regional-powergrid-dataset/reference_crop_dataset/Finalcrop_China+%2B+Southeast+Asia_BANA_2020_physical_area_ha_2020_0.00925926.tif)

### Code

- **vector2raster.py**: This script outlines the steps to process the vectorized grid network (grid.gpkg) and crop datasets to produce the `grid_1000m_raster_gf.tif` file. It applies a 1000m buffer around the medium-voltage grid and rasterizes the results.

### Dataset Sources

- **Gridfinder**: The source of the vectorized transmission line network used in the creation of this dataset. Available at [Gridfinder](https://gridfinder.rdrn.me/).
  
- **Finalcrop Dataset**: This reference crop dataset is used as an additional input in the analysis to account for crop areas in the regions of interest. Available [here](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/Regional-powergrid-dataset/reference_crop_dataset/Finalcrop_China+%2B+Southeast+Asia_BANA_2020_physical_area_ha_2020_0.00925926.tif).

### Output Dataset

The final dataset is available for download here:
- [grid_1000m_raster_gf.tif](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/Regional-powergrid-dataset/raster/grid_1000m_raster_gf.tif)
