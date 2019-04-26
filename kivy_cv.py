# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import cv2

Builder.load_file('kivy_cv.kv')


class CvCamera(App):
    def build(self):
        self._cap = cv2.VideoCapture(0)
        # UI
        layout2 = BoxLayout(orientation='horizontal', size_hint=(1.0, 1.0))
        # text input
        self.s1Label = Label(
            text='IP', size_hint=(0.1, 1.0))
        slider1 = Slider(size_hint=(0.3, 1.0))
        slider1.bind(value=self.slideCallback)
        layout2.add_widget(self.s1Label)
        layout2.add_widget(slider1)
        # button
        button1 = Button(text='Button', size_hint=(
            0.1, 0.1), pos_hint={"x": 0.2, "y": 0.2})
        button1.bind(on_press=self.buttonCallback)
        self.img1 = Image(size_hint=(1.0, 1.0))

        layout = BoxLayout(orientation='vertical', size_hint=(1.0, 1.0))
        layout.add_widget(self.img1)
        layout.add_widget(layout2)
        layout.add_widget(button1)

        while not self._cap.isOpened():
            pass
        Clock.schedule_interval(self.update, 1.0/30.0)
        return layout

    def slideCallback(self, instance, value):
        # Slider横のLabelをSliderの値に
        self.s1Label.text = 'Slider %s' % int(value)

    def buttonCallback(self, instance):
        # 何かのフラグに使える
        print('Buttn <%s> is pressed.' % (instance))

    def update(self, dt):
        # 基本的にここでOpenCV周りの処理を行なってtextureを更新する
        ret, img = self._cap.read()
        img = cv2.flip(img, 0)
        texture1 = Texture.create(
            size=(img.shape[1], img.shape[0]), colorfmt='bgr')
        texture1.blit_buffer(img.tostring(), colorfmt='bgr', bufferfmt='ubyte')
        self.img1.texture = texture1

    def on_stop(self):
        self._cap.release()


if __name__ == '__main__':
    CvCamera().run()
