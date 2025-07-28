import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    try:
        with open("artifacts/columns.json", "r") as f:
            data = json.load(f)
            print("Loaded JSON from columns.json:", data)
            __data_columns = data['data_column']  # ✅ your confirmed key
            __locations = __data_columns[3:]      # Skip sqft, bath, bhk
            print("Extracted locations:", __locations)
    except Exception as e:
        print("❌ Error loading columns.json:", e)

    try:
        with open("artifacts/bengaluru_house_prices.pkl", "rb") as f:
            __model = pickle.load(f)
            print("Model loaded successfully.")
    except Exception as e:
        print("❌ Error loading model.pkl:", e)

    print("loading saved artifacts...done")

def get_location_names():
    print("Returning locations from util:", __locations)
    return __locations

def get_data_columns():
    return __data_columns

# Optional: Run locally for testing
if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))
    print(get_estimated_price('Ejipura', 1000, 2, 2))
