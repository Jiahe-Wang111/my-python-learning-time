import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

chooser = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while chooser == "y":
    # TODO 1: 首先创造我这个玩家的游玩规则：起步默认随机选择两张牌，玩家可以选择hit或者stand，选择hit则继续随机抽取一张牌，选择stand则保持原牌组不变
    my_initial_card = [random.choice(cards), random.choice(cards)]
    current_score = sum(my_initial_card)

    # TODO 3:创建电脑默认模式：电脑一开始也是随机抽取两张牌作为初始牌组，当所有总和<17时必须继续执行hit的操作。当电脑总和>21同样判定失败
    # computer's card:
    computer_initial_card = [random.choice(cards), random.choice(cards)]
    computer_score = sum(computer_initial_card)

    print(f"Your cards: {my_initial_card}, current score: {current_score}")
    print(f"Computer's first card: {computer_initial_card[0]}, computer's card: {computer_initial_card}, computer's score: {computer_score}")

    game_over = False

    #TODO 2:选择是否抽取新牌，要注意的是一旦我的总和>21自动默认我输掉。如果总和<21可以选择是继续抽牌还是暂停
    hit_or_stand = input(f"Type 'y' to get another card, type 'n' to pass: ")
    while hit_or_stand == "y":
        new_card = random.choice(cards)
        my_initial_card.append(new_card)
        current_score = sum(my_initial_card)
        print(f"Your cards: {my_initial_card}, current score: {current_score}")

        # Check if player busts
        if current_score > 21:
            print(f"Computer's first card: {computer_initial_card[0]}, computer's card: {computer_initial_card}, computer's score: {computer_score}")
            print("You went over, you lose.😢")
            game_over = True
            break

        else:
            while computer_score < 17:
                computer_new_card = random.choice(cards)
                computer_initial_card.append(computer_new_card)
                computer_score = sum(computer_initial_card)
                print(f"Computer's first card: {computer_initial_card[0]}, computer's card: {computer_initial_card}, computer's score: {computer_score}")

                # Check if dealer busts
                if computer_score > 21:
                    game_over = True
                    print(f"Computer went over, you win!😁")
                    break

        # Ask player again
        hit_or_stand = input(f"Type 'y' to get another card, type 'n' to pass: ")

    if not game_over:
        print(f"Your final hand: {my_initial_card}, final score: {current_score}")
        print(f"Computer's final hand: {computer_initial_card}, final score: {computer_score}")
        if current_score < computer_score:
            print("You lose.😢")
        elif current_score == computer_score:
            print("Draw~🤣")
        else:
            print("You win!😁")

    input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
