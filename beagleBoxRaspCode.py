import RPi.GPIO as GPIO
import time
import serial

#Configura a serial e a velocidade de transmissao
ser = serial.Serial("/dev/ttyAMA0", 9600,timeout = 1)

GPIO.setmode(GPIO.BOARD)

#Define o pino do botao como entrada
GPIO.setup(18, GPIO.IN)

#Mensagem inicial
print ("Comunicacao Rasp <-> Arduino BeagleBox")

while(1):
        dado = raw_input("Digite o comando: ")
        ser.write(dado)
        #print("Enviado"+dado)
        #Aguarda reposta
        if (dado == 'q'):
                resposta = ser.readline()
                #Mostra na tela a resposta enviada pelo Arduino
                print resposta
        if (dado == 'e'):
                resposta = ser.readline()
                print resposta
        #Aguarda 0,5 segundos e reinicia o processo
        time.sleep(0.5)
