merk ={
    "oppo": "Oppo A16",
    "vivo": "Vivo Y20",
}
for urutan, (brand, model) in enumerate(merk.items(), start=1):
    print(f"{urutan}. {brand}: {model}")
    