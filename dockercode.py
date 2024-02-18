import os 
import string
import socket
def main():
    outputString = open("/home/output/result.txt", "w+")
    path = "/home/data"
    dir_list = os.listdir(path)
    outputString.write("a.Path of the text files\n")
    outputString.write(path)
    outputString.write("\nText files in the above mentioned path is\n")
    for x in dir_list:
        outputString.write(x+"\n")
    IF_file = open('/home/data/IF.txt','r')
    data = IF_file.read()
    wordsInIFFile=data.split()
    Lime_file = open('/home/data/Limerick.txt','r')
    data = Lime_file.read()
    wordsInLimeFile=data.split(" ")
    outputString.write(" \n")
    wordIF=[]
    for i in wordsInIFFile:
        jo=i.translate(str.maketrans('', '', string.punctuation))
        jo=jo.capitalize()
        wordIF.append(jo)
    outputString.write("b.Total number of words in both the files\n")
    outputString.write("Total number of words in IF.txt file are: "+str(len(wordIF))+"\n")
    outputString.write("Total number of words in Limerick.txt file are: "+str(len(wordsInLimeFile))+"\n")
    outputString.write(" \n")
    outputString.write("c.Total number of words in both the files (Grand Total): "+str(len(wordIF) + len(wordsInLimeFile))+"\n")
    countIF = []
    IFSet = set(wordIF)
    for i in IFSet: 
        countIF.append(wordIF.count(i))
    wordIF = list(set(wordIF))
    order_countIF= sorted(countIF,reverse=True)
    outputString.write("\n")
    outputString.write("d.Top three words with maximum number of count in IF.txt are: ")
    j=0
    for j in range(0,3):
         for i in range(0,len(countIF)):
             if(countIF[i]== order_countIF[j]):
                 outputString.write("\n")
                 outputString.write(""+wordIF[i]+" - "+ str(countIF[i]) )
    hostname = socket.gethostname()
    IPAdr = socket.gethostbyname(hostname)
    outputString.write("\n")
    outputString.write("\ne.IP Address of the machine:" + IPAdr) 
    outputString.close()
    outputString_file = open('/home/output/result.txt','r')
    data_outputString = outputString_file.read()
    print(data_outputString)

if __name__ == "__main__":
    main()


