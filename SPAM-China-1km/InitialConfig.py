import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Add sections and options with values
config["directories"] = {
    # Directory for province shapefiles
    "dir_provshp": "./shp/",
    
    # Directory for SPAM GeoTIFF files
    "dir_prodtif": "C:/Users/Yuchen.Guo/OneDrive/WRI/project/RiskImpact/spam2010v2r0_global_prod.geotiff/",
    
    # Directory for production Excel files
    "dir_prodxls": "./excel/",
    
    # Output directory
    "dir_output": "./out/",
}


"""
province can be selected

"""

"""
Crops can be selectd:
['wheat', '小麦'],
['rice', '稻谷'],
['maize', '玉米'],
['barley', '大麦'],
['sorghum', '高粱'],
['potato', '马铃薯'],
['bean', '豆类'],
['soybean', '大豆'],
['groundnut', '花生'],
['sunflower', '葵花籽'],
['rapeseed', '油菜籽'],
['sesameseed', '芝麻'],
['sugarcane', '甘蔗'],
['sugarbeet', '甜菜'],
['cotton', '棉花'],
['tobacco', '烟叶'],
['vegetables', '蔬菜']

"""
config["crops"] = {
    "crop": "wheat"
}

"""

Years can be selectd: from 2010 to 2022

"""

config["years"] = {
    "target_year": "2020"
}

"""
['云南省','北京市','天津市','河北省',
 '山西省', '内蒙古自治区','辽宁省',
 '吉林省', '黑龙江省','上海市',
 '江苏省', '浙江省','安徽省',
 '福建省', '江西省','山东省',
 '河南省', '湖北省','湖南省',
 '广东省', '广西壮族自治区','海南省',
 '重庆市', '四川省','贵州省',
 '西藏自治区', '陕西省', '甘肃省', '青海省',
 '宁夏回族自治区', '新疆维吾尔自治区']

"""

config["regions"] = {
    "province": '云南省'
}


# Save the configuration to a file
with open("config.ini", "w") as configfile:
     config.write(configfile)
     
province = ['云南省','北京市','天津市','河北省',
 '山西省', '内蒙古自治区','辽宁省',
 '吉林省', '黑龙江省','上海市',
 '江苏省', '浙江省','安徽省',
 '福建省', '江西省','山东省',
 '河南省', '湖北省','湖南省',
 '广东省', '广西壮族自治区','海南省',
 '重庆市', '四川省','贵州省',
 '西藏自治区', '陕西省', '甘肃省', '青海省',
 '宁夏回族自治区', '新疆维吾尔自治区']
"""
import subprocess
import time

for pp in province:
    print(pp)
    
    config["regions"] = {
        "province": pp
    }

    # Save the configuration to a file
    with open("config.ini", "w") as configfile:
        config.write(configfile)
    
    # Define the path to your script
    script_path = 'SPAMChina1km.py'

    # Run the script
    process = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(25) 
   
"""
