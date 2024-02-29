import streamlit as st
import pickle
import pandas as pd
import requests

# To get PNG path
#def fetch_course_png(course_id):
    #response = requests.get('https://course_png{}?api_key=34327846374638638'.format(course_id))
    #data = response.json()
    #return "https://image./s/d/..." + data['png_path']

similarity = pickle.load(open('similarity.pkl', 'rb'))

#def recommend_course_category(course):
    #index = courses1[courses1['course_name'] == course].index[0]
   # sim = similarity[index]
   # courses_category_list = sorted(list(enumerate(sim)), reverse =True, key=lambda x:x[1])[1:6]
   # recommended_course_category_name = []
   # for i in courses_category_list:
     #   recommended_course_category_name.append(courses1.iloc[i[0]].course_category_name)
    #return recommended_course_category_name


def recommend(course):
    course_index = courses1[courses1['course_name'] == course].index[0]
    sim = similarity[course_index]
    sim1 = list(enumerate(sim))
    sim_scores = sorted(sim1, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    courses_list = sorted(list(enumerate(sim)), reverse =True, key=lambda x:x[1])[1:6]
    recommended_courses = []
    recommended_course_category_name = []
    for i in courses_list:
        # course_id = courses.iloc[i[0]].course_id
        #course_cat_name = courses_filled.iloc[i[0]].course_category_name
        recommended_courses.append(courses1.iloc[i[0]].course_name)
            # To fetch the PNG
        recommended_course_category_name.append(courses1.iloc[i[0]].course_category_name)
            # to return both use below line
    # return recommended_courses, recommended_courses_png
    return recommended_courses, sim_scores, recommended_course_category_name


courses_dict = pickle.load(open('course_dict.pkl', 'rb'))
courses = pd.DataFrame(courses_dict)

courses_dict_1 = pickle.load(open('cf.pkl', 'rb'))
courses1 = pd.DataFrame(courses_dict_1)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Course Recommendation System')
selected_course_name = st.selectbox(
    'Choose a Course or Enter Course Name to get Recommendations',
    courses1['course_name'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_course_name)
    for i in recommendations:
        st.write(i)
    # use below line to get both Name and PNG
    #recommendations, png = recommend(selected_course_name)
    #col1, col2, col3, col4, col5 = st.columns(5)
    #with col1:
        #st.text(recommendations[0])
        #st.text(category[0])
    #with col2:
        #st.text(recommendations[1])
        #st.text(category[1])
    #with col3:
        #st.text(recommendations[2])
        #st.text(category[2])
    #with col4:
        #st.text(recommendations[3])
        #st.text(category[3])
    #with col5:
        #st.text(recommendations[4])
        #st.text(category[4])


