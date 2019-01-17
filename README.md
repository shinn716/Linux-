# 一般常用  
sudo su     &nbsp;&nbsp;&nbsp;最高權限  
cd ..		    &nbsp;&nbsp;&nbsp;上一層  
cd usr/pi/	&nbsp;&nbsp;&nbsp;進入pi資料夾  
cat xxxx.py &nbsp;&nbsp;&nbsp;觀看xxxx.py 內容  
ls -l	      &nbsp;&nbsp;&nbsp;目前檔案清單  
clear       &nbsp;&nbsp;&nbsp;清除cmd  
sudo rm -d dirname/ &nbsp;&nbsp;&nbsp;移除目錄  
sudo rm filename    &nbsp;&nbsp;&nbsp;移除檔案  
sudo reboot &nbsp;&nbsp;&nbsp;重新開機    
  
  
# 使用Nano開啟/編譯
sudo nano hello.py	  &nbsp;&nbsp;&nbsp;開啟 hello.py (如果沒有檔案, 自動產生新檔)  
sudo python hello.py  &nbsp;&nbsp;&nbsp;編譯並執行 hello.py  
  
  
# 列出使用的 usb/port 清單  
sudo lsusb            &nbsp;&nbsp;&nbsp;usb	清單  
sudo ls -l /dev/tty* &nbsp;&nbsp;&nbsp;列出所有使用的port (控Arduino常用)  
  
  
# Ipconfig  
ip a  
ip addr  
ip address  
ip addr show  
  
  
# Install  
sudo python2 -m pip list  &nbsp;&nbsp;&nbsp;python2 module 清單  
sudo python3 -m pip list  &nbsp;&nbsp;&nbsp;python3 module 清單  
sudo pip3 install python-osc  &nbsp;&nbsp;&nbsp;安裝 python-osc  
  
  
# 啟動自動執行
切換到root賬戶　　          &nbsp;&nbsp;&nbsp;sudo su  
修改rc.local文件　　        &nbsp;&nbsp;&nbsp;sudo nano /etc/rc.local  
在exit 0 之前添加執行命令　　&nbsp;&nbsp;&nbsp;sudo python /xx/xx/xx.py  
  
 
# 壓縮 解壓縮  
http://note.drx.tw/2008/04/command.html  
  
  
# Module  
sudo pip install xxxx or  
sudo git clone https://github.com/raspberrypi-tw/gpio-game-console.git   
sudo git clone https://github.com/boppreh/keyboard  
sudo git clone https://github.com/attwad/python-osc  
sudo git clone https://github.com/pybluez/pybluez  
sudo git clone https://github.com/pyinstaller/pyinstaller  
sudo git clone https://github.com/pyserial/pyserial  
    
  
# VisualCode on Pi  
1. https://medium.com/@melzoghbi/install-visual-studio-code-on-raspbian-eedc566c616d  
2. https://github.com/stevedesmond-ca/vscode-arm  
  
  
# Processing on Pi  
1. https://pi.processing.org/download/  
  
  
# Pyhton 版本設定
1. https://blog.csdn.net/u011489887/article/details/79099419  
2. https://sites.google.com/view/nardotime/python-%E4%B8%96%E7%95%8C%E5%A5%BD%E5%A5%BD%E7%8E%A9/%E5%A6%82%E4%BD%95%E8%AE%8A%E6%9B%B4python%E9%A0%90%E8%A8%AD%E7%89%88%E6%9C%AC    
  
  
# SSH 連線  
https://sites.google.com/site/raspberrypidiy/pc-to-rpi/ssh  
  
  
# Pi & OSC
1. https://ianshelanskey.com/2014/08/11/raspberry-pi-and-osc-part-1/  
2. https://learn.adafruit.com/raspberry-pi-open-sound-control/setting-up-your-raspberry-pi  
  
  
# pygame has no member  
1. https://blog.csdn.net/W_C_X/article/details/84302186  
  
  
# RPi 安裝  
1. https://home.gamer.com.tw/creationDetail.php?sn=3908401  
2. https://wwssllabcd.github.io/blog/2013/01/31/how-to-setup-raspberry-pi/  
3. http://www.powenko.com/wordpress/01-%E5%A6%82%E4%BD%95%E5%AE%89%E8%A3%9D%E5%92%8C%E5%9F%B7%E8%A1%8C-python-%E7%A8%8B%E5%BC%8F/    
