import time

def countdown(seconds):
    while seconds>0:
        mins=int(seconds/60)
        secs=int(seconds%60)
        if secs<10:
            secs=f"0{secs}"
        timer=f"{mins}:{secs}"
        print(timer,end="\r")
        seconds-=1
        time.sleep(1)
    print("Time Up")

seconds=input("Enter the time in number of seconds: ")
countdown(int(seconds))