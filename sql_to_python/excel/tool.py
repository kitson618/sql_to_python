from pathlib import Path
from typing import List, Dict

from sql_to_python.filter.logic import generate_data_list
from sql_to_python.translator.translator_q1 import query_all
from sql_to_python.translator.translator_q2 import query_with_filter
from sql_to_python.translator.translator_q3 import query_with_order
from sql_to_python.translator.translator_q4 import delete_record_query
from sql_to_python.translator.translator_q5 import update_record_query
from sql_to_python.translator.translator_q6 import add_table_column_query
from sql_to_python.translator.translator_q7 import query_with_groupby
from sql_to_python.translator.translator_q8 import query_multiple_tables_A
from sql_to_python.translator.translator_q9 import query_multiple_tables_B
from sql_to_python.translator.translator_q10 import create_table

import pandas as pd
import xlsxwriter
from xlsxwriter import Workbook
# Reference:
# https://xlsxwriter.readthedocs.io/tutorial01.html
# https://xlsxwriter.readthedocs.io/worksheet.html
# https://xlsxwriter.readthedocs.io/working_with_cell_notation.html
# https://pythonspot.com/read-excel-with-pandas/
# http://www.blog.pythonlibrary.org/2018/06/06/creating-and-manipulating-pdfs-with-pdfrw/


def create_spreadsheet(sheet_name: str,workbook: Workbook):
    pass


def generate_excel(import_path_name: Path, export_path_name: Path):
    workbook = xlsxwriter.Workbook(str(export_path_name.absolute()))

    # Q1
    result = query_all(import_path_name, "Emp")
    write_excel(result, "Q1", workbook)
    # Q2
    result = query_with_filter(import_path_name, "Emp")
    write_excel(result, "Q2", workbook)
    # Q3
    result = query_with_order(import_path_name, "Emp", "empNo", "mgr")
    write_excel(result, "Q3", workbook)
    # Q4
    result = delete_record_query(import_path_name, "Emp", "eName", "MARTIN")
    write_excel(result, "Q4", workbook)
    # Q5
    result = update_record_query(import_path_name, "Emp", "salary", 60000, "empNo", 7839)
    write_excel(result, "Q5", workbook)
    # Q6
    result = add_table_column_query(import_path_name, "Salgrade", "diff", "hiSal", "loSal")
    write_excel(result, "Q6", workbook)
    # Q7
    result = query_with_groupby(import_path_name, "Emp", "deptNo", "empNo", "job", "CLERK")
    write_excel(result, "Q7", workbook)
    # Q8
    result = query_multiple_tables_A(import_path_name, "Emp", "empNo", "mgr", "empNo", "eName")
    write_excel(result, "Q8", workbook)
    # Q9
    result = query_multiple_tables_B(import_path_name, "Emp", "salary", "empNo", "empNo", "eName", "salary")
    write_excel(result, "Q9", workbook)
    # Q10
    result = create_table(import_path_name)
    write_excel(result, "Publisher", workbook)

    workbook.close()


def write_excel(results: List[Dict[str,str]], sheet_name: str, workbook: Workbook):

    #get current sheet and update
    pass


def get_excel_sheetnames(file_path_name: Path) -> (List[str]):
    pass


def read_excel_dataframes(file_path_name: Path,sheet_name: str):
    pass



