import pickle

# تحميل الموديل
with open("best_model.pkl", "rb") as file:
    model = pickle.load(file)
