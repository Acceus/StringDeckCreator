
import random
n=0
while (n==0):
    print("Select Option From Below:\n")
    print("1) Add Card To Deck\n")
    print("2) Remove Card From Deck\n")
    print("3) See Cards in Deck\n")
    print("4) Draw Random Card From The Deck\n")
    print("5) Exit Card App\n")
    option_selection = input("Enter Selection Here: ")
    if (option_selection == "1"):
        while(True):
            card_value = input("Enter Card Content Here: ")
            text = card_value + "\n"
            cardsFile_append = open("cards.txt","a")
            cardsFile_append.write(text)
            cardsFile_append.close()
            exit_or_continue = input("Enter c to add another card or anything else to return to menu: ")
            if (exit_or_continue=="c"):
                continue
            else:
                break

    if (option_selection=="2"):
        cardsFile_delete_read = open("cards.txt","r").readlines()
        line_to_delete = input("Enter the card number you wish to delete: ")
        line_to_delete_convertInt=int(line_to_delete)-1
        line_to_delete_array = []
        for index, line in enumerate(cardsFile_delete_read):
            if (index!=line_to_delete_convertInt):
                line_to_delete_array.append(line)
        delete_all_lines = open("cards.txt","w")
        delete_all_lines.close()
        add_new_list = open("cards.txt","a")
        add_new_list.writelines(line_to_delete_array)
        add_new_list.close()
        
        
    if (option_selection=="3"):
        cardsFile_read = open("cards.txt","r")
        cardsFile_read_list = cardsFile_read.read().splitlines()
        while(True):
            for x in enumerate(cardsFile_read_list,1):
                
                print(x)
            exit_cardsFile_read_list = input("enter x and press enter to exit: ")
            if (exit_cardsFile_read_list=="x"):
                cardsFile_read.close()
                break

    if (option_selection=="4"):
       while(True):
           deck_strings_list = []
           cardsFile_list_read = open("cards.txt","r").readlines()
           for line in cardsFile_list_read:
               deck_strings_list.append(line)
           random.shuffle(deck_strings_list)
           random_card = random.choice(deck_strings_list) 
           print("The card you have selected is: ", random_card)
           exit_deck_draw=input("Enter c to draw another card or anything other than c to return to menu: ")
           if(exit_deck_draw=="c"):
               continue
           else:
               break

    if (option_selection=="5"):
        n=1
