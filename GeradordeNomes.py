import random
import string

VOWEL_TO_NUMBER = {
    'a': '4',
    'e': '3',
    'i': '1',
    'o': '0',
    'u': '7'
}

MASCULINE_SYLLABLES = [
    'mar', 'jo', 'lu', 'ca', 'ri', 'mi', 'an', 'jo', 'se', 'pe', 'to', 'dan', 'vic', 'al', 'fa', 'gi', 'ri', 'el'
]

FEMININE_SYLLABLES = [
    'ma', 'ri', 'la', 'so', 'na', 'ka', 'li', 'be', 'le', 'za', 'ti', 'ja', 'vi', 'sa', 're', 'di', 'mo', 'fa'
]

def generate_base_name(gender, min_length=5, max_length=9):
    """
    Generate a random base name (without numbers) based on gender.
    It combines random syllables until the length is within [min_length, max_length].
    """
    syllables = MASCULINE_SYLLABLES if gender.lower() == 'masculino' else FEMININE_SYLLABLES
    name = ''
    while len(name) < min_length:
        name += random.choice(syllables)
    # Trim if longer than max_length
    if len(name) > max_length:
        name = name[:max_length]
    return name.capitalize()

def insert_numbers_middle(name, num_digits=2):
    """
    Insert num_digits random digits into the middle of the name.
    The insertion point will be roughly middle of the name (excluding first and last char).
    """
    if len(name) <= 2:
        # If name too short, just append numbers at the end
        return name + ''.join(random.choices(string.digits, k=num_digits))
    digits = ''.join(random.choices(string.digits, k=num_digits))
    middle_pos = len(name) // 2
    # Insert digits around middle
    return name[:middle_pos] + digits + name[middle_pos:]

def append_numbers_end(name, num_digits=2):
    """
    Append num_digits random digits at the end of the name.
    """
    digits = ''.join(random.choices(string.digits, k=num_digits))
    return name + digits

def replace_vowels_with_numbers(name):
    """
    Replace vowels in the name with numbers according to VOWEL_TO_NUMBER mapping.
    Only lowercase vowels are replaced; name is case-insensitive but output capitalized properly.
    """
    result = ''
    for ch in name.lower():
        if ch in VOWEL_TO_NUMBER:
            result += VOWEL_TO_NUMBER[ch]
        else:
            result += ch
    # Capitalize first letter, keep rest as is (numbers remain)
    return result.capitalize()

def generate_name(gender='masculino', numbers_option=None):
    """
    Generate a random name with options for numbers.
    numbers_option can be:
    - None: no numbers (default)
    - 'middle': numbers inserted in middle
    - 'end': numbers appended at end
    - 'replace': vowels replaced with numbers
    """
    base_name = generate_base_name(gender)
    if numbers_option is None:
        return base_name
    elif numbers_option == 'middle':
        return insert_numbers_middle(base_name)
    elif numbers_option == 'end':
        return append_numbers_end(base_name)
    elif numbers_option == 'replace':
        return replace_vowels_with_numbers(base_name)
    else:
        raise ValueError(f"Invalid numbers_option: {numbers_option}")

def main():
    print("Gerador de nomes aleatórios")
    gender = input("Escolha o gênero (masculino/feminino): ").strip().lower()
    if gender not in ['masculino', 'feminino']:
        print("Gênero inválido. Usando masculino como padrão.")
        gender = 'masculino'

    print("""
Como deseja os números no nome? Escolha uma opção:
1 - Sem números
2 - Números no meio do nome
3 - Números no final do nome
4 - Números substituindo vogais
""")
    option = input("Digite o número da opção desejada: ").strip()
    option_map = {
        '1': None,
        '2': 'middle',
        '3': 'end',
        '4': 'replace'
    }
    numbers_option = option_map.get(option, None)

    name = generate_name(gender, numbers_option)
    print(f"Nome gerado: {name}")

if __name__ == "__main__":
    main()

