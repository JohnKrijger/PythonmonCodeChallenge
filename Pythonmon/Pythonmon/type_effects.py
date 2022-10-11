class TypeEffects:
    
    # Matrix containing type effects
    effectiveness_matrix = {
        "Dragon": {
            "Dragon": 2.0,
            "Fire": 1.0,
            "Grass": 1.0,
            "Ground": 1.0,
            "Steel": 0.5,
            "Water": 1.0,
            },
        "Fire": {
            "Dragon": 0.5,
            "Fire": 0.5,
            "Grass": 2.0,
            "Ground": 1.0,
            "Steel": 2.0,
            "Water": 0.5,
            },
        "Grass": {
            "Dragon": 0.5,
            "Fire": 0.5,
            "Grass": 0.5,
            "Ground": 2.0,
            "Steel": 0.5,
            "Water": 2.0,
            },
        "Ground": {
            "Dragon": 1.0,
            "Fire": 2.0,
            "Grass": 0.5,
            "Ground": 1.0,
            "Steel": 2.0,
            "Water": 1.0,
            },
        "Steel": {
            "Dragon": 1.0,
            "Fire": 0.5,
            "Grass": 1.0,
            "Ground": 1.0,
            "Steel": 0.5,
            "Water": 0.5,
            },
        "Water": {
            "Dragon": 0.5,
            "Fire": 2.0,
            "Grass": 0.5,
            "Ground": 2.0,
            "Steel": 1.0,
            "Water": 0.5,
            },
        }

    def effectiveness(attacking_type, defending_type):
        """Get effectiveness between types."""
        try:
            return TypeEffects.effectiveness_matrix[
                attacking_type][defending_type]
        except KeyError:
            return 1.0


