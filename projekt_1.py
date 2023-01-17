"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Jan Černý
email: JohnyBgoode@seznam.cz
discord: JohnyBgoode84
"""

TEXTS = [
'''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

sel_edit_text = list()
separator = "-" * 40
users = {
    "bob": "123", 
    "ann": "pass123", 
    "mike": "password123", 
    "liz": "pass123"
    }

# 1) Vyžádá si od uživatele přihlašovací jméno a heslo
user_input = input("username: ")
pass_input = input("password: ")

print(separator)

# 2) Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů
if users.get(user_input) == pass_input:
    print(f"Welcome to the app, {user_input}.\nWe have 3 texts to be analyzed.")
    print(separator)
else:
    print("Unregistered user, terminating the program...")
    quit()

# 3) Pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty
#   - pokud není registrovaný, upozorni jej a ukonči program
print(f"""
1) {TEXTS[0]}

2) {TEXTS[1]}

3) {TEXTS[2]}
""")

num_input = input("Enter a number btw. 1 and 3 to select: ")

if num_input.isdigit() and int(num_input) in range(1,4):
    sel_edit_text = [
        sel_edit.strip(",.")
        for sel_edit in TEXTS[int(num_input)-1].split()
    ]
    print(separator)
else:
    print("Out of value or unspecified number, terminating the program...")
    quit()

# 5) Pro vybraný text spočítá následující statistiky
#   - počet slov
all_words_count = len(sel_edit_text)

#   - počet slov začínajících velkým písmenem
all_title_words_count = len([
    title_words
    for title_words in sel_edit_text
    if title_words.istitle()
])

#   - počet slov psaných velkými písmeny
all_upper_words_count = len([
    upper_words
    for upper_words in sel_edit_text
    if upper_words.isupper() and upper_words.isalpha()
])

#   - počet slov psaných malými písmeny
all_lower_words_count = len([
    lower_words
    for lower_words in sel_edit_text
    if lower_words.islower()
])

#   - počet čísel (ne cifer)
all_num_count = len([
    num_count
    for num_count in sel_edit_text
    if num_count.isnumeric()
])
# - sumu všech čísel (ne cifer) v textu
all_sum_num = sum([
    int(sum_num)
    for sum_num in sel_edit_text
    if sum_num.isnumeric()
])

print(f"""
There are {all_words_count} words in the selected text.
There are {all_title_words_count} titlecase words.
There are {all_upper_words_count} uppercase words.
There are {all_lower_words_count} lowercase words.
There are {all_num_count} numeric strings.
The sum of all the numbers is {all_sum_num}.
""")
print(separator)

# 6) Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu
len_words = sorted([
    len(len_words)
    for len_words in sel_edit_text
])

count_len_words = {
    count_len: len_words.count(count_len)
    for count_len in len_words
}

print( 
    "{0:3}|{1:20}|{2}".format("LEN", "OCCURENCES".center(20), "NR.")
    )
print(separator)

for index, w_count in enumerate(count_len_words.items()):
    print( 
    "{0:3}|{1:20}|{2}".format(w_count[0], "*" * w_count[1], w_count[1])
    )




quit()
pocet_slov_full = list()
for pocet_slov in range(len(sel_edit_text)):
    if pocet_slov == 0:
        pocet_slov_full = 1
    elif pocet_slov >= 1:
        pocet_slov_full = pocet_slov_full + 1

print(pocet_slov_full)


a_words_count = len([
    words_count
    for words_count in range(len(sel_edit_text))
])

print(all_words_count)

all_len_words_count = {
    len_words: len(len_words)
    for len_words in sel_edit_text
}