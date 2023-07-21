import streamlit as st
import os
import streamlit_google_oauth as oauth
from datarobot_streamlit import streamlit_app

client_id = os.getenv('clientid')
client_secret = os.getenv('clientsecret')
redirect_uri = os.getenv('redirecturi')


if __name__ == "__main__":
    app_name = '''
    DataRobot Streamlit Google Authentication Demo
    '''
    app_desc = '''
    Demo of DataRobot Streamlit which has a Google login page
    '''
    login_info = oauth.login(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        app_name=app_name,
        app_desc=app_desc,
        logout_button_text="Logout",
    )
    if login_info:
        user_id, user_email = login_info
        streamlit_app.main()