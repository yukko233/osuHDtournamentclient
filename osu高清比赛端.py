import os
import time
import win32gui
#-----------------复位文件部分---------------------------
# 请把你比赛端tournament.cfg文件路径填入这里，记得是双斜杠
file_path = "D:\\game\\osu比赛端\\tournament.cfg"

# 定义manager的分辨率，一般只需要改队伍规模以及比赛名字
new_content = {
    "TeamSize": "3",
    "acronym": "ZKFC S2",
    "Height": "864",
    "ClientNameSize": "60"
}

# 打开文件，读取原始内容
with open(file_path, "r", encoding="utf-8") as f:
    old_content = f.read()

# 遍历要修改的内容，用replace方法替换原始内容中对应的部分
for key, value in new_content.items():
    # 构造要替换的字符串，格式为key = value
    old_string = key + " = " + old_content.split(key + " = ")[1].split("\n")[0]
    new_string = key + " = " + value
    # 用新字符串替换旧字符串
    old_content = old_content.replace(old_string, new_string)

# 打开文件，写入修改后的内容
with open(file_path, "w", encoding="utf-8") as f:
    f.write(old_content)

# 打印提示信息
print("文件复位成功！")
#-----------------更改分辨率部分---------------------------
def find_osu_window():
    # 这个函数返回osu窗口的句柄，如果存在的话，否则返回None
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and 'Tournament Manager' in win32gui.GetWindowText(hwnd):
            hwnds.append(hwnd)
        return True

    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds[0] if hwnds else None

def modify_tournament_cfg():
    # 请把你比赛端tournament.cfg文件路径填入这里，记得是双斜杠
    cfg_path = 'D:\\game\\osu比赛端\\tournament.cfg'
    #把更改后的分辨率以及比赛名称填在这里
    with open(cfg_path, 'r') as f:
        lines = f.readlines()
    with open(cfg_path, 'w') as f:
        for line in lines:
            if line.startswith('TeamSize'):
                line = 'TeamSize = 3\n'
            elif line.startswith('acronym'):
                line = 'acronym = ZKFC S2\n'
            elif line.startswith('Height'):
                line = 'Height = 1080\n'
            elif line.startswith('ClientNameSize'):
                line = 'ClientNameSize = 60\n'
            f.write(line)

while True:
    # 这个循环每隔0.5秒检查一次osu窗口是否存在，如果存在就修改tournament.cfg文件
    hwnd = find_osu_window()
    if hwnd:
        print('osu窗口找到了')
        modify_tournament_cfg()
        print('tournament.cfg修改完成')
        input("按任何键继续...")
        
    else:
        print('osu窗口没找到')
        time.sleep(0.5) # 等待0.5秒