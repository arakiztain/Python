def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    for i in range(1, days + 1):
        print("Day", i)
    print("Harvest time!")


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def helper(day, total):
        if day > total:
            print("Harvest time!")
            return
        print("Day ", day)
        helper(day + 1, total)

    helper(1, days)
