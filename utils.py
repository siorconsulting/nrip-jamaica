import arcpy

__all__ = ['change_first_character_to_alphabetic',
           'rename_feature_class_if_already_exists',
           'create_geodatabase'
          ]

def change_first_character_to_alphabetic(name):
    """Adds AA_ prefix to a string if its first character is not alphabetic
    
    Inputs:
        name : string
        
    Returns:
        name : string
    """
    if not(name[0].isalpha()):
        return 'AA_' + name
    else:
        return name

def rename_feature_class_if_already_exists(gdb_folder_path, gdb_name, out_feature_class):
    """Adds numeric suffix to a feature class name if this already exists in the specified geodatabase
    
    Inputs:
        gdb_folder_path : str
        gdb_name : str
        out_feature_class : str
        
    Returns:
        out_feature_clas : str
    """
    if not(arcpy.Exists(os.path.join(gdb_folder_path,gdb_name,out_feature_class))):
        return out_feature_class
    
    else:
        new_out_feature_class = out_feature_class + '_1'
    
        i = 1
        while arcpy.Exists(os.path.join(gdb_folder_path,gdb_name,new_out_feature_class)):
            i = i + 1
            new_out_feature_class = out_feature_class + f'_{i}'
    
        return new_out_feature_class
    

def create_geodatabase(gdb_folder_path, gdb_name):
    """Creates a new file geodabatase at the specified location and, if needed, overwrites the existing one.
    
    Inputs:
        gdb_folder_path : str
        gdb_name : str
        
    Returns:
        None
        
    """
    arcpy.management.Delete(os.path.join(gdb_folder_path,gdb_name))
    arcpy.management.CreateFileGDB(gdb_folder_path, gdb_name)

def reclassify_raster(in_raster, reclass_field, save_raster=False, save_raster_path=None):
    """Reclassify raster
    
    Inputs:
           in_raster : raster
           reclass_field :
           remap :
    
    Returns:
           None
    """
    
    outReclassify = Reclassify(in_raster, reclass_field, remap,
    if save_raster:
           outReclassify.save(save_raster_path)          
