import os
import sys
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout

# 入力フォルダと出力フォルダを固定
INPUT_DIR = ""
OUTPUT_DIR = ""

def split_video(input_dir, output_dir, split_duration):
    """
    動画を指定時間ごとに分割して保存し、前後1.5秒にフェードイン/フェードアウトを適用する関数。
    また、動画ごとに専用のサブフォルダを作成し、すでにサブフォルダが存在する場合は処理をスキップ。

    Args:
        input_dir (str): 元動画が保存されているディレクトリ。
        output_dir (str): 分割された動画を保存するディレクトリ。
        split_duration (int): 分割する時間（秒単位）。
    """
    # 出力フォルダが存在しない場合は作成
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 指定ディレクトリ内の動画ファイルを処理
    for video_file in os.listdir(input_dir):
        video_path = os.path.join(input_dir, video_file)

        # 動画ファイル形式の確認
        if video_file.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
            try:
                # 出力フォルダのパスを準備
                base_name = os.path.splitext(video_file)[0]
                video_output_dir = os.path.join(output_dir, base_name)

                # フォルダがすでに存在する場合はスキップ
                if os.path.exists(video_output_dir):
                    print(f"Skipping {video_file} as {video_output_dir} already exists.")
                    continue

                print(f"Processing: {video_file}")
                video = VideoFileClip(video_path)
                total_duration = video.duration

                # 動画ごとのサブフォルダを作成
                os.makedirs(video_output_dir)

                # 分割して保存
                part = 1
                for start_time in range(0, int(total_duration), split_duration):
                    end_time = min(start_time + split_duration, total_duration)
                    subclip = video.subclip(start_time, end_time)

                    # フェードインとフェードアウトを適用（各1.5秒）
                    subclip = fadein(subclip, 1.5)
                    subclip = fadeout(subclip, 1.5)

                    # 出力ファイル名
                    output_name = f"{base_name}_part{part}.mp4"
                    output_path = os.path.join(video_output_dir, output_name)

                    # 保存
                    print(f"Saving: {output_name} in {video_output_dir}")
                    subclip.write_videofile(output_path, codec="libx264", audio_codec="aac")

                    part += 1
                video.close()
                print(f"Finished processing {video_file}")
            except Exception as e:
                print(f"Error processing {video_file}: {e}")


if __name__ == "__main__":
    # 引数のチェック
    if len(sys.argv) < 2:
        print("Usage: python split_video.py <split_duration>")
        print("Example: python split_video.py 10")
        sys.exit(1)

    try:
        # 引数で分割時間を取得
        split_duration = int(sys.argv[1])
        if split_duration <= 0:
            raise ValueError("Split duration must be a positive integer.")
    except ValueError as e:
        print(f"Invalid split duration: {e}")
        sys.exit(1)

    # 動画分割処理を実行
    split_video(INPUT_DIR, OUTPUT_DIR, split_duration)
