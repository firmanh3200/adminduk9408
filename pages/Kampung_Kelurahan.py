import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Adminduk 9408', layout='wide')

with st.container(border=True):
    with st.container(border=True):
        st.title(':blue[Administrasi Kependudukan] :green[Kepulauan Yapen] :orange[Semester 1 2024]')
        st.caption('Sumber: https://gis.dukcapil.kemendagri.go.id/peta/')


from data import datapenduduk
from data import datajeniskelamin
datapenduduk = datapenduduk.sort_values(by=['Kecamatan', 'Kelurahan/Desa'])
        
with st.container(border=True):    
    kol1, kol3 = st.columns(2)
    with kol1:
        kec = datapenduduk['Kecamatan'].unique()
        kecterpilih = st.selectbox('Pilih Distrik', kec)
        
    with kol3:
        desa = datapenduduk[(datapenduduk['Kecamatan'] == kecterpilih)]['Kelurahan/Desa'].unique()
        desaterpilih = st.selectbox('Pilih Kampung/ Kelurahan', desa)

st.subheader('', divider='orange')

with st.container(border=True):
    st.subheader(f'PROFIL PENDUDUK KAMPUNG/ KELURAHAN :green[{desaterpilih}], DISTRIK :blue[{kecterpilih}]')

            
if kecterpilih and desaterpilih:
    penduduk = datapenduduk[(datapenduduk['Kecamatan'] == kecterpilih) & (datapenduduk['Kelurahan/Desa'] == desaterpilih)]
    jk = datajeniskelamin[(datajeniskelamin['Kecamatan'] == kecterpilih) & (datajeniskelamin['Kelurahan/Desa'] == desaterpilih)]
    
# METRIK
kol1a, kol1b, kol1c, kol1d = st.columns(4)
with kol1a:
    with st.container(border=True):
        with st.container(border=True):
            st.write(':blue[Penduduk]')
            st.title(f':blue[{penduduk.iloc[0,3]}]')
    
with kol1b:
    with st.container(border=True):
        with st.container(border=True):
            st.write(':green[Laki-laki]')
            st.title(f':green[{jk.iloc[0,3]}]')
            
with kol1c:
    with st.container(border=True):
        with st.container(border=True):
            st.write(':orange[Perempuan]')
            st.title(f':orange[{jk.iloc[0,4]}]')
    
with kol1d:
    with st.container(border=True):
        with st.container(border=True):
            st.write('Keluarga')
            st.title(f'{penduduk.iloc[0,4]}')
                
            
st.subheader('', divider='orange')

with st.container(border=True):
    st.subheader(f'Menurut Jenis Kelamin')
    kol2a, kol2b = st.columns(2)
    with kol2a:
        with st.container(border=True):
            from data import datajeniskelamin2
            jk2 = datajeniskelamin2[(datajeniskelamin2['Kecamatan'] == kecterpilih) & (datajeniskelamin2['Kelurahan/Desa'] == desaterpilih)]
            bar_jk = px.bar(jk2, x='Jenis Kelamin', y='Jumlah Penduduk')
            st.plotly_chart(bar_jk, use_container_width=True)
    
    with kol2b:
        with st.container(border=True):
            pie_keluarga = px.pie(jk2, values='Jumlah Penduduk', color='Jenis Kelamin')
            st.plotly_chart(pie_keluarga, use_container_width=True)
            
        
st.subheader('', divider='orange')

tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(['Status Kawin', 'Agama', 
                                              'Kelompok Umur', 'Pendidikan', 'Golongan Darah', 
                                              'Usia Pendidikan', 'Pekerjaan'])

with tab2:
    from data import datastatuskawin2
    statuskawin2 = datastatuskawin2[(datastatuskawin2['Kecamatan'] == kecterpilih) & (datastatuskawin2['Kelurahan/Desa'] == desaterpilih)]
    statuskawin2 = statuskawin2.sort_values(by='Jumlah Penduduk')
    trimep2 = px.treemap(statuskawin2, path=['Kelurahan/Desa', 'Status Kawin'], values='Jumlah Penduduk')
    bar2 = px.bar(statuskawin2, x='Status Kawin', y='Jumlah Penduduk')
    pie2 = px.pie(statuskawin2, values='Jumlah Penduduk', color='Status Kawin')
    with st.container(border=True):
        kol2c, kol2d, kol2e = st.columns(3)
        with kol2c:
            with st.container(border=True):
                st.plotly_chart(trimep2, use_container_width=True)
        with kol2d:
            with st.container(border=True):
                st.plotly_chart(pie2, use_container_width=True)
        with kol2e:
            with st.container(border=True):
                st.plotly_chart(bar2, use_container_width=True)
            
with tab3:
    from data import dataagama2
    agama = dataagama2[(dataagama2['Kecamatan'] == kecterpilih) & (dataagama2['Kelurahan/Desa'] == desaterpilih)]
    trimep3 = px.treemap(agama, path=['Kelurahan/Desa', 'Agama'], values='Jumlah Penduduk')
    bar3 = px.bar(agama, x='Agama', y='Jumlah Penduduk')
    pie3 = px.pie(agama, values='Jumlah Penduduk', color='Agama')
    with st.container(border=True):
        kol3c, kol3d, kol3e = st.columns(3)
        with kol3c:
            with st.container(border=True):
                st.plotly_chart(trimep3, use_container_width=True)
        with kol3d:
            with st.container(border=True):
                st.plotly_chart(pie3, use_container_width=True)
        with kol3e:
            with st.container(border=True):
                st.plotly_chart(bar3, use_container_width=True)
            
with tab4:
    from data import dataumur2
    umur = dataumur2[(dataumur2['Kecamatan'] == kecterpilih) & (dataumur2['Kelurahan/Desa'] == desaterpilih)]
    trimep4 = px.treemap(umur, path=['Kelurahan/Desa', 'Kelompok Umur'], values='Jumlah Penduduk')
    bar4 = px.bar(umur, x='Jumlah Penduduk', y='Kelompok Umur')
    pie4 = px.pie(umur, values='Jumlah Penduduk', color='Kelompok Umur')
    with st.container(border=True):
        kol4c, kol4d, kol4e = st.columns(3)
        with kol4c:
            with st.container(border=True):
                st.plotly_chart(trimep4, use_container_width=True)
        with kol4d:
            with st.container(border=True):
                st.plotly_chart(pie4, use_container_width=True)
        with kol4e:
            with st.container(border=True):
                st.plotly_chart(bar4, use_container_width=True)
            
with tab5:
    from data import datapendidikan2
    pendidikan = datapendidikan2[(datapendidikan2['Kecamatan'] == kecterpilih) & (datapendidikan2['Kelurahan/Desa'] == desaterpilih)]
    pendidikan = pendidikan.sort_values(by='Jumlah Penduduk')
    trimep5 = px.treemap(pendidikan, path=['Kelurahan/Desa', 'Pendidikan'], values='Jumlah Penduduk')
    bar5 = px.bar(pendidikan, x='Jumlah Penduduk', y='Pendidikan')
    pie5 = px.pie(pendidikan, values='Jumlah Penduduk', color='Pendidikan')
    with st.container(border=True):
        kol4c, kol4d, kol4e = st.columns(3)
        with kol4c:
            with st.container(border=True):
                st.plotly_chart(trimep5, use_container_width=True)
        with kol4d:
            with st.container(border=True):
                st.plotly_chart(pie5, use_container_width=True)
        with kol4e:
            with st.container(border=True):
                st.plotly_chart(bar5, use_container_width=True)
            
with tab6:
    from data import datagolongandarah2
    goldar = datagolongandarah2[(datagolongandarah2['Kecamatan'] == kecterpilih) & (datagolongandarah2['Kelurahan/Desa'] == desaterpilih)]
    goldar = goldar.sort_values(by='Jumlah Penduduk')
    trimep6 = px.treemap(goldar, path=['Kelurahan/Desa', 'Golongan Darah'], values='Jumlah Penduduk')
    bar6 = px.bar(goldar, x='Jumlah Penduduk', y='Golongan Darah')
    pie6 = px.pie(goldar, values='Jumlah Penduduk', color='Golongan Darah')
    with st.container(border=True):
        kol4c, kol4d, kol4e = st.columns(3)
        with kol4c:
            with st.container(border=True):
                st.plotly_chart(trimep6, use_container_width=True)
        with kol4d:
            with st.container(border=True):
                st.plotly_chart(pie6, use_container_width=True)
        with kol4e:
            with st.container(border=True):
                st.plotly_chart(bar6, use_container_width=True)
            
with tab7:
    from data import datausiadidik2
    usia = datausiadidik2[(datausiadidik2['Kecamatan'] == kecterpilih) & (datausiadidik2['Kelurahan/Desa'] == desaterpilih)]
    trimep7 = px.treemap(usia, path=['Kelurahan/Desa', 'Usia Pendidikan'], values='Jumlah Penduduk')
    bar7 = px.bar(usia, y='Jumlah Penduduk', x='Usia Pendidikan')
    pie7 = px.pie(usia, values='Jumlah Penduduk', color='Usia Pendidikan')
    with st.container(border=True):
        kol4c, kol4d, kol4e = st.columns(3)
        with kol4c:
            with st.container(border=True):
                st.plotly_chart(trimep7, use_container_width=True)
        with kol4d:
            with st.container(border=True):
                st.plotly_chart(pie7, use_container_width=True)
        with kol4e:
            with st.container(border=True):
                st.plotly_chart(bar7, use_container_width=True)
            
with tab8:
    from data import datapekerjaan2
    pekerjaan = datapekerjaan2[(datapekerjaan2['Kecamatan'] == kecterpilih) & (datapekerjaan2['Kelurahan/Desa'] == desaterpilih)]
    pekerjaan = pekerjaan.sort_values(by='Jumlah Penduduk')
    trimep8 = px.treemap(pekerjaan, path=['Kelurahan/Desa', 'Pekerjaan'], values='Jumlah Penduduk')
    bar8 = px.bar(pekerjaan, x='Jumlah Penduduk', y='Pekerjaan')
    pie8 = px.pie(pekerjaan, values='Jumlah Penduduk', color='Pekerjaan')
    with st.container(border=True):
        kol4c, kol4d, kol4e = st.columns(3)
        with kol4c:
            with st.container(border=True):
                st.plotly_chart(trimep8, use_container_width=True)
        with kol4d:
            with st.container(border=True):
                st.plotly_chart(pie8, use_container_width=True)
        with kol4e:
            with st.container(border=True):
                st.plotly_chart(bar8, use_container_width=True)
