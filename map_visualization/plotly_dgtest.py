#1번 choropleth mapbox에 마커띄우는게가능한지 choroplethmapbox에 스크립트를 표시할수있는지

# https://codeburst.io/how-i-understood-displaying-interactive-maps-using-python-leaflet-js-and-folium-bd9b98c26e0e
# 4번과 6번을 통해서 chropleth 상에 마커를 띄우고, 마커에 스크립트 표현 가능할 것 같습니다.



#2번 catter mapbox와 choropleth가 연동이나 호환이 되는지
import plotly.express as px
import pandas as pd
import os
import json

# 스케터
px.set_mapbox_access_token(open("mapbox_token.py").read())
df = pd.read_csv("C:\\Users\\a\\Desktop\\zrental_shop\\z210131.csv", encoding='cp949')
fig = px.scatter_mapbox(df, lat="위도", lon="경도", color="위도", size="대여소번호", hover_name="보관소(대여소)명", hover_data=["자치구"])
fig.update_layout(mapbox = {"style": "light", 'zoom':7}, showlegend = False)
fig.show()


# 크로프레스
geometry_gj = json.load(open('13.서울시_법정경계(시군구).geojson', encoding='utf-8'))
budget_df = pd.read_excel("budget.xlsx", header=1)

df1 = budget_df[['기간', '자치구', '예산']]
df1 = df1[df1['기간'] == 2017]
df1.drop(0, inplace=True)
df1.drop(['기간'], axis=1, inplace=True)
fig = px.choropleth(df1, geojson=geometry_gj, locations=df1.자치구, featureidkey='properties.SIG_KOR_NM', color='예산', color_continuous_scale='Blues')
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(title_text='서울시 2017년도 자치구 별 예산', title_font_size=20)
fig.show()

# 해결책?
'''
choropleth_data = {
     # Your choropleth data here
}

scatter_data = {
     # Your scatter data here
}

figure = {
    "data": [
        choropleth_data,
        scatter_data
    ]
   "layout": {
        # Your layout dictionary here
   }
}
'''
# 이런 예시인데 스케터 컬러바 생성하기 어렵다고 하는 것 같습니다.
import plotly.express as px

df = px.data.gapminder()
print(df)
fig = px.choropleth(df, locations="iso_alpha",
                    color="lifeExp", # lifeExp is a column of gapminder
                    hover_name="country", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma,
                    animation_frame='year')
fig2 = px.scatter_geo(df, locations="iso_alpha",
                    size="lifeExp", # lifeExp is a column of gapminder
                    hover_name="country", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma,
                    animation_frame='year')
fig.add_trace(fig2.data[0])
for i, frame in enumerate(fig.frames):
    fig.frames[i].data += (fig2.frames[i].data[0],)
fig.show()


#이건 애러났음..
'''
chropleth_data = {
    geometry_gj = json.load(open('13.서울시_법정경계(시군구).geojson', encoding='utf-8'))
    budget_df = pd.read_excel("budget.xlsx", header=1)
    df1 = budget_df[['기간', '자치구', '예산']]
    df1 = df1[df1['기간'] == 2017]
    df1.drop(0, inplace=True)
    df1.drop(['기간'], axis=1, inplace=True)
    fig = px.choropleth(df1, geojson=geometry_gj, locations=df1.자치구, featureidkey='properties.SIG_KOR_NM', color='예산', color_continuous_scale='Blues')
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(title_text='서울시 2017년도 자치구 별 예산', title_font_size=20)}
scatter_data={
    px.set_mapbox_access_token(open("mapbox_token.py").read())
    df = pd.read_csv("C:\\Users\\a\\Desktop\\zrental_shop\\z210131.csv", encoding='cp949')
    fig = px.scatter_mapbox(df, lat="위도", lon="경도", color="위도", size="대여소번호", hover_name="보관소(대여소)명", hover_data=["자치구"])
    fig.update_layout(mapbox = {"style": "light", 'zoom':7}, showlegend = False)
}
figure = {
    "data":[
        chropleth_data,
        scatter_data
    ]
    "latout":{
        fig.show()
    }
}
'''

