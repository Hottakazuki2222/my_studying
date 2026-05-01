#tkiinter laerning
import tkinter

root = tkinter.Tk()
root.title('tkinter学習')
root.geometry('800x600')
######################################部品など処理を記入####################################
class Application(tkinter.Frame): #継承
    def __init__(self,root): #←受け取る
        #処理
        super().__init__(root,width = 800,height = 600,borderwidth = 4,relief = 'groove') #super().__init__(root←わたす)
        #width:境界線の太さ,relief:境界線の種類

        self.root = root
        self.pack()
        self.pack_propagate(0) #サイズ調整
        self.create_widgets()
    
    def create_widgets(self):
        #消すボタンの作成
        quit_btn = tkinter.Button(self) #ボタンのクラス
        quit_btn['text'] = '閉じる'
        quit_btn['command'] = self.root.destroy #土台アプリの終了
        quit_btn.pack(side = 'bottom')
        #テキストボックスの作成
        self.text_box = tkinter.Entry(self)
        self.text_box['width'] = 10
        self.text_box.pack()
        #実行ボタン作成
        submit_btn = tkinter.Button(self) #実行ボタン
        submit_btn['text'] = '実行'
        submit_btn['command'] = self.input_handler
        submit_btn.pack()
        #テキスト読み取り
        self.message = tkinter.Message(self)
        self.message.pack()

        
    def input_handler(self):
        #値の取得
        text = self.text_box.get() #値が取得できる
        self.message['text'] = text + '!!' #文字列を設定

######################################部品など処理を記入####################################
app = Application(root = root)
root.mainloop() #アプリ起動
