# To display the smallest and largest word from the string

text = input("Enter a sentence:")
text_list = list(text.split())
print(text_list)
sort_list = sorted(text_list, key=len)
print(sort_list[0])
print(sort_list[-1])


