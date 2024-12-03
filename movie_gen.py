import os
from moviepy.editor import ColorClip, AudioFileClip

# ベースフォルダのパス
base_folder = "/Users/yusuke_omura/Documents/MovieGen"
audio_folder = os.path.join(base_folder, "audio")
video_folder = os.path.join(base_folder, "video")

# 必要なフォルダがなければ作成
if not os.path.exists(audio_folder):
    os.makedirs(audio_folder)
if not os.path.exists(video_folder):
    os.makedirs(video_folder)

# `audio`フォルダ内のすべての音声ファイルを処理
for audio_file in os.listdir(audio_folder):
    # 音声ファイルのパス
    audio_path = os.path.join(audio_folder, audio_file)
    
    # サポートする音声形式のみ処理
    if audio_file.lower().endswith(('.mp3', '.wav', '.m4a')):
        try:
            # 音声ファイルの読み込み
            audio = AudioFileClip(audio_path)
            video_duration = audio.duration
            
            # 黒い背景の動画クリップ作成
            video_size = (1280, 720)  # 16:9のHD解像度
            black_background = ColorClip(size=video_size, color=(0, 0, 0), duration=video_duration)
            video = black_background.set_audio(audio)
            
            # 出力ファイル名（拡張子は.mp4に変換）
            output_name = os.path.splitext(audio_file)[0] + ".mp4"
            output_path = os.path.join(video_folder, output_name)
            
            # 動画ファイルを保存
            print(f"Processing: {audio_file}")
            video.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac")
            print(f"Saved: {output_path}")
        except Exception as e:
            print(f"Error processing {audio_file}: {e}")
