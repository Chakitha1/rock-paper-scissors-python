f=input()
s=input()
if f=="Rock" and s=="Scissors":
    print("Abhinav Wins")
if f=="Scissors" and s=="Rock":
    print("Anjali Wins")
if f=="Paper" and s=="Scissors":
    print("Anjali Wins")
if f=="Scissors" and s=="Paper":
    print("Abhinav Wins")
if f=="Rock" and s=="Paper":
    print("Anjali Wins")
if f=="Paper" and s=="Rock":
    print("Abhinav Wins")
if f==s:
    print("Tie")
