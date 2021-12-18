def game():
    """
    Pick a number from 1 to 1000, computer will try to guess it.
    :return:
    """

    while True:
        try:
            correct_number = int(input('Pomyśl liczbę od 0 do 1000 a ja ją zgadnę w max 10 próbach: '))
            if correct_number not in range(1001):
                raise ValueError
            break
        except ValueError:
            print("Wprowadź liczbę od 0 do 1000")

    min = 0
    max = 1000

    while True:
        guess = int((max - min) / 2 + min)
        print(f'Zgaduję: {guess}')

        answers = ('Za dużo', 'Za mało', 'Zgadłeś')

        for s in answers:
            print(f'{answers.index(s)} - {s}')

        while True:
            try:
                user_reply = int(input('Zgadłem? '))
                if user_reply not in range(3):
                    raise ValueError
                break
            except ValueError:
                print("Wybierz odpowiedź od 0 do 1")

        if user_reply == 2:
            print(f'{answers[2]}')
            return
        elif user_reply == 0:
            print(f'{answers[0]}')
            max = guess
        elif user_reply == 1:
            print(f'{answers[1]}')
            min = guess


game()