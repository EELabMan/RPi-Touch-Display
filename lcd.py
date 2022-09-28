from tkinter import*
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)
GPIO.output(21,GPIO.LOW)
duty = 0
root = Tk()
# setting attribute
root.title("My Project")

def ledOn(event):
    global fade
    fade=False
    GPIO.output(21, GPIO.HIGH)


def ledOff(event):
    global fade
    fade=False
    GPIO.output(21, GPIO.LOW)


def ledFade(event):
    pwm = GPIO.PWM(21, 2000) # PWM frequency in Hz
    pwm.start(duty) # start at 0%
    GPIO.output(21, GPIO.LOW)

    for dc in range(1, 101, 1): # Increase duty cycle: 0~100
        pwm.ChangeDutyCycle(dc) # Change duty cycle
        time.sleep(0.02)
    for dc in range(100, 0, -1): # Decrease duty cycle: 100~0
        pwm.ChangeDutyCycle(dc)
        time.sleep(0.02)

button_1 = Button(root, text="Turn on LED")
button_1.config(height=5, width=40)
button_1.bind("<Button-1>", ledOn)
button_2 = Button(root, text="Turn off LED")
button_2.config(height=5, width=40)
button_2.bind("<Button-1>", ledOff)
button_3 = Button(root, text="Fade LED")
button_3.config(height=5, width=40)
button_3.bind("<Button-1>", ledFade)
button_1.pack()
button_2.pack()
button_3.pack()


root.mainloop()





