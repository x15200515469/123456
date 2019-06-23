department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.11111
COURSE_FEES_Python = 1234.3456


line1 = 'Deprtment1 name:%-10s Manager:%-10s COURSE FEES:%-10.2f The end!' % (department1,depart1_m,COURSE_FEES_SEC)
line2 = 'Deprtment2 name:%-10s Manager:%-10s COURSE FEES:%-10.2f The end!' % (department2,depart2_m,COURSE_FEES_Python)

line1 = 'Deprtment1 name:{0:<10} Manager:{0:<10} COURSE FEES:{2:<10.2f} The end!'.format(department1,depart1_m,COURSE_FEES_SEC)
line2 = 'Deprtment2 name:{0:<10} Manager:{0:<10} COURSE FEES:{2:<10.2f} The end!'.format(department2,depart2_m,COURSE_FEES_Python)

length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)
