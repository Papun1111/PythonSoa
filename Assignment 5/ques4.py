e2f={
"dog":"chien",
"cat":"chat",
"walrus":"morse"
    }

while True:
    b=input("Enter exit to exit dictionary or choose among dog,cat,walrus:")
    if b=="exit":
        break
    item=e2f.get(b)
    print(f"{b} is {item}")
    
