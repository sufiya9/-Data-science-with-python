'''
how to run
- open terminal/console  and type
-cd app1
-streamlit run main.py
'''

import streamlit as st

st.title('This is A title')
st.header('This is Heading')
st.subheader('subheading')
st.text('A very normal text on a normal day')
st.write('this is a magic function to write stuff')
st.success(' this is the text written for success message ')
st.error('this is the text written for error message')
st.info('this is a information message text')
st.warning(' this is a warning text')
st.markdown('''
this is a markdown text, hear u are free to use
<h5> HTML <h5>
<p> this is a paragraph </p>
<ul>
    <li>One Two </li> 
    <li> Three Four </li> 
    <li> Five Six </li> 
</ul>
or
# Markdown Heading
''',unsafe_allow_html=True)
st.code('area where we can put code')


