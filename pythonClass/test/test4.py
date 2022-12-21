exStr = "I have a dream that one day every valley shall be exalted and every hill and mountain shall be made low. Create the highest, grandest vision possible for your life, because you become what you believe."

reStr = exStr.replace(".", "").replace(",","")
setStr = set(reStr.split(" "))

print(f"사용된 단어의 개수 : {len(setStr)}")
print(setStr)