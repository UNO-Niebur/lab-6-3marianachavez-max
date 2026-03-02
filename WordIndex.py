#WordIndex.py
#Name: Mariana Chavez
#Date: 03.01.2026
#Assignment: Lab 6

def main():
  fileName = input("Enter a File Name: ")
  if fileName == "gettysberg.txt" or fileName == "fish.txt":
    textFile = open(fileName, 'r')
    
    words = {} #create an empty dictionary
    lineNum = 0

    for line in textFile:
      lineNum = lineNum + 1
      wordList = line.split()
      
      for w in wordList:
        w = w.lower()
        w = w.replace(",","")
        w = w.replace(".","")
        w = w.replace("!","")
        w = w.replace("—","")
        w = w.replace("-","")

        if w != "":
          if w in words:
            if lineNum not in words[w]:
              words[w].append(lineNum)
          else:
            words[w] = [lineNum]

    for word in sorted(words.keys()):
      print(word, words[word])
  
  else: 
    print(f"Error: File '{fileName}' not found. Try a different file.")

if __name__ == '__main__':
  main()
