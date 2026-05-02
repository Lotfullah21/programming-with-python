empty_list = []
print(empty_list)

football_items = ["football", "socks", "shinguards", "pump", "tshirts"]
cricket_items = ["bats", "stumps"]
print("Football items", football_items)
print("index-0", football_items[0])
print("index-1", football_items[1])
print("index-2", football_items[2])
print("index-1 + shoes", football_items[1]+"and shoes")
print(cricket_items+football_items)

football_items[0] = "ground"
print("items after mutation", football_items)
