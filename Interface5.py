import streamlit as st
import numpy as np
import pandas as pd
import random as rd
import math
from Class_Preguntas import Questionary, preguntas
from Imagenes import *

#=========================Configuration of the page============================
#Width of the content
st.set_page_config(layout="wide") #centered

#Creation of the sidebar
st.sidebar.markdown("<h1 style='font-size:36px;'>StaticGenius</h1>", unsafe_allow_html=True)
way=st.sidebar.radio("Seleccione su método de estudio",options=["Práctica","Teoría"])
respuesta_usuario = {}
if way=="Teoría":
    st.sidebar.header("Teoría")
else:
    st.sidebar.header("Práctica")
    complexity=st.sidebar.radio("Nivel de dificultad",options=["Fácil","Medio","Díficil"]) 
    respuesta_usuario['complexity'] = complexity
    
    topic=st.sidebar.selectbox("Seleccione el tema", options=["Equilibrio de partículas"])
    #topic=st.sidebar.selectbox("Seleccione el tema", options=["Equilibrio de partículas","Momento","Incertidumbre","Sistemas equivalentes","Apoyos y reacciones","Armaduras","Centroides","Fuerzas distribuidas","Fuerzas internas"])
    respuesta_usuario['topic'] = topic
    
    if topic=="Equilibrio de partículas":
        subtopic=st.sidebar.selectbox("Seleccione el subtema", options=["Vectores 2D","Vectores 3D","Vector unitario","Equilibrio 2D","Equilibrio 3D"])
    #elif topic=="Momento":
    #    subtopic=st.sidebar.selectbox("Seleccione el subtema", options=["Momento en un punto 2D","Momento en un punto 3D","Momento alrededor de un eje","Momentos pares"])
    #elif topic=="Incertidumbre":
    #    subtopic=st.sidebar.selectbox("Seleccione el subtema", options=["Equilibrio de partículas","Momento","Apoyos y reacciones","Armaduras","Centroides","Fuerzas distribuidas","Fuerzas internas"])
    #elif topic=="Sistemas equivalentes":
    #    subtopic=st.sidebar.selectbox("Seleccione el subtema", options=["Sistemas equivalentes 2D","Sistemas equivalentes 3D"])
    #elif topic=="Apoyos y reacciones":
    #    subtopic=st.sidebar.selectbox("Seleccione el subtema", options=["Apoyos","Reacciones"])
    #elif topic=="Armaduras":
    #    subtopic=st.sidebar.selectbox("Seleccione el subtema", options=["Cerchas: Método de los nodos","Cerchas: Elementos de fuerza cero","Cerchas: Método de las secciones","Marcos"])
    #elif topic=="Centroides":
    #    subtopic=st.sidebar.selectbox("Seleccione el subtema", options=["Centroides","Centro de gravedad","Centro de masa"])
    #elif topic=="Fuerzas distribuidas":
    #    subtopic=st.sidebar.selectbox("Seleccione el subtema", options=["Vigas","Presión hidrostática","Empuje de suelo"])
    #elif topic=="Fuerzas internas":
    #    subtopic=st.sidebar.selectbox("Seleccione el subtema", options=["Fuerzas internas en un punto","Diagramas: Método analítico","Diagramas: Método simplificado"])

#Storage the user's selection
    respuesta_usuario['subtopic'] = subtopic
complexity_user=respuesta_usuario['complexity']
topic_user=respuesta_usuario['topic']
subtopic_user=respuesta_usuario['subtopic']


#List filtrered of questions according to the user's selection
preguntas_filtradas = Questionary.filtrar_preguntas(preguntas, topic_user, subtopic_user, complexity_user)


#=========================Functions to generate the questions============================

#Function to create the boxes for the user's answers
def render_input_widgets(preguntas_filtradas, pregunta_actual):
    col1, col2, col3 = st.columns(3)
    if preguntas_filtradas[pregunta_actual].no_answers == 1:
        response1 = col1.number_input(f"{preguntas_filtradas[pregunta_actual].a1_name}", key=f"response1_{preguntas_filtradas[pregunta_actual]}", value=0.00)
        response2 = 0.0
        response3 = 0.0
    elif preguntas_filtradas[pregunta_actual].no_answers == 2:
        response1 = col1.number_input(f"{preguntas_filtradas[pregunta_actual].a1_name}", key=f"response1_{preguntas_filtradas[pregunta_actual]}", value=0.00)
        response2 = col2.number_input(f"{preguntas_filtradas[pregunta_actual].a2_name}", key=f"response2_{preguntas_filtradas[pregunta_actual]}", value=0.00)
        response3 = 0.0
    elif preguntas_filtradas[pregunta_actual].no_answers == 3:
        response1 = col1.number_input(f"{preguntas_filtradas[pregunta_actual].a1_name}", key=f"response1_{preguntas_filtradas[pregunta_actual]}", value=0.00)
        response2 = col2.number_input(f"{preguntas_filtradas[pregunta_actual].a2_name}", key=f"response2_{preguntas_filtradas[pregunta_actual]}", value=0.00)
        response3 = col3.number_input(f"{preguntas_filtradas[pregunta_actual].a3_name}", key=f"response3_{preguntas_filtradas[pregunta_actual]}", value=0.00)
  
    return response1, response2, response3

#Function to evaluate the user's answers
def resultado(preguntas_filtradas, response1, response2, response3,pregunta_actual):
    respx1 = preguntas_filtradas[pregunta_actual].answer1
    respx2 = preguntas_filtradas[pregunta_actual].answer2
    respx3 = preguntas_filtradas[pregunta_actual].answer3

    outxt = 'Error'
    cont = 0
    if preguntas_filtradas[pregunta_actual].no_answers == 1:
        if (respx1 - response1)<0.1:
            outxt = 'Felicitaciones!!!! La respuesta es correcta.'
            cont = 1
        else:
            outxt = 'La respuesta no es correcta, presione el boton de "Ayuda", o trate de nuevo.'
    elif preguntas_filtradas[pregunta_actual].no_answers == 2:
        if (abs(respx1 - response1)>0.1) and (abs(respx2 - response2)>0.1):
            outxt = 'Las respuestas no son correctas, presione el boton de "Ayuda", o trate de nuevo.'
        else:
            if (abs(respx1 - response1)<0.1) and (abs(respx2 - response2)<0.1):
                outxt ='Felicitaciones!!!! La respuesta es correcta.'
                cont = 1
            elif (abs(respx1 - response1)<0.1) and (abs(respx2 - response2)>0.1):
                outxt = 'Solamente la primera respuesta es correcta, presione el boton de "Ayuda", o trate de nuevo.'
            elif (abs(respx1 - response1)>0.1) and (abs(respx2 - response2)<0.1):
                outxt = 'Solamente la segunda respuesta es correcta, presione el boton de "Ayuda", o trate de nuevo.'
                
    elif preguntas_filtradas[pregunta_actual].no_answers == 3:
        if abs(respx1 - response1)>0.1 and abs(respx2 - response2)>0.1 and abs(respx3 - response3)>0.1:
            outxt = 'Las respuestas no son correctas, presione el boton de "Ayuda", o trate de nuevo.'
        else:
            if  abs(respx1 - response1)<0.1 and abs(respx2 - response2)<0.1 and abs(respx3 - response3)<0.1:
                outxt = 'Felicitaciones!!!! La respuesta es correcta.'
                cont = 1
            if  abs(respx1 - response1)<0.1 and abs(respx2 - response2)>0.1 and abs(respx3 - response3)>0.1:
                outxt = 'Solamente la primera respuesta es correcta, presione el boton de "Ayuda", o trate de nuevo.'
            elif  abs(respx1 - response1)>0.1 and abs(respx2 - response2)<0.1 and abs(respx3 - response3)>0.1:
                outxt = 'Solamente la segunda respuesta es correcta, presione el boton de "Ayuda", o trate de nuevo.'
            elif  abs(respx1 - response1)>0.1 and abs(respx2 - response2)>0.1 and abs(respx3 - response3)<0.1:
                outxt = 'Solamente la tercera respuesta es correcta, presione el boton de "Ayuda", o trate de nuevo.'
            elif (respx1 - response1)<0.1 and abs(respx2 - response2)<0.1 and abs(respx3 - response3)>0.1:
                outxt = 'Solamente las dos primeras respuestas son correctas, presione el boton de "Ayuda", o trate de nuevo.'
            elif (respx1 - response1)<0.1 and abs(respx2 - response2)>0.1 and abs(respx3 - response3)<0.1:
                outxt = 'Solamente la primera y la tercera respuesta son correctas, presione el boton de "Ayuda", o trate de nuevo.'
            elif  abs(respx1 - response1)>0.1 and abs(respx2 - response2)<0.1 and abs(respx3 - response3)<0.1:
                outxt = 'Solamente la la segunda y la tercera respuesta son correctas, presione el boton de "Ayuda", o trate de nuevo.'
    
    return outxt, cont

#Function to Generate the Question Image 
def filtrar_imagenes_preguntas(pregunta_no,version_no, subtopic, difficulty):
    left_col, center_col, right_col = st.columns(3)
    #with left_col:
        #st.write("")

    #with right_col:
        #st.write("")
    with center_col:
        if difficulty == "Fácil":
            if subtopic == "Vectores 2D" or subtopic == "Vector unitario":
                if  pregunta_no <= 2: #Vectores 2D y Vector unitario
                    if version_no == 1:
                        st.image(image_paths[0], width=325) 
                    elif version_no == 2:
                        st.image(image_paths[1], width=350)
                    elif version_no == 3:
                        st.image(image_paths[2], width=350)
                    elif version_no == 4:
                        st.image(image_paths[3], width=350)   
                    
                elif pregunta_no > 2 and pregunta_no<=4: #Vectores 2D y Vector unitario
                    if  version_no==1:
                        st.image(image_paths[4], width=200)
                    elif version_no==2:
                        st.image(image_paths[5], width=200)
                    elif version_no==3:
                        st.image(image_paths[6], width=200)
                    elif version_no==4:
                        st.image(image_paths[7], width=200)

        
        if difficulty == "Medio":
            if subtopic == "Vectores 2D":
                if pregunta_no == 1:
                    if version_no == 1:
                        st.image(image_paths[8],width=250)
                    elif version_no == 2:
                        st.image(image_paths[9])
                    elif version_no == 3:
                        st.image(image_paths[10])
                    elif version_no == 4:
                        st.image(image_paths[11])
                
                if pregunta_no == 2:
                    if version_no == 1:
                        st.image(image_paths[12],width=300)
                    elif version_no == 2:
                        st.image(image_paths[13])
                    elif version_no == 3:
                        st.image(image_paths[14])
                    elif version_no == 4:
                        st.image(image_paths[15])
                
                if pregunta_no == 3:
                    st.image(image_paths[16],width=330)

                if pregunta_no == 4:
                    st.image(image_paths[17],width=180)
        
        if difficulty == "Díficil":
            if subtopic == "Vectores 2D":
                if pregunta_no == 1 or pregunta_no == 2:
                    if version_no == 1:
                        st.image(image_paths[18])
                    elif version_no == 2:
                        st.image(image_paths[19],width=250)
                    elif version_no == 3:
                        st.image(image_paths[20],width=250)
                    elif version_no == 4:
                        st.image(image_paths[21],width=250)
                if pregunta_no == 3:
                    if version_no == 1:
                        st.image(image_paths[22],width=250)
                    elif version_no == 2:
                        st.image(image_paths[23],width=250)
                    
    return

#Function to Generate the Answer Image 
def filtrar_imagenes_respuestas_P1(pregunta_no,version_no, subtopic, difficulty):
    left_col, center_col, right_col = st.columns(3)

    with left_col:
        if difficulty == "Díficil":
            if subtopic == "Vectores 2D":
                if  pregunta_no == 1 or pregunta_no == 2: 
                    if version_no == 1:
                        st.image(rtas_paths[0], width=600) 
                    elif version_no == 2:
                        st.image(rtas_paths[1])
                    elif version_no == 2:
                        st.image(rtas_paths[2])
                    elif version_no == 2:
                        st.image(rtas_paths[3])
                if  pregunta_no == 3: 
                    if version_no == 1:
                        st.image(rtas_paths[4]) 
                    elif version_no == 2:
                        st.image(rtas_paths[5])
    return

#Function to create "Ayuda" button, it shows the helps sequentially
def butt_ayuda(preguntas_filtradas, pregunta_actual,ayuda_clicked):
        ayudas = [preguntas_filtradas[st.session_state.pregunta_actual].ayuda1, preguntas_filtradas[st.session_state.pregunta_actual].ayuda2, preguntas_filtradas[st.session_state.pregunta_actual].ayuda3]
        
        ayudas_no_vacias = [ayuda for ayuda in ayudas if ayuda.strip() != ""]
        if 'ayuda_index' not in st.session_state:
            st.session_state.ayuda_index = 0 
        if ayuda_clicked:
            if ayudas_no_vacias:
                help_text_placeholder = st.empty() 
                help_text_placeholder.write(ayudas[st.session_state.ayuda_index])
                st.session_state.ayuda_index = (st.session_state.ayuda_index + 1) %len(ayudas_no_vacias)

# Function to Generate a New Version of the Question  
def nueva_version_callback():
    no_pregunta_actual = preguntas_filtradas[st.session_state.pregunta_actual].no_pregunta
    preguntas_actuales = [pregunta for pregunta in preguntas_filtradas if pregunta.no_pregunta == no_pregunta_actual]
    versiones = sorted(set([pregunta.version for pregunta in preguntas_actuales]))
    
    if len(versiones) == 1:
        misma_pregunta = preguntas_filtradas[st.session_state.pregunta_actual]
        misma_pregunta.regenerate_values()
        st.session_state.Intento = 0
    else:
        indice_version_actual = versiones.index(st.session_state.version_actual)
        siguiente_version = (indice_version_actual + 1) % len(versiones)
        st.session_state.version_actual = versiones[siguiente_version]

        for i, pregunta in enumerate(preguntas_filtradas):
            if pregunta.no_pregunta == no_pregunta_actual and pregunta.version == st.session_state.version_actual:
                st.session_state.pregunta_actual = i
                st.session_state.Intento = 0
                break
                
# Function to Generate a New Problem
def nuevo_problema_callback():
    nuevo_problema = st.session_state.pregunta_actual + 1
    while nuevo_problema < len(preguntas_filtradas) and preguntas_filtradas[nuevo_problema].no_pregunta == preguntas_filtradas[st.session_state.pregunta_actual].no_pregunta:
        nuevo_problema += 1
    if nuevo_problema >= len(preguntas_filtradas):
        nuevo_problema = 0
    st.session_state.pregunta_actual = nuevo_problema
    st.session_state.version_actual = 1 
    st.session_state.Intento = 0

#Initialize the "Intento" Variable to Count the Number of User's Attempts to Verify Their Answer
if 'Intento' not in st.session_state:
    st.session_state.Intento = 0
#Initialize the State for the "mostrar_respuesta" Function When the User Verifies Their Answer
if 'mostrar_respuesta' not in st.session_state:
    st.session_state.mostrar_respuesta = False
#Initialize the questions to show
if 'pregunta_actual' not in st.session_state:
    st.session_state.pregunta_actual = 0 
#Initialize the version of the question to show    
if 'version_actual' not in st.session_state:    
    st.session_state.version_actual = 1

#Function to Display the Answer Explanation
def mostrar_respuesta():
    st.write(preguntas_filtradas[st.session_state.pregunta_actual].respuesta_P1)
    filtrar_imagenes_respuestas_P1(preguntas_filtradas[st.session_state.pregunta_actual].no_pregunta, preguntas_filtradas[st.session_state.pregunta_actual].version, preguntas_filtradas[st.session_state.pregunta_actual].subtopic, preguntas_filtradas[st.session_state.pregunta_actual].complexity)
    st.write(preguntas_filtradas[st.session_state.pregunta_actual].respuesta_P2) 

#Function to display the Answer Explanation for the "Quiero ver la respuesta" button
def on_button_click():
    st.session_state.mostrar_respuesta = True

#Function to generate the questions
def generate_questions():
 
    st.markdown('<h3 style="font-size:18px;">Pregunta</h3>', unsafe_allow_html=True) #Title Pregunta
    st.write(preguntas_filtradas[st.session_state.pregunta_actual].pregunta) #Write the statement question
    filtrar_imagenes_preguntas(preguntas_filtradas[st.session_state.pregunta_actual].no_pregunta, preguntas_filtradas[st.session_state.pregunta_actual].version, preguntas_filtradas[st.session_state.pregunta_actual].subtopic, preguntas_filtradas[st.session_state.pregunta_actual].complexity) #Select the image
    

    st.markdown('<h3 style="font-size:18px;">Respuestas</h3>', unsafe_allow_html=True) #Title Respuestas
    st.markdown('<p style="font-size: 14px;">Ingrese sus respuestas con dos decimales</p>', unsafe_allow_html=True) #Title of instructions
    response1, response2, response3 = render_input_widgets(preguntas_filtradas,st.session_state.pregunta_actual) #Create boxes to the user's answers

    st.markdown('<h3 style="font-size:18px;">Acciones</h3>', unsafe_allow_html=True) #Title Acciones
    
    #Create butttons
    respuesta_pressed, ayuda_pressed, repetir_pressed, nuevo_pressed = st.columns(4)
    respuesta_clicked = respuesta_pressed.button("Verificar respuesta", key=f"respuesta_button_{st.session_state.pregunta_actual}", help="Explicación de la respuesta", use_container_width=True)
    ayuda_clicked = ayuda_pressed.button("Ayuda", key=f"ayuda_button_{st.session_state.pregunta_actual}", help="Ayuda para la solución", use_container_width=True)
    repetir_pressed.button("Nueva versión", key="nueva_version_button", help="Genera una nueva versión del problema", use_container_width=True, on_click=nueva_version_callback)
    nuevo_pressed.button("Siguiente problema", key=f"nuevo_problema_button{st.session_state.pregunta_actual}", help="Genera un nuevo problema", use_container_width=True, on_click=nuevo_problema_callback)

    return response1, response2, response3, respuesta_clicked, ayuda_clicked

#Function main
def main():
    
    response1, response2, response3, respuesta_clicked, ayuda_clicked = generate_questions()

    # "Verificar respuesta" button - Evaluation of the validity of the result input by user
    if respuesta_clicked:
        st.session_state.Intento +=1
        outputx, is_correct = resultado(preguntas_filtradas, response1, response2, response3, st.session_state.pregunta_actual)
        st.write(outputx)
        if is_correct == 1:
            st.session_state.mostrar_respuesta = True
            mostrar_respuesta()
        elif is_correct == 0:
            #st.write(f"Intentos: {st.session_state.Intento}") #Display the number of Attempts
            if st.session_state.Intento >3:
                st.button(":pensive: Quiero ver la respuesta",key=f"ver_respuesta_button{st.session_state.pregunta_actual}", help="Permite ver la respuesta", on_click = on_button_click)
    
    if st.session_state.mostrar_respuesta:
        mostrar_respuesta()
        st.session_state.mostrar_respuesta = False
                
    # "Ayuda" button - It shows helps 
    if ayuda_clicked:    
        butt_ayuda(preguntas_filtradas,st.session_state.pregunta_actual,ayuda_clicked)

if __name__ == '__main__':
    main()
