fuel_per_hour = 2.5     # litres per hour
cost_per_litre = 1800   # Price per litre RWF
hours = 5               # Hours the generator runs
Total_fuel_consumed = fuel_per_hour * hours
Total_cost = Total_fuel_consumed * cost_per_litre
print("Generator Fuel Consumption:")
print("Fuel consumed per hour:",fuel_per_hour,"litres")
print("Cost of fuel per litre:",cost_per_litre,"RWF")
print("The genarator runs for:",hours,"hours")
print("The total fuel consumed is:",Total_fuel_consumed,"litres")
print("The total cost is:",Total_cost,"RWF")