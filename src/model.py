import string

class model():
    def __init__(self):
        self.ingredient_dict = self._get_ingredient_dict()
        self.last_searched = ""
        self.remaining = None

    def _get_ingredient_dict(self):
        ingredients_file = open("resources/ingredients.txt", "r")
        ingredients = ingredients_file.read()
        ingredients = ingredients.split("\n")
        ingredients.remove("")
        ingredients.sort()

        ingredients_dict = {}
        for ingredient in ingredients:
            if ingredient[0] in ingredients_dict:
                ingredients_dict[ingredient[0]].append(ingredient)
            else:
                ingredients_dict[ingredient[0]] = [ingredient]

        return ingredients_dict


    def get_ingredients(self, user_input):
        if not self.remaining:
            out = self.ingredient_dict.get(user_input[0])
        else:
            out = self.remaining
            remove = []
            for word in out:
                if not word.startswith(user_input):
                    remove.append(word)
            for word in remove:
                out.remove(word)
        self.last_searched = user_input
        self.remaining = out
        return out


if __name__ == "__main__":
    model = model()
    print(model.get_ingredients("m"))
    print(model.get_ingredients("mi"))
    print(model.get_ingredients("mil"))
    print(model.get_ingredients("milk"))