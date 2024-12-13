import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import os

def play_text():
    # الحصول على النص من مربع النص
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        try:
            # تحويل النص إلى كلام باستخدام gTTS
            tts = gTTS(text, lang='en')
            tts.save("output.mp3")
            os.system("start output.mp3" if os.name == "nt" else "open output.mp3")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Warning", "Please enter some text to play.")

def exit_app():
    # إغلاق التطبيق
    root.destroy()

def clear_text():
    # مسح النص من مربع النص
    text_entry.delete("1.0", tk.END)

# إنشاء نافذة التطبيق الرئيسية
root = tk.Tk()
root.title("Text-to-Speech App")
root.geometry("400x300")

# إنشاء مربع النص
text_entry = tk.Text(root, wrap=tk.WORD, height=10, width=40)
text_entry.pack(pady=10)

# إنشاء الأزرار
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# زر تشغيل النص
play_button = tk.Button(button_frame, text="Play", command=play_text)
play_button.pack(side=tk.LEFT, padx=5)

# زر الخروج مع اللون الأحمر
exit_button = tk.Button(button_frame, text="Exit", command=exit_app, bg="red", fg="white")
exit_button.pack(side=tk.LEFT, padx=5)

# زر مسح النص
set_button = tk.Button(button_frame, text="Set", command=clear_text)
set_button.pack(side=tk.LEFT, padx=5)

# تشغيل التطبيق
root.mainloop()
