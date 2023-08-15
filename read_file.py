#q1
words_status={}

with open("D:\python file\poem.txt","r") as f:
    for line in f:
        clean_line=line.strip()
        words=clean_line.split(' ')
        for word in words:
            if word in words_status:
                words_status[word]+=1
            else:
                words_status[word]=1
print(words_status)

max_oc_word=[]
word_count=list(words_status.values())
max_count=max(word_count)
for k,v in words_status.items():
    if v==max_count:
        max_oc_word.append(k)
print(f"max counted words are[{max_count}]",max_oc_word)
#q2
with open("D:\python file\stocks.csv","r") as f , open("D:\python file\out.csv","w") as out:
    next(f)
    out.write("Company Name,PE Ratio, PB Ratio\n")
    for line in f:
        tokens = line.split(",")
        stock = tokens[0]
        price = float(tokens[1])
        eps = float(tokens[2])
        book = float(tokens[3])
        pe = round(price / eps, 2)
        pb = round(price / book, 2)
        out.write(f"{stock},{pe},{pb}\n")
