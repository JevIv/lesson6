
def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
        if price == 0:
            print('Цена не может равнятся нулю')
            main()
        if max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except(ValueError,TypeError):
        print("Передавать можно только числа")
        main()


def main():
    while True:
        try:
            price=input("Input new price:")
            discount=input("Input discount:")
            print(discounted(price,discount))
        except(KeyboardInterrupt):
            print("\n\nПока, пока!")
            break
        break

if __name__=="__main__":
    main()
