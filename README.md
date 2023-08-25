![Rice](/docs/assets/rice.png "rice")

## 📋 Details
<table>
  <thead>
    <tr>
      <th style="text-align:center" colspan="2">Components</th>
    </tr>
  </thead>
  <tbody align="center">
    <tr>
      <td>OS</td>
      <td><a href="https://archlinux.org/">Arch Linux</a></td>
    </tr>
    <tr>
      <td>Shell</td>
      <td><a href="https://www.gnu.org/software/bash/">Bash</a></td>
    </tr>
    <tr>
      <td>Fetch</td>
      <td><a href="https://github.com/unxsh/nitch">Nitch</a></td>
    </tr>
    <tr>
      <td>Terminal</td>
      <td><a href="https://github.com/alacritty/alacritty">Alacritty</a></td>
    </tr>
    <tr>
      <td>TWM</td>
      <td><a href="https://github.com/baskerville/bspwm">Bspwm</a></td>
    </tr>
    <tr>
      <td>Compositor</td>
      <td><a href="https://github.com/yshui/picom">Picom</a></td>
    </tr>
    <tr>
      <td>Status bar</td>
      <td><a href="https://github.com/polybar/polybar">Polybar</a> (<a href="https://github.com/polybar/polybar-scripts/tree/master/polybar-scripts/openweathermap-simple">openweather-simple</a>)</td>
    </tr>
    <tr>
      <td>App launcher</td>
      <td><a href="https://github.com/davatorium/rofi">Rofi</a></td>
    </tr>
    <tr>
      <td>File manager</td>
      <td><a href="https://github.com/linuxmint/nemo">Nemo</a></td>
    </tr>
    <tr>
      <td>Hotkey daemon</td>
      <td><a href="https://github.com/baskerville/sxhkd">Sxhkd</a></td>
    </tr>
    <tr>
      <td>Browser</td>
      <td><a href="https://github.com/brave/brave-browser">Brave</a></td>
    </tr>
    <tr>
      <td>Note taking</td>
      <td><a href="https://github.com/logseq/logseq">Logseq</a></td>
    </tr>
    <tr>
      <td>Discord client</td>
      <td><a href="https://github.com/BetterDiscord/BetterDiscord">BetterDiscord</a></td>
    </tr>
    <tr>
      <td>Code editor</td>
      <td><a href="https://github.com/VSCodium/vscodium">Vscodium</a></td>
    </tr>
    <tr>
      <td>Video/audio player</td>
      <td><a href="https://github.com/mpv-player/mpv">mpv</a></td>
    </tr>
    <tr>
      <td>Countdown/Stopwatch</td>
      <td><a href="https://github.com/trehn/termdown">Termdown</a></td>
    </tr>
    <tr>
      <td>Youtube search in terminal</td>
      <td><a href="https://github.com/pystardust/ytfzf">Ytfzf</a></td>
    </tr>
    <tr>
      <td>Screen capture</td>
      <td><a href="https://github.com/flameshot-org/flameshot">Flameshot</a></td>
    </tr>
    <tr>
      <td>Page color scheme</td>
      <td><a href="https://chrome.google.com/webstore/detail/dark-reader/eimadpbcbfnmbkopoojfekhnkhdbieeh?hl=en">Dark Reader</a></td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th style="text-align:center" colspan="4">Themes</th>
    </tr>
  </thead>
  <tbody align="center">
    <tr>
      <td>Dark Reader</td>
      <td colspan="3"><a href="https://github.com/catppuccin/dark-reader">Tokyonight (built-in)</a></td>
    </tr>
    <tr>
      <td>GTK-3.0</td>
      <td colspan="3"><a href="https://github.com/Fausto-Korpsvart/Tokyo-Night-GTK-Theme">Tokyonight (modified)</a></td>
    </tr>
    <tr>
      <td>Brave</td>
      <td colspan="3"><a href="https://chrome.google.com/webstore/detail/catppuccin-chrome-theme-m/bkkmolkhemgaeaeggcmfbghljjjoofoh">Catppuccin Mocha (modified)</a></td>
    </tr>
    <tr>
      <td>Alacritty</td>
      <td colspan="3"><a href="https://github.com/zatchheems/tokyo-night-alacritty-theme">Tokyonight</a></td>
    </tr>
    <tr>
      <td>Vscodium</td>
      <td colspan="3"><a href="https://github.com/enkia/tokyo-night-vscode-theme">Tokyonight</a></td>
    </tr>
    <tr>
      <td>Discord (BetterDiscord)</td>
      <td colspan="3"><a href="https://github.com/Dyzean/Tokyo-Night">Tokyonight</a></td>
    </tr>
    <tr>
      <td>Rofi</td>
      <td colspan="3"><a href="https://github.com/Murzchnvok/rofi-collection">Tokyonight</a></td>
    </tr>
    <tr>
      <td>Logseq</td>
      <td colspan="3"><a href="https://github.com/nmartin84/logseq-tokyo-theme">Ayu</a></td>
    </tr>
    <tr>
      <td>Icons</td>
      <td colspan="3"><a href="https://github.com/bikass/kora">Kora</a></td>
    </tr>
    <tr>
      <td>Fonts</td>
      <td><a href="https://github.com/JetBrains/JetBrainsMono">JetBrains Mono</a></td>
      <td><a href="https://github.com/microsoft/cascadia-code">Cascadia code</a></td>
      <td><a href="https://archlinux.org/packages/community/any/ttf-nerd-fonts-symbols-1000-em/">Nerd Fonts Symbols</a></td>
    </tr>
  </tbody>
</table>

## ⚙️ Modified things
### GTK - Tokyonight
If you want to disable the rounded corner of the pop-up menu, then modify this
```
$HOME/.local/share/themes/Tokyonight-Dark-BL/gtk-3.0/gtk.css
```
(if you're using `gtk-application-prefer-dark-theme=true` on `.config/gtk-3.0/settings.ini`, then modify `gtk-dark.css` instead of `gtk.css`)

Now set `border-radius` to `0px` on `menu,.menu,.context-menu`.

<img height="200px" src="/docs/assets/gtk-context-menu.png" alt="Part that you&#39;ll need to modify" title="Part to be modified">

### Brave - Catppuccin Mocha
If you want to change the pastel pink letter color of the search bar, then modify the `manifest.json` file in the theme version folder.
```
$HOME/.config/BraveSoftware/Brave-Browser/Default/Extensions/bkkmolkhemgaeaeggcmfbghljjjoofoh/
```
or you can locate with this
```
find $HOME/.config/BraveSoftware -type f -iname manifest.json -print0 | xargs -0 grep Catppuccin
```
Now set `ntp-link` and `omnibox-text` to `[ 169, 177, 214 ]`.

To load the modified Catppuccin Mocha theme:
 - Go to `brave://extensions/`
 - Enable *Developer mode*
 - Click on *Load unpacked*
 - Select the folder of `manisfest.json` alredy modified

## 📜 Some scripts
### print-maim
Shows a "+" to select a window or an area to print, then moves the screenshot to clipboard and /tmp

- Dependencies:
    - [maim](https://github.com/naelstrof/maim)
    - [xclip](https://github.com/astrand/xclip)

Note: print-maim-delayed is the same, but with 5 seconds of delay

### monocle-0-1
Capture when monocle mode in bspwm is on or off. I use this in conjunction with a picom opacity rule (`0:monocle@:32c = 1 && !focused`). The result of this is what you see in the image below.

<img height="350px" src="/docs/assets/monocle-script-on.png" alt="monocle-script-on" title="monocle-script-on">

Instead of this

<img height="350px" src="/docs/assets/monocle-script-off.png" alt="monocle-script-off" title="monocle-script-off">

## 🌸 Others...
### Logseq Journal Template
If you plan to use this, please understand that when I write something in my journal, I delete empty hashtags (#empty). This is because when I use the filter tool in "Linked references", I can exclude blocks that are empty and only see those with content.

Do you want to know how to set my journal template as the default journal page? See [here](https://thinkstack.club/how-to-set-up-an-automated-daily-template-in-logseq/#how-to-set-a-daily-recurring-template)

### Inspirations 
- `dotfiles` [HynDuf7/dotfiles](https://github.com/HynDuf7/dotfiles)
- `dotfiles` [r/unixporn](https://www.reddit.com/r/unixporn/)
- `journal` [Cara Antonaccio](https://www.youtube.com/watch?v=PN6tjeQfxRc)

### Notes
- if any english grammar is wrong, I'll be glad to know, tell me on [reddit](https://www.reddit.com/user/Arsemy)
