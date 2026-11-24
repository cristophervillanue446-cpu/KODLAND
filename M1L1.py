meme_dict = {
            "HILL": "Alguien que es inocente ",
           "CAUSA": "Forma de decir a un amigo",
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
   print(meme_dict[word])
else:
   print("PALABRA NO RECONOCIDA")
