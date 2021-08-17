import os
from tkinter import * # __all__ 에 저장된 모듈 임포트됨
import tkinter.ttk as ttk
from tkinter import filedialog # 파일 불로오는 기능 (서브 모듈이라 *로 안불러와짐)
import tkinter.messagebox as msgbox  # 메세지 박스 사용시 불러옴
from PIL import Image # 이미지 관련 모듈

from enlighten_inference import EnlightenOnnxModel
import cv2
import time


model = EnlightenOnnxModel()

root = Tk()
root.title("저조도개선프로그램(hwankko)")  # 제목

# 파일 추가 (선택한 파일 모두)
def add_file():          # 복수개의 파일 선택
    files =  filedialog.askopenfilenames(title="개선시킬 저조도 이미지 파일을 선택하세요", \
         filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")), \
              initialdir = "D:/")

    
    # 사용자가 선택한 파일 목록
    for file in files:
        list_file.insert(END, file) # 리스트 파일 프레임에 추가


# 선택 파일 목록에서 삭제
def del_file():
    for index in reversed(list_file.curselection()): # reversed : 거꾸로 반환해줌 (인덱스의 경우 뒤에서부터 재껴야됨)
        list_file.delete(index)


# 저장 경로 (폴더)
def brows_dest_path():
    folder_selected = filedialog.askdirectory() # 폴더 선택
    if folder_selected == '': #사용자가 취소를 누를 때
        print('폴더 선택 취소')
        return
    txt_dest_path.delete(0, END)  # 먼저 저장되어있는거 삭제
    txt_dest_path.insert(0, folder_selected) # 경로란에 들어가짐
    

###########
# 이미지 조도 개선
def improve_image():

    try:  # 예외처리, 버그(저장 문제)
            
        # 포맷
        img_format = cmb_format.get().lower() # 확장자 값 받아와서 소문자로 변경
        a = list_file.get(0)
        images = cv2.imread(str(a))

        curr_time = time.strftime("_%Y%m%d_%H%M%S")  # 시간값 ex)20210814_191320
        processed = model.predict(images)

        file_name = ("result_image{}.".format(curr_time)) + img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)  # 저장경로 설정
        cv2.imwrite(dest_path, processed)
        
        msgbox.showinfo("알림", "조도개선이 완료되었습니다.")

        # 이미지 미리보기
        cv2.imshow('dst14', processed)
        cv2.waitKey()
        cv2.destroyAllWindows()

    except Exception as err: # 예외처리
        msgbox.showerror("에러", err)

# 시작
def start():
    # 각 옵션 값들 확인
    print("포맷 : ", cmb_format.get())

    # 파일 목록 확인
    if list_file.size() == 0:  # 파일 선택 없을시 경고메세지
        msgbox.showwarning("경고", "이미지 파일을 추가하세요")
        return

    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요")
        return

    ##########
    # 저조도 개선 작업
    improve_image()


# 파일 프레임 (파일 추가, 선택 삭제)

file_frame = Frame(root)
file_frame.pack(fill="x", padx= 5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5,width =12, text="파일추가", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame,padx=5, pady=5,width =12, text="파일삭제", command=del_file)
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx= 5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set) # yscrollcommand=scrollbar.set 이걸 해줘야 서로 맵핑이됨
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx= 5, pady=5, ipady=5) # fill="x"  : 프레임 늘려줌

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True,  padx= 5, pady=5, ipady=4, ipadx=40) # ipad : 안쪽 패딩

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=brows_dest_path)
btn_dest_path.pack(side="right", padx= 5, pady=5)


# 옴션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx= 5, pady=5, ipady=5)


# 파일 포맷 옵션
# 파일포맷 옵션 레이블
lbl_format = Label(frame_option, text="포맷", width=8)
lbl_format.pack(side="left", padx= 5, pady=5)

# 파일포맷 옵션 콤보
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0) # 첫번째 값 기본선택
cmb_format.pack(side="left", padx= 5, pady=5)


# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx= 5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx= 5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="저조도개선", width=12, command= start)
btn_start.pack(side="right", padx= 5, pady=5)



root.resizable(False, False) # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)
root.mainloop()  # 창이 닫히지 않도록 해줌
