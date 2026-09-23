countries = ['USA', 'Canada', 'Mexico', 'Brazil', 'Ireland', 'France', 'Germany', 'Italy', 'Spain', 'Portugal', 'India']

output = []
count = 0

for country in countries:
    if country.startswith('I'): 
        output.append(country)
        count += 1
        
        
print(f"Country starting with 'I': {output}")
print(f"Number of countries starting with 'I': {count}")
        