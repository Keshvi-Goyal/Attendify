import streamlit as st
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.ui.base_layout import style_background_dashboard 
from src.ui.base_layout import style_base_layout
from src.database.db import check_teacher_exists, create_teacher, teacher_login

def teacher_screen():
  
  style_background_dashboard()
  style_base_layout()
  
  if "teacher_data" in st.session_state:
    teacher_dashboard()
  elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type=="login":
     teacher_screen_login()
  elif st.session_state.teacher_login_type =="register":
    teacher_screen_register()
        
def teacher_dashboard():
  teacher_data = st.session_state.teacher_data
  c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
  with c1:
   header_dashboard()
  with c2:   
   st.subheader(f"""Welcome, {teacher_data['name']}  """)
   if st.button("Logout", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
      st.session_state['is_logged_in']
      del st.session_state.teacher_data
      st.rerun()

  st.space()

  if 'current_teacher_tab' not in st.session_state:
    st.session_state.current_teacher_tab = 'take_attendence'

  tab1, tab2, tab3 = st.columns(3)

  with tab1:
    type1 = "primary" if st.session_state.current_teacher_tab == 'take_attendence' else "tertiary"
    if st.button('Take Attendence', type = type1,  width='stretch', icon=':material/ar_on_you:'):
      st.session_state.current_teacher_tab = 'take_attendence'
      st.rerun()

  with tab2:
    type2 = "primary" if st.session_state.current_teacher_tab == 'manage_subjects' else "tertiary"
    if st.button('Manage Subjects',type = type2,  width='stretch', icon=':material/book_ribbon:'):
      st.session_state.current_teacher_tab = 'manage_subjects'
      st.rerun()

  with tab3:
    type3 = "primary" if st.session_state.current_teacher_tab == 'attendence_records' else "tertiary"
      
    if st.button('Attendence Records', type = type3,  width='stretch', icon=':material/cards_stack:'):
      st.session_state.current_teacher_tab = 'attendence_records'
      st.rerun()     

  if st.session_state.current_teacher_tab == 'take_attendence':
    teacher_tab_take_attendence() 

  if st.session_state.current_teacher_tab == 'manage_subjects':
    teacher_tab_manage_subjects()    

  if st.session_state.current_teacher_tab == 'attendence_records':
    teacher_tab_attendence_records()   

  footer_dashboard()

def  teacher_tab_take_attendence():
  st.header("Take AI Attendence")

def  teacher_tab_manage_subjects():
  teacher_id = st.session_state.teacher_data['teacher_id']
  col1, col2 = st.columns(2)
  with col1:
    st.header("Manage Subjects", width = 'stretch')
  with col2:
    if st.button("Create New Subject", width = 'stretch'):
      create_subject_dialog(teacher_id)

def  teacher_tab_attendence_records():
  st.header("Attendence Records")
  

def login_teacher(username, password):
  if not username or not password:
    return False
  teacher = teacher_login(username, password)
  if teacher:
    st.session_state.user_role = 'teacher'
    st.session_state.teacher_data = teacher
    st.session_state.is_logged_in = True
    return True
  return False


def teacher_screen_login():
  c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
  with c1:
    header_dashboard()
  with c2:   
    if st.button("Go back to Home", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
      st.session_state['login_type']=None
      st.rerun()

  st.header('Login Using Password', text_alignment = 'center')
  st.space()
  st.space()
  teacher_username = st.text_input("Enter Username", placeholder='Please enter you username')
  teacher_pass = st.text_input("Enter Password", type='password', placeholder='Please enter you password')

  st.divider()
  btnc1, btnc2 = st.columns(2, vertical_alignment='center')
  with btnc1:
    if st.button('Login', icon=':material/passkey:', shortcut="control+enter", width='stretch', use_container_width=True):
      if login_teacher(teacher_username, teacher_pass):
        st.toast("Welcome back!")
        import time
        time.sleep(1)
        st.rerun()
      else:
        st.error("Ivalid username and password combo")
  with btnc2:
    if st.button('Register Instead',type='primary', icon=':material/passkey:',  width='stretch', use_container_width=True):
     st.session_state.teacher_login_type = 'register'
     

  footer_dashboard()
            
def register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm):
  if not teacher_username or not teacher_name or not teacher_pass:
    return False, "All fields are required!"
  if check_teacher_exists(teacher_username):
    return False, "Username already taken"
  if teacher_pass != teacher_pass_confirm:
    return False, "Password doesn't match"
  
  try:
    create_teacher(teacher_username, teacher_pass, teacher_name)
    return True, "Successfully created! Login Now"
  except Exception as e:
    return False, "Unexpected error!"
  
def teacher_screen_register():
  c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
  with c1:
    header_dashboard()
  with c2:   
    if st.button("Go back to Home", type='secondary', key='loginbackbtn1', shortcut="control+backspace"):
      st.session_state['login_type']=None
      st.rerun()
  st.header("Register your Teacher profile")
  st.space()
  st.space()
  teacher_username = st.text_input("Enter Username", placeholder='Please enter you username')
  teacher_name = st.text_input("Enter Name", placeholder='Please enter you name')
  teacher_pass = st.text_input("Enter Password", type='password', placeholder='Please enter you password')
  teacher_pass_confirm = st.text_input("Confirm Your Password", type='password', placeholder='Confirm Your Password')
  st.divider()
  btnc1, btnc2 = st.columns(2, vertical_alignment='center')
  with btnc1:
    if st.button('Login instead', icon=':material/passkey:',  width='stretch', use_container_width=True):
     st.session_state.teacher_login_type = 'login'
     st.rerun()
  with btnc2:
    if st.button('Register now',type='primary', icon=':material/passkey:',  width='stretch', use_container_width=True):
      success, message = register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm)
      if success:
        st.success(message)
        import time
        time.sleep(2)
        st.session_state.teacher_login_type = "login"
        st.rerun()
      else:
        st.error(message)

  footer_dashboard()         