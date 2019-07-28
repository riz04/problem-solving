def combine_words(word,**kwargs):
        if "prefix" in kwargs:
            return kwargs["prefix"] + word
        elif "suffix" in kwargs:
            return word + kwargs["suffix"]
        return word

print(combine_words("man",prefix = "child"))

print(combine_words("hero",suffix = "children"))

print(combine_words("children"))