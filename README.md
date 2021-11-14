# juukulius

Julius / Japanese Dictation Kitのラッパー（予定）

- Julius: <https://github.com/julius-speech/julius>
- Japanese Dictation Kit: <https://github.com/julius-speech/dictation-kit>

## 日本語音声ファイルの文字起こし
`./data`ディレクトリに音声ファイル`a.wav`を配置して、以下のコマンドを実行。

標準出力に文字起こし結果が出力される。

```shell
make build

./recognize /data/a.wav
```
