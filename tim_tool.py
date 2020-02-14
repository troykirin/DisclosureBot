# quote = input("Enter quote to trim: ")
# %%

with open("text_to_trim.txt", "r") as f:
    clean = f.read().replace('\n', '')

print(clean)


# %%
