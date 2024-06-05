
import time
now = time.ctime()


qna={
    "hi":"hey",
    "how are you":"I am Good",
    "what is your name":"my name is yash",
    "how old are you":"I am 20 years old",
    "what is your favourite color":"My favourite color is black",
    "what is the time now": now,
}
while True :
    qs = input()

    if (qs == "quit"):
        break

    else:
        print(qna[qs])

