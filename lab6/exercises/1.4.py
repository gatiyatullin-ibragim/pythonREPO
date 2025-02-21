def counting_lines(text):
    f = open("text.txt", "r")
    print(len(f.readlines()))
    f.close()
    
your_text = input("enter your text: ")
counting_lines(your_text)