#  Power Grid Dataset

This dataset focuses on creating a medium-voltage grid dataset with a 1000m buffer in China and Southeast Asia, stored in the [China_Southeast_Asia_grid_1000m_raster_gf.tif](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/power_grid_dataset/output/China_Southeast_Asia_grid_1000m_raster_gf.tif) file. The script [power_grid_to_raster.py](power_grid_to_raster.py) outlines the steps to process the vectorized grid network and the referenced crop dataset, providing a spatial representation of predicted and existing power grids.

### Files and Datasets
- **grid.gpkg**: Vectorized dataset predicting the distribution of the transmission line network, including existing Open Street Map transmission lines tagged under the 'source' column. The source of the data is from [Gridfinder](https://gridfinder.rdrn.me/), the column `gf` represents medium-voltage.

- **reference_dataset**: This folder contains reference datasets used in the generation of the grid. A key file is [China_Southeast_Asia_BANA_2020.tif](https://china-data-team-bucket-public.s3.cn-northwest-1.amazonaws.com.cn/power_grid_dataset/reference_dataset/China_Southeast_Asia_BANA_2020.tif), which represents a crop dataset across China and Southeast Asia.

- **China_Southeast_Asia_grid_1000m_raster_gf.tif**: The final output raster dataset represents the medium-voltage grid with a 1000m buffer in China and Southeast Asia.

##### * Please contact the WRI China Data team if you need raw data for global power grids
