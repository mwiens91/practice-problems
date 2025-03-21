# @leet start
from collections import defaultdict, deque


class Solution:
    def findAllRecipes(
        self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]
    ) -> list[str]:
        # This is a graph problem for which we need to do a topological
        # sort. Build an adjacency list dictionary (ingredients which as
        # keys, recipes as a list of values) and an in-degree dictionary
        # (containing ingredients) first.
        adjacency_list_dict = defaultdict(list)
        in_degree_dict = defaultdict(int)

        for recipe, ingredients_list in zip(recipes, ingredients):
            for ingredient in ingredients_list:
                adjacency_list_dict[ingredient].append(recipe)
                in_degree_dict[recipe] += 1

        # Use Kahn's algorithm to process ingredients that are available
        # in topologically sorted order. Mark ingredients which are
        # recipes in a list.
        all_recipes_set = set(recipes)

        queue = deque(supplies)

        recipes_available = []

        while queue:
            # Get 0 in-degree ingredient and add it to the recipes
            # available if it's a recipe
            ingredient = queue.popleft()

            if ingredient in all_recipes_set:
                recipes_available.append(ingredient)

            # For each recipe the ingredient is used in, decrease its
            # in-degree by one. If its in-degree decreases to 0, add it
            # to the queue.
            for recipe in adjacency_list_dict[ingredient]:
                in_degree_dict[recipe] -= 1

                if in_degree_dict[recipe] == 0:
                    queue.append(recipe)

        return recipes_available


# @leet end
