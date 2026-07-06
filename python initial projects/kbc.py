name=input("enter the name of contestent")
print("welcome to KBC by AK18@AKSH")
sum=0
prise=(1000,2000,5000,10000,20000,40000,80000,320000,"1 cr")
question=[

"Q1 —₹1,000\nWhich planet is known as the Red Planet?\nA. Venus   B. Mars   C. Jupiter   D. Saturn",

"Q2 -easy| ₹2,000 \n How many sides does a hexagon have?\nA. 5   B. 6   C. 7   D. 8",

"Q3 — Easy-Medium | ₹5,000 \n Who wrote the Indian national anthem 'Jana Gana Mana'?\nA. Bankim Chandra   B. Rabindranath Tagore   C. Subhash Bose   D. Sarojini Naidu",

"Q4 — Medium | ₹10,000 \n What is the chemical symbol for gold? \n A. Go   B. Gd   C. Au   D. Ag",

"Q5 — Medium | ₹20,000 \n In which year did India gain independence? \n A. 1945   B. 1947   C. 1950   D. 1952",

"Q6 — Medium-Hard | ₹40,000 \n Which organ in the human body produces insulin? \n A. Liver   B. Kidney   C. Pancreas   D. Spleen",

"Q7 — Medium-Hard | ₹80,000\nWho discovered the law of gravitation?\nA. Einstein   B. Newton   C. Galileo   D. Archimedes",

"Q8 — Hard | ₹3,20,000 \n What is the speed of light in vacuum (approx.)?\nA. 3×10⁸ m/s   B. 3×10⁶ m/s   C. 3×10¹⁰ m/s   D. 3×10⁴ m/s",

"Q9 — Hard | ₹6,40,000\nWhich country has the longest coastline in the world?\nA. Russia   B. Australia   C. Norway   D. Canada",

"Q10 — Very Hard | ₹1 Crore\nWhat is the rarest blood type among humans?\nA. O negative   B. AB negative   C. B negative   D. AB positive"]
ans=("B","B","B","C","B","C","B","A","D","B")
C=0
for i in question:
    print(i) 
    cns=input("enter correct option")
    if(cns==ans[C]):
        print("congratulation your answer is correct" ,"you won" ,prise[C])
        sum=prise[C]
        C=C+1
    else:
            print("sorry your answer is incorrect" ,"you are disqualified ")
            break

print("total amount won by you=",sum)