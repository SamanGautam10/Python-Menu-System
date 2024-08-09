def main():
    totalCost = 0

    # Items in Menu 
    menu = {
        'Samosa (Pcs)': 40,
        'Chicken Mo:Mo (Plates)': 180,
        'Chowmein (Plates)': 220,
        'Pizza (Large)': 620,
        'Wings (6 Pcs)': 420
    }

    print("Items in the menu today:")

    # Showing items of menu to the user
    menu_list = list(menu.items())
    for i, (key, value) in enumerate(menu_list, start=1):
        print(f"{i}. {key}: Rs.{value}")

    # Taking order from customer
    order_placed = []
    print("Place Your Order")
    print("Place your order by giving item number in menu: ")
    while True:
        order = int(input("Item No.: "))
        order = order - 1
        placed_order = menu_list[order] # Taking order name from menu and appending it to order placed
        order_placed.append(placed_order)

        # Calculating pricing of the items
        quantity = int(input("Qualtity: "))
        price = menu_list[order][1]
        totalCost = (quantity * price) + totalCost
        print(f"Total Price: {totalCost}")
        
        # Checking if customer wants to order more items
        while True:
            cont = input("Do you want to order more items?(y/n)")

            if cont.lower() == 'y':
                break

            elif cont.lower() == 'n':
                for i, (key, value) in enumerate(order_placed, start=1):
                    print("Items in your order:")
                    print(f"{i}. {key}: {value}")
                    print(f"Total Price: {totalCost}")
                exit()

            else:
                print("Invalid Option! Please try again!")

if __name__ == "__main__":
    main()