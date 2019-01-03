# Linux Command (筆記)
# 一般常用  
sudo ....   最高權限 (ex: sudo lsusb, sudo python hello.py...)  
cd ..		    上一層  
cd usr/pi/	進入pi資料夾  
ls 		      目前檔案清單  
clear 清除cmd  
  
  
# 使用Nano開啟/編譯
[root@pi] nano hello.py	  開啟 hello.py (如果沒有檔案, 自動產生新檔)  
[root@pi] python hello.py 編譯並執行 hello.py  
  
  
# 列出使用的 usb/port 清單  
[root@pi] susb       usb	清單  
[root@pi] ls -l /dev/tty* 列出所有使用的port (控Arduino常用)  
  
  
# Ipconfig  
ip a  
ip addr  
ip address  
ip addr show  
  
  
# Install  
[root@pi] python2 -m pip list  python2 module 清單  
[root@pi] python3 -m pip list  python3 module 清單  
[root@pi] pip3 install python-osc  安裝 python-osc  
  
  
# radio.py啟動自動執行
[root@pi] cp radio.py /etc/init.d/radio     
[root@pi] chmod 755 /etc/init.d/radio  
[root@pi] update-rc.d radio defaults  
  
移除
[root@pi] update-rc.d -f radio remove
