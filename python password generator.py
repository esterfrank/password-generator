import random
import string

def generate_password(length=12, use_digits=True, use_specials=True):
    letters = string.ascii_letters
    digits = string.digits if use_digits else ""
    specials = string.punctuation if use_specials else ""

    all_chars = letters + digits + specials

    if not all_chars:
        raise ValueError("Nenhum conjunto de caracteres selecionado!")

    password = "".join(random.choice(all_chars) for _ in range(length))
    return password

if __name__ == "__main__":
    print("=== Gerador de Senhas Seguras ===")
    length = int(input("Digite o tamanho da senha (padrão 12): ") or 12)
    use_digits = input("Incluir números? (s/n): ").lower() != "n"
    use_specials = input("Incluir caracteres especiais? (s/n): ").lower() != "n"

    senha = generate_password(length, use_digits, use_specials)
    print(f"\nSua senha gerada é: {senha}")
