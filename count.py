import csv

filePath = "" //Path of extract2.py
SaveList = []
dic = {}

with open(filePath, "r") as f:
    lines = f.readlines()
    content = f.read()
    print(content)
    for line in lines:
        country = line.split()[0]
        year = line.split()[1]
        if year not in dic:
            dic[year] = {}
        if country not in dic[year]:
            dic[year][country] = 1
        else:
            dic[year][country] += 1

with open('country_counts.csv', 'w', newline='') as csvfile:
    fieldnames = ['Year', 'Country', 'Count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for year, country_counts in dic.items():
        for country, count in country_counts.items():
            writer.writerow({'Year': year, 'Country': country, 'Count': count})

f.close()
