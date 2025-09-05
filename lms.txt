import streamlit as st
import pickle
import pandas as pd

# Load dataset
df = pd.read_csv("cleaned_croma_laptops.csv")

models = {
    "Linear Regression": "linear_laptop_price_model.pkl",
    "Ridge Regression": "ridge_model.pkl",
    "Lasso Regression": "lasso_model.pkl",
    "Random Forest": "random_forest_model.pkl",
    "Decision Tree": "decision_model.pkl"
}


st.sidebar.title("Laptop Price Prediction")
model_choice = st.sidebar.selectbox("Choose a model", list(models.keys()))


with open(models[model_choice], "rb") as file:
    model = pickle.load(file)



st.title("Laptop Price Prediction App")


brand = st.selectbox("Brand", ["HP", "Dell", "Lenovo", "Apple", "Asus", "Acer", "MSI", "Other"])
ram = st.number_input("RAM (GB)", min_value=4, max_value=64, step=4, value=8)
storage = st.number_input("Storage (GB)", min_value=128, max_value=2000, step=128, value=512)
cpu = st.selectbox("CPU", ["Apple","Intel i3", "Intel i5", "Intel i7", "Intel i9", "Ryzen 3", "Ryzen 5", "Ryzen 7", "Other"])
gpu = st.selectbox("GPU", ["Integrated", "NVIDIA", "AMD", "Other"])
color = st.selectbox("Color", df["Color"].dropna().unique())
screen_size = st.selectbox("Screen Size (inches)", df["Screen Size"].dropna().unique())



input_data = pd.DataFrame([{
    "Brand": brand,
    "Screen Size": screen_size,
    "RAM": ram,
    "Storage": storage,
    "Color": color,
    "CPU": cpu,
    "GPU": gpu
}])


if st.button("Predict Price"):
    predicted_price = model.predict(input_data)[0]
    st.success(f"Estimated Laptop Price: ₹{predicted_price:,.2f}")












# import streamlit as st
# import pickle
# import pandas as pd

# # Load dataset
# df = pd.read_csv("cleaned_croma_laptops.csv")

# # Models
# models = {
#     "Linear Regression": "linear_laptop_price_model.pkl",
#     "Ridge Regression": "ridge_model.pkl",
#     "Lasso Regression": "lasso_model.pkl",
#     "Random Forest": "random_forest_model.pkl",
#     "Decision Tree": "decision_model.pkl"
# }

# # Sidebar
# st.sidebar.title("Laptop Price Prediction")
# model_choice = st.sidebar.selectbox("Choose a model", list(models.keys()))

# # Load selected model
# with open(models[model_choice], "rb") as file:
#     model = pickle.load(file)

# # Title
# st.title("💻 Laptop Price Prediction App")

# # --- User Inputs (dynamic from dataset) ---
# brand = st.selectbox("Brand", df["Brand"].dropna().unique())
# screen_size = st.selectbox("Screen Size (inches)", df["Screen Size"].dropna().unique())
# color = st.selectbox("Color", df["Color"].dropna().unique())  # ✅ added
# ram = st.selectbox("RAM (GB)", sorted(df["RAM"].dropna().unique()))
# storage = st.selectbox("Storage (GB)", sorted(df["Storage"].dropna().unique()))
# cpu = st.selectbox("CPU", df["CPU"].dropna().unique())
# gpu = st.selectbox("GPU", df["GPU"].dropna().unique())

# # Input DataFrame (must match training columns exactly)
# input_data = pd.DataFrame([{
#     "Brand": brand,
#     "Screen Size": screen_size,
#     "Color": color,
#     "RAM": ram,
#     "Storage": storage,
#     "CPU": cpu,
#     "GPU": gpu
# }])

# # Predict
# if st.button("Predict Price"):
#     predicted_price = model.predict(input_data)[0]
#     st.success(f"💰 Estimated Laptop Price: ₹{predicted_price:,.2f}")














# import streamlit as st
# import pandas as pd
# import pickle
# import matplotlib.pyplot as plt

# # --- Load Dataset ---
# df = pd.read_csv("cleaned_croma_laptops.csv")

# # --- Load Models ---
# models = {
#     "Linear Regression": "linear_laptop_price_model.pkl",
#     "Ridge Regression": "ridge_model.pkl",
#     "Lasso Regression": "lasso_model.pkl",
#     "Random Forest": "random_forest_model.pkl",
#     "Decision Tree": "decision_model.pkl"
# }

# # --- Sidebar Menu ---
# st.sidebar.title("Laptop Price Prediction App")
# menu = st.sidebar.radio("Select Section", ["EDA", "Prediction"])

# # ==============================
# # 📊 EDA Section
# # ==============================
# if menu == "EDA":
#     st.title("📊 Exploratory Data Analysis")

#     st.subheader("Dataset Preview")
#     st.dataframe(df.head())

#     st.subheader("Summary Statistics")
#     st.write(df.describe())

#     st.subheader("Price Distribution")
#     fig, ax = plt.subplots()
#     ax.hist(df["Price"], bins=30, color="skyblue", edgecolor="black")
#     ax.set_xlabel("Price")
#     ax.set_ylabel("Frequency")
#     st.pyplot(fig)

#     st.subheader("Average Price by Brand")
#     fig, ax = plt.subplots(figsize=(10, 5))
#     avg_price = df.groupby("Brand")["Price"].mean().sort_values()
#     avg_price.plot(kind="bar", ax=ax, color="lightgreen")
#     ax.set_ylabel("Average Price")
#     st.pyplot(fig)

#     st.subheader("Correlation Heatmap")
#     corr = df.corr(numeric_only=True)
#     fig, ax = plt.subplots(figsize=(8, 6))
#     cax = ax.matshow(corr, cmap="coolwarm")
#     fig.colorbar(cax)
#     ax.set_xticks(range(len(corr.columns)))
#     ax.set_yticks(range(len(corr.columns)))
#     ax.set_xticklabels(corr.columns, rotation=90)
#     ax.set_yticklabels(corr.columns)
#     st.pyplot(fig)

# # ==============================
# # 💻 Prediction Section
# # ==============================
# elif menu == "Prediction":
#     st.title("💻 Laptop Price Prediction")

#     # --- Select Model ---
#     model_choice = st.selectbox("Choose a model", list(models.keys()))

#     # Load Selected Model
#     with open(models[model_choice], "rb") as file:
#         model = pickle.load(file)

#     # --- User Inputs ---
#     brand = st.selectbox("Brand", df["Brand"].unique())
#     ram = st.number_input("RAM (GB)", min_value=4, max_value=64, step=4, value=8)
#     storage = st.number_input("Storage (GB)", min_value=128, max_value=2000, step=128, value=512)
#     cpu = st.selectbox("CPU", df["CPU"].unique())
#     gpu = st.selectbox("GPU", df["GPU"].unique())
#     screen_size = st.number_input("Screen Size (inches)", min_value=11.0, max_value=20.0, step=0.1, value=15.6)
#     color = st.selectbox("Color", df["Color"].dropna().unique()) 

#     # Convert to DataFrame
#     input_data = pd.DataFrame([{
#         "Brand": brand,
#         "RAM": ram,
#         "Storage": storage,
#         "CPU": cpu,
#         "GPU": gpu,
#         "Screen Size": screen_size,
#         "Color": color
#     }])

#     # --- Predict ---
#     if st.button("Predict Price"):
#         predicted_price = model.predict(input_data)[0]
#         st.success(f"💰 Estimated Laptop Price: ₹{predicted_price:,.2f}")
