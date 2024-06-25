import tkinter as tk
from tkinter import filedialog

def remove_ok_from_file():
    # Tạo cửa sổ Tkinter
    root = tk.Tk()
    root.withdraw()  # Ẩn cửa sổ chính

    # Mở hộp thoại chọn tệp
    file_path = filedialog.askopenfilename(title="Chọn tệp văn bản để xóa từ 'ok'", filetypes=[("Text files", "*.txt")])
    
    if not file_path:
        print("Không có tệp nào được chọn.")
        return
    
    try:
        # Mở tệp để đọc
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Xóa từ "ok" khỏi mỗi dòng
        modified_lines = [line.replace("ok", "") for line in lines]
        
        # Ghi các dòng đã sửa đổi vào tệp ban đầu
        with open(file_path, 'w') as file:
            file.writelines(modified_lines)
        
        print(f"Đã xóa từ 'ok' khỏi tệp: {file_path}")
    
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

if __name__ == "__main__":
    remove_ok_from_file()
