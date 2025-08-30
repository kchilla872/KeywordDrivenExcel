import openpyxl
import pytest
import keywords

# Define step ranges per test case
step_ranges = {
    "TC001": range(1, 6),   # Steps 1 to 5 included
    "TC002": range(6, 11),  # Steps 6 to 10 included
    "TC003": range(11, 13), # Steps 11 to 12 included
    "TC004": range(13, 18)  # Steps 13 to 18 included
}

def run_test_case_from_excel(page, test_case_id, excel_file):
    workbook = openpyxl.load_workbook(excel_file)
    sheet = workbook.active
    for row in sheet.iter_rows(min_row=2, values_only=True):
        current_test_case = row[0]
        step_no = row[1]
        if current_test_case == test_case_id and step_no in step_ranges[test_case_id]:
            keyword = str(row[2]).strip().lower()
            locator = row[3]
            input_data = row[4]
            action_func = getattr(keywords, keyword, None)
            if not action_func:
                raise Exception(f"Keyword '{keyword}' not implemented in keywords.py")
            if keyword == "openurl":
                action_func(page, input_data)
            elif keyword == "click":
                action_func(page, locator)
            elif keyword == "inputtext":
                action_func(page, locator, input_data)
            elif keyword == "waitforelement":
                timeout = int(input_data) if input_data else 5000
                action_func(page, locator, timeout)
            elif keyword == "select":
                action_func(page, locator, input_data)
            elif keyword == "check_checkbox":
                action_func(page, locator)
            elif keyword == "click":
                action_func(page, locator)
            else:
                raise Exception(f"Keyword '{keyword}' usage not defined")


@pytest.mark.parametrize("test_case_id", ["TC001", "TC002", "TC003", "TC004"])
def test_run_keyword_driven(page, test_case_id):
    excel_file = "./test_suite/testdata.xlsx"
    run_test_case_from_excel(page, test_case_id, excel_file)
