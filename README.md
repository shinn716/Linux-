# Linux Command (筆記)
# 一般常用  
sudo su     最高權限
cd ..		    上一層  
cd usr/pi/	進入pi資料夾  
ls -l	      目前檔案清單  
clear       清除cmd  
sudo reboot 重新開機    
  
  
# 使用Nano開啟/編譯
sudo nano hello.py	  開啟 hello.py (如果沒有檔案, 自動產生新檔)  
sudo python hello.py  編譯並執行 hello.py  
  
  
# 列出使用的 usb/port 清單  
sudo susb            usb	清單  
sudo ls -l /dev/tty* 列出所有使用的port (控Arduino常用)  
  
  
# Ipconfig  
ip a  
ip addr  
ip address  
ip addr show  
  
  
# Install  
sudo python2 -m pip list  python2 module 清單  
sudo python3 -m pip list  python3 module 清單  
sudo pip3 install python-osc  安裝 python-osc  
  
  
# 啟動自動執行
切換到root賬戶　　          sudo su  
修改rc.local文件　　        sudo nano /etc/rc.local  
在exit 0 之前添加執行命令　　sudo python /xx/xx/xx.py  
