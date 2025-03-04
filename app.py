import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# 🌟 Басты тақырып
st.title("📌 Координаталық жазықтықтағы нүктенің қозғалысы")

# 📝 Пайдаланушыдан x және y координаталарын енгізуін сұрау
x_target = st.number_input("➡️ x координатасын енгізіңіз:", value=0)
y_target = st.number_input("⬆️ y координатасын енгізіңіз:", value=0)

# 🏃‍♂️ Анимация панелі
graph_area = st.empty()

# 🔵 Нүктенің бастапқы орны (0,0)
x_start, y_start = 0, 0

# 📊 Графикті салып, жаңарту
fig, ax = plt.subplots()
ax.axhline(0, color='black', linewidth=1)  # x осі
ax.axvline(0, color='black', linewidth=1)  # y осі
ax.grid(True, linestyle="--", alpha=0.5)
sc = ax.scatter(x_start, y_start, color="red", s=100, label="Нүкте")
ax.legend()

graph_area.pyplot(fig)  # Алғашқы график

# 🏃‍♂️ Нүктені (0,0) бастап x_target, y_target координатасына баяу жылжыту
frames = 20  # Қанша қадамда жететіні
for i in range(1, frames + 1):
    new_x = x_start + (x_target - x_start) * (i / frames)
    new_y = y_start + (y_target - y_start) * (i / frames)
    
    sc.set_offsets([new_x, new_y])  # Нүктенің жаңа орны
    
    graph_area.pyplot(fig)  # Графикті жаңарту
    time.sleep(0.1)  # Анимация жылдамдығы (секунд)

# ✅ Соңғы координатаны көрсету
st.success(f"🔴 Нүкте ({x_target}, {y_target}) координатасына жетті!")
