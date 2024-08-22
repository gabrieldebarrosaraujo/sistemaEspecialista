def verificar_compatibilidade_sanguinea(rh_doador, tipo_sanguineo_doador, rh_receptor, tipo_sanguineo_receptor):
    tipos_compatíveis = {
        'O-': ['O-', 'A-', 'B-', 'AB-'],
        'O+': ['O+', 'A+', 'B+', 'AB+'],
        'A-': ['A-', 'AB-'],
        'A+': ['A+', 'AB+'],
        'B-': ['B-', 'AB-'],
        'B+': ['B+', 'AB+'],
        'AB-': ['AB-'],
        'AB+': ['AB+']
    }

    if tipo_sanguineo_receptor in tipos_compatíveis.get(tipo_sanguineo_doador, []):
        if (rh_doador == 'positivo' and rh_receptor == 'positivo') or (rh_doador == 'negativo'):
            return True
        elif rh_doador == rh_receptor:
            return True
    return False

def main():
    try:
        idade = int(input("Digite sua idade: "))

        if 18 <= idade <= 65:
            peso = float(input("Digite seu peso (em kg): "))

            if peso > 50:
                rh_doador = input("Seu fator RH é positivo ou negativo? ").strip().lower()
                tipo_sanguineo_doador = input("Digite seu tipo sanguíneo (O-, O+, A-, A+, B-, B+, AB-, AB+): ").strip().upper()

                rh_receptor = input("O fator RH do receptor é positivo ou negativo? ").strip().lower()
                tipo_sanguineo_receptor = input("Digite o tipo sanguíneo do receptor (O-, O+, A-, A+, B-, B+, AB-, AB+): ").strip().upper()

                if verificar_compatibilidade_sanguinea(rh_doador, tipo_sanguineo_doador, rh_receptor, tipo_sanguineo_receptor):
                    print("Doação possível: Compatibilidade confirmada.")
                else:
                    print("Doação não é possível: Incompatibilidade sanguínea.")
            else:
                print("Você não atende ao peso para doação.")
        else:
            print("Você não atende a idade para doação.")
    except ValueError:
        print("Resposta incorreta.")

if __name__ == "__main__":
    main()
