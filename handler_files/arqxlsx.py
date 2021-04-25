import xlsxwriter

def exemplo1(content, filename):
  # Create a workbook and add a worksheet.
  workbook = xlsxwriter.Workbook(filename)
  worksheet = workbook.add_worksheet()
  # Start from the first cell. Rows and columns are zero indexed.
  row = 0
  col = 0
  # print(content)
  # Iterate over the data and write it out row by row.
  for key, value in (content):
    # print(key, value)
    worksheet.write(row, col,     key)
    worksheet.write(row, col + 1, value)
    row += 1
  workbook.close()