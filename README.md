# audio
 
機械学習を用いたSpleeterを使用して音楽ファイルのボーカルとそれ以外を分離します。
もっと色々できそうですが、とりあえず  

waveファイルで扱うため、mp3等のファイルが入力された場合、新たに同名のwaveファイルを作成します。
また、出力は共にwaveファイルで出力されます。


# 動作
以下が動作例です  
音楽ファイルは著作権等の観点から、個人のものを利用してください


waveファイルでない場合

    ファイルパスを入力(ファイル名を含む):
    (wavファイルでない場合、新たにwavファイルを作成します)
    /Users/name/Documents/musics/Where We Started.mp3
    inputフォルダにWhere We Started.wavを作成しました
    Instructions for updating:
    Colocations handled automatically by placer.
    INFO:spleeter:File output/Where We Started/accompaniment.wav written succesfully
    INFO:spleeter:File output/Where We Started/vocals.wav written succesfully
    outputフォルダに結果を保存しました
    
waveファイルの場合

    ファイルパスを入力(ファイル名を含む):
    (wavファイルでない場合、新たにwavファイルを作成します)
    /Users/name/Documents/musics/Where We Started.wav
    Instructions for updating:
    Colocations handled automatically by placer.
    INFO:spleeter:File output/Where We Started/accompaniment.wav written succesfully
    INFO:spleeter:File output/Where We Started/vocals.wav written succesfully
    outputフォルダに結果を保存しました
