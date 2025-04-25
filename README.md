# Budget App

- **Ce code permet de gérer un budget par catégories (dépôt, retrait, transfert, solde).**
- **Il propose une méthode d’affichage claire du ledger et un graphique textuel du pourcentage de dépenses par catégorie.**
- **Idéal pour visualiser la répartition des dépenses dans un style simple et lisible.**
---

## Algorithme Utilisé

### **Gestion de budget par catégories**

- **Ledger** : Liste de dictionnaires pour enregistrer chaque opération.
- **Calcul des soldes et des dépenses** : Parcours de la liste pour additionner les montants.
- **Création du graphique** : Calcul des pourcentages, affichage ligne par ligne du graphique à barres verticales, puis des noms de catégories en colonne.

### 1. **Classe `Category`**

Cette classe représente une catégorie budgétaire (par exemple : Food, Entertainment, Business).

#### a. **Initialisation**

```python
def __init__(self, name):
    self.name = name
    self.ledger = []
```
- **`name`** : nom de la catégorie.
- **`ledger`** : liste des transactions (dépôts, retraits, transferts).

---

#### b. **Affichage de la catégorie**

```python
def __str__(self):
    title = f"{self.name:*^30}\n"
    items = ""
    for i in self.ledger:
        desc = i["description"][:23].ljust(23)
        amt = f"{i['amount']:>7.2f}"
        items += f"{desc}{amt}\n"
    total = f"Total: {self.get_balance():.2f}"
    return title + items + total + "\n"
```
- Affiche la catégorie joliment :
  - Le nom centré et entouré d’astérisques.
  - Chaque opération avec sa description (23 caractères max) et le montant aligné à droite.
  - Le total en bas.

---

#### c. **Méthodes de gestion du budget**

- **Dépôt d’argent**
  ```python
  def deposit(self, amount, description=""):
      return self.ledger.append({'amount': amount, 'description': description})
  ```
  - Ajoute un montant positif dans le ledger.

- **Retrait d’argent**
  ```python
  def withdraw(self, amount, description=""):
      if self.check_funds(amount):
          self.ledger.append({'amount': -amount, 'description': description})
          return True
      return False
  ```
  - Ajoute un montant négatif si les fonds sont suffisants.

- **Solde courant**
  ```python
  def get_balance(self):
      total = 0
      for i in self.ledger:
          total += i["amount"]
      return total
  ```
  - Calcule la somme de toutes les opérations.

- **Transfert d’argent**
  ```python
  def transfer(self, amount, category):
      if self.check_funds(amount):
          self.withdraw(amount, f"Transfer to {category.name}")
          category.deposit(amount, f"Transfer from {self.name}")
          return True
      return False
  ```
  - Retire de cette catégorie et dépose dans une autre, si possible.

- **Vérification des fonds**
  ```python
  def check_funds(self, amount):
      if amount > self.get_balance():
          return False
      return True
  ```
  - Vérifie si le montant demandé est disponible.

---

### 2. **Fonction `create_spend_chart(categories)`**

Cette fonction crée un graphique à barres verticales du pourcentage de dépenses par catégorie.

#### a. **Calcul des dépenses**

```python
spent = []
total_spent = 0
for cat in categories:
    cat_spent = sum(-item["amount"] for item in cat.ledger if item["amount"] 3}|"
    for p in pourcentage:
        line += " o " if p >= n else "   "
    line += " "
    chart += line + "\n"

chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
```
- Pour chaque niveau de pourcentage (100, 90, ..., 0), ajoute une ligne avec un "o" si la catégorie atteint ce niveau.

#### d. **Affichage des noms de catégories verticalement**

```python
max_len = max(len(cat.name) for cat in categories)
for m in range(max_len):
    line = "     "
    for item in categories:
        if m < len(item.name):
            line += item.name[m] + "  "
        else:
            line += "   "
    if m < max_len - 1:
        chart += line + "\n"
    else:
        chart += line
```
- Affiche les noms de catégories verticalement sous le graphique.

---

### 3. **Exemple d’utilisation**

```python
if __name__ == "__main__":
    food = Category('Food')
    food.deposit(1000, 'deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')

    entertainment = Category("Entertainment")
    business = Category("Business")
    entertainment.deposit(900, "deposit")
    entertainment.withdraw(33.40, "movies")
    entertainment.withdraw(10, "games")

    business.deposit(900, "deposit")
    business.withdraw(10, "office supplies")
    business.withdraw(90, "paper")

    print(food)
    print(create_spend_chart([food, entertainment, business]))
```
- Crée trois catégories, effectue des opérations, affiche le ledger de `food` et le graphique des dépenses.

---


---
