# clothing_size_converter.py

def convert_to_inches(value, unit):
    """Converts a measurement value to inches if the unit is centimeters."""
    if unit.lower() == "cm":
        return value / 2.54
    return value

def get_hm_sizes(measurements, gender):
    """Calculates H&M clothing sizes based on measurements."""
    sizes = {}
    if gender.lower() == "men":
        chest_in_inches = convert_to_inches(measurements["chest"], measurements["unit"])
        if chest_in_inches <= 36:
            sizes["H&M"] = "S"
        elif chest_in_inches <= 40:
            sizes["H&M"] = "M"
        elif chest_in_inches <= 44:
            sizes["H&M"] = "L"
        else:
            sizes["H&M"] = "XL"
    elif gender.lower() == "women":
        bust_in_inches = convert_to_inches(measurements["bust"], measurements["unit"])
        if bust_in_inches <= 34:
            sizes["H&M"] = "S"
        elif bust_in_inches <= 38:
            sizes["H&M"] = "M"
        elif bust_in_inches <= 42:
            sizes["H&M"] = "L"
        else:
            sizes["H&M"] = "XL"
    return sizes

def get_zara_sizes(measurements, gender):
    """Calculates Zara clothing sizes based on measurements."""
    sizes = {}
    if gender.lower() == "men":
        chest_in_inches = convert_to_inches(measurements["chest"], measurements["unit"])
        if chest_in_inches <= 38:
            sizes["Zara"] = "S"
        elif chest_in_inches <= 42:
            sizes["Zara"] = "M"
        elif chest_in_inches <= 46:
            sizes["Zara"] = "L"
        else:
            sizes["Zara"] = "XL"
    elif gender.lower() == "women":
        bust_in_inches = convert_to_inches(measurements["bust"], measurements["unit"])
        if bust_in_inches <= 35:
            sizes["Zara"] = "S"
        elif bust_in_inches <= 39:
            sizes["Zara"] = "M"
        elif bust_in_inches <= 43:
            sizes["Zara"] = "L"
        else:
            sizes["Zara"] = "XL"
    return sizes

def get_levis_sizes(measurements, gender):
    """Calculates Levi's clothing sizes based on measurements."""
    sizes = {}
    if gender.lower() == "men":
        waist_in_inches = convert_to_inches(measurements["waist"], measurements["unit"])
        if waist_in_inches <= 30:
            sizes["Levi's"] = "S"
        elif waist_in_inches <= 34:
            sizes["Levi's"] = "M"
        elif waist_in_inches <= 38:
            sizes["Levi's"] = "L"
        else:
            sizes["Levi's"] = "XL"
    elif gender.lower() == "women":
        waist_in_inches = convert_to_inches(measurements["waist"], measurements["unit"])
        if waist_in_inches <= 27:
            sizes["Levi's"] = "28"
        elif waist_in_inches <= 30:
            sizes["Levi's"] = "30"
        elif waist_in_inches <= 33:
            sizes["Levi's"] = "32"
        else:
            sizes["Levi's"] = "34"
    return sizes

def main():
    """Main function to run the clothing size converter application."""
    print("Welcome to Clothing Size Converter! 👕👖")

    while True:
        gender = input("Enter your gender (Men/Women): ").strip().lower()
        if gender in ["men", "women"]:
            break
        print("Invalid gender. Please enter 'Men' or 'Women'.")

    while True:
        unit = input("Enter your measurement unit (Inches/cm): ").strip().lower()
        if unit in ["inches", "cm"]:
            break
        print("Invalid unit. Please enter 'Inches' or 'cm'.")

    measurements = {"unit": unit}
    try:
        if gender == "men":
            measurements["chest"] = float(input(f"Enter chest size (in {unit}): "))
            measurements["waist"] = float(input(f"Enter waist size (in {unit}): "))
        else:  # women
            measurements["bust"] = float(input(f"Enter bust size (in {unit}): "))
            measurements["waist"] = float(input(f"Enter waist size (in {unit}): "))
            measurements["hips"] = float(input(f"Enter hips size (in {unit}): "))
    except ValueError:
        print("Invalid input. Please enter a numerical value for your measurements.")
        return

    sizes = {}
    sizes.update(get_hm_sizes(measurements, gender))
    sizes.update(get_zara_sizes(measurements, gender))
    sizes.update(get_levis_sizes(measurements, gender))

    print("\nEquivalent Sizes:")
    if not sizes:
        print("Could not determine sizes with the provided measurements.")
    else:
        for brand, size in sizes.items():
            print(f"{brand}: {size}")

if __name__ == "__main__":
    main()