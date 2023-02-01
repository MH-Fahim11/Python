fruits = input("Item:")
if fruits.lower() in ["apple","avocado","banana","sweet cherries","kiwifruit", "pear","Cantaloupe","strawberries"]:
    if fruits.lower() == "apple":
        print("Calories: 130")
    elif fruits.lower() == "avocado" or fruits.lower() == "cantaloupe" or fruits.lower() == "strawberries":
        print("Calories: 50")
    elif fruits.lower() == "banana":
        print("Calories: 110")
    elif fruits.lower() == "sweet cherries" or fruits.lower() == "pear" :
        print("Calories: 100")
    elif fruits.lower() == "kiwifruit":
        print("Calories: 90")

