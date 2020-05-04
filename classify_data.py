import pandas as pd
import file_sheet_name as fsname


def divide_by_target(excelName, sheetName=None):
    df = pd.read_excel(excelName, skiprows=[], sheet_name=sheetName, keep_default_na=None)
    target_sequence = pd.read_excel(excelName, fsname.sheetName2).iloc[0:28, 1]
    for sequence in target_sequence:
        tmp_df = df[ df['Target sequence'] == sequence ]
        tmp_df.to_excel('./classify/' + sequence + '.xlsx', index=False)


if __name__ == "__main__":
    divide_by_target(fsname.inputFile, fsname.sheetName1)