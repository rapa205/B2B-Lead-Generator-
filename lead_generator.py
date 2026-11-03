import csv
print("==================================================")
print("📊 B2B LEAD GENERATOR & SCRAPER TOOL")
print("==================================================")

# Имитация собранных данных по американским стартапам / фрилансерам
leads = [
    {"Name": "John Doe", "Niche": "SaaS Founder", "Email": "john@example-saas.com", "Status": "New"},
    {"Name": "Sarah Connor", "Niche": "E-commerce Owner", "Email": "sarah@shop-US.com", "Status": "New"},
    {"Name": "Alex Smith", "Niche": "Marketing Agency", "Email": "alex@growth-agency.io", "Status": "New"}
]

filename = "generated_leads.csv"

print(f"\n⏳ Scraping target directory & filtering leads...")
print(f"✨ Found {len(leads)} potential high-value leads.")

# Экспорт в чистый CSV, который можно сразу открыть в Excel
try:
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Niche", "Email", "Status"])
        writer.writeheader()
        for lead in leads:
            writer.writerow(lead)
    print(f"\n✅ SUCCESS! Leads successfully exported to '{filename}'.")
except Exception as e:
    print(f"❌ Error saving file: {e}")

print("==================================================")