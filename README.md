<h1 align="center">MH-HP-Overlay-For-PSP-Emulator</h1>

<div align="center">

  [![StaticBadge](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/)
  [![App](https://img.shields.io/badge/App-1.0.0-green)](https://github.com/Alexander-Lancellott/MH-HP-Overlay-For-PSP-Emulator)

</div>

## Description

A simple open-source HP overlay that I've developed for MHF/2/U, MHP/2/2G and MHP3RD/HD in Python. This project is a port of another one I previously created called [MH-HP-Overlay-For-3DS-Emulator](https://github.com/Alexander-Lancellott/MH-HP-Overlay-For-3DS-Emulator), but this time it's designed to work with PSP emulator, [PPSSPP](https://www.ppsspp.org/download/), on their PC (Windows) versions.

You can support me by donating! I’d really appreciate it. But either way, thank you for using this mod!

<a href='https://ko-fi.com/B0B115WKYH' target='_blank'>
  <img height='45' style='border:0px;height:45px;' src='https://storage.ko-fi.com/cdn/kofi2.png?v=6' border='0' alt='Buy Me a Coffee at ko-fi.com' />
</a>

## Compatibility

Tested on **PPSSPP v1.19.3**

- **MHF (USA/EUR)** - ULES00318 - ULUS10084
- **MHP (JPN)** - ULJM05066
- **MHF2 (USA/EUR)** - ULES00851 - ULUS10266
- **MHP2 (JPN)** - ULJM05156
- **MHFU (USA/EUR)** - ULES01213 - ULUS10391
- **MHP2G (JPN)** - ULJM05500
- **MHP3RD/HD (JPN)** - ULJM05800 - NPJB40001

## High DPI Scaling (optional, only if you notice it)

If your monitor has a resolution higher than 1080p, it's likely you're using a DPI scale above 100%. In this case, the initial position of the overlay may not be the same as when using 100% scaling. To mitigate this, you have three options:

- Set your screen scaling to 100%. You can follow this [guide](https://support.microsoft.com/en-us/windows/view-display-settings-in-windows-37f0e05e-98a9-474c-317a-e85422daa8bb).

- If setting your monitor’s scaling to 100% is not ideal for you, then disable automatic DPI scaling for PPSSPP. To do this, right-click on `PPSSPPWindows64.exe`, select Properties, then go to the Compatibility tab. You'll see a checkbox that says, **"Override high DPI scaling behavior."** A drop-down menu will let you choose one of three options. Select `System` or `System Enhanced`. You can find a helpful guide [here](https://www.majorgeeks.com/content/page/how_to_change_dpi_scaling_settings_in_windows.html).

- If neither of the previous options suits you, use the [Fix X & Fix Y](#fix-x--fix-y) options to adjust the overlay more precisely and correct the slight misalignment.

## How to use

To use the overlay, simply open the `MH-HP-PSP-Overlay.exe` file.

> [!IMPORTANT]  
> If the overlay is not working properly, try running it with administrator privileges to ensure it functions correctly. If you're unsure how to do this, you can check this [guide](https://www.majorgeeks.com/content/page/how_to_run_an_app_as_administrator_in_windows_10.html).

If one of the games from the [compatibility list](#compatibility) isn't running in the emulator, you will see a red message in the overlay console saying **No game running** and a countdown starting from 20 minutes. When the countdown reaches zero, the overlay will automatically close to save resources.

![No game running](https://res.cloudinary.com/dms5y8rug/image/upload/c_thumb,g_face,q_auto:best/MH-HP-Overlay-For-PSP-Emulator/no_game_running.webp)

Otherwise, if one of the games from the [compatibility list](#compatibility) is running in the emulator, you will see a green message in the overlay console indicating which of the compatible games is currently running.

![Game running](https://res.cloudinary.com/dms5y8rug/image/upload/c_thumb,g_face,q_auto:best/MH-HP-Overlay-For-PSP-Emulator/game_running.webp)

If everything works correctly, upon starting a hunting mission, you should see `labels` arranged one below the other, displaying the monster's name along with its HP in the top right corner of the game window.

<div align="center">

  ![Labels](https://res.cloudinary.com/dms5y8rug/image/upload/c_thumb,g_face,q_auto:best/MH-HP-Overlay/labels.png)

</div>

If you don't like the color of the overlay or its position in the top right corner of the window, go directly to the [Customize Overlay](#customize-overlay) section to edit it to your liking. However, I recommend that you continue reading this section first.

### Borderless screen system & Native full-screen mode

In the latest versions of the PPSSPP emulator, the overlay remains visible even when using the native full-screen mode. However, just in case this changes in future updates or in specific configurations where the overlay might stop being visible, a **borderless screen system** has been implemented as a fallback.

This system mimics the emulator’s full-screen mode **as closely as possible**, although the emulator’s toolbar unfortunately remains visible in this mode. You can toggle it on or off using the default keyboard shortcut `Ctrl + Alt + F`. To exit this mode, simply press the same shortcut again.

Note that this is different from PPSSPP’s native full-screen shortcut (`F11` by default). If you wish to change the default shortcut for the overlay, you can do so in the [Hotkey, Reset Hotkey & Monster Selection Hotkey](#hotkey-reset-hotkey--monster-selection-hotkey) subsection.

<table>
  <tr align="center">
    <td>
      <strong>Native full-screen mode</strong>
    </td>
  </tr>
  <tr>
    <td>
      <img alt="Full-screen"
        src="https://res.cloudinary.com/dms5y8rug/image/upload/c_thumb,g_face,q_auto:best/MH-HP-Overlay-For-PSP-Emulator/native_fullscreen.webp"
        style="min-width: 397.5px;" />
    </td>
  </tr>
</table>
<table>
  <tr align="center">
    <td>
      <strong style="white-space: nowrap;">
        Borderless screen system
      </strong>
    </td>
  </tr>
  <tr>
    <td>
      <img alt="Borderless"
        src="https://res.cloudinary.com/dms5y8rug/image/upload/c_thumb,g_face,q_auto:best/MH-HP-Overlay-For-PSP-Emulator/borderless.webp"
        style="min-width: 397.5px;" />
    </td>
  </tr>
</table>

## Customize Overlay

Inside the root folder, there is a file called `config.ini`, which stores the values for options that can be edited using a text editor like [Notepad++](https://notepad-plus-plus.org/downloads/) to customize the overlay.

**It's important to close and reopen the overlay each time you edit this file for the changes to take effect.**

Below, you will find sub-sections dedicated to documenting each of the available options in the `config.ini`.

### Hotkey, Reset Hotkey & Monster Selection Hotkey

The `config.ini` file includes several customizable hotkeys that control different overlay functions:

**`hotkey`**
This option defines the keyboard shortcut used to toggle the borderless screen system on or off. By default, this shortcut is `Ctrl + Alt + F`. You can replace it with another shortcut if the default one is inconvenient for you.

**`reset_hotkey`**
This defines a keyboard shortcut used to forcefully reset the overlay in case it becomes frozen or unresponsive due to unexpected behavior. This allows for a quick recovery without needing to close and reopen the application manually. By default, it's set to `Ctrl + R`.

**`monster_selected_hotkey`**
Unlike the 3DS version, which used the target camera, this version includes a hotkey to manually select which monster’s abnormal statuses you want to view. This hotkey is defined by the `monster_selected_hotkey` option in `config.ini` and is set to the `Enter` key by default.

Here's how it works:

- Pressing it once selects the first (or only) monster.
- If there are two monsters, pressing it again selects the second.
- Pressing it a third time resets the selection.
- If there's only one monster, pressing it a second time will also reset the selection.

Remember to close and reopen the overlay after making changes to the `config.ini` file for these adjustments to take effect.

<table>
  <tr align="center">
    <td>
      <strong>Option</strong>
    </td>
    <td>
      <strong style="white-space: nowrap; ">
        Default value
      </strong>
    </td>
    <td>
      <strong>Type</strong>
    </td>
    <td>
      <strong>Observation</strong>
    </td>
  </tr>
  <tr align="center">
    <td>hotkey</td>
    <td>^!f</td>
    <td>string</td>
    <td>
      Must be valid hotkey, check this: https://www.autohotkey.com/docs/v1/Hotkeys.htm#Symbols
    </td>
  </tr>
  <tr align="center">
    <td>reset_hotkey</td>
    <td>^r</td>
    <td>string</td>
    <td>
      Must be valid hotkey, check this: https://www.autohotkey.com/docs/v1/Hotkeys.htm#Symbols
    </td>
  </tr>
  <tr align="center">
    <td>monster_selected_hotkey</td>
    <td>Enter</td>
    <td>string</td>
    <td>
      Must be valid hotkey, check this: https://www.autohotkey.com/docs/v1/Hotkeys.htm#Symbols
    </td>
  </tr>
</table>

### Debugger

If the `debugger` option in the `config.ini` file is set to `true`, a .log file will be generated where all application logs will be stored. This option is intended solely for testing and troubleshooting, so its default value is `false`.

<table>
  <tr align="center">
    <td>
      <strong>Option</strong>
    </td>
    <td>
      <strong style="white-space: nowrap; ">
        Default value
      </strong>
    </td>
    <td>
      <strong>Type</strong>
    </td>
    <td>
      <strong>Observation</strong>
    </td>
  </tr>
  <tr align="center">
    <td>
      debugger
    </td>
    <td>
      false
    </td>
    <td>
      boolean
    </td>
    <td>
      This is case-insensitive and recognizes boolean values from 'yes'/'no', 'on'/'off', 'true'/'false' and '1'/'0'
    </td>
  </tr>
</table>

### Font

Within the `config.ini` file, you can customize the type, weight, and size of the font used in the overlay by editing the following options:

- `font_family`: Allows you to change the font type. You should use fonts that are compatible with the web (**Web Safe Fonts**). You can find a list of these fonts [here](https://www.cssfontstack.com/).
<br>&nbsp;
- `font_weight`: Allows you to adjust the font weight. Common values include `normal` for regular weight and `bold` for bold weight.
<br>&nbsp;
- `font_size`: Allows you to specify the font size in pixels.

Make sure to use **Web Safe Fonts** and to close and reopen the overlay after making changes in the `config.ini` file for these adjustments to take effect.

<table>
  <tr align="center">
    <td>
      <strong>Option</strong>
    </td>
    <td>
      <strong style="white-space: nowrap; ">
        Default value
      </strong>
    </td>
    <td>
      <strong>Type</strong>
    </td>
    <td>
      <strong>Observation</strong>
    </td>
  </tr>
  <tr align="center">
    <td>font_family</td>
    <td>Consolas, monaco, monospace</td>
    <td>string</td>
    <td>
      This is a <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/font-family">CSS property</a> and must be a <a href="https://www.cssfontstack.com/">Web Safe Font</a>
    </td>
  </tr>
  <tr align="center">
    <td>font_weight</td>
    <td>bold</td>
    <td>string</td>
    <td>
      This is a <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight">CSS property</a>
    </td>
  </tr>
  <tr align="center">
    <td>font_size</td>
    <td>18</td>
    <td>integer</td>
    <td>
      This is a <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/font-size">CSS property</a>, its value is in pixels and must be greater than or equal to 1
    </td>
  </tr>
</table>

### HP update time

The `hp_update_time` option in the `config.ini` file allows you to adjust the HP value update interval in seconds. The default value is `0.6`, which is equivalent to 600 milliseconds, and the minimum value is `0.1`.

You can modify this value to increase or decrease the time interval for updating the HP value. Higher values will increase the update interval and may improve performance.

Remember to close and reopen the overlay after making changes to the `config.ini` file for these adjustments to take effect.

<table>
  <tr align="center">
    <td>
      <strong>Option</strong>
    </td>
    <td>
      <strong style="white-space: nowrap; ">
        Default value
      </strong>
    </td>
    <td>
      <strong>Type</strong>
    </td>
    <td>
      <strong>Observation</strong>
    </td>
  </tr>
  <tr align="center">
    <td>hp_update_time</td>
    <td>0.6</td>
    <td>float</td>
    <td>Must be greater than or equal to 0.1</td>
  </tr>
</table>

### Show Initial HP

The `show_initial_hp` option in the `config.ini` file allows you to show or hide each monster's maximum HP. Its default value is set to `true`.

Remember to close and reopen the overlay after making changes to the `config.ini` file for these adjustments to take effect.

<table>
  <tr align="center">
    <td>
      <strong>Option</strong>
    </td>
    <td>
      <strong style="white-space: nowrap; ">
        Default value
      </strong>
    </td>
    <td>
      <strong>Type</strong>
    </td>
    <td>
      <strong>Observation</strong>
    </td>
  </tr>
  <tr align="center">
    <td>
      show_initial_hp
    </td>
    <td>
      true
    </td>
    <td>
      boolean
    </td>
    <td>
      This is case-insensitive and recognizes boolean values from 'yes'/'no', 'on'/'off', 'true'/'false' and '1'/'0'
    </td>
  </tr>
</table>

### Show HP Percentage

The `show_hp_percentage` option in the `config.ini` file allows you to show or hide HP as a percentage for each monster. Its default value is set to `true`.

Remember to close and reopen the overlay after making changes to the `config.ini` file for these adjustments to take effect.

<table>
  <tr align="center">
    <td>
      <strong>Option</strong>
    </td>
    <td>
      <strong style="white-space: nowrap; ">
        Default value
      </strong>
    </td>
    <td>
      <strong>Type</strong>
    </td>
    <td>
      <strong>Observation</strong>
    </td>
  </tr>
  <tr align="center">
    <td>
      show_hp_percentage
    </td>
    <td>
      true
    </td>
    <td>
      boolean
    </td>
    <td>
      This is case-insensitive and recognizes boolean values from 'yes'/'no', 'on'/'off', 'true'/'false' and '1'/'0'
    </td>
  </tr>
</table>

### Show Small Monsters

The `show_small_monsters` option in the `config.ini` file determines whether the overlay will display all monsters, including small ones. By default, this option is set to `true`.

To display only large monsters, change the value of `show_small_monsters` to `false`.

Remember to close and reopen the overlay after making changes to the `config.ini` file for these adjustments to take effect.

<table>
  <tr align="center">
    <td>
      <strong>Option</strong>
    </td>
    <td>
      <strong style="white-space: nowrap; ">
        Default value
      </strong>
    </td>
    <td>
      <strong>Type</strong>
    </td>
    <td>
      <strong>Observation</strong>
    </td>
  </tr>
  <tr align="center">
    <td>
      show_small_monsters
    </td>
    <td>
      true
    </td>
    <td>
      boolean
    </td>
    <td>
      This is case-insensitive and recognizes boolean values from 'yes'/'no', 'on'/'off', 'true'/'false' and '1'/'0'
    </td>
  </tr>
</table>

### Show Size Multiplier & Crown

The `show_size_multiplier` and `show_crown` options in the `config.ini` file allow you to show or hide the size multiplier and crown of each monster.

<div align="center">

![Size Multiplier & Crown](https://res.cloudinary.com/dms5y8rug/image/upload/c_thumb,g_face,q_auto:best/MH-HP-Overlay/size_multiplier_and_crown.png)

</div>

<table>
  <tr align="center">
    <td>
      <strong>Option</strong>
    </td>
    <td>
      <strong style="white-space: nowrap; ">
        Default value
      </strong>
    </td>
    <td>
      <strong>Type</strong>
    </td>
    <td>
      <strong>Observation</strong>
    </td>
  </tr>
  <tr align="center">
    <td>
      show_size_multiplier
    </td>
    <td>
      true
    </td>
    <td>
      boolean
    </td>
    <td>
      This is case-insensitive and recognizes boolean values from 'yes'/'no', 'on'/'off', 'true'/'false' and '1'/'0'
    </td>
  </tr>
  <tr align="center">
    <td>
      show_crown
    </td>
    <td>
      true
    </td>
    <td>
      boolean
    </td>
    <td>
      This is case-insensitive and recognizes boolean values from 'yes'/'no', 'on'/'off', 'true'/'false' and '1'/'0'
    </td>
  </tr>
</table>

### Show Abnormal Status

The `show_abnormal_status` option in the `config.ini` file allows you to enable or disable the display of abnormal status for large monsters. To see this information, you must manually select a monster using the [monster_selected_hotkey](#hotkey-reset-hotkey--monster-selection-hotkey).

<table>
  <tr align="center">
    <td>
      <strong>Monster 1</strong>
    </td>
    <td>
      <strong>Monster 2</strong>
    </td>
  </tr>
  <tr>
    <td>
      <img alt="abnormal_status"
      src="https://res.cloudinary.com/dms5y8rug/image/upload/c_thumb,g_face,q_auto:best/MH-HP-Overlay/jywc9byttd1o7tfmbztw.webp"
      style="max-width: 250px;"/>
    </td>
    <td>
      <img alt="abnormal_status"
      src="https://res.cloudinary.com/dms5y8rug/image/upload/c_crop,c_thumb,g_face,q_auto:best/MH-HP-Overlay/cm5js4xsjmgd94y3lchr.webp" 
      style="max-width: 250px;"/>
    </td>
  </tr>
</table>

These abnormal statuses are self-explanatory, except for the `Rage` state, which is not an abnormal status but a `timer` that indicates how long the monster will remain enraged. This can be useful, for example, to anticipate when Teostra will unleash its Supernova, as it does so upon exiting its enraged state.

<table>
  <tr align="center">
    <td>
      <strong>Option</strong>
    </td>
    <td>
      <strong style="white-space: nowrap; ">
        Default value
      </strong>
    </td>
    <td>
      <strong>Type</strong>
    </td>
    <td>
      <strong>Observation</strong>
    </td>
  </tr>
  <tr align="center">
    <td>
      show_abnormal_status
    </td>
    <td>
      true
    </td>
    <td>
      boolean
    </td>
    <td>
      This is case-insensitive and recognizes boolean values from 'yes'/'no', 'on'/'off', 'true'/'false' and '1'/'0'
    </td>
  </tr>
</table>

### Always show abnormal status

The always_show_abnormal_status option in the config.ini file allows abnormal statuses to always be displayed without the need to manually select a monster using the [monster_selected_hotkey](#hotkey-reset-hotkey--monster-selection-hotkey).

<table>
  <tr align="center">
    <td>
      <strong>always_show_abnormal_status = true</strong>
    </td>
  </tr>
  <tr align="center">
    <td>
      <img alt="abnormal_status"
      src="https://res.cloudinary.com/dms5y8rug/image/upload/c_thumb,g_face,q_auto:best/MH-HP-Overlay/Screenshot_2025-03-16_224548.webp" 
      style="max-width: 290px;"/>
    </td>
  </tr>
</table>

<table>
  <tr align="center">
    <td>
      <strong>Option</strong>
    </td>
    <td>
      <strong style="white-space: nowrap; ">
        Default value
      </strong>
    </td>
    <td>
      <strong>Type</strong>
    </td>
    <td>
      <strong>Observation</strong>
    </td>
  </tr>
  <tr align="center">
    <td>
      always_show_abnormal_status
    </td>
    <td>
      false
    </td>
    <td>
      boolean
    </td>
    <td>
      This is case-insensitive and recognizes boolean values from 'yes'/'no', 'on'/'off', 'true'/'false' and '1'/'0'
    </td>
  </tr>
</table>

### Language

The `language` option in the `config.ini` file allows you to specify the overlay’s language. By default, the overlay uses `en_US`, which does not require any external `.yaml` file.

Currently, only one example translation file is included: `es_ES.yaml.example`. This is an **incomplete Spanish translation**, provided as a reference. It includes some translated strings, but most large and small monster names are still missing.

If you'd like to use this example translation, rename the file to `es_ES.yaml` (remove the `.example` extension), complete the missing entries, and set `language=es_ES` in your `config.ini`.

> [!NOTE]
> In the `language` option of the `config.ini` file, make sure to enter only the filename without the `.yaml` extension.

You’re also free to create your own translation file. Just use the `es_ES.yaml.example` file as a starting point and place your completed file inside the locales folder.

<table>
  <tr align="center">
    <td>
      <strong>Option</strong>
    </td>
    <td>
      <strong style="white-space: nowrap; ">
        Default value
      </strong>
    </td>
    <td>
      <strong>Type</strong>
    </td>
    <td>
      <strong>Observation</strong>
    </td>
  </tr>
  <tr align="center">
    <td>
      language
    </td>
    <td>
      en_US
    </td>
    <td>
      string
    </td>
    <td>
      You must use one of the available languages from the locales folder by writing only the filename without the .yaml extension, or create your own translation file (.yaml). Except for 'en_US', which does not require a file as it is the default language.
    </td>
  </tr>
</table>

### Position (X & Y)

The `x` and `y` options within the `config.ini` file allow you to adjust the position of the overlay using Cartesian coordinates. These values are relative and percentage-based to the size of the target window, with a minimum range of `0` and maximum of `100` for each coordinate.

- `x`: Controls the horizontal position of the overlay.
<br>&nbsp;
- `y`: Controls the vertical position of the overlay.

Adjust these values to move the overlay to the desired position on the screen.

Remember to close and reopen the overlay after making changes in the `config.ini` file for these adjustments to take effect.

<table>
  <tr align="center">
    <td>
      <strong>Option</strong>
    </td>
    <td>
      <strong style="white-space: nowrap; ">
        Default value
      </strong>
    </td>
    <td>
      <strong>Type</strong>
    </td>
    <td>
      <strong>Observation</strong>
    </td>
  </tr>
  <tr align="center">
    <td>x</td>
    <td>100</td>
    <td>integer</td>
    <td>Must be greater than or equal to 0 and less than or equal to 100</td>
  </tr>
  <tr align="center">
    <td>y</td>
    <td>0</td>
    <td>integer</td>
    <td>Must be greater than or equal to 0 and less than or equal to 100</td>
  </tr>
</table>

<table>
  <tr align="center">
    <td>
      <strong>x = 100</strong>
      <br>
      <strong>y = 0</strong>
    </td>
  </tr>
  <tr>
    <td>
      <img alt="x-100"
      src="https://res.cloudinary.com/dms5y8rug/image/upload/c_thumb,g_face,q_auto:best/MH-HP-Overlay/x-100.webp"
      style="min-width: 397.5px;" />
    </td>
  </tr>
</table>
<table>
  <tr align="center">
    <td>
      <strong>x = 0<strong>
      <br>
      <strong>y = 0<strong>
    </td>
  </tr>
  <tr>
    <td>
      <img alt="x-0"
      src="https://res.cloudinary.com/dms5y8rug/image/upload/c_thumb,g_face,q_auto:best/MH-HP-Overlay/x-0.webp"
      style="min-width: 397.5px;" />
    </td>
  </tr>
</table>
<table>
  <tr align="center">
    <td>
      <strong>x = 0<strong>
      <br>
      <strong>y = 100<strong>
    </td>
  </tr>
  <tr>
    <td>
      <img alt="y-100"
      src="https://res.cloudinary.com/dms5y8rug/image/upload/c_thumb,g_face,q_auto:best/MH-HP-Overlay/y-100.webp"
      style="min-width: 397.5px;" />
    </td>
  </tr>
</table>

### Fix X & Fix Y

The `fix_x` and `fix_y` options in the `config.ini` file allow you to adjust the position of the overlay in situations where modifying the `x` and `y` coordinates may not be sufficient. For example, if you want the overlay to extend outside the window to view it on a secondary monitor without obstructing the game's UI, or if changing the opacity or color isn't a solution for you, or when adjusting the `x` and `y` coordinates doesn't adequately address the overlay's placement.

Remember to close and reopen the overlay after making changes in the `config.ini` file for these adjustments to take effect.

<table>
  <tr align="center">
    <td>
      <strong>Option</strong>
    </td>
    <td>
      <strong style="white-space: nowrap; ">
        Default value
      </strong>
    </td>
    <td>
      <strong>Type</strong>
    </td>
    <td>
      <strong>Observation</strong>
    </td>
  </tr>
  <tr align="center">
    <td>fix_x</td>
    <td>0</td>
    <td>integer</td>
    <td>It must be any integer, whether positive or negative, its value is in pixels</td>
  </tr>
  <tr align="center">
    <td>fix_y</td>
    <td>0</td>
    <td>integer</td>
    <td>It must be any integer, whether positive or negative, its value is in pixels</td>
  </tr>
</table>

<table>
  <tr align="center">
    <td>
      <strong>fix_x = 0</strong>
    </td>
    <td>
      <strong>fix_x = 500</strong>
    </td>
  </tr>
  <tr>
    <td>
      <img alt="fix-y-0"
      src="https://res.cloudinary.com/dms5y8rug/image/upload/c_thumb,g_face,q_auto:best/MH-HP-Overlay/fix_x_0.webp" />
    </td>
    <td>
      <img alt="fix-y-10"
      src="https://res.cloudinary.com/dms5y8rug/image/upload/c_thumb,g_face,q_auto:best/MH-HP-Overlay/fix_x_500.webp" />
    </td>
  </tr>
</table>

### Align

Within the `config.ini` file, the `align` option controls the alignment of labels in the overlay. When set to `true`, all labels will adjust their width to match the width of the largest label.

This ensures a consistent and orderly presentation of labels in the overlay interface.

Remember to close and reopen the overlay after making changes to the `config.ini` file for these adjustments to take effect.

<table>
  <tr align="center">
    <td>
      <strong>Option</strong>
    </td>
    <td>
      <strong style="white-space: nowrap; ">
        Default value
      </strong>
    </td>
    <td>
      <strong>Type</strong>
    </td>
    <td>
      <strong>Observation</strong>
    </td>
  </tr>
  <tr align="center">
    <td>align</td>
    <td>true</td>
    <td>boolean</td>
    <td>
      This is case-insensitive and recognizes boolean values from 'yes'/'no', 'on'/'off', 'true'/'false' and '1'/'0'
    </td>
  </tr>
</table>

<table>
  <tr align="center">
    <td>
      <strong>align = true</strong>
    </td>
    <td>
      <strong>align = false</strong>
    </td>
  </tr>
  <tr>
    <td>
      <img alt="labels"
      src="https://res.cloudinary.com/dms5y8rug/image/upload/c_thumb,g_face,q_auto:best/MH-HP-Overlay/labels.webp" />
    </td>
    <td>
      <img alt="align"
      src="https://res.cloudinary.com/dms5y8rug/image/upload/c_thumb,g_face,q_auto:best/MH-HP-Overlay/align.webp" />
    </td>
  </tr>
</table>

### Orientation

The `orientation` option within the `config.ini` file allows you to define the position of content within the `labels`. You can configure this option with one of the following values:

- `center`: Centers the content within the `labels`.
<br>&nbsp;
- `left`: Aligns the content to the left within the `labels`.
<br>&nbsp;
- `right`: Aligns the content to the right within the `labels`.

Remember to close and reopen the overlay after making changes in the `config.ini` file for these adjustments to take effect.

<table>
  <tr align="center">
    <td>
      <strong>Option</strong>
    </td>
    <td>
      <strong style="white-space: nowrap; ">
        Default value
      </strong>
    </td>
    <td>
      <strong>Type</strong>
    </td>
    <td>
      <strong>Observation</strong>
    </td>
  </tr>
  <tr align="center">
    <td>orientation</td>
    <td>center</td>
    <td>string</td>
    <td>Must be center, left or right</td>
  </tr>
</table>

<table>
  <tr align="center">
    <td colspan="2">
      <strong>align = true</strong>
    </td>
    <td>
      <strong>align = false</strong>
    </td>
  </tr>
  <tr align="center">
    <td>
      <strong>orientation = center</strong>
    </td>
    <td>
      <strong>orientation = left</strong>
    </td>
    <td>
      <strong>orientation = right<strong>
    </td>
  </tr>
  <tr>
    <td>
      <img alt="labels"
      src="https://res.cloudinary.com/dms5y8rug/image/upload/c_thumb,g_face,q_auto:best/MH-HP-Overlay/labels.webp" />
    </td>
    <td>
      <img alt="left"
      src="https://res.cloudinary.com/dms5y8rug/image/upload/c_thumb,g_face,q_auto:best/MH-HP-Overlay/left.webp" />
    </td>
    <td>
      <img alt="right"
      src="https://res.cloudinary.com/dms5y8rug/image/upload/c_thumb,g_face,q_auto:best/MH-HP-Overlay/right.webp" />
    </td>
  </tr>
</table>

### Color

Within the `config.ini` file, you can customize the color of text and background in the overlay `labels`, as well as their opacity. The available options are as follows:

- `text_color`: Specifies the color of the text within the `labels`. You can use any of the color names from **CSS SVG Colors**. You can view a list of these colors [here](https://upload.wikimedia.org/wikipedia/commons/2/2b/SVG_Recognized_color_keyword_names.svg).
<br>&nbsp;
- `background_color`: Defines the background color of the `labels` in the overlay. Similar to text_color, you can use any valid color name from **CSS SVG Colors**.
<br>&nbsp;
- `text_opacity`: Controls the opacity of the text within the `labels`.
<br>&nbsp;
- `background_opacity`: Controls the opacity of the background of the `labels`.
<br>&nbsp;
- `abnormal_status_text_color`: It's the same as `text_color` but for `abnormal status labels`.
<br>&nbsp;
- `abnormal_status_background_color`: It's the same as `background_color` but for `abnormal status labels`.
<br>&nbsp;
- `abnormal_status_text_opacity`: It's the same as `text_opacity` but for `abnormal status labels`.
<br>&nbsp;
- `abnormal_status_background_opacity`: It's the same as `background_opacity` but for `abnormal status labels`.

Adjust these values according to your preferences to customize the visual appearance of the overlay.

Remember to close and reopen the overlay after making changes in the `config.ini` file for these adjustments to take effect.

<table>
  <tr align="center">
    <td>
      <strong>Option</strong>
    </td>
    <td>
      <strong style="white-space: nowrap; ">
        Default value
      </strong>
    </td>
    <td>
      <strong>Type</strong>
    </td>
    <td>
      <strong>Observation</strong>
    </td>
  </tr>
  <tr align="center">
    <td>text_color</td>
    <td>aquamarine</td>
    <td>string</td>
    <td>
      Must be a <a href="https://upload.wikimedia.org/wikipedia/commons/2/2b/SVG_Recognized_color_keyword_names.svg">CSS SVG Color</a>
    </td>
  </tr>
  <tr align="center">
    <td>background_color</td>
    <td>darkslategray</td>
    <td>string</td>
    <td>
      Must be a <a href="https://upload.wikimedia.org/wikipedia/commons/2/2b/SVG_Recognized_color_keyword_names.svg">CSS SVG Color</a>
    </td>
  </tr>
  <tr align="center">
    <td>text_opacity</td>
    <td>100</td>
    <td>integer</td>
    <td>Must be greater than or equal to 1 and less than or equal to 100</td>
  </tr>
  <tr align="center">
    <td>background_opacity</td>
    <td>60</td>
    <td>integer</td>
    <td>Must be greater than or equal to 1 and less than or equal to 100</td>
  </tr>
  <tr align="center">
    <td>abnormal_status_text_color</td>
    <td>yellow</td>
    <td>string</td>
    <td>
      Must be a <a href="https://upload.wikimedia.org/wikipedia/commons/2/2b/SVG_Recognized_color_keyword_names.svg">CSS SVG Color</a>
    </td>
  </tr>
  <tr align="center">
    <td>abnormal_status_background_color</td>
    <td>green</td>
    <td>string</td>
    <td>
      Must be a <a href="https://upload.wikimedia.org/wikipedia/commons/2/2b/SVG_Recognized_color_keyword_names.svg">CSS SVG Color</a>
    </td>
  </tr>
  <tr align="center">
    <td>abnormal_status_text_opacity</td>
    <td>100</td>
    <td>integer</td>
    <td>Must be greater than or equal to 1 and less than or equal to 100</td>
  </tr>
  <tr align="center">
    <td>abnormal_status_background_opacity</td>
    <td>50</td>
    <td>integer</td>
    <td>Must be greater than or equal to 1 and less than or equal to 100</td>
  </tr>
</table>

## Building - (For Developers)

```
$ git clone
```

```
$ python -m venv .venv
$ .venv\Scripts\activate
$ pip install .
$ build
```
You will find the `build` in the `build/dist` folder

## Python modules used

- ahk[binary] - v1.8.0
- ahk-wmutil - v0.1.0
- colorama - v0.4.6
- PySide6 - v6.7.2
- Pymem - v1.13.1
- cx_Freeze - v8.0.0
- cursor - v1.3.5
- pywin32 - v306
- numpy - v2.2.4
- art - v6.2
- PyYAML - v6.0.2
- pcre2 - v0.5.2
