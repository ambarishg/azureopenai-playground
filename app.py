import streamlit as st
from openaing import *

st.set_page_config(layout="wide")
st.title("Question Answering System ")

deployment_plan = st.selectbox('Select Deployment Plan',
                                ['text-davinci','GPT-3.5', 'GPT-4'])

text_to_analyze = st.text_area('Text to analyze', '''The men's high jump event at the 2020 Summer Olympics took place between 30 July and 1 August 2021 at the Olympic Stadium.33 athletes from 24 nations competed; the total possible number depended on how many nations would use universality places to enter athletes in addition to the 32 qualifying through mark or ranking (no universality places were used in 2021).Italian athlete Gianmarco Tamberi along with Qatari athlete Mutaz Essa Barshim emerged as joint winners of the event following a tie between both of them as they cleared 2.37m. Both Tamberi and Barshim agreed to share the gold medal in a rare instance where the athletes of different nations had agreed to share the same medal in the history of Olympics.                     
Barshim in particular was heard to ask a competition official "Can we have two golds?" in response to being offered a 'jump off'. Maksim Nedasekau of Belarus took bronze. The medals were the first ever in the men's high jump for Italy and Belarus, the first gold in the men's high jump for Italy and Qatar, and the third consecutive medal in the men's high jump for Qatar (all by Barshim). Barshim became only the second man to earn three medals in high jump, joining Patrik Sjöberg of Sweden (1984 to 1992).''',height=200)

prompt = st.text_input('Your Question')

if st.button('Submit'):
    reply = generate_answer_from_context(prompt, text_to_analyze,deployment_plan)
    st.write(reply)

