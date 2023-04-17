monthConversions = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March"
}

print(monthConversions["Feb"])
print(monthConversions.get("Jan"))
print(monthConversions.get("Mah", "Not a valid key"))