import streamlit as st
from pymongo import MongoClient
from streamlit_extras.card import card
from streamlit_extras.stoggle import stoggle

# Koneksi ke MongoDB Atlas
client = MongoClient("mongodb+srv://nabielfauzanti23:FK1BUAaeOUAKDzXK@clusterbdnabiel.pf6x7.mongodb.net/?retryWrites=true&w=majority&appName=ClusterBDNabiel")
db = client["TokoOnline"] 
collectionA = db["KatalogElektronik"]  
collectionB = db["KatalogPakaian"] 

st.markdown("<h1 style='color: orange;'># 💻 Selamat Datang Di TokoOnline Kelompok 1</h1>", unsafe_allow_html=True)
st.markdown("### 👥 Anggota Kelompok:")
st.write("- Nabiel Fauzan (20230040222)")
st.write("- Rizky Fadillah (20230040083)")
st.write("- Ilham Adi Muslim (20230040156)")
st.write("- Muhammad Khaifan")

st.divider()

# Form Input Produk Elektronik
# Form Input Produk
st.markdown("<h1 style='color: green;'>Tambah / Update Stok Produk Elektronik</h1>", unsafe_allow_html=True)
with st.form("form_tambah_produk_elektronik"):
    nama_produk = st.text_input("Nama Produk")
    harga = st.number_input("Harga", min_value=0)
    stok_tambah = st.number_input("Tambah Stok", min_value=0)

    with st.expander("Spesifikasi (Opsional)"):
        ram = st.text_input("RAM")
        processor = st.text_input("Processor")
        storage = st.text_input("Storage")

    # Tombol Simpan
    submit = st.form_submit_button("Simpan")

    if submit:
        if nama_produk and harga > 0 and stok_tambah >= 0:
            # Cek apakah produk sudah ada di database
            existing_product = collectionA.find_one({"nama": nama_produk})

            spesifikasi = {
                "RAM": ram,
                "Processor": processor,
                "Storage": storage
            }

            if existing_product:
                # Jika produk sudah ada, update stok
                new_stok = existing_product["stok"] + stok_tambah
                collectionA.update_one(
                    {"nama": nama_produk},
                    {"$set": {"stok": new_stok, "harga": harga, }}
                )
                st.success(f"✅ Stok produk '{nama_produk}' berhasil ditambahkan! Stok sekarang: {new_stok}")
            else:
                # Jika produk belum ada, tambahkan baru
                data_produk = {
                    "Brand": nama_produk,
                    "harga": harga,
                    "stok": stok_tambah,
                    "Spesifikasi": spesifikasi
                }
                collectionA.insert_one(data_produk)
                st.success(f"✅ Produk baru '{nama_produk}' berhasil ditambahkan!")

        else:
            st.error("❌ Mohon isi semua data dengan benar!")


st.markdown("<h1 style='color: yellow;'>Tambah / Update Stok Produk Pakaian</h1>", unsafe_allow_html=True)
with st.form("form_tambah_produk_pakaian"):
    nama_produk = st.text_input("Nama Brand")
    jenis_produk = st.selectbox("Jenis ", ["Celana", "Kaos", "Kameja", "jaket"])
    size_produk = st.selectbox("Size ", ["S", "M", "L", "XL"])  
    Bahan_produk = st.text_input("Bahan")
    harga = st.number_input("Harga", min_value=0)
    stok_tambah = st.number_input("Tambah Stok", min_value=0)

    # Tombol Simpan
    submit = st.form_submit_button("Simpan")

    if submit:
        if nama_produk and harga > 0 and stok_tambah >= 0:
            # Cek apakah produk sudah ada di database
            existing_product = collectionB.find_one({"nama": nama_produk})

            if existing_product:
                # Jika produk sudah ada, update stok
                new_stok = existing_product["stok"] + stok_tambah
                collectionB.update_one(
                    {"nama": nama_produk},
                    {"$set": {"stok": new_stok, "harga": harga,}}
                )
                st.success(f"✅ Stok produk '{nama_produk}' berhasil ditambahkan! Stok sekarang: {new_stok}")
            else:
                # Jika produk belum ada, tambahkan baru
                data_produk = {
                    "Brand": nama_produk,
                    "Size": size_produk,
                    "Jenis": jenis_produk,
                    "Harga": harga,
                    "Bahan": Bahan_produk,
                    "stok": stok_tambah,
                }
                collectionB.insert_one(data_produk)
                st.success(f"✅ Produk baru '{nama_produk}' berhasil ditambahkan!")

        else:
            st.error("❌ Mohon isi semua data dengan benar!")