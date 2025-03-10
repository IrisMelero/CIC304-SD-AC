# Dicionários para conversão
bin_oct = ['000', '001', '010', '011', '100', '101', '110', '111']
bin_hex = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
            '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
octal = ['0', '1', '2', '3', '4', '5', '6', '7']
hexadecimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

# Funções base:
def entry():
    print("Olá, bem vinda(o) a nossa calculadora de conversão ;)\n\nps: para funcionar insira as bases no formato correto!")
    s_number = input("Insira o número que deseja converter: ").upper()
    s_base = int(input("Insira a base do número atualmente: "))
    f_base = int(input("Insira a base para qual deseja converter: "))
    return s_number, s_base, f_base

def org_number(s_number, f_base):
    """Organiza o número adicionando zeros à esquerda conforme necessário."""
    if f_base == 8:
        remainder = len(s_number) % 3
        if remainder != 0:
            s_number = '0' * (3 - remainder) + s_number
    elif f_base == 16:
        remainder = len(s_number) % 4
        if remainder != 0:
            s_number = '0' * (4 - remainder) + s_number
    return s_number

def cut_number(org_number, f_base):
    """Corta o número em grupos conforme a base de destino."""
    group_size = 3 if f_base == 8 else 4 if f_base == 16 else 1
    return [org_number[i:i+group_size] for i in range(0, len(org_number), group_size)]

def convert_to_10(number, base):
    """Converte um número de qualquer base para decimal."""
    decimal = 0
    for i, digit in enumerate(reversed(number)):
        if base == 16:
            decimal += hexadecimal.index(digit) * (base ** i)
        elif base == 8:
            decimal += octal.index(digit) * (base ** i)
        elif base == 2:
            decimal += int(digit) * (base ** i)
        elif base == 10:
            decimal += int(digit) * (base ** i)
    return decimal

def convert_from_10(number, base):
    """Converte um número decimal para qualquer base."""
    if number == 0:
        return "0"
    digits_result = []
    while number > 0:
        if base == 16:
            digits_result.append(hexadecimal[number % base])
        elif base == 8:
            digits_result.append(octal[number % base])
        elif base == 2:
            digits_result.append(str(number % base))
        elif base == 10:
            digits_result.append(str(number % base))
        number = number // base
    return ''.join(reversed(digits_result))

def convert_to_2(number, base):
    """Converte um número de qualquer base para binário."""
    if base == 10:
        decimal = convert_to_10(number, base)
        return convert_from_10(decimal, 2)
    elif base == 8:
        binary = ""
        for digit in number:
            binary += bin_oct[octal.index(digit)]
        return binary
    elif base == 16:
        binary = ""
        for digit in number:
            binary += bin_hex[hexadecimal.index(digit)]
        return binary
    elif base == 2:
        return number

def convert_to_8(number, base):
    """Converte um número de qualquer base para octal."""
    if base == 10:
        decimal = convert_to_10(number, base)
        return convert_from_10(decimal, 8)
    elif base == 2:
        org_number_result = org_number(number, 8)
        cut_number_result = cut_number(org_number_result, 8)
        octal_number = ""
        for group in cut_number_result:
            octal_number += octal[bin_oct.index(group)]
        return octal_number
    elif base == 16:
        binary = convert_to_2(number, 16)
        return convert_to_8(binary, 2)
    elif base == 8:
        return number

def convert_to_16(number, base):
    """Converte um número de qualquer base para hexadecimal."""
    if base == 10:
        decimal = convert_to_10(number, base)
        return convert_from_10(decimal, 16)
    elif base == 2:
        org_number_result = org_number(number, 16)
        cut_number_result = cut_number(org_number_result, 16)
        hex_number = ""
        for group in cut_number_result:
            hex_number += hexadecimal[bin_hex.index(group)]
        return hex_number
    elif base == 8:
        binary = convert_to_2(number, 8)
        return convert_to_16(binary, 2)
    elif base == 16:
        return number

def compare_number(cut_number, s_base, f_base):
    """Escolhe a função de conversão correta com base nas bases de origem e destino."""
    if f_base == 2:
        return convert_to_2(''.join(cut_number), s_base)
    elif f_base == 8:
        return convert_to_8(''.join(cut_number), s_base)
    elif f_base == 10:
        return str(convert_to_10(''.join(cut_number), s_base))
    elif f_base == 16:
        return convert_to_16(''.join(cut_number), s_base)

def main():
    s_number, s_base, f_base = entry()
    org_number_result = org_number(s_number, f_base)
    cut_number_result = cut_number(org_number_result, f_base)
    f_number = compare_number(cut_number_result, s_base, f_base)
    print(f"O número convertido é: {f_number}")


main()
