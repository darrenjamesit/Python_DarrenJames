import xlsxwriter

temp = []
names = []
grades = []
av = []
values = []
with open("note.txt", "r") as read:
    for line in read:
        temp.append(str(line).replace(";", ":", 1).replace(";", ",").replace("\n", "").split(':'))
        for element in temp:
            names.append(element[0])
            grades = element[1].split(',')
            for num in grades:
                av.append(int(num))
            mean = round(sum(av) / len(av), 1)
            values.append(mean)
            av.clear()
            temp.clear()

dc = dict(zip(names, values))

# I noticed when trying to modify my workbook to add formatting after I created it the first time that I didn't have
# permission and I had to constantly delete the xlsx file and run the code again...
# so I read https://xlsxwriter.readthedocs.io/introduction.html, and it said the following:
# Disadvantages:
# It cannot read or modify existing Excel XLSX files.

row = 1
col = 0

workbook = xlsxwriter.Workbook('ex8_5.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column(0, 0, 20)
worksheet.set_column(1, 1, 10)
bold = workbook.add_format({'bold': True})
worksheet.write('A1', 'Elev', bold)
worksheet.write('B1', 'Media', bold)
for key, value in dc.items():
    worksheet.write(row, col,     key)
    worksheet.write(row, col + 1, value)
    row += 1
workbook.close()
