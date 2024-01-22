import os
import time
import win32gui
# 请把你比赛端tournament.cfg,osu文件路径填入这里，记得是双斜杠
file_path = "D:\\game\\osu比赛端\\tournament.cfg"
osu_path = "D:\\game\\osu比赛端\\osu!.exe"
# 定义manager的分辨率，一般只需要改队伍规模以及比赛名字
lines = [
        "TeamSize = 3",
        "acronym = ZKFC S2",
        "Height = 864",
        "ClientNameSize = 60"
    ]
# 把更改后的分辨率以及填在这里(只需要改Height值就行)
lines2 = [
        "TeamSize = 3",
        "acronym = ZKFC S2",
        "Height = 1080",
        "ClientNameSize = 60"
    ]
#以下部分不要修改，除非你知道你在干什么

# -----------------复位文件部分---------------------------
def resetfile():
    text = "\n".join(lines)
	# 打开文件，写入修改后的内容
    with open(file_path, 'w') as f:
        f.write(text)

    # 打印提示信息
    print("文件复位成功！")
    os.startfile(osu_path)
    print("已启动osu!.exe")

# -----------------更改分辨率部分---------------------------
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
    text = "\n".join(lines2)
	# 打开文件，写入修改后的内容
    with open(file_path, 'w') as f:
        f.write(text)

# -----------------判断配置文件是否存在---------------------
if os.path.isfile(file_path):
    print("tournament.cfg文件存在")
    resetfile()
else:
    print("tournament.cfg文件不存在，所以我不认为你需要启动比赛端或者你路径填错了")
    input("按任何键继续...")
    sys.exit()
# 这个循环每隔0.5秒检查一次osu窗口是否存在，如果存在就修改tournament.cfg文件
while True:
    hwnd = find_osu_window()
    if hwnd:
        print('osu窗口找到了')
        modify_tournament_cfg()
        print('tournament.cfg修改完成')
        input("按任何键继续...")
        sys.exit()

    else:
        print('osu窗口没找到')
        time.sleep(0.5)  # 等待0.5秒
