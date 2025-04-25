class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for i in self.ledger:
            desc = i["description"][:23].ljust(23)
            amt = f"{i['amount']:>7.2f}"
            items += f"{desc}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total+"\n"

    def deposit(self,amount,description=""):
        return self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self,amount,description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        total = 0
        for i in self.ledger:
            total+=i["amount"]
        return total
    
    def transfer(self,amount,category):
        if self.check_funds(amount):
            self.withdraw(amount,f"Transfer to {category.name}")
            category.deposit(amount,f"Transfer from {self.name}") 
            return True
        return False
    
    def check_funds(self,amount):
        if amount > self.get_balance():
            return False
        return True


def create_spend_chart(categories):
    spent = []
    total_spent = 0
    for cat in categories:
        cat_spent = sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
        spent.append(cat_spent)
        total_spent+=cat_spent
    
    pourcentage = [int(i/total_spent*100) // 10 * 10 for i in spent]

    chart = "Percentage spent by category\n"
    for n in range(100,-1,-10):
        line =f"{n:>3}|"
        for p in pourcentage:
            line+=" o " if p>=n else "   "
        line += " " 
        chart+=line + "\n"

    chart += "    " + "-"*(len(categories)*3+1) + "\n" 

    max_len = max(len(cat.name) for cat in categories)
    for m in range(max_len):
        line ="     "
        for item in categories:
            if m < len(item.name):
                line += item.name[m]+ "  "
            else:
                line += "   "
        if m < max_len - 1:
            chart += line + "\n"
        else:
            chart += line  # Pas de retour à la ligne final
    return chart

if __name__=="__main__":
    food = Category('Food')
    food.deposit(1000, 'deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')
    #clothing = Category('Clothing')
    #food.transfer(50, clothing)

    print(food)
    #print(clothing)

    entertainment = Category("Entertainment")
    business = Category("Business")
    entertainment.deposit(900, "deposit")
    entertainment.withdraw(33.40, "movies")
    entertainment.withdraw(10, "games")

    business.deposit(900, "deposit")
    business.withdraw(10, "office supplies")
    business.withdraw(90, "paper")

    print(create_spend_chart([food, entertainment, business]))
