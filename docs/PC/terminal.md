# PC terminal 美化方案

## 安装 Windows Terminal

在微软商店进行安装

## 安装 Powershell 7

参考：[教程](https://blog.csdn.net/weixin_52802958/article/details/123636511)

设置PROFILE `code $PROFILE`:

```
# 设置预测文本来源为历史记录
Set-PSReadLineOption -PredictionSource History

# 每次回溯输入历史，光标定位于输入内容末尾
Set-PSReadLineOption -HistorySearchCursorMovesToEnd

# 设置 Tab 为菜单补全和 Intellisense
Set-PSReadLineKeyHandler -Key "Tab" -Function MenuComplete

# 设置 Ctrl+d 为退出 PowerShell
Set-PSReadlineKeyHandler -Key "Ctrl+d" -Function ViExit

# 设置 Ctrl+z 为撤销
Set-PSReadLineKeyHandler -Key "Ctrl+z" -Function Undo

# 设置向上键为后向搜索历史记录
Set-PSReadLineKeyHandler -Key UpArrow -Function HistorySearchBackward

# 设置向下键为前向搜索历史纪录
Set-PSReadLineKeyHandler -Key DownArrow -Function HistorySearchForward

# 美化部分：
oh-my-posh init pwsh --config 'C:\Users\boobyuuuu\AppData\Local\Programs\oh-my-posh\themes\mojada.omp.json' | Invoke-Expression
```

## 对 终端 进行设置

- 方法一：在终端的设置界面进行设置

- 方法二：设置终端 `json profile` 文件

## 安装 oh-my-posh

参考：[CSDN](https://blog.csdn.net/wk198786/article/details/132265190) 和 [BILIBILI](https://www.bilibili.com/video/BV1Qa411T7Au/?spm_id_from=333.337.search-card.all.click&vd_source=e11ee48b4ecfcc4ed9ab26adbfc4a67b)

显示conda环境: [CSDN](https://blog.csdn.net/Momosaki/article/details/137779874)

设置PROFILE，美化主题 `C:\Users\boobyuuuu\AppData\Local\Programs\oh-my-posh\themes\bubbles.omp.json`：

```
{
"$schema": "https://raw.githubusercontent.com/JanDeDobbeleer/oh-my-posh/main/themes/schema.json",
"blocks": [
    {
    "alignment": "right",
    "segments": [
        {
        "type": "python",
        "style": "plain",
        "foreground": "#98C379",
        "properties": {
        "display_virtual_env": true,
        "dispplay_default": true,
        "display_version": false,
        "home_enabled": true,
        "prefix": "\uE235 ",
        "postfix": " ",
        "display_mode": "always"
        }
        },
        {
        "background": "#29315A",
        "foreground": "#E64747",
        "leading_diamond": "\ue0b6",
        "style": "diamond",
        "template": "{{ .UserName }}",
        "trailing_diamond": "\ue0b4 ",
        "type": "session"
        },
        {
        "background": "#29315A",
        "foreground": "#3EC669",
        "leading_diamond": "\ue0b6",
        "properties": {
            "style": "folder"
        },
        "style": "diamond",
        "template": "\ue5ff {{ .Path }}",
        "trailing_diamond": "\ue0b4",
        "type": "path"
        },
        {
        "background": "#29315A",
        "foreground": "#43CCEA",
        "leading_diamond": " \ue0b6",
        "properties": {
            "branch_icon": ""
        },
        "style": "diamond",
        "template": "{{ .HEAD }}",
        "trailing_diamond": "\ue0b4",
        "type": "git"
        },
        // {
        //   "background": "#29315A",
        //   "foreground": "#E4F34A",
        //   "leading_diamond": " \ue0b6",
        //   "properties": {
        //     "fetch_version": false
        //   },
        //   "style": "diamond",
        //   "template": "\ue235{{ if .Error }}{{ .Error }}{{ else }}{{ if .Venv }}{{ .Venv }} {{ end }}{{ .Full }}{{ end }}",
        //   "trailing_diamond": "\ue0b4",
        //   "type": "python"
        // },
        {
        "background": "#29315A",
        "foreground": "#7FD5EA",
        "leading_diamond": " \ue0b6",
        "properties": {
            "fetch_version": false
        },
        "style": "diamond",
        "template": "\ue626{{ if .Error }}{{ .Error }}{{ else }}{{ .Full }}{{ end }}",
        "trailing_diamond": "\ue0b4",
        "type": "go"
        },
        {
        "background": "#29315A",
        "foreground": "#42E66C",
        "leading_diamond": " \ue0b6",
        "properties": {
            "fetch_version": false
        },
        "style": "diamond",
        "template": "\ue718{{ if .PackageManagerIcon }}{{ .PackageManagerIcon }} {{ end }}{{ .Full }}",
        "trailing_diamond": "\ue0b4",
        "type": "node"
        },
        {
        "background": "#29315A",
        "foreground": "#E64747",
        "leading_diamond": " \ue0b6",
        "properties": {
            "fetch_version": false
        },
        "style": "diamond",
        "template": "\ue791{{ if .Error }}{{ .Error }}{{ else }}{{ .Full }}{{ end }}",
        "trailing_diamond": "\ue0b4",
        "type": "ruby"
        },
        {
        "background": "#29315A",
        "foreground": "#E64747",
        "leading_diamond": " \ue0b6",
        "properties": {
            "fetch_version": false
        },
        "style": "diamond",
        "template": "\ue738{{ if .Error }}{{ .Error }}{{ else }}{{ .Full }}{{ end }}",
        "trailing_diamond": "\ue0b4",
        "type": "java"
        },
        {
        "background": "#29315A",
        "foreground": "#9B6BDF",
        "leading_diamond": " \ue0b6",
        "properties": {
            "fetch_version": false
        },
        "style": "diamond",
        "template": "\ue624{{ if .Error }}{{ .Error }}{{ else }}{{ .Full }}{{ end }} ",
        "trailing_diamond": "\ue0b4",
        "type": "julia"
        },
        {
        "background": "#29315A",
        "foreground": "#9B6BDF",
        "foreground_templates": [
            "{{if eq \"Charging\" .State.String}}#40c4ff{{end}}",
            "{{if eq \"Discharging\" .State.String}}#ff5722{{end}}",
            "{{if eq \"Full\" .State.String}}#4caf50{{end}}"
        ],
        "leading_diamond": " \ue0b6",
        "properties": {
            "charged_icon": " ",
            "charging_icon": "\u21e1 ",
            "discharging_icon": "\u21e3 "
        },
        "style": "diamond",
        "template": "{{ if not .Error }}{{ .Icon }}{{ .Percentage }}{{ end }}{{ .Error }}",
        "trailing_diamond": "\ue0b4",
        "type": "battery"
        }
    ],
    "type": "prompt"
    },
    {
    "alignment": "left",
    "newline": true,
    "segments": [
        {
        "background": "#29315A",
        "foreground": "#AEA4BF",
        "leading_diamond": "\ue0b6",
        "properties": {
            "style": "austin",
            "threshold": 150
        },
        "style": "diamond",
        "template": "{{ .FormattedMs }}",
        "trailing_diamond": "\ue0b4 ",
        "type": "executiontime"
        },
        {
        "background": "#29315A",
        "foreground": "#7FD5EA",
        "leading_diamond": "\ue0b6",
        "style": "diamond",
        "template": "\u276f",
        "trailing_diamond": "\ue0b4",
        "type": "text"
        }
    ],
    "type": "prompt"
    }
],
"final_space": true,
"version": 3
}
```