#!/data/data/com.termux/files/usr/bin/python3
import numpy as np
from pydub import AudioSegment
from pydub.playback import play
import os

NOTE_FREQ = {
    "c": 261.63, "c#": 277.18, "d": 293.66, "d#": 311.13,
    "e": 329.63, "f": 349.23, "f#": 369.99, "g": 392.00,
    "g#": 415.30, "a": 440.00, "a#": 466.16, "b": 493.88
}

def make_note(freq, duration_ms):
    fs = 44100
    t = np.linspace(0, duration_ms/1000, int(fs*duration_ms/1000), False)
    note = np.sin(freq*2*np.pi*t)
    audio = np.int16(note*32767)
    return AudioSegment(
        audio.tobytes(), 
        frame_rate=fs,
        sample_width=audio.dtype.itemsize, 
        channels=1
    )

def load_or_create():
    files = [f for f in os.listdir() if f.endswith(".mp3")]
    if not files:
        return AudioSegment.silent(0), None
    print("File MP3 hiện có:")
    for i,f in enumerate(files,1):
        print(f"{i}. {f}")
    sel = input("Chọn số file để sửa hoặc ENTER tạo file mới: ").strip()
    if sel.isdigit() and 1 <= int(sel) <= len(files):
        filename = files[int(sel)-1]
        song = AudioSegment.from_mp3(filename)
        print(f"Đang sửa {filename}")
        return song, filename
    return AudioSegment.silent(0), None

def main():
    song, filename = load_or_create()
    if not filename:
        filename = input("Tên file MP3 mới (không cần .mp3): ").strip() + ".mp3"
    
    print("Nhập nốt dạng key:duration (vd: c:500), nhập # để kết thúc.")
    print("Nhập 'u' để undo nốt cuối.")
    count = 1
    notes_history = []

    while True:
        inp = input(f"Nốt {count}: ").strip()
        if inp == "#":
            break
        if inp.lower() == "u":
            if notes_history:
                removed = notes_history.pop()
                song = AudioSegment.silent(0)
                for n in notes_history:
                    song += n
                print("Đã xóa nốt cuối!")
                count = len(notes_history)+1
            else:
                print("Chưa có nốt nào để xóa!")
            continue
        try:
            key, dur = inp.split(":")
            dur = int(dur)
            freq = NOTE_FREQ.get(key.lower())
            if freq is None:
                print("Nốt không hợp lệ!")
                continue
            note_seg = make_note(freq, dur)
            print(f"Đang play: {key}:{dur}")
            play(note_seg)
            song += note_seg
            notes_history.append(note_seg)
            count += 1
        except:
            print("Lỗi định dạng! VD: c:500")
            continue
    
    song.export(filename, format="mp3")
    print(f"Đã lưu file {filename}")

if __name__ == "__main__":
    main()
