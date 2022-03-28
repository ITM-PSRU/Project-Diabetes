import streamlit as st
import pickle
import os

with open('Tree_model.pkl','rb') as model:
    model_dt = pickle.load(model)

def main():
    st.set_page_config(page_title="Diabetes Health Check App", page_icon="⚕️", layout="centered",initial_sidebar_state="auto")

    html_temp = """ 
        <div style ="background-color:pink;padding:11px"> 
        <h1 style ="color:black;text-align:center;text-shadow: 2px 2px 5px #FF3399;">Prediction Diabetes</h1> 
        </div><br/>
         <h5 style ="font-family:Arial;text-align:center;text-shadow: 2px 2px 5px #DCDCDC;">เว็บแอปพลิเคชันทำนายความเสี่ยงเป็นโรคเบาหวาน</h5>
         กรุณากรอกข้อมูลด้านล่างนี้ ให้ครบถ้วน
        """

    html_sidebar = """
        <div style ="background-color:pink;padding:10px"> 
        <style>a:link,a:visited {background-color:#ffd3db;color:black;padding:10px;text-align:center;text-decoration:none;display:inline-block;width: 100%;text-shadow: 2px 2px 5px #FF99CC;}
        a:hover,a:active {background-color: #f9a2b1;}</style>
                <h1 style ="color:black;text-align:center;text-shadow: 2px 2px 5px #FF3399;">สาระสุขภาพ</h1>
                <p style ="color:black;text-shadow: 2px 2px 5px #DCDCDC;">เนื้อหาข้อมูลด้านล่างนี้  มาจากเว็บไซต์ของ โรงพยาบาลศิริราช ปิยมหาราชการุณย์ ที่ให้ความรู้และให้คำปรึกษาด้านสุขภาพต่างๆ ที่เป็นประโยชน์ที่ดีต่อท่าน</p>
                <p><a href="https://www.siphhospital.com/th/news/article/share/diabetes-2" target="_blank">เบาหวาน รู้ทันป้องกันได้</a></p>
                <p><a href="https://www.siphhospital.com/th/news/article/share/diabetes-exercise" target="_blank">ออกกำลังกาย พิชิตเบาหวาน</a></p>
                <p><a href="https://www.siphhospital.com/th/news/article/share/food-exchange" target="_blank">อาหารสำหรับผู้เป็นเบาหวาน</a></p>
                <p><a href="https://www.siphhospital.com/th/news/article/share/diabetes-mellitus" target="_blank">ภาวะแทรกซ้อน จากโรคเบาหวาน</a></p>
                <p><a href="" target="_blank">แบบสอบถามความพึงพอใจ</a></p> 

    </div> 
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    st.sidebar.write(html_sidebar, unsafe_allow_html=True)
    Age = st.selectbox("ช่วงระดับ อายุของคุณ", ("18-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80+"))
    if Age == '18-24':
        Age = 1
    elif Age == '25-29':
        Age = 2
    elif Age == '30-34':
        Age = 3
    elif Age == '35-39':
        Age = 4
    elif Age == '40-44':
        Age = 5
    elif Age == '45-49':
        Age = 6
    elif Age == '50-54':
        Age = 7
    elif Age == '55-59':
        Age = 8
    elif Age == '60-64':
        Age = 9
    elif Age == '65-69':
        Age = 10
    elif Age == '70-74':
        Age = 11
    elif Age == '75-79':
        Age = 12
    elif Age == '80+':
        Age = 13

    weight = st.number_input(label="ระบุน้ำหนักของคุณ (kg)", min_value=0, max_value=None, value=1, step=1)
    high = st.number_input(label="ระบุส่วนสูงของคุณ (cm)", min_value=0, max_value=None, value=1, step=1) / 100
    # bmi = weight / (high ** 2)
    BMI = weight / (high ** 2)

    HighBP = st.radio("ระดับความดันโลหิตของคุณ สูงมากกว่า 120/80 ใช่หรือไม่?", ["ไม่ใช่", "ใช่"])
    if HighBP == 'ไม่ใช่':
        HighBP = 0
    elif HighBP == 'ใช่':
        HighBP = 1

    HighBS = st.radio("ระดับน้ำตาลในเลือดของคุณ สูงมากกว่า 100 - 125 มิลลิกรัมต่อเดซิลิตร ใช่หรือไม่?",
                      ["ไม่ใช่", "ใช่"])
    if HighBS == 'ไม่ใช่':
        HighBS = 0
    elif HighBS == 'ใช่':
        HighBS = 1

    GenHlth = st.selectbox("ดัชนีสุขภาพของคุณตอนนี้เป็นอย่างไร?", ("สุขภาพแข็งแรงดีมาก", "สุขภาพดี", "สุขภาพทรงตัว เริ่มรู้สึกว่าร่างกายอ่อนแอลง", "สุขภาพแย่ เจ็บป่วยบ่อย","สุขภาพแย่มาก ต้องเข้ารับการรักษาที่โรงพยาบาลบ่อยครั้ง"))
    if GenHlth == 'สุขภาพแข็งแรงดีมาก':
        GenHlth = 1
    elif GenHlth == 'สุขภาพดี':
        GenHlth = 2
    elif GenHlth == 'สุขภาพทรงตัว เริ่มรู้สึกว่าร่างกายอ่อนแอลง':
        GenHlth = 3
    elif GenHlth == 'สุขภาพแย่ เจ็บป่วยบ่อย':
        GenHlth = 4
    elif GenHlth == 'สุขภาพแย่มาก ต้องเข้ารับการรักษาที่โรงพยาบาลบ่อยครั้ง':
        GenHlth = 5

    if st.button('ทำนายผล'):
        result = prediction(HighBP,HighBS,BMI,GenHlth,Age)
        if (result == 1):
            st.warning('คำเตือน! คุณมีโอกาสเสี่ยงที่จะเป็นโรคเบาหวาน')
            st.warning('โปรดดูแลสุขภาพของคุณให้ดี หรือเข้าพบแพทย์เพื่อตรวจโรคเบาหวานอย่างละเอียด')
        elif (result == 0):
            st.success('ขอแสดงความยินดี คุณมีสุขภาพที่ดี และไม่มีความเสี่ยงเป็นโรคเบาหวาน')

def prediction(HighBP, HighBS,BMI, GenHlth, Age):
    predicted_output = model_dt.predict([[HighBP, HighBS,BMI, GenHlth, Age]])
    return predicted_output

if __name__ == '__main__':
    main()


















