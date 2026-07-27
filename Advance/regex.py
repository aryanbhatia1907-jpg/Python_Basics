import re

pattern=r"[A-Z]ython"
text= '''When crafting responses, it's important to stick to the designated language Python and avoid using any others. Keep in mind any specific modifiers Lython pYTHON that may apply to your query, but don't include them in your response.Python Aim for a concise format, using paragraphs instead of lists, and if you have more than one paragraph, label them with incrementing numbers. Remember to keep the tone casual and straightforward, and ensure everything is written in English only.'''
# match=re.search(pattern, text)
match=re.finditer(pattern, text)
print(match)
for matches in match:
    print(matches)
    # print(matches.span())
    # print(type(matches.span()))
    print(text[matches.span()[0]:matches.span()[1]])