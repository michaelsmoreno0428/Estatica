#class Questionary stores the information of each exercises
class Questionary:
    def __init__(self, code, no_pregunta, topic, subtopic, pregunta, opcion_1, opcion_2, opcion_3, opcion_4, opcion_correcta, ayuda_1, ayuda_2, ayuda_3, respuesta_P1,respuesta_P2):
        self.code = code ##### Topic, Subtopic, No de la pregunta
        self.no_pregunta = no_pregunta
        self.topic = topic
        self.subtopic = subtopic
        self.pregunta_func=pregunta
        self.pregunta = ""
        self.opcion_1 = opcion_1
        self.opcion_2 = opcion_2
        self.opcion_3 = opcion_3
        self.opcion_4 = opcion_4
        self.opcion_correcta = opcion_correcta
        self.ayuda_1 = ayuda_1
        self.ayuda_2 = ayuda_2
        self.ayuda_3 = ayuda_3
        self.respuesta_P1 = respuesta_P1
        self.respuesta_P2 = respuesta_P2

conceptuales = [

    #=================================================EQUILIBRIO DE PARTÍCULAS===================================================
    #-------------------------------------------------       Vectores         ---------------------------------------------------
    #-------------------------------------------------          11#           ---------------------------------------------------

    Questionary(#1
        code = 111,
        no_pregunta = 1,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        pregunta = "",
        opcion_1 = "",
        opcion_2 = "",
        opcion_3 = "",
        opcion_4 = "",
        opcion_correcta = "",
        ayuda_1 = "",
        ayuda_2 = "",
        ayuda_3 = "",
        respuesta_P1 = "",
        respuesta_P2 = "",
        ),
    
    Questionary(#2
        code = 112,
        no_pregunta = 2,
        topic = "Equilibrio de partículas",
        subtopic = "Vectores",
        pregunta = "",
        opcion_1 = "",
        opcion_2 = "",
        opcion_3 = "",
        opcion_4 = "",
        opcion_correcta = "",
        ayuda_1 = "",
        ayuda_2 = "",
        ayuda_3 = "",
        respuesta_P1 = "",
        respuesta_P2 = "",
        ),
     
]