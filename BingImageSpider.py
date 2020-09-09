import tkinter as tk, urllib.request as ur, re
import tkinter.filedialog, threading

class Spider():
    def __init__(self, word, length, file_name):
        self.word = word
        self.length = length
        self.file_name = file_name

    def searchImage(self):
        response = ur.urlopen('https://cn.bing.com/images/search?q=' + self.word + '&qs=n&form=QBIR&sp=-1'
                              '&pq=pythonyu%27yan&sc=8-12&sk=&cvid=AFBECCB75C9C438199AFED39457DD443')
        html = response.read().decode()
        self.now, self.end, self.error = 0, 0, 0
        for i in range(int(self.length)):
            try:
                r = re.search(r'"https://tse[0-9]-mm\.cn\.bing\.net/th[?]id=OIP\..*?"', html[self.end:])
                self.now = r.start() + self.end
                self.end = r.end() + self.end
                url = html[self.now + 1: self.end - 1]
                image = ur.urlopen(url).read()
                f = open('C:/Users/Creeper/Desktop/Image/' + self.word + str(i) + '.jpg', 'wb')
                f.write(image)
            except:
                self.error += 1
        message = MessageBox('读取成功, 出现了 %d 个错误' % self.error)


class MessageBox():
    def __init__(self, message):
        root = tk.Tk()
        root.title('提示')
        label = tk.Label(root, text=message, padx=10, pady=5)
        label.pack()
        root.mainloop()

class APP():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Bing图片爬虫')

        label1 = tk.Label(self.root, text='搜索关键词').grid(row=0, column=0,
                                                        padx=10, pady=5)
        label2 = tk.Label(self.root, text='读取张数').grid(row=1, column=0,
                                                        padx=10, pady=5)
        label3 = tk.Label(self.root, text='存储地址:').grid(row=2, column=0,
                                                        padx=10, pady=5)
        label4 = tk.Label(self.root, text='读取过程会有点慢, 请耐心等待').grid(row=3, column=1)
        self.e1 = tk.Entry(self.root)
        self.e2 = tk.Entry(self.root)

        self.e1.grid(row=0, column=1, padx=10, pady=5)
        self.e2.grid(row=1, column=1, padx=10, pady=5)

        button = tk.Button(self.root, text='选择文件夹', command = self.showDialog).grid(row=2, column=1)
        button1 = tk.Button(self.root, text='爬取', command=self.spider).grid(row=3, column=0, sticky=tk.W)
        button2 = tk.Button(self.root, text='退出', command=self.root.quit).grid(row=3, column=2, sticky=tk.W)

        self.root.mainloop()

    def showDialog(self):
        fd = tkinter.filedialog.askdirectory(title='选择文件夹保存')
        self.f = fd + '/'

    def spider(self):
        spider = Spider(self.e1.get(), self.e2.get(), self.f)
        t = threading.Thread(target=spider.searchImage())
        t.start()

if __name__ == '__main__':
    app = APP()