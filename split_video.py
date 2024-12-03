import os
import sys
from moviepy.video.io.VideoFileClip import VideoFileClip

def split_video(input_dir, output_dir, split_duration):
    """
    動画を指定時間ごとに分割して保存する関数

    Args:
        input_dir (str): 元動画が保存されているディレクトリ
        output_dir (str): 分割された動画を保存するディレクトリ
        split_duration (int): 分割する時間（秒単位）
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
                print(f"Processing: {video_file}")
                video = VideoFileClip(video_path)
                total_duration = video.duration

                # 分割して保存
                part = 1
                for start_time in range(0, int(total_duration), split_duration):
                    end_time = min(start_time + split_duration, total_duration)
                    subclip = video.subclip(start_time, end_time)

                    # 出力ファイル名
                    output_name = f"{os.path.splitext(video_file)[0]}_part{part}.mp4"
                    output_path = os.path.join(output_dir, output_name)

                    # 保存
                    print(f"Saving: {output_name}")
                    subclip.write_videofile(output_path, codec="libx264", audio_codec="aac")

                    part += 1
                video.close()
                print(f"Finished processing {video_file}")
            except Exception as e:
                print(f"Error processing {video_file}: {e}")


if __name__ == "__main__":
    # 引数の読み込み
    if len(sys.argv) < 4:
        print("Usage: python split_video.py <input_dir> <output_dir> <split_duration>")
        print("Example: python split_video.py ./videos ./split_videos 10")
        sys.exit(1)

    input_directory = sys.argv[1]  # 元動画のディレクトリ
    output_directory = sys.argv[2]  # 分割された動画を保存するディレクトリ
    split_time = int(sys.argv[3])  # 分割する時間（秒）

    # 動画分割処理を実行
    split_video(input_directory, output_directory, split_time)
