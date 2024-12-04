tlds={
'Canada':'ca',
'United States':'us',
'Mexico':'mx'
}
if 'Canada' in tlds:
    print("Canada is present is the dictionary")
if 'France' in tlds:
    print("France is present is the dictionary")

for i,j in tlds.items():
    print(f"{i}={j}")

tlds.update({"Sweden":"sw"})
tlds.update({"Sweden":"se"})
newtlds={v:k for k,v in tlds.items() }
print(tlds)
print(newtlds)

