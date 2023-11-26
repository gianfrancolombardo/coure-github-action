import argparse

def main(parametro):
    print("Se ejecutó el trigger " + parametro)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("parametro", help="Parámetro a imprimir junto con el mensaje")
    args = parser.parse_args()
    main(args.parametro)