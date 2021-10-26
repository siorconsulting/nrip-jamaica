import whitebox
wbt = whitebox.WhiteboxTools()

__all__ = ['euclidean_distance',
           'intersect',
           'zonal_statistics',
           'k_nearest_mean_filter'
          ]

def euclidean_distance(input_raster, output_raster):
    wbt.euclidean_distance(input_raster, output_raster)
    
def intersect(input_vector_file, overlay, output_vector_file):
    wbt.intersect(input_vector_file, overlay, output_vector_file)

def zonal_statistics():
    wbt.zonal_statistics()
    
def k_nearest_mean_filter():
    wbt.k_nearest_mean_filter()
