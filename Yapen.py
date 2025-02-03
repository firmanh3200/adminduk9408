import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Adminduk 9408', layout='wide')

with st.container(border=True):
    with st.container(border=True):
        st.title(':blue[Administrasi Kependudukan] :green[Kepulauan Yapen] :orange[Semester 1 2024]')
        st.caption('Sumber: https://gis.dukcapil.kemendagri.go.id/peta/')

st.subheader('', divider='orange')

from data import datapenduduk
penduduk2 = datapenduduk.groupby(['Kabupaten/Kota', 'Kecamatan'])['Jumlah Penduduk'].sum().reset_index()
keluarga = datapenduduk.groupby(['Kabupaten/Kota', 'Kecamatan'])['Jumlah Kepala Keluarga'].sum().reset_index()

with st.container(border=True):
    st.subheader(f'Jumlah Penduduk')
    kol1a, kol1b = st.columns(2)
    with kol1a:
        with st.container(border=True):
            penduduk3 = penduduk2.sort_values(by='Jumlah Penduduk', ascending=False)
            bar_penduduk = px.bar(penduduk3, x='Jumlah Penduduk', y='Kecamatan')
            st.plotly_chart(bar_penduduk, use_container_width=True)
    
    with kol1b:
        with st.container(border=True):
            pie_penduduk = px.pie(penduduk3, values='Jumlah Penduduk', color='Kecamatan')
            st.plotly_chart(pie_penduduk, use_container_width=True)
            
    with st.expander('Unduh Tabel'):
        st.dataframe(penduduk3, hide_index=True, use_container_width=True)

st.subheader('', divider='orange')

with st.container(border=True):
    st.subheader(f'Jumlah KK')
    kol2a, kol2b = st.columns(2)
    with kol2a:
        with st.container(border=True):
            keluarga2 = keluarga.sort_values(by='Jumlah Kepala Keluarga', ascending=False)
            bar_keluarga = px.bar(keluarga2, x='Jumlah Kepala Keluarga', y='Kecamatan')
            st.plotly_chart(bar_keluarga, use_container_width=True)
    
    with kol2b:
        with st.container(border=True):
            pie_keluarga = px.pie(keluarga2, values='Jumlah Kepala Keluarga', color='Kecamatan')
            st.plotly_chart(pie_keluarga, use_container_width=True)
            
    with st.expander('Unduh Tabel'):
        st.dataframe(keluarga2, hide_index=True, use_container_width=True)
        
st.subheader('', divider='orange')

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(['Jenis Kelamin', 'Status Kawin', 'Agama', 
                                                          'Kelompok Umur', 'Pendidikan', 'Golongan Darah', 
                                                          'Usia Pendidikan', 'Pekerjaan'])

with tab1:
    from data import datajeniskelamin2
    jeniskelamin3 = datajeniskelamin2.groupby(['Kabupaten/Kota', 'Kecamatan', 'Jenis Kelamin'])['Jumlah Penduduk'].sum().reset_index()
    trimep1 = px.treemap(jeniskelamin3, path=['Kabupaten/Kota', 'Kecamatan', 'Jenis Kelamin'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep1, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(jeniskelamin3, hide_index=True, use_container_width=True)

with tab2:
    from data import datastatuskawin2
    statuskawin = datastatuskawin2.groupby(['Kabupaten/Kota', 'Kecamatan', 'Status Kawin'])['Jumlah Penduduk'].sum().reset_index()
    trimep2 = px.treemap(statuskawin, path=['Kabupaten/Kota', 'Kecamatan', 'Status Kawin'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep2, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(statuskawin, hide_index=True, use_container_width=True)
            
with tab3:
    from data import dataagama2
    agama = dataagama2.groupby(['Kabupaten/Kota', 'Kecamatan', 'Agama'])['Jumlah Penduduk'].sum().reset_index()
    trimep3 = px.treemap(agama, path=['Kabupaten/Kota', 'Kecamatan', 'Agama'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep3, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(agama, hide_index=True, use_container_width=True)
            
with tab4:
    from data import dataumur2
    umur = dataumur2.groupby(['Kabupaten/Kota', 'Kecamatan', 'Kelompok Umur'])['Jumlah Penduduk'].sum().reset_index()
    trimep4 = px.treemap(umur, path=['Kabupaten/Kota', 'Kecamatan', 'Kelompok Umur'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep4, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(umur, hide_index=True, use_container_width=True)
            
with tab5:
    from data import datapendidikan2
    pendidikan = datapendidikan2.groupby(['Kabupaten/Kota', 'Kecamatan', 'Pendidikan'])['Jumlah Penduduk'].sum().reset_index()
    trimep5 = px.treemap(pendidikan, path=['Kabupaten/Kota', 'Kecamatan', 'Pendidikan'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep5, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(pendidikan, hide_index=True, use_container_width=True)
            
with tab6:
    from data import datagolongandarah2
    goldar = datagolongandarah2.groupby(['Kabupaten/Kota', 'Kecamatan', 'Golongan Darah'])['Jumlah Penduduk'].sum().reset_index()
    trimep6 = px.treemap(goldar, path=['Kabupaten/Kota', 'Kecamatan', 'Golongan Darah'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep6, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(goldar, hide_index=True, use_container_width=True)
            
with tab7:
    from data import datausiadidik2
    usia = datausiadidik2.groupby(['Kabupaten/Kota', 'Kecamatan', 'Usia Pendidikan'])['Jumlah Penduduk'].sum().reset_index()
    trimep7 = px.treemap(usia, path=['Kabupaten/Kota', 'Kecamatan', 'Usia Pendidikan'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep7, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(usia, hide_index=True, use_container_width=True)
            
with tab8:
    from data import datapekerjaan2
    pekerjaan = datapekerjaan2.groupby(['Kabupaten/Kota', 'Kecamatan', 'Pekerjaan'])['Jumlah Penduduk'].sum().reset_index()
    trimep8 = px.treemap(pekerjaan, path=['Kabupaten/Kota', 'Kecamatan', 'Pekerjaan'], values='Jumlah Penduduk')
    with st.container(border=True):
        st.plotly_chart(trimep8, use_container_width=True)
        with st.expander('Unduh Tabel'):
            st.dataframe(pekerjaan, hide_index=True, use_container_width=True)