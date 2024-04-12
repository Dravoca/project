meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "CAP": "Tanggapan umum terhadap suatu yang salah/bohong",
            "SUP": "kata untuk menyapa seseorang",
            "AGGRO": "kata Untuk menjadi agresif/marah",
            "WKWK" : "kata untuk mengekspresikan ketawa",
            "CREEPY" : "menakutkan,tidak menyenangkan"
            }
            
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
if word in meme_dict.keys():
    print("Makna kata:", meme_dict[word])
else:
    print("maaf, kata itu tidak ada di dictonary")
