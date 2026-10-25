from datetime import datetime, timedelta
import pandas as pd
import streamlit as st

# Judul Web
st.title("💰 Simulasi Cash Flow 30 Hari")
st.write(
    "Aplikasi web sederhana untuk menghitung estimasi pengeluaran harian dan"
    " weekend."
)

# Sidebar untuk Pengaturan Anggaran
st.sidebar.header("Pengaturan Anggaran")
makan_siang = st.sidebar.number_input(
    "Makan Siang (Rp)", value=25000, step=5000
)
makan_malam = st.sidebar.number_input(
    "Makan Malam (Rp)", value=30000, step=5000
)
pengeluaran_tetap = st.sidebar.number_input(
    "Pengeluaran Tetap Harian (Rp)", value=10000, step=2000
)
dana_weekend = st.sidebar.number_input(
    "Alokasi Dana Weekend (Rp)", value=75000, step=10000
)

# Tombol Simulasi
if st.button("Generate Simulasi 30 Hari"):
  start_date = datetime.now()
  data = []

  for i in range(30):
    current_date = start_date + timedelta(days=i)
    tanggal_str = current_date.strftime("%Y-%m-%d")
    is_weekend = current_date.weekday() >= 5  # Sabtu / Minggu

    # Masukkan pengeluaran rutin
    data.append({
        "Tanggal": tanggal_str,
        "Kategori": "Makan Siang",
        "Nominal": makan_siang,
    })
    data.append({
        "Tanggal": tanggal_str,
        "Kategori": "Makan Malam",
        "Nominal": makan_malam,
    })
    data.append({
        "Tanggal": tanggal_str,
        "Kategori": "Tetap Harian",
        "Nominal": pengeluaran_tetap,
    })

    if is_weekend:
      data.append({
          "Tanggal": tanggal_str,
          "Kategori": "Dana Weekend",
          "Nominal": dana_weekend,
      })

  df = pd.DataFrame(data)

  # Hitung Total
  total_pengeluaran = df["Nominal"].sum()

  st.success(
      f"Simulasi Berhasil! Total estimasi pengeluaran 30 hari: Rp"
      f" {total_pengeluaran:,.0f}"
  )

  # Tampilkan Tabel
  st.dataframe(df, use_container_width=True)

  # Tampilkan Grafik Pengeluaran per Kategori
  st.subheader("Grafik Pengeluaran Berdasarkan Kategori")
  chart_data = df.groupby("Kategori")["Nominal"].sum()
  st.bar_chart(chart_data)
