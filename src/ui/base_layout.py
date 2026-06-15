import streamlit  as st

def style_background_home():
    st.markdown("""   
         <style>
                .stApp{
                     background: #F5DCE0 !important;
                }
               
                .stApp div[data-testid="stColumn"]{
                    background-color:#E0E3FF !important;
                    padding:2.5rem !important;
                    border-radius: 5rem !important;
                    }

        </style>
                       """ 
                ,unsafe_allow_html=True)

def style_background_dashboard():
    st.markdown("""   
         <style>
                .stApp{
                     background: #5865F2 !important;
                }


        </style>
                       """ 
                ,unsafe_allow_html=True)
    
def style_base_layout():
    st.markdown("""   
     <style>
                
                @import url('https://fonts.googleapis.com/css2?family=Luckiest+Guy&display=swap');

                @import url('https://fonts.googleapis.com/css2?family=Luckiest+Guy&family=Outfit:wght@100..900&display=swap');    

          #MainMenu, footer, header{
            visibility: hidden;
            }     

        .block-container {
           padding-top: 0.5rem !important;
        }

        h1{
             font-family: 'Luckiest Guy', cursive !important;
             font-size: 5rem !important;
             margin-top: -1.5rem !important;
             margin-bottom: 0rem !important;
                
             -webkit-text-stroke: 2px black;
   
        }
                
        h3, h4, p{
                   font-family: 'Outfit', sans-serif;    
        }
                       
                
        button{
                border-radius: 1.5rem !important;
                background-color: #cb426b !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button:hover{
                transform :scale(1.05)}    
                        
     </style>
                       """ 
                ,unsafe_allow_html=True)    