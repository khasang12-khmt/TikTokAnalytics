import json
import pandas as pd

def process_results(data):
    # Define which nested columns should be expanded and diminished
    nested_values = ['video','author','music','stats','authorStats','challenges','duetInfo','stickersOnItem','textExtra','mixInfo','warnInfo','effectStickers']
    ignore_values = ['challenges','duetInfo','stickersOnItem','textExtra','mixInfo','warnInfo','effectStickers']
    
    flatten_data = {}
    # foreach item in list_dict
    for idx, value in enumerate(data):
        flatten_data[idx] = {}
        # foreach item in dict
        for prop_key, prop_value in value.items():
            if prop_key in nested_values: 
                # ignore some columns
                if prop_key in ignore_values:
                    pass
                else:
                    # unpack some columns
                    for nested_key, nested_value in prop_value.items():
                        # Reformatting to avoid name conflicts
                        flatten_data[idx][prop_key+'_'+nested_key] = nested_value            
            else:
                flatten_data[idx][prop_key] = prop_value
    return flatten_data