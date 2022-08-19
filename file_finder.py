import pandas as pd
import shutil
import os


def file_copy_func(path_source_list, path_source_folder, path_target_folder, file_ext):
    # path_source_list = input("Please enter path of source list excel:") working
    # r"C:\Users\haaksuman\Desktop\development\python\FileFinder\RFI_LIST.xlsx"  # inputting excel file path
    df_source_list = pd.read_excel(path_source_list, usecols="A", na_filter=False, header=None)
    df_source_list = df_source_list.drop_duplicates()

    error_list = []
    for index_df, row_df in df_source_list.iterrows():
        print(row_df)
        file_full_name = df_source_list.iloc[index_df][0] + file_ext
        file_absolute_path = os.path.join(path_source_folder, file_full_name)
        if os.path.exists(file_absolute_path):
            shutil.copy2(file_absolute_path, path_target_folder)
        else:
            error_list.append(row_df)
    df_error = pd.DataFrame(error_list)
    df_error.to_excel(os.path.join(path_target_folder, "error_log.xlsx"))


if __name__ == '__main__':
    input_list2found = r"C:\Users\haaksuman\Desktop\development\python\FileFinder\search_list.xlsx"
    input_dir_files = r"\\fs-awp\04_QA_QC\08_RFI\01_RFI"
    input_dir_copy = r"C:\Users\haaksuman\Desktop\development\python\FileFinder\rfi_folder"
    input_file_ext = ".pdf"

    file_copy_func(input_list2found, input_dir_files, input_dir_copy, input_file_ext)
