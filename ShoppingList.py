#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the library

import pandas as pd


# In[2]:


# Sample data in multiple lists

Fresh_Produce = ["Apples", "Bananas", "Strawberries", "Avocados", "Bell Peppers", "Carrots", "Potatoes", "Spinach", "Tomatoes", "Mangoes", "Kiwi", "Papaya", "Peaches", "Pears", "Watermelon"]
Grains = ["Breadcrumbs", "Pasta", "Quinoa", "Rice", "Sandwich Bread", "Tortillas", "Oatmeal", "Barley", "Bulgur", "Couscous", "Cornmeal", "Whole wheat tortillas", "Farro", "Millet", "Wild rice"]
Meat = ["Chicken breasts", "Ground beef", "Pork chops", "Salmon fillets", "Turkey", "Bacon", "Lamb chops", "Shrimp", "Tilapia fillets", "Sausages", "Beef steaks", "Ground turkey", "Pork tenderloin", "Ham", "Duck breast"]
Dairy = ["Milk", "Eggs", "Butter", "Yogurt", "Cheese", "Sour cream", "Cottage cheese", "Cream cheese", "Heavy cream", "Whipping cream", "Buttermilk", "Ricotta cheese", "Parmesan cheese", "Gouda cheese", "Goat cheese"]
Baking_Goods = ["Baking powder", "Baking Soda", "Granulated Sugar", "Brown Sugar", "Flour", "Honey", "Vanilla Extract", "Dry Yeast", "Chocolate Chips", "Cocoa Powder", "Powdered Sugar", "Food coloring", "Sprinkles", "Powdered sugar", "Almond extract"]
Freezer = ["Berries", "Frozen Veggies", "Juice Concentrate", "Pizza", "Convenience Meals", "Pie Crust", "Cookie Dough" ,"Shrimp", "Ice cream", "dumplings", "appetizers", "seafood", "Waffles", "Pancakes", "Potstickers"]
Canned = ["Chicken stock", "Broth", "Salsa", "Diced Tomatoes", "Jam", "Jelly", "Peanut Butter", "Pasta Sauce", "Beans", "Soups", "Tuna", "Green Chiles", "Canned Veggies", "Coffee", "Tea"]
Condiments = ["Black Pepper", "Chili Powder", "Cinnamon", "Crushed Red Pepper", "Cumin", "Garlic Powder", "Ketchup", "Mustard", "Mayo", "Nutmeg", "Paprika", "Salt", "Soy Sauce", "Steak Sauce", "Buffalo Sauce"]
Oils_Vinegars = ["Coconut Oil", "Olive Oil", "Vegetable", "Canola Oil", "Peanut oil", "Avocado oil", "Sesame oil", "Grapeseed oil", "Walnut oil", "Apple cider vinegar", "Balsamic vinegar", "Red Wine Vinegar", "White Vinegar", "Cooking Wine", "White Wine Vinegar"]


# In[3]:


# Create a DataFrame from the lists
data = {
    'Fresh_Produce': Fresh_Produce,
    'Grains': Grains,
    'Meat': Meat,
    'Dairy': Dairy,
    'Baking_Goods': Baking_Goods,
    'Freezer': Freezer,
    'Canned': Canned,
    'Condiments': Condiments,
    'Oils_Vinegars': Oils_Vinegars
}


# In[4]:


df = pd.DataFrame(data)


# In[5]:


# Display the DataFrame as a table

print("Table:")
print(df)


# In[8]:


# Save the DataFrame to a CSV file
csv_filename = "D:\DOCS\Downloads\Shopping_List.csv"
df.to_csv(csv_filename, index=True)


# In[ ]:





# In[ ]:




