def dateSort(date):
    year = int(date[4:8])
    month = int(date[2:4])
    day = int(date[0:2])
    return year,month,day

dateA = "08012004"
yearA, monthA, dayA = dateSort(dateA) 

dateSort(dateA)

print(monthA,dayA,yearA, sep='/')
