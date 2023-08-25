import streamlit as st
from streamlit_chat import message
from streamlit_Utilities import *
# from instadev import *
if 'instagram' not in st.session_state:
    st.session_state['instagram'] = []
    st.session_state['instagramImage'] = []
if 'twitter' not in st.session_state:
    st.session_state['twitter'] = []
    st.session_state['twitterImage'] = []
if 'facebook' not in st.session_state:
    st.session_state['facebook'] = []
    st.session_state['faceebokImage'] = []
if 'linkedin' not in st.session_state:
    st.session_state['linkedin'] = []
    st.session_state['linkedinImage'] = []
if 'blogPost' not in st.session_state:
    st.session_state['blogPost'] = []
    st.session_state['blogImage'] = []

st.title('🦜🔗 Rayn')
prompt = st.text_input('Write Your Topic.')

insta_button, twitter_button, facebook_button, linkedIn_button, blog_button = st.columns(5)

if prompt:
    with insta_button:
        if st.button("Instagram"):
            st.session_state['instagram'] = generate_Instagram_content(prompt)
            instaRefineText=TextRefine(prompt)
            st.session_state['instagramImage']=generate_thumbnail_background(instaRefineText)
            # newRespone=TextRefine(prompt)
    with twitter_button:
        if st.button("Twitter"):
            st.session_state['twitter'] = generate_Twitter_content(prompt)
            twiitwerRefineText=TextRefine(prompt)
            st.session_state['twitterImage']=generate_thumbnail_background(twiitwerRefineText)
            # newRespone=TextRefine(prompt)

    with facebook_button:
        if st.button("Facebook"):
            text= generate_Facebook_content(prompt)
            #removing left emojis
            st.session_state['facebook'] =remove_emojis(text)
            fbRefineText=TextRefine(prompt)
            st.session_state['faceebokImage']=generate_thumbnail_background(fbRefineText)
            # newRespone=TextRefine(prompt)
    with linkedIn_button:
        if st.button("LinkedIn"):
            text=generate_LinkedIn_content(prompt)
            st.session_state['linkedin'] =remove_emojis(text)
            linkedinRefineText=TextRefine(prompt)
            st.session_state['linkedinImage']=generate_thumbnail_background(linkedinRefineText)
            # newRespone=TextRefine(prompt)
    with blog_button:
        if st.button("Blog Post"):
            st.session_state['blogPost'] = generate_Blog_Structure(prompt)
            st.session_state['blogPost'] = generate_Blog_Content(prompt, st.session_state['blogPost'])
            blogRefineText=blogMultiPromptGenerator(prompt,st.session_state['blogPost'])
            st.session_state['blogImage']=generate_multi_thumbnail_background(blogRefineText)

if st.session_state['blogPost']:
    st.write("Blog Post")
    # message(videoLink)
    # message(blogTitle[0][2:-1])
    # message(seo_key)
    # message(st.session_state['blogPost'])
    part1,part2,part3=split_text(st.session_state['blogPost'])
    TextList=[part1,part2,part3]
    # # message(st.session_state['blogPost'])
    for i in range(0,3):
        message(TextList[i])
        counter=f"Add_gen{i}.jpg"
        st.image(counter,caption='Generated Image',use_column_width=True)
    # message(seo_key)    
    # st.write(newRespone)
if st.session_state['twitter']:
    st.write("Twitter")
    message(st.session_state['twitter'])
    st.image(st.session_state['twitterImage'],caption='Generated Image',use_column_width=True)
    # st.write(newRespone)
if st.session_state['instagram']:
    st.write("Instagram")
    message(st.session_state['instagram'])
    st.image(st.session_state['instagramImage'],caption='Generated Image',use_column_width=True)
    # st.write(newRespone)
if st.session_state['facebook']:
    st.write("Facebook")
    message(st.session_state['facebook'])
    st.image( st.session_state['faceebokImage'],caption='Generated Image',use_column_width=True)
    # st.write(newRespone)
if st.session_state['linkedin']:
    st.write("LinkedIn")
    message(st.session_state['linkedin'])
    st.image(st.session_state['linkedinImage'],caption='Generated Image',use_column_width=True)
    # st.write(newRespone)