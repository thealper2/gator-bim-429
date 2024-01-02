import streamlit as st
import pickle
import numpy as np
import pandas as pd
import ast

st.title('Turkish TV Series Classification')

years = [i for i in range(1997, 2024)]
year = st.selectbox('Yayın tarihi:', years)

if year:
    score_df = pd.read_csv(f'./best_models/best_df.csv', index_col=0)
    score_df = score_df[score_df['Year'] == year]
    features = score_df['Selected Features'].values[0]
    model_name = score_df['Model Name'].values[0]
    st.write(model_name)

    model = pickle.load(open(f'./best_models/{year}/{model_name}.pkl', 'rb'))
    rs = pickle.load(open(f'./best_models/{year}/rs.pkl', 'rb'))
    day_encoder = pickle.load(open(f'./best_models/{year}/day_encoder.pkl', 'rb'))
    le = pickle.load(open(f'./best_models/{year}/le.pkl', 'rb'))


    features_to_models = {
        'Tarih': -2,
        'Dizi Adı Uzunluğu': -2,
        'Dizi Adındaki Kelime Sayısı': -2,
        'Dizi Adında Bağlaç': -2,
        'Dizi Adında Yer İsmi': -2,
        'Dizi Adında Özel İsim': -2,
        'Aile': -2,
        'Aksiyon': -2,
        'Aşk': -2,
        'Bilim Kurgu': -2,
        'Dram': -2,
        'Gençlik': -2,
        'Gerilim': -2,
        'Komedi': -2,
        'Polisiye': -2,
        'Romantik': -2,
        'Tarihî': -2,
        'TRT 1': -2,
        'Kanal D': -2,
        'atv': -2,
        'Star TV': -2,
        'Show TV': -2,
        'FOX': -2,
        'Samanyolu TV': -2,
        'TV8': -2,
        'in_turkey': -2,
        'out_turkey': -2,
        'book_to_movie': -2,
        'act_count': -2,
        'paid_channel': -2, 
        'Publication Day': '?',
        'summer_series': -2,
        'duration': -2,
        'Ödüllü': -2,
        'Senaristlerin Dizi Sayısı': -2,
        'Ödüllü Senarist Sayısı': -2,
        'Senaristlerin Aldığı Ödül Sayısı': -2,
        'Başrollerin Dizi Sayısı': -2,
        'Ödüllü Başrol Sayısı': -2,
        'Başrollerin Aldığı Ödül Sayısı': -2,
        'Yönetmenlerin Dizi Sayısı': -2,
        'Ödüllü Yönetmen Sayısı': -2,
        'Yönetmenlerin Aldığı Ödül Sayısı': -2,
        'Görüntü Yönetmenlerinin Dizi Sayısı': -2,
        'Yapım Şirketleri Dizi Sayısı': -2,
        'Besteci Dizi Sayısı': -2,
        'on_youtube': -2,
        'on_facebook': -2,
        'on_twitter': -2,
        'on_instagram': -2,
        'total_sm_accounts': -2,
    }

    if "'Tarih'" in features:
        features_to_models['Tarih'] = year
    if "'Dizi Adı Uzunluğu'" in features:
        features_to_models['Dizi Adı Uzunluğu'] = st.number_input('Dizi adı uzunluğu:')
    if "'Dizi Adındaki Kelime Sayısı'" in features:
        features_to_models['Dizi Adındaki Kelime Sayısı'] = st.number_input('Dizi adındaki kelime sayısı:')
    if "'Dizi Adında Bağlaç'" in features:
        features_to_models['Dizi Adında Bağlaç'] = st.number_input('Dizi adında bağlaç var mı ? (0-Hayır, 1-Evet):')
    if "'Dizi Adında Yer İsmi'" in features:
        features_to_models[''] = st.number_input('Dizi adında yer ismi var mı ? (0-Hayır, 1-Evet):')
    if "'Dizi Adında Özel İsim'" in features:
        features_to_models['Dizi Adında Özel İsim'] = st.number_input('Dizi adında özel isim var mı ? (0-Hayır, 1-Evet):')
    if "'Aile'" in features:
        features_to_models['Aile'] = st.number_input('Aile türünde mi ? (0-Hayır, 1-Evet):')
    if "'Aksiyon'" in features:
        features_to_models['Aksiyon'] = st.number_input('Aksiyon türünde mi ? (0-Hayır, 1-Evet):')
    if "'Aşk'" in features:
        features_to_models['Aşk'] = st.number_input('Aşk türünde mi ? (0-Hayır, 1-Evet):')
    if "'Bilim Kurgu'" in features:
        features_to_models['Bilim Kurgu'] = st.number_input('Bilim Kurgu türünde mi ? (0-Hayır, 1-Evet):')
    if "'Dram'" in features:
        features_to_models['Dram'] = st.number_input('Dram türünde mi ? (0-Hayır, 1-Evet):')
    if "'Gençlik'" in features:
        features_to_models['Gençlik'] = st.number_input('Gençlik türünde mi ? (0-Hayır, 1-Evet):')
    if "'Gerilim'" in features:
        features_to_models['Gerilim'] = st.number_input('Gerilim türünde mi ? (0-Hayır, 1-Evet):')
    if "'Komedi'" in features:
        features_to_models['Komedi'] = st.number_input('Komedi türünde mi ? (0-Hayır, 1-Evet):')
    if "'Polisiye'" in features:
        features_to_models['Polisiye'] = st.number_input('Polisiye türünde mi ? (0-Hayır, 1-Evet):')
    if "'Romantik'" in features:
        features_to_models['Romantik'] = st.number_input('Romantik türünde mi ? (0-Hayır, 1-Evet):')
    if "'Tarihî'" in features:
        features_to_models['Tarihî'] = st.number_input('Tarihî türünde mi ? (0-Hayır, 1-Evet):')
    if "'TRT 1'" in features:
        features_to_models['TRT 1'] = st.number_input('TRT 1  kanalında mı yayınlanıyor ? (0-Hayır, 1-Evet):')
    if "'Kanal D'" in features:
        features_to_models['Kanal D'] = st.number_input('Kanal D  kanalında mı yayınlanıyor ? (0-Hayır, 1-Evet):')
    if "'atv'" in features:
        features_to_models['atv'] = st.number_input('atv  kanalında mı yayınlanıyor ? (0-Hayır, 1-Evet):')
    if "'Star TV'" in features:
        features_to_models['Star TV'] = st.number_input('Star TV  kanalında mı yayınlanıyor ? (0-Hayır, 1-Evet):')
    if "'Show TV'" in features:
        features_to_models['Show TV'] = st.number_input('Show TV  kanalında mı yayınlanıyor ? (0-Hayır, 1-Evet):')
    if "'FOX'" in features:
        features_to_models['FOX'] = st.number_input('FOX  kanalında mı yayınlanıyor ? (0-Hayır, 1-Evet):')
    if "'Samanyolu TV'" in features:
        features_to_models['Samanyolu TV'] = st.number_input('Samanyolu TV  kanalında mı yayınlanıyor ? (0-Hayır, 1-Evet):')
    if "'TV8'" in features:
        features_to_models['TV8'] = st.number_input('TV8  kanalında mı yayınlanıyor ? (0-Hayır, 1-Evet):')
    if "'in_turkey'" in features:
        features_to_models['in_turkey'] = st.number_input('Türkiyede mi çekildi ? (0-Hayır, 1-Evet):')
    if "'out_turkey'" in features:
        features_to_models['out_turkey'] = st.number_input('Yurtdışında mı çekildi ? (0-Hayır, 1-Evet):')
    if "'book_to_movie'" in features:
        features_to_models['book_to_movie'] = st.number_input('Uyarlama mı ? (0-Hayır, 1-Evet):')
    if "'act_count'" in features:
        features_to_models['act_count'] = st.number_input('Başroldeki aktör sayısı:')
    if "'paid_channel'" in features:
        features_to_models['paid_channel'] = st.number_input('Ücretli bir kanalda mı yayınlanıyor ? (0-Hayır, 1-Evet):')
    if "'Publication Day'" in features:
        features_to_models['Publication Day'] = st.text_input('Yayınlandığı gün (İngilizce olarak girin.):')
    if "'summer_series'" in features:
        features_to_models['summer_series'] = st.number_input('Yaz dizisi (Temmuz, Ağustos) mi ? (0-Hayır, 1-Evet):')
    if "'duration'" in features:
        features_to_models['duration'] = st.number_input('Ortalama bölüm uzunluğu:')
    if "'Ödüllü'" in features:
        features_to_models['Ödüllü'] = st.number_input('Altın kelebek ödülü aldı mı ?:')
    if "'Senaristlerin Dizi Sayısı'" in features:
        features_to_models['Senaristlerin Dizi Sayısı'] = st.number_input('Senaristlerin yazdığı ortalama dizi sayısı:')
    if "'Ödüllü Senarist Sayısı'" in features:
        features_to_models['Ödüllü Senarist Sayısı'] = st.number_input('Ödüllü senarist sayısı:')
    if "'Senaristlerin Aldığı Ödül Sayısı'" in features:
        features_to_models['Senaristlerin Aldığı Ödül Sayısı'] = st.number_input('Senaristlerin aldığı ortalama ödül sayısı:')
    if "'Başrollerin Dizi Sayısı'" in features:
        features_to_models['Başrollerin Dizi Sayısı'] = st.number_input('Başrollerin ortalama dizi sayısı:')
    if "'Ödüllü Başrol Sayısı'" in features:
        features_to_models['Ödüllü Başrol Sayısı'] = st.number_input('Ödüllü başrol sayısı:')
    if "'Başrollerin Aldığı Ödül Sayısı'" in features:
        features_to_models['Başrollerin Aldığı Ödül Sayısı'] = st.number_input('Başrollerin aldığı ortalama ödül sayısı:')
    if "'Yönetmenlerin Dizi Sayısı'" in features:
        features_to_models['Yönetmenlerin Dizi Sayısı'] = st.number_input('Yönetmenlerin ortalama dizi sayısı:')
    if "'Ödüllü Yönetmen Sayısı'" in features:
        features_to_models['Ödüllü Yönetmen Sayısı'] = st.number_input('Ödüllü yönetmen sayısı:')
    if "'Yönetmenlerin Aldığı Ödül Sayısı'" in features:
        features_to_models['Yönetmenlerin Aldığı Ödül Sayısı'] = st.number_input('Yönetmenlerin aldığı ortalama ödül sayısı:')
    if "'Görüntü Yönetmenlerinin Dizi Sayısı'" in features:
        features_to_models['Görüntü Yönetmenlerinin Dizi Sayısı'] = st.number_input('Görüntü yönetmenlerinin ortalama dizi sayısı:')
    if "'Yapım Şirketleri Dizi Sayısı'" in features:
        features_to_models['Yapım Şirketleri Dizi Sayısı'] = st.number_input('Yapım şirketlerinin ortalama dizi sayısı:')
    if "'Besteci Dizi Sayısı'" in features:
        features_to_models['Besteci Dizi Sayısı'] = st.number_input('Bestecilerin ortalama dizi sayısı:')
    if "'on_youtube'" in features:
        features_to_models['on_youtube'] = st.number_input('Youtube hesabı var mı ? (0-Hayır, 1-Evet):')
    if "'on_facebook'" in features:
        features_to_models['on_facebook'] = st.number_input('Facebook hesabı var mı ? (0-Hayır, 1-Evet):')
    if "'on_twitter'" in features:
        features_to_models['on_twitter'] = st.number_input('Twitter hesabı var mı ? (0-Hayır, 1-Evet):')
    if "'on_instagram'" in features:
        features_to_models['on_instagram'] = st.number_input('Instagram hesabı var mı ? (0-Hayır, 1-Evet):')
    if "'total_sm_accounts'" in features:
        features_to_models['total_sm_accounts'] = st.number_input('Toplam sosyal medya hesabı sayısı:')

    if st.button('Tahmin Et'):
        test = pd.DataFrame(features_to_models, index=[0])
        test_df_names = []

        for key, value in features_to_models.items():
            if value != -2 and value != '?':
                test_df_names.append(key)

        #st.write(test_df)
        numerical_variables = [col for col in test.columns if pd.api.types.is_numeric_dtype(test[col])]
        if features_to_models['Publication Day'] != '?':
            test['Publication Day'] = day_encoder.transform(test['Publication Day'].values.reshape(-1, 1))
        test[numerical_variables] = rs.transform(test[numerical_variables])

        test_small = test[test_df_names]
        #st.dataframe(test_small)

        predicted = model.predict(test_small)
        prediction = le.classes_[predicted]
        st.success(f'Tahminen bu dizi {prediction}')