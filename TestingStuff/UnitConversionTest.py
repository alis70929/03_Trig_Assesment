unit_list = ["mm", "cm", "dm", "m", "dam", "hm", "km"]

unit_to_convert = input("unit to convert")
to_conver_to = input("unit to convert to")

index1 = unit_list.index(unit_to_convert)
index2 = unit_list.index(to_conver_to)

power = index2 - index1
print(power)
