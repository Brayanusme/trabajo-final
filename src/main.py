import menu

def main():
    try:
        import colorama
    except ImportError:
        print("Atención: colorama no está instalado. Puede instarlo con 'pip install colorama'")
        
    menu.iniciar_app()

if __name__ == "__main__":
    main()