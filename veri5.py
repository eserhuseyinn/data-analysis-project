import pandas as pd
import matplotlib.pyplot as plt

# Excel dosyasını oku
veri = pd.read_excel(
    r"C:/Users/pc/Desktop/veri5.xlsx",
    sheet_name="sayfa1"
)

# Eksik verileri kontrol et
print(veri.isnull().sum())

# Şehir bazlı toplam kar
sehir_kar = veri.groupby("Sehir")["Toplam_Kar"].sum()

# Büyükten küçüğe sırala
sehir_kar = sehir_kar.sort_values(ascending=False)

print(sehir_kar)

# Grafik oluştur
sehir_kar.head(10).plot(kind="bar")

plt.title("En Yüksek Kara Sahip 10 Şehir")
plt.xlabel("Şehir")
plt.ylabel("Toplam Kar")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()