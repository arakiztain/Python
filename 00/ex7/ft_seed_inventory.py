def ft_seed_inventory(seed_type: str, quantity: int, unit: str) ->None:
    def handle_packets():
        print(seed_type.capitalize(), "seeds:", quantity, unit, "avaliable")
    def handle_grams():
        print(seed_type.capitalize(), "seeds:", quantity, unit, "total")
    def handle_area():
        print(seed_type.capitalize(), "seeds: covers", quantity, "square meters")
    
    handlers = {
        "packets": handle_packets,
        "grams": handle_grams,
        "area": handle_area 
    }
    
    if unit not in ("packets", "grams", "area"):
        print("Unknown unit type")
        return

    handlers[unit]()
