# quote = input("Enter quote to trim: ")
# %%

with open("text_to_trim.txt", "r") as f:
    clean_quote = f.read().replace('\n', '')

new_filename = "clean_text.txt"
# clean_file = open(new_filename, "x")
clean_file = open(new_filename, "w")

clean_file.write(clean_quote)

clean_file.close()

print(clean_quote)


# %%
