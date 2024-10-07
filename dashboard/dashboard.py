import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np
from babel.numbers import format_currency
sns.set(style='dark')

bike_sepeda = pd.read_csv("sepeda.csv")

st.title("Bike Sharing Dataset")


# container 1 berisi rata-rata cnt tiap season
with st.container():

    st.subheader("1. Rata-rata Penyewa Sepeda di setiap Season")
    st.write(""" Sebelum melihat visual dari data, keterangan berikut akan membantu Anda memahami visual dari data. Berikut ini adalah keterangan season: """)
    st.markdown("""
            - **Season 1** = Springer
            - **Season 2** = Summer
            - **Season 3** = Fall
            - **Season 4** = Winter
            """)
    st.write("""Untuk lebih jelas mengenai spesifik angka rata-rata penyewa tiap season, Anda dapat melihat pada keterangan dibawah ini: """)
    st.markdown("""
            - **Season 1** = 2604.13 
            - **Season 2** = 4992.33 
            - **Season 3** = 5644.3
            - **Season 4** = 4728.16 
            """)
    st.write("Dibawah ini merupakan visual dari data rata-rata penyewa sepeda pada setiap season.")

    def create_mean_renter_df(df):
        mean_renter_df = df.groupby("season").agg({"cnt":"mean"})
        return mean_renter_df

    def plot_mean_renter_bar_chart(mean_renter_df):
        fig, ax = plt.subplots(figsize=(10, 6))
        mean_renter_df.plot(kind="bar", ax=ax)
        ax.set_title("rata-rata penyewa tiap season")
        ax.set_xlabel("season")
        ax.set_ylabel("jumlah penyewa")
        ax.set_xticks(range(len(mean_renter_df)))
        ax.set_xticklabels(mean_renter_df.index, rotation=0)
        st.pyplot(fig)
    mean_renter_df = create_mean_renter_df(bike_sepeda)
    plot_mean_renter_bar_chart(mean_renter_df)

    st.write(""" Dapat disimpulkan dari grafik batang diatas bahwa jumlah rata-rata penyewa sepeda paling banyak ada
             disaat Season ke-3 (fall) dengan jumlah rata-rata penyewa sebanyak 5644.3.
             Dan penyewa paling sedikit ada pada season ke-1 (springer) dengan jumlah rata-rata penyewa sebanyak 2604.13. 
            """)
    

# container 2 berisi penyewa kasual dan penyewa registered tiap season
with st.container():

    st.subheader("2. Penyewa Casual dan Penyewa Registered Sepeda di setiap Season")
    st.write("""  Grafik batang dibawah akan memvisualkan penyewa casual dan penyewa registered pada setiap season.
             Untuk lebih jelas mengenai spesifik angka penyewa casual dan penyewa registered setiap season, Anda dapat melihat pada keterangan dibawah ini: """)
    st.markdown("""
        - season 1:
            - casual = 60622
            - registered = 410726
        - season 2:
            - casual = 203522
            - registered = 715067
        - season 3:
            - casual = 226091
            - registered = 835038
        - season 4:
            - casual = 129782
            - registered = 711831
            """)
    st.write("Dibawah ini merupakan visual dari data penyewa casual dan penyewa registered sepeda pada setiap season.")

    def create_cnt1_season_df(df):
        cnt1_season_df = df.groupby("season").agg({"casual":"sum", "registered":"sum"})
        return cnt1_season_df

    def plot_cnt1_season_bar_chart(cnt1_season_df):
        fig, ax = plt.subplots(figsize=(10, 6))
        cnt1_season_df.plot(kind="bar", ax=ax)
        ax.set_title("penyewa casual dan penyewa registered tiap season")
        ax.set_xlabel("season")
        ax.set_ylabel("jumlah penyewa")
        ax.set_xticks(range(len(cnt1_season_df)))
        ax.set_xticklabels(cnt1_season_df.index, rotation=0)
        st.pyplot(fig)
    cnt1_season_df = create_cnt1_season_df(bike_sepeda)
    plot_cnt1_season_bar_chart(cnt1_season_df)

    st.write(""" Dapat disimpulkan dari grafik batang diatas bahwa penyewa casual dan penyewa registered sepeda paling banyak ada
             disaat Season ke-3 (fall) dengan jumlah penyewa casual sebanyak 226091 dan penyewa registered sebanyak 835038.
             Sedangkan penyewa casual dan penyewa registered paling sedikit ada pada season ke-1 (springer) dengan jumlah penyewa casual sebanyak 60622 dan penyewa registered sebanyak 410726.""")


# container ke 3 berisi total casual dan registered berdasarkan season
with st.container():

    st.subheader("3. Seluruh Penyewa Sepeda di setiap Season")
    st.write(""" Grafik batang dibawah akan memvisualisasikan penyewa casual dan penyewa registered pada setiap
             season. Untuk mengetahui angka spesifik dari seluruh penyewa sepeda di setiap seasonnya, Anda dapat melihat
             pada keterangan dibawah ini: """)
    st.markdown("""
            - **Season 1** = 471348
            - **Season 2** = 918589
            - **Season 3** = 1061129
            - **Season 4** = 841613
            """)

    st.write("""  Dibawah ini merupakan data rata-rata penyewa sepeda pada setiap season.""")
    st.caption("_note: 1e6 adalah notasi ilmiah yang berarti 1 x 1.000.000 (satu juta)_")
    def create_cnt2_season_df(df):
        cnt2_season_df = df.groupby("season").agg({"cnt":"sum"})
        return cnt2_season_df

    def plot_cnt2_season_bar_chart(cnt2_season_df):
        fig, ax = plt.subplots(figsize=(10, 6))
        cnt2_season_df.plot(kind="bar", ax=ax)
        ax.set_title("penyewa casual dan penyewa registered tiap season")
        ax.set_xlabel("season")
        ax.set_ylabel("jumlah penyewa")
        ax.set_xticks(range(len(cnt2_season_df)))
        ax.set_xticklabels(cnt2_season_df.index, rotation=0)
        st.pyplot(fig)
    cnt2_season_df = create_cnt2_season_df(bike_sepeda)
    plot_cnt2_season_bar_chart(cnt2_season_df)

    st.write(""" Dapat disimpulkan dari grafik batang diatas bahwa total dari penyewa casual dan penyewa registered sepeda paling banyak ternyata masih sama,
             yaitu disaat Season ke-3 (fall) dengan jumlah keseluruhan penyewa sepeda sebanyak 1061129.
             Sedangkan jumlah kesulurah penyewa sepeda paling sedikit ada pada season ke-1 (springer) dengan jumlah kesuluran penyewa sepeda sebanyak 841613.""")











# container 4 berisi rata-rata cnt tiap weathersit
with st.container():

    st.subheader("4. Rata-rata Penyewa Sepeda di setiap weathersit")
    st.write(""" Sebelum melihat visual dari data, keterangan berikut akan membantu Anda memahami visual dari data. Berikut ini adalah keterangan weathersit: """)
    st.markdown("""
            - **weathersit 1** = Clear, Few clouds, Partly cloudy, Partly cloudy
            - **weathersit 2** = Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
            - **weathersit 3** = Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
            - **weathersit 4** = Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog

            """)
    st.write("""Untuk lebih jelas mengenai spesifik angka rata-rata penyewa tiap weathersit, Anda dapat melihat pada keterangan dibawah ini: """)
    st.markdown("""
            - weathersit 1 = 4876.78
            - weathersit 2 = 4035.86
            - weathersit 3 = *tidak ada data penyewa saat weathersit 3*
            - weathersit 4 = 1803.28
            """)
    st.write("Dibawah ini merupakan visual dari data rata-rata penyewa sepeda pada setiap weathersit. Karena tidak ada data penyewa pada weathersit 3 maka tidak ada titik 3 pada grafik batang.")

    def create_mean_renter_df(df):
        mean_renter_df = df.groupby("weathersit").agg({"cnt":"mean"})
        return mean_renter_df

    def plot_mean_renter_bar_chart(mean_renter_df):
        fig, ax = plt.subplots(figsize=(10, 6))
        mean_renter_df.plot(kind="bar", ax=ax)
        ax.set_title("rata-rata penyewa tiap weathersit")
        ax.set_xlabel("weathersit")
        ax.set_ylabel("jumlah penyewa")
        ax.set_xticks(range(len(mean_renter_df)))
        ax.set_xticklabels(mean_renter_df.index, rotation=0)
        st.pyplot(fig)
    mean_renter_df = create_mean_renter_df(bike_sepeda)
    plot_mean_renter_bar_chart(mean_renter_df)

    st.write(""" Dapat disimpulkan dari grafik batang diatas bahwa jumlah rata-rata penyewa sepeda paling banyak ada
             disaat weathersit ke-1 (Clear, Few clouds, Partly cloudy, Partly cloudy) dengan jumlah rata-rata penyewa sebanyak 4876.78.
             Dan penyewa paling sedikit ada pada weathersit ke-4 (Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog) dengan jumlah rata-rata penyewa sebanyak 1803.28. 
            """)
    

# container 5 berisi penyewa kasual dan penyewa registered tiap weathersit
with st.container():

    st.subheader("5. Penyewa Casual dan Penyewa Registered Sepeda di setiap weathersit")
    st.write("""  Grafik batang dibawah akan memvisualkan penyewa casual dan penyewa registered pada setiap weathersit.
             Untuk lebih jelas mengenai spesifik angka penyewa casual dan penyewa registered setiap weathersit, Anda dapat melihat pada keterangan dibawah ini: """)
    st.markdown("""
        - weathersit 1:
            - casual = 446346
            - registered = 1811606
        - weathersit 2:
            - casual = 169776
            - registered = 827082
        - weathersit 3:
            - casual = *tidak ada data penyewa saat weathersit 3*
            - registered = *tidak ada data penyewa saat weathersit 3*
        - weathersit 4:
            - casual = 3895
            - registered = 33974
            """)
    st.write("Dibawah ini merupakan visual dari data penyewa casual dan penyewa registered sepeda pada setiap weathersit. Karena tidak ada data penyewa pada weathersit 3 maka tidak ada titik 3 pada grafik batang.")
    st.caption("_note: 1e6 adalah notasi ilmiah yang berarti 1 x 1.000.000 (satu juta)_")

    def create_cnt1_weathersit_df(df):
        cnt1_weathersit_df = df.groupby("weathersit").agg({"casual":"sum", "registered":"sum"})
        return cnt1_weathersit_df

    def plot_cnt1_weathersit_bar_chart(cnt1_weathersit_df):
        fig, ax = plt.subplots(figsize=(10, 6))
        cnt1_weathersit_df.plot(kind="bar", ax=ax)
        ax.set_title("penyewa casual dan penyewa registered tiap weathersit")
        ax.set_xlabel("weathersit")
        ax.set_ylabel("jumlah penyewa")
        ax.set_xticks(range(len(cnt1_weathersit_df)))
        ax.set_xticklabels(cnt1_weathersit_df.index, rotation=0)
        st.pyplot(fig)
    cnt1_weathersit_df = create_cnt1_weathersit_df(bike_sepeda)
    plot_cnt1_weathersit_bar_chart(cnt1_weathersit_df)

    st.write(""" Dapat disimpulkan dari grafik batang diatas bahwa penyewa casual dan penyewa registered sepeda paling banyak ada
             disaat weathersit ke-1 (Clear, Few clouds, Partly cloudy, Partly cloudy) dengan jumlah penyewa casual sebanyak 446346 dan penyewa registered sebanyak 1811606.
             Sedangkan penyewa casual dan penyewa registered paling sedikit ada pada weathersit ke-4 (Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog) dengan jumlah penyewa casual sebanyak 3895 dan penyewa registered sebanyak 33974.""")


# container ke 6 berisi total casual dan registered berdasarkan weathersit
with st.container():

    st.subheader("6. Seluruh Penyewa Sepeda di setiap weathersit")
    st.write(""" Grafik batang dibawah akan memvisualisasikan penyewa casual dan penyewa registered pada setiap
             weathersit. Untuk mengetahui angka spesifik dari seluruh penyewa sepeda di setiap weathersitnya, Anda dapat melihat
             pada keterangan dibawah ini: """)
    st.markdown("""
            - **weathersit 1** = 2257952
            - **weathersit 2** = 996858
            - **weathersit 3** = *tidak ada data penyewa saat weathersit 3*
            - **weathersit 4** = 37869
            """)

    st.write("""  Dibawah ini merupakan data rata-rata penyewa sepeda pada setiap weathersit. Karena tidak ada data penyewa pada weathersit 3 maka tidak ada titik 3 pada grafik batang.""")
    st.caption("_note: 1e6 adalah notasi ilmiah yang berarti 1 x 1.000.000 (satu juta)_")

    def create_cnt2_weathersit_df(df):
        cnt2_weathersit_df = df.groupby("weathersit").agg({"cnt":"sum"})
        return cnt2_weathersit_df

    def plot_cnt2_weathersit_bar_chart(cnt2_weathersit_df):
        fig, ax = plt.subplots(figsize=(10, 6))
        cnt2_weathersit_df.plot(kind="bar", ax=ax)
        ax.set_title("penyewa casual dan penyewa registered tiap weathersit")
        ax.set_xlabel("weathersit")
        ax.set_ylabel("jumlah penyewa")
        ax.set_xticks(range(len(cnt2_weathersit_df)))
        ax.set_xticklabels(cnt2_weathersit_df.index, rotation=0)
        st.pyplot(fig)
    cnt2_weathersit_df = create_cnt2_weathersit_df(bike_sepeda)
    plot_cnt2_weathersit_bar_chart(cnt2_weathersit_df)

    st.write(""" Dapat disimpulkan dari grafik batang diatas bahwa total dari penyewa casual dan penyewa registered sepeda paling banyak ternyata masih sama,
             yaitu disaat weathersit ke-1 (Clear, Few clouds, Partly cloudy, Partly cloudy) dengan jumlah keseluruhan penyewa sepeda sebanyak 2257952.
             Sedangkan jumlah kesulurah penyewa sepeda paling sedikit ada pada weathersit ke-4 (Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog) dengan jumlah kesuluran penyewa sepeda sebanyak 37869.""")









