import speech_recognition as sr
import os
import plyer

r = sr.Recognizer()

run = True

class GetComands:
    def __init__(self):
        pass

    def get_comand(self,value):
        value = value.lower()
        value = value.split(' ')
        print(value)
        if (('дальше' in value)==False):
            if ('відкрий' in value or 'запусти' in value):
                if ('google' in value
                 or 'chrome' in value
                 or ('google' in value and 'chrome' in value)):
                 os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
            if ('привіт' in value):
                plyer.notification.notify(
                    message='Hello Maksym!',
                    app_name='Helper',
                    title='Helper')
            if ('порахуй' in value):
                res_0 = value[1:]
                res_1 = ''
                for i in res_0:
                    res_1 += str(i)

                try:
                    plyer.notification.notify(
                        message=str(eval(res_1)),
                        app_name='Helper',
                        title='Helper')
                except:
                    plyer.notification.notify(
                        message='Error',
                        app_name='Helper',
                        title='Helper')
            if ('запиши' in value):
                res_0 = value[1:]
                res_1 = ''
                for i in res_0:
                    res_1 += str(i)

                f.open('writed.txt', 'w')
                f.write(res_1)
                plyer.notification.notify(
                        message='Готово, все збережено в файл writed.txt',
                        app_name='Helper',
                        title='Helper')
get_comand = GetComands()

while run:
    with sr.Microphone() as source:
        print('Speak anything...')
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio,language='uk-UK')
            get_comand.get_comand(text)
            #print(text)
            if (text.lower()=='пока'):
                run = False
        except:
            print('bad')