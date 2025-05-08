import webbrowser

done=False

while not done:
    print('O que você deseja fazer?')
    print('1. Aprender Python')
    print('2. Aprender JavaScript')
    print('3. Aprender Java')
    print('4. Sair')


    choice = input ('>')
    
    if choice == '1':
        webbrowser.open('https://www.w3schools.com/python/')
    elif choice == '2':
        webbrowser.open('https://www.w3schools.com/js/')
    elif choice == '3':
        webbrowser.open('https://www.w3schools.com/java/')
    elif choice == '4':
        done=True
    else:
        print('Opção inválida. Tente novamente.')
