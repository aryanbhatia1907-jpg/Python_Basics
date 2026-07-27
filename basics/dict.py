#dict se hum kissi particulate value ki info nikaal sakte h jo daali h 
# Syntax- dict={key: value} print(dict(key)) 
dict={
    "Aryan": "Human Being",
    "Spoon": "Chamach", 
    786:"Khiladi",
    420:"Chachi"
}
print(dict[786])
print(dict.get("bhatia"))     # Upar wale mein agar unknown daale jo exist nhi karta toh woh "error" deta but yeh "none" dega , baaki yeh upar ka hi ek version hai.

print(dict.keys())            # Keys ko print karne ke liye
print(dict.values())          # Values ko

# Iterate karni hai values uske liye
for key in dict.keys():
    print(f"The value corresponds to the key {key} is {dict.keys()}")

print(dict.items())           # Alag-2 order banane ke liye keys ke
