import os
from pydub import AudioSegment
from spleeter.separator import Separator


print("ファイルパスを入力(ファイル名を含む):")
print("(wavファイルでない場合、新たにwavファイルを作成します)")
filepath=input() 
#filepath="[filepath]"

filename = os.path.splitext(os.path.basename(filepath))[0] #拡張子なしファイル名
file_ext = os.path.splitext(filepath)[1][1:] #拡張子


if file_ext != 'wave' and file_ext != 'wav' :
    os.makedirs("input", exist_ok=True)
    try:
        AudioSegment.from_file(filepath,file_ext).export("input/"+ filename +".wav", format="wav")
        print("inputフォルダに"+ filename +".wavを作成しました")
        input_audio = "input/"+ filename +".wav"
    except:
        print("ファイルを変換できません")
else:
    input_audio = filepath


separator_2stem = Separator('spleeter:2stems')
os.makedirs("output", exist_ok=True)
separator_2stem.separate_to_file(input_audio, "output") 
print("outputフォルダに結果を保存しました")

exit()

