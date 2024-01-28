def create_alphabet(F_Path, LPL):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    file = open(F_Path, 'w')

    for i in range(0, len(alphabet), LPL):
        line = alphabet[i:i + LPL]
        file.write(line + '\n')

    print(f"File '{F_Path}' created successfully!")

    file.close()


file1 = input("Enter the path for the alphabet file: ")
LPL = int(input("Enter the number of letters per line: "))

create_alphabet(file1, LPL)