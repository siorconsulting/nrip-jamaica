import os 
from wbt_utils import *
import geopandas as gpd

# import whitebox
# wbt = whitebox.WhiteboxTools()

wbt = wbt_setup()

__all__ = ['intersect', # NOT TESTED
           'zonal_statistics', # NOT TESTED
           'distance_from_points', # NOT TESTED
           'distance_from_lines', # NOT TESTED
           'distance_from_polygons', # NOT TESTED
           'distance_from_raster', # NOT TESTED
           'hotspots_from_points', # NOT TESTED
           'hotspots_from_lines', # NOT TESTED
           'hotspots_from_polygons', # NOT TESTED
           'hotspots_from_raster', # NOT TESTED
           'interpolate_points', # NOT TESTED 
           'SummarizeWithin',
          ]

def intersect(input_vector_file, overlay, output_vector_file):
    """
    Function to return all feature parts that occur in both input layers

    Inputs:
        input_vector_file: str <-- path to vector(.shp) file
        overlay: str <-- path to overlay vector(.shp) file
        output_vector_file: str <-- name of output vector(.shp) file

    Outputs:
        output_vector_file: shapefile  <-- output vector shapefile
    """
    wbt.intersect(input_vector_file, overlay, output_vector_file)

def zonal_statistics(input_raster, input_zones, output_raster, stat='mean', input_zones_is_raster=True):
    """Calculates zonal statistics based on an input raster, using raster or polygon zones. 
    
    Inputs:
        input_raster : str <-- path to raster(.tif) file
        input_zones : str <-- input path to raster(.tif) or polygon(.shp)
        output_raster : str <-- output raster(.tif) file name
        stat [optional] : str <-- default value is 'mean'
        input_zones_is_raster [optional] : boolean <-- default value is 'True'

    Exports:
        output_raster : raster <-- output raster(.tif) file

    Returns:
        None

    """

    if input_zones_is_raster:
        input_zones_raster = input_zones # if statement assigning input_zones to raster variable if already a raster
    else:
        input_zones_raster = 'temp_input_raster.tif' # assigning file name
        wbt.vector_polygons_to_raster(input_zones, input_zones_raster) # transforming polygon to raster if input_zones is a polygon
    
    wbt.zonal_statistics(i=input_raster, features=input_zones_raster, output=output_raster, stat=stat)

    if not input_zones_is_raster:
        os.remove(os.path.join(wbt.work_dir,input_zones_raster)) # removing temporary raster file if one had to be created
    
def distance_from_points(input_points, output_raster):
    """
    Creates new raster showing distances between input points

    Inputs:
        input_points: str <-- path to input point (.shp) file
        output_raster: str <-- raster(.tif) file name

    Outputs: 
        output_raster: raster <-- raster(.tif) file

    Returns:
        None
    """
    input_raster = 'temp_input_raster.tif' # assigning file name
    wbt.vector_points_to_raster(input_points,input_raster) # points to raster transformation
    wbt.euclidean_distance(input_raster, output_raster) # euclidean distance calculated on created raster
    os.remove(os.join.path(wbt.work_dir,input_raster)) # removes temporary raster file

def distance_from_lines(input_lines, output_raster):
    """
    Creates new raster showing distances between lines

    Inputs: 
        input_lines: str <-- path to input point(.shp) file
        output_raster: str <-- raster(.tif) file name
    """
    input_raster = 'temp_input_raster.tif'  # assigning file name
    wbt.vector_points_to_raster(input_lines,input_raster) # lines to raster transformation
    wbt.euclidean_distance(input_raster, output_raster) # euclidean distance calculated on created raster
    os.remove(os.join.path(wbt.work_dir,input_raster)) # removes temporary raster file

def distance_from_polygons(input_polygons, output_raster):
    """
    Creates new raster showing distances between polygons
    """
    input_raster = 'temp_input_raster.tif' # assigning file name
    wbt.vector_points_to_raster(input_polygons,input_raster) # polygons to raster transformation
    wbt.euclidean_distance(input_raster, output_raster) # euclidean distance calculated on created raster
    os.remove(os.join.path(wbt.work_dir,input_raster)) # removes temporary raster file

def distance_from_raster(input_raster, output_raster):
    """
    Creates new raster showing distances within raster
    """
    wbt.euclidean_distance(input_raster, output_raster) # euclidean distance calculated on input raster

def hotspots_from_points(input_points, output_raster, filterx=11, filtery=11, k=5):
    """
    Creates hotspot raster from input point shapefile

    Inputs:
        input_points: str <-- path to input point(.shp) file
        output_raster: str <-- name of output raster(.tif) file
        filterx [optional] : int <-- size of kernel in x-direction, default value is '11'
        filtery [optional] : int <-- size of kernel in y-direction, default value is '11'
        k [optional] : int <-- number of nearest-valued neighbours to use, default value is '5'

    Outputs:
        output_raster: raster <-- output raster(.tif) file

    Returns:
        None
    """
    input_raster = 'temp_hotspots_from_points.tif' # assigning temporary file name
    wbt.vector_points_to_raster(input_points, input_raster) # points to raster transformation
    wbt.k_nearest_mean_filter(input_raster, output_raster, filterx=filterx, filtery=filtery, k=k) 
    os.remove(os.path.join(wbt.work_dir, input_raster)) # remove temporary raster file

def hotspots_from_lines(input_lines, output_raster, filterx=11, filtery=11, k=5):
    """
    Creates hotspot raster from input line shapefile

    Inputs:
        input lines: str <-- path to input line(.shp) file
        output_raster: str <-- raster(.tif) file name
        filterx [optional] : int <-- size of kernel in x-direction, default value is '11'
        filtery [optional] : int <-- size of kernel in y-direction, default value is '11'
        k [optional] : int <-- number of nearest-valued neighbours to use, default value is '5'

    Outputs:
        output_raster: raster <-- raster(.tif) file 

    Returns:
        None
    """
    input_raster = 'temp_hotspots_from_lines.tif' # assigning temporary file name
    wbt.vector_lines_to_raster(input_lines, input_raster) # lines to raster transformation
    wbt.k_nearest_mean_filter(input_raster, output_raster, filterx=filterx, filtery=filtery, k=k)
    os.remove(os.path.join(wbt.work_dir, input_raster)) # remove temporary file

def hotspots_from_polygons(input_polygons, output_raster, filterx=11, filtery=11, k=5):
    """
    Creates hotspot raster from input polygon shapefile

    Inputs:
        input polygons: str <-- path to input line(.shp) file
        output_raster: str <-- raster(.tif) file name
        filterx [optional] : int <-- size of kernel in x-direction, default value is '11'
        filtery [optional] : int <-- size of kernel in y-direction, default value is '11'
        k [optional] : int <-- number of nearest-valued neighbours to use, default value is '5'

    Output:
        output_raster: raster <-- raster(.tif) file
    
    Returns:
    None
    """
    input_raster = 'temp_hotspots_from_polygons.tif' # assigning temporary file name
    wbt.vector_polygons_to_raster(input_polygons, input_raster) # polygons to raster transformation
    wbt.k_nearest_mean_filter(input_raster, output_raster, filterx=filterx, filtery=filtery, k=k)
    os.remove(os.path.join(wbt.work_dir, input_raster)) # remove temporary file

def hotspots_from_raster(input_raster, output_raster, filterx=11, filtery=11, k=5):
    """
    Creates hotspot raster from input raster file

    Inputs:
        input polygons: str <-- path to input line(.shp) file
        output_raster: str <-- raster(.tif) file name
        filterx [optional] : int <-- size of kernel in x-direction, default value is '11'
        filtery [optional] : int <-- size of kernel in y-direction, default value is '11'
        k [optional] : int <-- number of nearest-valued neighbours to use, default value is '5'
    
    Outputs:
        output_raster: raster <-- raster(.tif) file
    
    Returns:
        None
    """
    wbt.k_nearest_mean_filter(input_raster, output_raster, filterx=filterx, filtery=filtery, k=k)

def interpolate_points(input_points, output_raster):
    """
    Intepolates points into a raster surface 

    Inputs:
        input_points: str <-- path to input point shapefile
        output_raster : str <-- name of output raster(.tif) file 

    Outputs:
        output_raster: raster <-- output raster(.tif) file

    Returns:
        None
    """
    wbt.radial_basis_function_interpolation(i=input_points, output=output_raster) # interpolation function

def SummarizeWithin(input_vector, feature_polygons, output_polygon, field_to_summarize, aggfunc='mean'):
    """
    Summarizies vector data relative to exisiting polygons

    Inputs:
        input_vector: str <-- path to input vector(.shp) file. Can be point/lines/polygons
        feature_polygons: str <-- path to input polygons(.shp)
        output_polygon: str <-- name of output polygon(.shp) file
        field_to_summarize: str <-- name of field to summarize
        aggfunc [optional]: str: aggregation function, default is 'mean'

    Outputs:
        output_polygon: shapefile <-- polygon(.shp) file
    """
    input_vector = gpd.read_file(input_vector) # geopandas read vector
    feature_polygons = gpd.read_file(feature_polygons) # geopandas polygons 
    input_vector_join = input_vector[field_to_summarize].join(other=feature_polygons,rsuffix='_polygon') # attribute join on both inputs
    input_vector_join.dissolve(by='FID_polygon', aggfunc=aggfunc) # dissolve geometries
    input_vector_join.to_file(os.path.join(wbt.work_dir, output_polygon)) # save as file ouput_polygons