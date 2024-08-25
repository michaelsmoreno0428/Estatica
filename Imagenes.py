#Paths of the images
image_paths=[]
image_paths= [
#Vectores 2D _ Cálculo de los ángulos _ Nivel fácil
"https://github.com/lbtriana/Estatica/blob/main/Imagenes/EQ/Fvec_0a.png", #[0] Pregunta < 2 _ 0 <alpha_x <= 90
#"C:\Users\Luisa\Videos\Estatica\Imagenes\Preguntas\EQ\Fvec_0a.png"
#"C:\Users\Luisa\Videos\Estatica\Imagenes\EQ\Fvec_0a.png"
#Imagenes/EQ/Fvec_0a.png
"D:/Estática/App/Imagenes/EQ/Fvec_0b.png", #[1] Pregunta < 2 _ 90 <alpha_x <= 180
"D:/Estática/App/Imagenes/EQ/Fvec_0c.png", #[2] Pregunta < 2 _ 180 <alpha_x <= 270
"D:/Estática/App/Imagenes/EQ/Fvec_0d.png", #[3] Pregunta < 2 _ 270 <alpha_x <= 360

#Vectores 2D _ Distancia Pendiente _ Nivel fácil
"D:/Estática/App/Imagenes/EQ/Lvec_0a.png", #[4] Pregunta < 4 _ x1p < x2p and y1p < y2p
"D:/Estática/App/Imagenes/EQ/Lvec_0b.png", #[5] Pregunta < 4 _ x1p > x2p and y1p > y2p
"D:/Estática/App/Imagenes/EQ/Lvec_0c.png", #[6] Pregunta < 4 _ x1p > x2p and y1p < y2p
"D:/Estática/App/Imagenes/EQ/Lvec_0d.png", #[7] Pregunta < 4 _ x1p < x2p and y1p > y2p

#Vectores 2D _ Vector resultante _ Nivel medio
"D:/Estática/App/Imagenes/EQ/V2D/EQ_V2_M_1a.png", #[8] Pregunta 1 _ Versión 1 _ Nivel medio
"D:/Estática/App/Imagenes/EQ/V2D/EQ_V2_M_1b.png", #[9] Pregunta 1 _ Versión 2 _ Nivel medio
"D:/Estática/App/Imagenes/EQ/V2D/EQ_V2_M_1c.png", #[10] Pregunta 1 _ Versión 3 _ Nivel medio
"D:/Estática/App/Imagenes/EQ/V2D/EQ_V2_M_1d.png", #[11] Pregunta 1 _ Versión 4 _ Nivel medio

#Vectores 2D _ Vector resultante _ Nivel medio
"D:/Estática/App/Imagenes/EQ/V2D/EQ_V2_M_2a.png", #[12] Pregunta 2 _ Versión 1 _ Nivel medio
"D:/Estática/App/Imagenes/EQ/V2D/EQ_V2_M_2b.png", #[13] Pregunta 2 _ Versión 2 _ Nivel medio
"D:/Estática/App/Imagenes/EQ/V2D/EQ_V2_M_2c.png", #[14] Pregunta 2 _ Versión 3 _ Nivel medio
"D:/Estática/App/Imagenes/EQ/V2D/EQ_V2_M_2d.png", #[15] Pregunta 2 _ Versión 4 _ Nivel medio

#Vectores 2D _ Vector resultante _ Nivel medio
"D:/Estática/App/Imagenes/EQ/V2D/EQ_V2_M_3a.png", #[16] Pregunta 3 _ Versión 1 _ Nivel medio

#Vectores 2D _ Vector resultante _ Nivel medio
"D:/Estática/App/Imagenes/EQ/V2D/EQ_V2_M_4a.png", #[17] Pregunta 4 _ Todas _ Nivel medio

#Vectores 2D _ Componentes u y v _ Nivel díficil
"D:/Estática/App/Imagenes/EQ/V2D/EQ_V2_D_1a.png", #[18] Pregunta 1 y 2 _ Versión 1 _ Nivel díficil
"D:/Estática/App/Imagenes/EQ/V2D/EQ_V2_D_1b.png", #[19] Pregunta 1 y 2 _ Versión 2 _ Nivel díficil
"D:/Estática/App/Imagenes/EQ/V2D/EQ_V2_D_1c.png", #[20] Pregunta 1 y 2 _ Versión 3 _ Nivel díficil
"D:/Estática/App/Imagenes/EQ/V2D/EQ_V2_D_1d.png", #[21] Pregunta 1 y 2 _ Versión 4 _ Nivel díficil

#Vectores 2D _ Componentes u y v _ Nivel díficil
"D:/Estática/App/Imagenes/EQ/V2D/EQ_V2_D_3a.png", #[22] Pregunta 3 _ Versión 1 _ Nivel díficil
"D:/Estática/App/Imagenes/EQ/V2D/EQ_V2_D_3b.png", #[23] Pregunta 3 _ Versión 1 _ Nivel díficil


"D:/Estática/App/Imagenes/EQ/V2D/EQ_V2_D_2a.png", #[19] Pregunta 1 y 2 _ Versión 1 _ Nivel díficil





#Vectores 3D _ Ángulos _ Nivel fácil
"D:/Estática/App/Imagenes/EQ/V3D/EQ_V3_F_1a.png", #[18] Pregunta 1 y 2 _ Versión 1 _ Nivel fácil
"D:/Estática/App/Imagenes/EQ/V3D/EQ_V3_F_1b.png", #[19] Pregunta 1 y 2 _ Versión 2 _ Nivel fácil
"D:/Estática/App/Imagenes/EQ/V3D/EQ_V3_F_1c.png", #[20] Pregunta 1 y 2 _ Versión 3 _ Nivel fácil
"D:/Estática/App/Imagenes/EQ/V3D/EQ_V3_F_1d.png", #[21] Pregunta 1 y 2 _ Versión 4 _ Nivel fácil

#Vectores 3D _ Componentes _ Nivel fácil
"D:/Estática/App/Imagenes/EQ/V3D/EQ_V3_F_2a.png", #[23] Pregunta 1 y 2 _ Versión 1 _ Nivel fácil
"D:/Estática/App/Imagenes/EQ/V3D/EQ_V3_F_2b.png", #[24] Pregunta 1 y 2 _ Versión 2 _ Nivel fácil
"D:/Estática/App/Imagenes/EQ/V3D/EQ_V3_F_2c.png", #[25] Pregunta 1 y 2 _ Versión 3 _ Nivel fácil
"D:/Estática/App/Imagenes/EQ/V3D/EQ_V3_F_2d.png", #[26] Pregunta 1 y 2 _ Versión 4 _ Nivel fácil

]

rtas_paths= [
#Vectores 2D _ Ejes arbitrarios _ Nivel díficil
"D:/Estática/App/Respuestas/EQ/V2D/R_EQ_V2D_D_1a.png", #[0] Pregunta 1 _ Versión 1 _ Nivel díficil
"D:/Estática/App/Respuestas/EQ/V2D/R_EQ_V2D_D_1b.png", #[1] Pregunta 1 _ Versión 2 _ Nivel díficil
"D:/Estática/App/Respuestas/EQ/V2D/R_EQ_V2D_D_1c.png", #[2] Pregunta 1 _ Versión 3 _ Nivel díficil
"D:/Estática/App/Respuestas/EQ/V2D/R_EQ_V2D_D_1d.png", #[3] Pregunta 1 _ Versión 4 _ Nivel díficil

#Vectores 2D _ Ejes arbitrarios _ Nivel díficil
"D:/Estática/App/Respuestas/EQ/V2D/R_EQ_V2D_D_2a.png", #[4] Pregunta 3 _ Versión 1 _ Nivel díficil
"D:/Estática/App/Respuestas/EQ/V2D/R_EQ_V2D_D_2b.png", #[5] Pregunta 3 _ Versión 2 _ Nivel díficil
]
