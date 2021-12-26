import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle

from eda_app import run_eda_app
from ml_app import run_ml_app

def main():
    st.title('자동차 가격 책정 ')

    #사이드바 메뉴
    Kategorie = ['Home','Exploratory data analysis','machine learning']
    choice = st.sidebar.selectbox('카테고리',Kategorie)
    
    if choice =='Home' :
        st.subheader('플랫폼 : 비즈니스 마케팅(가격책정)')
        st.write('Exploratory data analysis:고객의 정보와 자동차 구매 데이터를 탐색적 데이터분석')
        st.write('machine learning:머신러닝을 통한 자동차 가격 책정')
    elif choice == 'Exploratory data analysis' :
        run_eda_app()
    elif choice =='machine learning' :
        run_ml_app()

if __name__ == '__main__' :
    main()
    