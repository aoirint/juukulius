# juukulius

Julius / Japanese Dictation Kitのラッパー（予定）

- Julius: <https://github.com/julius-speech/julius>
    - man: <https://julius.osdn.jp/refman/julius.html.en>
- Japanese Dictation Kit: <https://github.com/julius-speech/dictation-kit>

## 日本語音声ファイルの文字起こし

音声を録音する。

```shell
ffmpeg -f pulse -i default -ac 1 -ar 16000 a.wav
```

または、音声ファイルをwav形式・モノラル・16000Hzに変換する。

```shell
ffmpeg -i original.mp3 -ac 1 -ar 16000 a.wav
```

`./data`ディレクトリに音声ファイル`a.wav`を配置して、以下のコマンドを実行。

```shell
make build

./recognize /data/a.wav -cutsilence
```

標準出力に文字起こし結果が出力される。

詳細な出力が必要な場合は、`-v`オプションを付ける。
