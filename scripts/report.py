import pandas as pd

data = pd.read_excel("database.xlsx")

agency_names = list(data["Agency"].unique())
agency_totals = []
agency_antalyas = []
duplicated_totals = []
duplicated_antalyas = []
ratio_total = []
ratio_antalya = []

for agency_name in agency_names:
    agency_total = set(data["ID"].loc[(data["Agency"] == agency_name)])
    extracted_total = set(data["ID"].loc[(data["Agency"] != agency_name)])
    agency_antalya = set(data["ID"].loc[(data["Agency"] == agency_name) & (data["City"] == "Antalya")])
    extracted_antalya = set(data["ID"].loc[(data["Agency"] != agency_name) & (data["City"] == "Antalya")])
    duplicated_total = len(extracted_total.intersection(agency_total))
    duplicated_antalya = len(extracted_antalya.intersection(agency_antalya))
    
    agency_totals.append(len(agency_total))
    agency_antalyas.append(len(agency_antalya))
    duplicated_totals.append(duplicated_total)
    duplicated_antalyas.append(duplicated_antalya)
    ratio_total.append(duplicated_total/len(agency_total))
    ratio_antalya.append(duplicated_antalya/len(agency_antalya))
    
print(f"Villa Sayısı (Genel): {len(set(data['ID']))}")
print(f"Villa Sayısı (Antalya): {len(set(data['ID'].loc[(data['City'] == 'Antalya')]))}")
    
data = {
    "Acente": agency_names,
    "Villa Sayısı": agency_totals,
    "Kesişen Toplam": duplicated_totals,
    "Oran(Toplam)": ratio_total,
    "Villa Sayısı(Antalya)": agency_antalyas,
    "Kesişen Antalya": duplicated_antalyas,
    "Oran(Antalya)": ratio_antalya
}

df = pd.DataFrame(data)
df.set_index("Acente", inplace=True)
df.to_excel("duplicate_report.xlsx")
    
