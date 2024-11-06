import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
import joblib
from ctypes import windll
import ctypes

# Load the trained model
model = joblib.load('HeartDiseaseTrainedModel')


def predict():
    # Retrieve user inputs
    age = int(age_entry.get())
    gender = int(gender_var.get()) if gender_var.get() is not None else -1
    chest_pain = int(chest_pain_var.get()) if chest_pain_var.get() is not None else -1
    trestbps = int(trestbps_entry.get())
    chol = int(chol_entry.get())
    fbs = int(fbs_var.get()) if fbs_var.get() is not None else -1
    restecg = int(restecg_var.get()) if restecg_var.get() is not None else -1
    thalach = int(thalach_entry.get())
    exang = int(exang_var.get()) if exang_var.get() is not None else -1
    oldpeak = float(oldpeak_entry.get())
    slope = int(slope_var.get()) if slope_var.get() is not None else -1
    ca = int(ca_entry.get())
    thal = int(thal_var.get()) if thal_var.get() is not None else -1

    # Make prediction
    input_data = [[age, gender, chest_pain, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
    prediction = model.predict(input_data)

    # Display prediction result
    result_label.config(text="High chance of heart disease" if prediction == 1 else "Low chance of heart disease")
    return prediction


def reset_form():
    # Clear form fields
    age_entry.delete(0, tk.END)
    gender_var.set(None)
    chest_pain_var.set(None)
    trestbps_entry.delete(0, tk.END)
    chol_entry.delete(0, tk.END)
    fbs_var.set(None)
    restecg_var.set(None)
    thalach_entry.delete(0, tk.END)
    exang_var.set(None)
    oldpeak_entry.delete(0, tk.END)
    slope_var.set(None)
    ca_entry.delete(0, tk.END)
    thal_var.set(None)
    # Clear prediction result
    result_label.config(text='')


root = tk.Tk()
root.title("Heart Disease Predictor")
root.geometry("1500x900")
windll.shcore.SetProcessDpiAwareness(1)
root.configure(bg="#d1e8ff")

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('company.app.1')
root.iconphoto(False, tk.PhotoImage(file='heart64.png'))

# app frame
app_frame = tk.Frame(root)
app_frame.configure(bg="#d1e8ff")
app_frame.pack(padx=20, pady=20)

heading = ttk.Label(app_frame, text="Heart Disease Predictor", background="#d1e8ff", font=("poppins", 30))
heading.pack()

# Create form frame
form_frame = ttk.Frame(app_frame, style="Custom.TFrame")
form_frame.pack(padx=10, pady=10, anchor="w")
root.style = ttk.Style()
root.style.configure("Custom.TFrame", background="#d1e8ff")

r = ttk.Style()
r.configure('Wild.TRadiobutton', background="#d1e8ff", font=("poppins", 14))

l = ttk.Style()
l.configure('Custom.TLabel', background="#d1e8ff", width=30, font=("poppins", 15))

b = ttk.Style()
b.configure('Custom.TButton', background="#81c781", width=15, font=("poppins", 13), borderwidth=0)

# Age
age_label = ttk.Label(form_frame, text="Age:", background="#d1e8ff", font=("poppins", 15))
age_label.grid(row=0, column=0, sticky="w")
age_entry = ttk.Entry(form_frame, font=("poppins", 12))
age_entry.grid(row=0, column=1)

# Gender
gender_label = ttk.Label(form_frame, text="Gender :", style="Custom.TLabel")
gender_label.grid(row=1, column=0, sticky="w")
gender_var = tk.IntVar()
gender_female_radio = ttk.Radiobutton(form_frame, text="Female", variable=gender_var, value=0,
                                      style='Wild.TRadiobutton')
gender_male_radio = ttk.Radiobutton(form_frame, text="Male", variable=gender_var, value=1, style='Wild.TRadiobutton')
gender_female_radio.grid(row=1, column=1, sticky="w")
gender_male_radio.grid(row=1, column=2, sticky="w")
gender_var.set(None)  # Set to None initially

# Chest Pain Type
chest_pain_label = ttk.Label(form_frame, text="Chest Pain :", style="Custom.TLabel")
chest_pain_label.grid(row=2, column=0, sticky="w")
chest_pain_var = tk.IntVar()
chest_pain_typical_radio = ttk.Radiobutton(form_frame, text="Typical Angina", variable=chest_pain_var, value=0,
                                           style='Wild.TRadiobutton')
chest_pain_atypical_radio = ttk.Radiobutton(form_frame, text="Atypical Angina", variable=chest_pain_var, value=1,
                                            style='Wild.TRadiobutton')
chest_pain_non_anginal_radio = ttk.Radiobutton(form_frame, text="Non-anginal Pain", variable=chest_pain_var, value=2,
                                               style='Wild.TRadiobutton')
chest_pain_asymptomatic_radio = ttk.Radiobutton(form_frame, text="Asymptomatic", variable=chest_pain_var, value=3,
                                                style='Wild.TRadiobutton')
chest_pain_typical_radio.grid(row=2, column=1, sticky="w")
chest_pain_atypical_radio.grid(row=2, column=2, sticky="w")
chest_pain_non_anginal_radio.grid(row=2, column=3, sticky="w")
chest_pain_asymptomatic_radio.grid(row=2, column=4, sticky="w")
chest_pain_var.set(None)  # Set to None initially

# Resting Blood Pressure
trestbps_label = ttk.Label(form_frame, text="Blood Pressure :", style="Custom.TLabel")
trestbps_label.grid(row=3, column=0, sticky="w")
trestbps_entry = ttk.Entry(form_frame, font=("poppins", 12))
trestbps_entry.grid(row=3, column=1)

# Serum Cholesterol
chol_label = ttk.Label(form_frame, text="Cholesterol(mg/dl) :", style="Custom.TLabel")
chol_label.grid(row=4, column=0, sticky="w")
chol_entry = ttk.Entry(form_frame, font=("poppins", 12))
chol_entry.grid(row=4, column=1)

# Fasting Blood Sugar
fbs_label = ttk.Label(form_frame, text="Fasting Blood Sugar > 120 mg/dl:", style="Custom.TLabel")
fbs_label.grid(row=5, column=0, sticky="w")
fbs_var = tk.IntVar()
fbs_yes_radio = ttk.Radiobutton(form_frame, text="Yes", variable=fbs_var, value=1, style='Wild.TRadiobutton')
fbs_no_radio = ttk.Radiobutton(form_frame, text="No", variable=fbs_var, value=0, style='Wild.TRadiobutton')
fbs_yes_radio.grid(row=5, column=1, sticky="w")
fbs_no_radio.grid(row=5, column=2, sticky="w")
fbs_var.set(None)  # Set to None initially

# Resting Electrocardiographic Results
restecg_label = ttk.Label(form_frame, text="Electrocardiographic Results :", style="Custom.TLabel")
restecg_label.grid(row=6, column=0, sticky="w")
restecg_var = tk.IntVar()
restecg_normal_radio = ttk.Radiobutton(form_frame, text="Normal", variable=restecg_var, value=0,
                                       style='Wild.TRadiobutton')
restecg_stt_radio = ttk.Radiobutton(form_frame, text="ST-T Abnormality", variable=restecg_var, value=1,
                                    style='Wild.TRadiobutton')
restecg_probable_radio = ttk.Radiobutton(form_frame, text="Ventricular Hypertrophy", variable=restecg_var, value=2,
                                         style='Wild.TRadiobutton')
restecg_normal_radio.grid(row=6, column=1, sticky="w")
restecg_stt_radio.grid(row=6, column=2, sticky="w")
restecg_probable_radio.grid(row=6, column=3, sticky="w")
restecg_var.set(None)  # Set to None initially

# Maximum Heart Rate Achieved
thalach_label = ttk.Label(form_frame, text="Maximum Heart Rate :", style="Custom.TLabel")
thalach_label.grid(row=7, column=0, sticky="w")
thalach_entry = ttk.Entry(form_frame, font=("poppins", 12))
thalach_entry.grid(row=7, column=1)

# Exercise Induced Angina
exang_label = ttk.Label(form_frame, text="Exercise Induced Angina:", style="Custom.TLabel")
exang_label.grid(row=8, column=0, sticky="w")
exang_var = tk.IntVar()
exang_yes_radio = ttk.Radiobutton(form_frame, text="Yes", variable=exang_var, value=1, style='Wild.TRadiobutton')
exang_no_radio = ttk.Radiobutton(form_frame, text="No", variable=exang_var, value=0, style='Wild.TRadiobutton')
exang_yes_radio.grid(row=8, column=1, sticky="w")
exang_no_radio.grid(row=8, column=2, sticky="w")
exang_var.set(None)  # Set to None initially

# Oldpeak
oldpeak_label = ttk.Label(form_frame, text="ST Graph (Exercise Relative to Rest):", style="Custom.TLabel")
oldpeak_label.grid(row=9, column=0, sticky="w")
oldpeak_entry = ttk.Entry(form_frame, font=("poppins", 12))
oldpeak_entry.grid(row=9, column=1)

# Slope
slope_label = ttk.Label(form_frame, text="Slope of the Peak Exercise ST:", style="Custom.TLabel")
slope_label.grid(row=10, column=0, sticky="w")
slope_var = tk.IntVar()
slope_up_radio = ttk.Radiobutton(form_frame, text="Upsloping", variable=slope_var, value=0, style='Wild.TRadiobutton')
slope_flat_radio = ttk.Radiobutton(form_frame, text="Flat", variable=slope_var, value=1, style='Wild.TRadiobutton')
slope_down_radio = ttk.Radiobutton(form_frame, text="Downsloping", variable=slope_var, value=2,
                                   style='Wild.TRadiobutton')
slope_up_radio.grid(row=10, column=1, sticky="w")
slope_flat_radio.grid(row=10, column=2, sticky="w")
slope_down_radio.grid(row=10, column=3, sticky="w")
slope_var.set(None)  # Set to None initially

# Number of Major Vessels Colored by Fluoroscopy
ca_label = ttk.Label(form_frame, text="No. of Major Vessels (Fluoroscopy):", style="Custom.TLabel")
ca_label.grid(row=11, column=0, sticky="w")
ca_entry = ttk.Entry(form_frame, font=("poppins", 12))
ca_entry.grid(row=11, column=1)

# Thalasemmia
thal_label = ttk.Label(form_frame, text="Thalassemia :", style="Custom.TLabel")
thal_label.grid(row=12, column=0, sticky="w")
thal_var = tk.IntVar()
thal_null_radio = ttk.Radiobutton(form_frame, text="Null", variable=thal_var, value=0, style='Wild.TRadiobutton')
thal_normal_radio = ttk.Radiobutton(form_frame, text="Normal", variable=thal_var, value=1, style='Wild.TRadiobutton')
thal_fixed_radio = ttk.Radiobutton(form_frame, text="Fixed Defect", variable=thal_var, value=2,
                                   style='Wild.TRadiobutton')
thal_reversible_radio = ttk.Radiobutton(form_frame, text="Reversible Defect", variable=thal_var, value=3,
                                        style='Wild.TRadiobutton')
thal_null_radio.grid(row=12, column=1, sticky="w")
thal_normal_radio.grid(row=12, column=2, sticky="w")
thal_fixed_radio.grid(row=12, column=3, sticky="w")
thal_reversible_radio.grid(row=12, column=4, sticky="w")
thal_var.set(None)  # Set to None initially

# Predict button
predict_button = ttk.Button(app_frame, text="Predict", style='Custom.TButton', command=predict)
predict_button.pack(pady=10)

# Prediction result label
result_label = ttk.Label(app_frame, text="", background="#d1e8ff", width=40, font=("poppins", 20), anchor=CENTER)
result_label.pack(pady=10)

# Buttons frame
buttons_frame = ttk.Frame(app_frame, style="Custom.TFrame")
buttons_frame.pack(pady=10)

# Style configuration to set the background color
root.style = ttk.Style()
root.style.configure("Custom.TFrame", background="#d1e8ff")

# Reset button
reset_button = ttk.Button(buttons_frame, text="Predict Another", style='Custom.TButton', command=reset_form)
reset_button.pack(side="left", padx=5)

# Quit button
quit_button = ttk.Button(buttons_frame, text="Quit", style='Custom.TButton', command=root.quit)
quit_button.pack(side="left", padx=5)

root.mainloop()
