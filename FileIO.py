def standardFileIO():
    try:
        # read file
        filename = "YOURFILENAME HERE" #e.g. "RESULTS.txt", "DATA.csv"
        infile = open(filename,'r')
        lines = infile.readlines()
        
        for line in lines:
            line = line.strip('\n') # remove newline char
            print(line)
        
    except FileNotFoundError:
        print("File is not found")
