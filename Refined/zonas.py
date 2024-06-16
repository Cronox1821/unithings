import csv

def read_file():
    with open('Zonas.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
            region = row['Región'] 
            zonas = row['Zona']



def main():
    read_file()

if __name__ == '__main__':
    main()
