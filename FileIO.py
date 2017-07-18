def readValidation():
    try:
        filename = "uvuvwevwevwe_onyetenyevwe.txt"

        # readfile 
        infile = open(filename,'r')
        # random codes here like lines = infile.readlines()
        #YOUR CODE
        #close file
        infile.close()

    except FileNotFoundError:
        print("{} is not found".format(filename))

    except IOError:
        print("{} is corrupted cant read".format(filename))


def outfile1():
    with open("ugwemubwem_ossas.txt",'w') as outfile:
        outfile.write("uvuvwevwevwe onyetenyevwe ugwemubwem ossas \n")
        # using "with" removes the need to close
     
def outfile2():   
    outfile = open("ugwemubwem_ossas.txt", 'w')
    outfile.write("uvuvwevwevwe onyetenyevwe ugwemubwem ossas \n")
    outfile.close()

def standardFileIO():
    try:
        # read file
        filename = "YOURFILENAME HERE" #e.g. "RESULTS.txt", "DATA.csv"
        infile = open(filename,'r')
        lines = infile.readlines()
        
        for line in lines:
            line = line.strip('\n') # remove newline char
            print(line)
        infile.close()
        
    except FileNotFoundError:
        print("File is not found")
        
    except IOError:
        print("{} is corrupted cant read".format(filename))
 
def csvFileIO():
    import csv
    with open("starbucks.csv", newline='') as csvfile:
        records  = csv.reader(csvfile, delimiter=',')
        updatedPostals = []
        oldRecords = []
        zeros = 0
        for row in records:
            oldRecords.append(row)
            if row[0] == "Store Number":
                continue #ignore first row
            postals = row[0].split('-')
            zero1 = int(6-len(postals[0])) * '0' #additional 0 u have to add
            zero2 = int(6-len(postals[1])) * '0'
            zeros += (len(zero1)+len(zero2))
            #print(row[0])
            newPostal = "{}{}-{}{}".format(zero1,postals[0],zero2,postals[1])
            #print(newPostals)
            updatedPostals.append(newPostal)

        csvfile.close()

    with open("starbucks1.csv",'w', newline='') as csvfile1:
        writer = csv.writer(csvfile1, delimiter=',')
        i = 0
        for record in oldRecords:
            if record[0] == "Store Number":
                continue
            record[0] = updatedPostals[i]
            i+=1
            writer.writerow([record[0],record[1],record[2],record[3],record[4],record[5]])
        csvfile1.close()
