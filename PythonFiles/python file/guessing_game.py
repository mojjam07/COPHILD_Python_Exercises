enter_word = input("\nI have 5 secret words with me, can you guess one?\n\nIt is : ")

my_word = ["Success", "Money", "Love"]

#for word in my_word:
    
if enter_word in my_word:
    print(f"\nWow! {enter_word}, you're right.")
else:
    print(f"\nOops! {enter_word}, you're wrong! ")