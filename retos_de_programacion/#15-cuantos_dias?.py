import datetime

def days_between(date1, date2):
    try:
        date1_list = date1.split('/')
        date2_list = date2.split('/')

        date_class1 = datetime.date(int(date1_list[2]), int(date1_list[1]), int(date1_list[0]))
        date_class2 = datetime.date(int(date2_list[2]), int(date2_list[1]), int(date2_list[0]))

        return abs(date_class1 - date_class2)
    
    except:
        return 'El formato de fecha debe ser: dd/mm/yyyy'

print(days_between("15/6/2000", "27/10/2022"))