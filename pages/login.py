import streamlit as st
import pandas as pd
import auth_functions
import utils

## -------------------------------------------------------------------------------------------------
## Not logged in -----------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------------
if 'user_info' not in st.session_state:
    col1,col2,col3 = st.columns([1,2,1])

    # Authentication form layout
    do_you_have_an_account = col2.selectbox(label='Do you have an account?',options=('Yes','No','I forgot my password'))
    auth_form = col2.form(key='Authentication form',clear_on_submit=False)
    email = auth_form.text_input(label='Email')
    password = auth_form.text_input(label='Password',type='password') if do_you_have_an_account in {'Yes','No'} else auth_form.empty()
    auth_notification = col2.empty()

    # Sign In
    if do_you_have_an_account == 'Yes' and auth_form.form_submit_button(label='Sign In',use_container_width=True,type='primary'):
        with auth_notification, st.spinner('Signing in'):
            auth_functions.sign_in(email,password)

    # Create Account
    elif do_you_have_an_account == 'No' and auth_form.form_submit_button(label='Create Account',use_container_width=True,type='primary'):
        with auth_notification, st.spinner('Creating account'):
            auth_functions.create_account(email,password)

    # Password Reset
    elif do_you_have_an_account == 'I forgot my password' and auth_form.form_submit_button(label='Send Password Reset Email',use_container_width=True,type='primary'):
        with auth_notification, st.spinner('Sending password reset link'):
            auth_functions.reset_password(email)

    # Authentication success and warning messages
    if 'auth_success' in st.session_state:
        auth_notification.success(st.session_state.auth_success)
        del st.session_state.auth_success
    elif 'auth_warning' in st.session_state:
        auth_notification.warning(st.session_state.auth_warning)
        del st.session_state.auth_warning

## -------------------------------------------------------------------------------------------------
## Logged in --------------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------------
else:

    st.title("Welcome")

    with st.sidebar:
        # Show user information
        st.header('User information:')
        st.write(st.session_state.user_info["email"])

        # Sign out
        st.header('Sign out:')
        st.button(label='Sign Out',on_click=auth_functions.sign_out,type='primary')

        # Delete Account
        st.header('Delete account:')
        password = st.text_input(label='Confirm your password',type='password')
        st.button(label='Delete Account',on_click=auth_functions.delete_account,args=[password],type='primary')

    # authorize the clientsheet 
    client = utils.connect_gsheet()

    # get the instance of the Spreadsheet
    sheet = client.open('medilearn_qembed')

    # get the first sheet of the Spreadsheet
    sheet_instance = sheet.get_worksheet(0)
    # get all the records of the data
    df = sheet_instance.get_all_records()
    df = pd.DataFrame.from_dict(df)
    df = df[df.answers!=""]

    # get the first sheet of the Spreadsheet
    sheet_instance = sheet.get_worksheet(1)
    # get all the records of the data
    clusters = sheet_instance.get_all_records()
    clusters = pd.DataFrame.from_dict(clusters)
    cluster_dict = clusters["cluster_name"].to_dict()

    options = set(df.cluster.map(cluster_dict).values)
    topic = st.selectbox(options=options, label="Choose a topic")

    subset = df[df.cluster==clusters[clusters.cluster_name==topic].cluster_id.values[0]]

    for i in range(len(subset)):
        with st.expander(subset.iloc[i].questions):
            st.write(subset.iloc[i].answers)
            doc_id = subset.iloc[i].doc_id
            st.caption(f'{doc_id}, {st.session_state["pruefungsprotokolle"].iloc[i].values[0]}')
