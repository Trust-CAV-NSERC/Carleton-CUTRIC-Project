#Team： moran@genieview.com; steed@genieview.com; tong@genieview.com

#mRNA is created during the process of transcription, where an enzyme converts the gene into pre-mRNA，usually still contains introns removed in the process of RNA splicing, leaving only exons, regions that will encode the protein final amino acid sequence. 

#https://www.nature.com/articles/s41598-021-84840-3#further-reading

import re

def main():
  #Define the corresponding relation Dictionary of three labels （quantity of electron; net molecular mass; isoelectric point）
  q_Label = {'A':0, 'C':0, 'F':0, 'G':0, 'I':0, 'L':0, 'M':0, 'N':0, 'P':0, 'Q':0, 'S':0, 'T':0, 'V':0, 'W':0, 'Y':0, '-':0, 'H':1, 'K':1, 'R':1, 'D':-1, 'E':-1}
  n_Label = {'A':89.1, 'C':121.2, 'F':165.2, 'G':75.1, 'I':131.2, 'L':131.2, 'M':149.2, 'N':132.1, 'P':115.1, 'Q':146.2, 'S':105.1, 'T':119.1, 'V':117.1, 'W':204.2, 'Y':181.2, '-':144.8, 'H':155.2, 'K':146.2, 'R':174.2, 'D':133.1, 'E':147.1}
  e_Label = {'A':6.11, 'C':5.05, 'F':5.49, 'G':6.06, 'I':6.05, 'L':6.01, 'M':5.74, 'N':5.41, 'P':6.3, 'Q':5.65, 'S':5.68, 'T':5.6, 'V':6, 'W':5.89, 'Y':5.64, '-':5.9, 'H': 7.6, 'K':9.6, 'R':10.76, 'D':2.85, 'E':3.15}

  #inputMethod = input("Input from keyboard or file, type in \"k\" or \"f\": ")
  #Input amino acid sequence
  proteinString = input("Enter your input: ")
  #Use regular expressions to detect whether the characters in the sequence are out of the dictionary range. If they exceed the range, an error will be reported and the input will be requested
  datepat = re.compile(r'[^ACFGILMNPQSTVWT\-HKRDE]')
  if datepat.match(proteinString):
    print('Input error, illegal letter, please try again.')
    main()

  #Input protein sequence conversion type
  labelType = input("Enter label type, type in \"q\", \"n\" or \"e\": ")
  #Decide the output method (screen output or file output)
  outputMethod = input("Output to screen or file, type in \"s\" or \"f\": ")

  #Sequence conversion and output
  tmpStr = list(proteinString)
  #The sequence is converted to q_label and output
  if(labelType == "q"):
    qString = ""
    for t in tmpStr:
      qString += str(q_Label[t])
      qString += " "
    if(outputMethod == 's'):
      print(qString)
    #File output, will overwrite the original file content
    elif(outputMethod == 'f'):
      file = open('C:/Users/Moran/Documents/proteins/qLabelTemp.txt', 'w')
      file.write(qString)
      file.close()
        
  #The sequence is converted to n_label and output
  elif(labelType == "n"):
    nString = ""
    for t in tmpStr:
      nString +=  str(n_Label[t])
      nString += " "
    if(outputMethod == 's'):
      print(nString)
    #File output, the content of the original file will be overwritten
    elif(outputMethod == 'f'):
      file = open('C:/Users/Moran/Documents/proteins/nLabelTemp.txt', 'w')
      file.write(nString)
      file.close()

  #The sequence is converted to e_label and output
  elif(labelType == "e"):
    eString = ""
    for t in tmpStr:
      eString += str(e_Label[t])
      eString += " "
    if(outputMethod == 's'):
      print(eString)
    #File output, will overwrite the original file content
    elif(outputMethod == 'f'):
      file = open('C:/Users/Moran/Documents/proteins/eLabelTemp.txt', 'w')
      file.write(eString)
      file.close()

#！！！Used to determine the main function, deleted by mistake!
if __name__=="__main__":
    main()