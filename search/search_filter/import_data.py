import pandas as pd
from .models import car
from .models import property

housing_data = './USA Housing Dataset.csv'
car_data = './vehicles_dataset.csv'
house_read = pd.read_csv(housing_data)
car_read = pd.read_csv(car_data)

def run():
    # for index, row in house_read.iterrows():
    #     property_instance = property(
    #         price=row['price'],
    #         street=row['street'],
    #         city=row['city'],
    #         state_zip=row['statezip'],
    #         country=row['country'],
    #         square_feet=row['sqft_living'],
    #         beds=row['bedrooms'],
    #         baths=row['bathrooms'],
    #         lot_size=row['sqft_lot'],
    #         year_built=row['yr_built'],
    #         year_renovated=row['yr_renovated'],
    #     )
    #     property_instance.save()
    for index, row in car_read.iterrows():
        car_instance = car(
            manufacturer=row['make'],
            model=row['model'],
            trim=row['trim'],
            mileage=row['mileage'],
            year=row['year'],
            price=row['price'],
            description=row['description'],
            name=row['name'],
            drivetrain=row['drivetrain'],
        )
        car_instance.save()
    print("CSV data migrated into database.")