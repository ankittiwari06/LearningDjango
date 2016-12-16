import csv
with open('output.csv','w') as outfile:
    fileWriter = csv.writer(outfile)
    with open('detail - Sheet1.csv', 'r') as infile:
        fileReader = csv.DictReader(infile)
        for row in fileReader:
            if(row['Phone1']==""):
                row['Phone1']=row['Phone2']
                list = [row['Name'],row['Phone1']]
                print(list)
                #fileWriter.writerow(row)
                #fileWriter = csv.writer(outfile, quoting=csv.QUOTE_ALL)
                fileWriter.writerow(list)
