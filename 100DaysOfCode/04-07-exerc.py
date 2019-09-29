from itertools import chain
"""
1. Get all Jeeps
2. Get the first car of every manufacturer.
3. Get all vehicles containing the string Trail in their names (should work for other grep too)
4. Sort the models (values) alphabetically
"""

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    return ', '.join(cars['Jeep'])


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    return [model[0] for model in cars.values()] 

def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    grep = grep.lower()
    models = list(chain.from_iterable(cars.values()))
    matching_models = [model for model in models if grep in model.lower()]
    return sorted(matching_models)

    return [models for models in cars.values()]  

    

def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    return {manufacturer: sorted(models) for manufacturer, models in cars.items()}



all_jeeps = get_all_jeeps(cars)
print(all_jeeps)
first_models = get_first_model_each_manufacturer(cars)
print(first_models)
matching_models = get_all_matching_models(cars)
print(matching_models)
sorted_models = sort_car_models(cars)
print(sorted_models)

