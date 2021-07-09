def human_years_cat_years_dog_years(human_years):
    cat_years = 0
    dog_years = 0
    if human_years == 1:
        cat_years = dog_years = 15
    elif human_years == 2:
        cat_years = dog_years = 24
    elif human_years >= 3:
        cat_years = cat_years + 15 + 9 + 4 * (human_years - 2)
        dog_years = dog_years + 15 + 9 + 5 * (human_years - 2)
    return [human_years, cat_years, dog_years]

human_years = 10
print(human_years_cat_years_dog_years(human_years))