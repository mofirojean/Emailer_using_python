"""
*****************************************************************************
    Reads an excel file, extracts the information and store them in
    an organized list which contains a tuple of the information in each
    row in our excel file
*****************************************************************************
"""
import openpyxl


class ExcelReader:
    """Creates a constructor of our class"""
    def __init__(self, excel_doc):
        self._excel_doc = excel_doc
        self._sheet = None

    # Gets the required sheet to extract our data
    def required_sheet(self, activeSheet):
        excelDoc = openpyxl.load_workbook(self._excel_doc)
        rSheet = excelDoc[activeSheet]
        self._sheet = rSheet

    # Extracts the data store them in a list
    def extract_data_to_list(self):
        # extracts the raw data and keep in a list
        list_data = list()
        for row in self._sheet.iter_rows():
            primeList = list()
            for cell in row:
                primeList.append(cell.value)
            list_data.append(primeList)
        return list_data

    # contains the well formatted data in the form a tuple (name, email_address)
    def email_info(self):
        email_info_list = list()
        data = self.extract_data_to_list()
        for i in range(1, len(data)):
            info = [data[i][0], data[i][1]]
            email_info_list.append(tuple(info))
        return email_info_list
