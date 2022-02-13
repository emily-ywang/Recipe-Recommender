import string


class ingredient_searcher():
    def __init__(self):
        self.ingredient_dict = self._get_ingredient_dict()
        self.last_searched = {}  # dp table used for get_ingredients

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
        if user_input in self.ingredient_dict:
            out = self.ingredient_dict.get(user_input)
            self.last_searched = {}
            return out
        if user_input == "":
            self.last_searched = {}
            return self.ingredient_dict.get("a")

        if user_input in self.last_searched:
            out = self.last_searched.get(user_input)
            return out

        out = self.get_ingredients(user_input[:-1]).copy()
        remove = []
        for word in out:
            if not word.startswith(user_input):
                remove.append(word)
        for word in remove:
            out.remove(word)

        self.last_searched.update({user_input: out})
        return out


if __name__ == "__main__":
    ingredient_searcher = ingredient_searcher()
    print(ingredient_searcher.get_ingredients("m"))
    print(ingredient_searcher.get_ingredients("mi"))
    print(ingredient_searcher.get_ingredients("mil"))
    print(ingredient_searcher.get_ingredients("milk"))
    print("------------------------------------------------------------")
    print(ingredient_searcher.get_ingredients("sna"))
    print(ingredient_searcher.get_ingredients("sn"))
    print("------------------------------------------------------------")
    print(ingredient_searcher.get_ingredients(""))
