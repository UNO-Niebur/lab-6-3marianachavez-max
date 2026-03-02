#WordCount.py
#Name: Mariana Chavez
#Date: 03.01.2026
#Assignment: Lab 6

def main():
  textFileName = input("Enter a File Name: ")

  if textFileName == "gettysberg.txt" or textFileName == "fish.txt":
    textFile = open(textFileName, 'r')
    lineCount = 0
    wordCount = 0
    letterCount = 0

    for line in textFile:
      lineCount = lineCount + 1
      words = line.split()
      for w in words:
        wordCount = wordCount + 1
      letterCount = letterCount + len(line)

    textFile.close()

    print("Lines:", lineCount)
    print("Words:", wordCount)
    print("Characters:", letterCount)
  else:
    print(f"Error: File '{textFileName}' not found. Try a different file.")
  

if __name__ == '__main__':
  main()
