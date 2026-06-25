import sys
import os

# فحص وتحميل مكاتب إصلاح الخط العربي تلقائياً في الخلفية
try:
    import arabic_reshaper
    from bidi.algorithm import get_display
except ImportError:
    os.system('pip install arabic-reshaper python-bidi --quiet')
    import arabic_reshaper
    from bidi.algorithm import get_display

# نظام اعتراض وطباعة النصوص العربية بشكل صحيح في ترمكس
class ArabicTermuxStream:
    def __init__(self, original_stream):
        self.original_stream = original_stream

    def write(self, text):
        if text.strip():
            try:
                # إصلاح وتوجيه الحروف العربية لتظهر من اليمين إلى اليسار بشكل مستقيم
                reshaped_text = arabic_reshaper.reshape(text)
                bidi_text = get_display(reshaped_text)
                self.original_stream.write(bidi_text)
            except Exception:
                self.original_stream.write(text)
        else:
            self.original_stream.write(text)

    def flush(self):
        self.original_stream.flush()

# تشغيل الفلتر تلقائياً على التيرمنال
sys.stdout = ArabicTermuxStream(sys.stdout)

# استدعاء وتشغيل أداة الصيد المشفرة تلقائياً
try:
    import dvkrfb_3
except ImportError:
    print("\033[1;31m [!] Error: dvkrfb_3.so file not found or incompatible python version!\033[0m")
    sys.exit()
