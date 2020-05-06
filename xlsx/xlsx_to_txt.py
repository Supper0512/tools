import xlrd


class ParserXLSX(object):

    def __init__(self, xls, txt):
        self.xls_name = xls
        self.txt_name = txt
        self._xls_txt()

    def _xls_txt(self):
        open_work_book = xlrd.open_workbook(self.xls_name)
        table = open_work_book.sheets()[0]
        length_table = table.nrows
        for count in range(1, length_table):
            str_table = self._list_to_str(table.row_values(count))
            self._with_open_txt(str_table)

    @staticmethod
    def _list_to_str(table_list):
        length = len(table_list)
        str_table = ""
        for count in range(length):
            str_table = str_table + str(table_list[count]) + '\t'
        return str_table

    def _with_open_txt(self, table):
        with open(self.txt_name, 'a') as f:
            f.write(table + '\n')


