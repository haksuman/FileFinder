import os
import pandas as pd
# this script stands for files in specific folder to be listed

def list_files(src_path, output_file_name):
    list_element = os.listdir(src_path)
    df = pd.DataFrame()
    df['file_name'] = list_element
    dst_path = src_path + "\\" + output_file_name + ".xlsx"    
    df.to_excel(dst_path)

#if __name__ == '__main__':
#    pth = r'\\fs-awp\01_TECHNICAL_OFFICE\TECH_OFFICE_PP_QS\002-PROGRESS PAYMENT\000_Follow Up tables\3620-STEEL STRUCTURE\GRATING\Transport Nakladnaya' # folder path that needs to be listed
#    dst_path = r'\\fs-awp\01_TECHNICAL_OFFICE\TECH_OFFICE_PP_QS\002-PROGRESS PAYMENT\000_Follow Up tables\3620-STEEL STRUCTURE\GRATING\file_list.xlsx'


