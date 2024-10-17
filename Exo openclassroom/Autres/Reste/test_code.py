# str = 'Vive Python !'
# char_to_dots = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.', ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-', '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.' }

# str = str.upper()
# text = [char for char in str]

# take_code = []


# for char in text:
#     for j in char_to_dots:
#         if char == j:
#             take_code.append(char_to_dots[j])
            
# code_finally = "/".join(take_code)
# print(str(code_finally))


#Exo 2 

# student = {
#     'HE215614' : 2,
#     'HE215615' : 3,
#     'HE215616' : 1,
# }

# search_student = input("Entrer le matricule : ")

# for mat in student:
#     if search_student == mat:
#         print(student[mat])



votes = ['T1031', 'T2112', 'T1031', 'T1031']

if votes == 0:
    print('rien')
    garde = []
    meilleur = ''
    for vote in votes:
        for i in garde:
            if vote == garde[-1]:
                garde.append(vote)
                meilleur = i
    print(meilleur) 