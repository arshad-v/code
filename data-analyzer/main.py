#i = 10

###for i in range(1, 8):
    #if i == 5:
        #break
    #print(i)

# total = 0
# for i in range(1, 11):
#     total += i
#     print(i, total)
# print("Sum is:", total)

# word = "Python"
# for char in word:
#     print(char)

# for i in range(1, 11):
#     print(f"5 x {i} = {5*i}")

# for i in range(1,11):
#     print("*" * i)


# for i in range(1, 6):
#     print(" " * (5 - i) + "*" * (2 * i - 1))count = 5

# count = 10
# while count > 0:
#     print(count)
#     count -= 1


# command = ""
# while command != "exit":
#     command = input("Type 'exit' to stop: ")


# import csv

# # Open and read CSV file
# file_path = "C:\\Users\\arshu\Desktop\\projects\\nizz_projects\\code\\data-analyzer\\carprices.csv"
# with open(file_path, mode="r") as file:
#     reader = csv.reader(file)
    
#     for row in reader:
#         print(row)



# # ✅ Your data to write
# data = [
#     ["Brand", "Model", "Price"],
#     ["Toyota", "Corolla", 15000],
#     ["Honda", "Civic", 17000],
#     ["Ford", "Focus", 0000]
# ]

# # ✅ Write the data to file
# with open(file_path, mode="w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(data)

# print("✅ Data written to", file_path)


import pandas as pd
import sqlite3


import pandas as pd
print(pd.__version__)

df = pd.read_csv("carprices.csv")
print(df)

for index, row in df.iterrows():
    print(f"{row['Model']} of {row['Brand']} price is {row['Price']}.")
    break

print(df.head)



user_input = input("Enter a brand name: ")
print(f"\n📍 Cars from brand: {user_input}")
for index, row in df.iterrows():
    if row['Brand'].lower() == user_input.lower():
        print(f"✔️ {row['Brand']} {row['Model']} - ₹{row['Price']}")
    else:
        print(f"❌ Not {user_input}: {row['Brand']} {row['Model']}")

### sqlit
import sqlite3

connect = sqlite3.connect("sakila.db")
# ✅ List all tables in the database
tables_query = "SELECT name FROM sqlite_master WHERE type='table';"
tables = pd.read_sql_query(tables_query, connect)
print("📋 Tables in database:")
print(tables)

df = pd.read_sql_query("SELECT * FROM actor LIMIT 10;", connect)
print("\n🎭 Sample data from 'actor' table:")
print(df)


