# xlsx to db
 Manipulate xlsx data into SQLite db
Step1:	step1_xlsx2csv.py
	Creates a csv file from the xlsx file and removes unescessary columns.
Step2:	step2_transpose-csv.py
	Transposes rows into columns
Step3:	step3_CleanCSV.py
	Removes header in rown 1, removes all data after reading=2204
