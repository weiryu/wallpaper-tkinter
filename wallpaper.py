# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 09:48:00 2017

@author: Unknow
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 12:55:02 2016

@author: weir
"""

from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
import urllib.request
import re
import time
import win32gui,win32con,win32api
import os
import shutil


# 主窗口函数
class MainWindow:

    def buttonListener1(self,event):
        bing_wallpaper()
    def buttonListener2(self,event):
        nationalgeographic_wallpaper()
    def buttonListener3(self,event):
        wallheaven_wallpaper()
    def buttonListener4(self,event):
        pass
    def buttonListener5(self,event):  
        pass
    def buttonListener6(self,event):
        pass
            
        
    def  __init__(self):
        self.frame = Tk()    
        self.frame.title ("Wallpaper")        
       
        menubar = Menu(self.frame)
              
        # 创建下拉菜单setting
        settingmenu = Menu(menubar, tearoff=0)
        settingmenu.add_command(label="壁纸默认文件夹", command=set_file_save_dictionary)
        settingmenu.add_command(label="清空本地壁纸", command=delete_wallpaper)
        menubar.add_cascade(label="设置",menu=settingmenu)
        # 分隔线
        # filemenu.add_separator()
        
        # 创建下拉菜单Help
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="关于软件", command=about_software_information)
        helpmenu.add_command(label="使用说明", command=usage_help_information)
        menubar.add_cascade(label="帮助", menu=helpmenu)
        
        # 显示菜单
        self.frame.config(menu=menubar)        
                
        self.button1 = Button(self.frame,text = "bing每日壁纸",width = 15,height = 3,bg='DarkOrchid',fg='GhostWhite',relief="flat")
        self.button2 = Button(self.frame,text = "国家地理每日壁纸",width = 15,height = 3,bg='DarkOrchid',fg='GhostWhite',relief="flat")
        self.button3 = Button(self.frame,text = "wallheaven每日壁纸",width = 15,height = 3,bg='DarkOrchid',fg='GhostWhite',relief="flat")
        # 新功能预留        
        #self.button4 = Button(self.frame,text = "默认壁纸保存位置",width = 15,height = 3,bg='DarkOrchid',fg='GhostWhite',relief="flat")
        # 新功能预留
        #self.button5 = Button(self.frame,text = "清空本地壁纸",width = 15,height = 3,bg='DarkOrchid',fg='GhostWhite',relief="flat")
        # 新功能预留
        #self.button6 = Button(self.frame,text = "关于软件",width = 15,height = 3,bg='DarkOrchid',fg='GhostWhite',relief="flat")        

        #sticky选项指定对齐方式
        self.button1.grid(row = 0,column = 0,padx = 15,pady = 6,sticky=W+E+N+S)
        self.button2.grid(row = 0,column = 1,padx = 15,pady = 6,sticky=W+E+N+S)
        self.button3.grid(row = 1,column = 0,padx = 15,pady = 6,sticky=W+E+N+S)
        #self.button4.grid(row = 1,column = 1,padx = 15,pady = 6,sticky=W+E+N+S)
        #self.button5.grid(row = 2,column = 0,padx = 15,pady = 6,sticky=W+E+N+S)
        # 新功能预留
        #self.button6.grid(row = 2,column = 1,padx = 15,pady = 6,sticky=W+E+N+S)

        '''        
        bind代替command命令
        self.button1.bind("<Enter>",self.buttonListener1)#绑定回车
        self.button2.bind("<ButtonRelease-1>",self.buttonListener2)#绑定鼠标左键释放
        self.button3.bind("<Button-1>",self.buttonListener3)#绑定鼠标左键按下
        '''
        
        self.button1.bind("<ButtonRelease-1>",self.buttonListener1)
        self.button2.bind("<ButtonRelease-1>",self.buttonListener2)
        self.button3.bind("<ButtonRelease-1>",self.buttonListener3)
        #self.button4.bind("<ButtonRelease-1>",self.buttonListener4)
        #self.button5.bind("<ButtonRelease-1>",self.buttonListener5)
        # 新功能预留
        #self.button6.bind("<ButtonRelease-1>",self.buttonListener6)
        
        self.frame.mainloop()      


 
# 读取壁纸保存目录函数
def dictionary_get():
    # 设定第一次使用时默认壁纸保存目录
    if not os.path.isfile("壁纸保存目录.txt"):
        with open("壁纸保存目录.txt","w") as fp:
            fp.write("E:\壁纸")
            fp.close()
    # 读取壁纸保存目录
    with open("壁纸保存目录.txt","r") as fp:
        local = fp.read()
        fp.close()                
    return local

# 清空本地壁纸函数    
def delete_wallpaper():
    ask = tkinter.messagebox.askquestion('askquestion messagebox', '您确定要清空保存壁纸的文件夹吗?')
    if 'yes' == ask:
        local = dictionary_get()
        # 判断文件夹是否存在
        if os.path.exists(local):
            # 清空文件夹
            shutil.rmtree(local)           
    elif 'no' == ask:
        pass
    
# 相关信息模块函数
def about_software_information():
    tkinter.messagebox.showinfo(title = "关于软件",message = " 感谢您的使用\n Version 1.2\n Copyright@weir\n 2017.01",icon="info")        

def usage_help_information():
    tkinter.messagebox.showinfo(title = "使用说明",message = "本软件仅供技术交流使用，请勿用于商业用途\n相关图片版权归著作权人所有，请勿用于商业用途",icon="info")

# 设置壁纸保存文件夹函数
def set_file_save_dictionary():
    global local
    local=tkinter.filedialog.askdirectory()
    if local == "":
        pass
    else:
        with open("壁纸保存目录.txt","w") as fp:
            fp.write(local)
            fp.close()
            

       
# 设置壁纸函数（共用）
def setWallpaper(imagepath):
    k=win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(k,"WallpaperStyle",0,win32con.REG_SZ,"2")#2拉伸适应桌面，0桌面居中
    win32api.RegSetValueEx(k,"TileWallpaper",0,win32con.REG_SZ,"0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,imagepath,1+2)


# 通用网址解码函数
def open_url(url):
    # 增加浏览器头，防止反爬虫屏蔽
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
               'Referer':'https://alpha.wallhaven.cc/latest',
               'Connection':'keep-alive'}    
    # 异常处理
    try:
        req=urllib.request.Request(url,headers = headers)
        page=urllib.request.urlopen(req)
    except urllib.request.URLError as e:
        if hasattr(e,"reason"):
            print("Failed to reach the server")
            print("The reason:",e.reason)
        elif hasattr(e,"code"):
            print("The server couldn't fulfill the request")
            print("Error code:",e.code)
            print("Return content:",e.read())
    else:
        pass             
    html=page.read().decode('UTF-8')
    return html 


   
# 获得bing图片
def get_bing_img(html):    
    # 在这里local指定文件保存的文件夹位置！！！！！
    local = dictionary_get()
    local_bing = local+"\\"+"bing_wallpaper"
    # 正则匹配获得图片,可以匹配jpg和jpeg格式
    p='/az/.*?\.jpe*g'
    imglist=re.findall(p,html)
    print(imglist)
    # 获得系统时间作为文件名
    time.localtime(time.time())
    n=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    # 设定文件名，获得文件名后缀图片类型 
    filetype = imglist[0].split('.')[-1]
    filename='bing-'+str(n)+"."+str(filetype)
    # 修改当天更换过壁纸后无法再次更换的bug
    imagepath= local_bing+"\\"+filename       
    # 判断当前文件夹是否存在
    if not os.path.exists(local_bing):
        os.mkdir(local_bing)
    # 判断当前壁纸是否存在
    if os.path.isfile(local_bing+"\\"+filename):
        print("您今天已经更换过壁纸了")
    else:
        # 保存壁纸文件，返回文件位置
        bing_final_url = r'http://cn.bing.com'+imglist[0]
        urllib.request.urlretrieve(bing_final_url,imagepath)
    return imagepath

# bing壁纸主函数        
def bing_wallpaper():
    #bing主页网址
    url='http://cn.bing.com/?scope=web'
    imagepath=get_bing_img(open_url(url))
    setWallpaper(imagepath)

    
# 获得国家地理图片
def get_nationalgeographic_img(html):
    local = dictionary_get()
    local_nationalgeographic = local+"\\"+"nationalgeographic"
    p=r'/photography/.*?\.html'
    urllist=list(re.findall(p,html))
    new_urllist=[]
    for url in urllist:
        if urllist.count(url)>3:
            new_urllist.append(url)
    new_url = r"http://www.nationalgeographic.com.cn"+new_urllist[0]
    new_html=open_url(new_url)
    q=r"http://image.nationalgeographic.com.cn/.\d+/.\d+/.\d+.jpe*g"
    imglist=list(re.findall(q,new_html))
    n=time.strftime('%Y-%m-%d-%H',time.localtime(time.time()))    
    filetype = imglist[len(imglist)-1].split(".")[-1]    
    filename='national-geographic'+str(n)+"."+str(filetype)
    if not os.path.exists(local_nationalgeographic):
        os.mkdir(local_nationalgeographic)
    if os.path.isfile(local_nationalgeographic+"\\"+filename):
        print("您今天已经更换过壁纸了")
    else:
        urllib.request.urlretrieve(imglist[len(imglist)-1],local_nationalgeographic+"\\"+filename)
    # 修改当天更换过壁纸后无法再次更换的bug
    imagepath = local_nationalgeographic+"\\"+filename       
    return imagepath

#国家地理壁纸主函数        
def nationalgeographic_wallpaper():
    url = 'http://www.nationalgeographic.com.cn/photography/photo_of_the_day/'
    imagepath = get_nationalgeographic_img(open_url(url))
    setWallpaper(imagepath)


# 获得wallheaven图片    
def get_wallheaven_img(html):    
    local = dictionary_get()
    local_wallheaven = local+"\\"+"wallheaven"
    # 正则匹配获得图片网址
    # .\d+ 匹配出数字id,\d表示数字，+表示多位
    p='data-wallpaper-id=.\d+'
    imglist=re.findall(p,html)
    picture_id=imglist[0].replace("data-wallpaper-id=","").replace("\"","")
    # 获得中继网址
    temp_url=r"https://alpha.wallhaven.cc/wallpaper/"+str(picture_id)
    temp_html = open_url(temp_url)
    q ='<meta property="og:image" content="//wallpapers.wallhaven.cc/wallpapers/full/.*?" />'
    temp_result = re.findall(q,temp_html)
    temp_result[0] = temp_result[0].replace('<meta property="og:image" content=','').replace("/>","").replace("\"","")
    # 得到图片类型    
    filetype = temp_result[0].split('.')[-1]
    # 获得图片最终网址
    result = 'https:'+str(temp_result[0])
    # 获得系统时间作为文件名   
    time.localtime(time.time())
    # 针对该网站每日多张的特殊情况修改文件命名方式
    n=time.strftime('%Y-%m-%d-%H',time.localtime(time.time()))
    #设定文件名
    filename='wallhaven-'+str(n)+'.'+str(filetype)
    # 判断当前文件夹是否存在
    if not os.path.exists(local_wallheaven):
        os.mkdir(local_wallheaven)
    # 判断当前壁纸是否存在
    if os.path.isfile(local_wallheaven+"\\"+filename):
        print("您今天已经更换过壁纸了")
    else:
        # 保存壁纸文件，返回文件位置。直接使用urllib.request.urlretrieve函数会被封，必须增加opener
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(result, local_wallheaven+"\\"+filename)
    imagepath= local_wallheaven+"\\"+filename       
    return imagepath

# wallheaven壁纸主函数
def wallheaven_wallpaper():
    url='https://alpha.wallhaven.cc/latest'
    imagepath=get_wallheaven_img(open_url(url))
    setWallpaper(imagepath)     


# 主函数
if __name__=="__main__":
    window = MainWindow()
    
    
