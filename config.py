from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os
import subprocess

from libqtile import hook


mod = "mod4"
terminal = guess_terminal()


@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([script])



keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
 
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "m", lazy.spawn("rofi -show drun"), desc="Shows rofi app menu"), 



    ###Custom key maps
    Key([mod], "f",lazy.window.toggle_fullscreen(),desc="Toggle fullscreen",),


    # Built-in utilities buttons 
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +5%"), desc='Volume Up'),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -5%"), desc='volume down'),
    Key([], "XF86AudioMute", lazy.spawn("pamixer -t"), desc='Volume Mute'),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc='playerctl'),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc='playerctl'),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc='playerctl'),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 10%+"), desc='brightness UP'),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 10%-"), desc='brightness Down'),
    Key([], "Print", lazy.spawn("flameshot gui"), desc='Screenshot'),



    ]

groups = [Group(f"{i+1}", label="󰏃") for i in range(8)]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [

    layout.Columns( 
        margin= [10,5,10,5],
        border_focus='#611C52',
	    border_normal='#1F1D2E',
        border_width=3,
        insert_position = 1
    ),

    layout.Max(	
	    margin=10,
	    border_width=0,
    ),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()



#   _______                    
#  /       \                   
#  $$$$$$$  | ______   ______  
#  $$ |__$$ |/      \ /      \ 
#  $$    $$< $$$$$$  /$$$$$$  |
#  $$$$$$$  |/    $$ $$ |  $$/ 
#  $$ |__$$ /$$$$$$$ $$ |      
#  $$    $$/$$    $$ $$ |      
#  $$$$$$$/  $$$$$$$/$$/       


screens = [
    Screen(
        top=bar.Bar([

                widget.Spacer(
                    length=15,
                    background='#282738',
                ),

                 widget.Image(
                    filename='~/.config/qtile/Assets/launch_Icon.png',
                    margin=2,
                    background='#282738',
                    #mouse_callbacks={"Button1":power},
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/6.png',
                ),

                widget.GroupBox(
                    fontsize=24,
                    borderwidth=3,
                    highlight_method='block',
                    active='#CAA9E0',
                    block_highlight_text_color="#91B1F0",
                    highlight_color='#4B427E',
                    inactive='#282738',
                    foreground='#4B427E',
                    background='#353446',
                    this_current_screen_border='#353446',
                    this_screen_border='#353446',
                    other_current_screen_border='#353446',
                    other_screen_border='#353446',
                    urgent_border='#353446',
                    rounded=True,
                    disable_drag=True,
                 ),

                widget.Spacer(
                    length=8,
                    background='#353446',
                ),

                 widget.Image(
                    filename='~/.config/qtile/Assets/1.png',
                ),

                 widget.Image(
                    filename='~/.config/qtile/Assets/layout.png',
                    background="#353446"
                ),

                
                widget.CurrentLayout(
                    background='#353446',
                    foreground='#CAA9E0',
                    fmt='{}',
                    font="Kawkab Mono Bold",
                    fontsize=13,
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/5.png',
                ),


                widget.WindowName(
                    background='#282738',
                    #background = '#353446',
                    format = "{name}",
                    font='Kawkab Mono Bold',
                    foreground='#CAA9E0',
                    empty_group_string = 'Desktop',
                    fontsize=13,
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/3.png',
                ),

                widget.Systray(
                    background='#282738',
                    fontsize=2,
                ),

                widget.TextBox(
                    text=' ',
                    background='#282738',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/6.png',
                    background='#353446',
                ),
                
                ########

                widget.Image(
                    filename='~/.config/qtile/Assets/Misc/ram.png',
                    background='#353446',
                ),


                widget.Spacer(
                    length=-7,
                    background='#353446',
                ),

                widget.Memory(
                    background='#353446',
                    format='{MemUsed: .0f}{mm}',
                    foreground='#CAA9E0',
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    update_interval=5,
                ),

                ######
                widget.Image(
                    filename='~/.config/qtile/Assets/2.png',
                ),


                widget.Spacer(
                    length=8,
                    background='#353446',
                ),

                widget.BatteryIcon(
                    theme_path='~/.config/qtile/Assets/Battery/',
                    background='#353446',
                    scale=1,
                ),

                widget.Battery(
                    font='Kawbak Mono Bold',
                    background='#353446',
                    foreground='#CAA9E0',
                    format='{percent:2.0%}',
                    fontsize=13,
                ),


                ########################
                widget.Image(
                    filename='~/.config/qtile/Assets/2.png',
                ),


                widget.Spacer(
                    length=8,
                    background='#353446',
                ),

                widget.Volume(
                    font='Kawbak Mono Bold',
                    theme_path='~/.config/qtile/Assets/Volume/',
                    emoji=True,
                    fontsize=13,
                    background='#353446',
                ),

                widget.Spacer(
                    length=-4,
                    background='#353446',
                    ),

                widget.Volume(
                    font='Kawbak Mono Bold',
                    background='#353446',
                    foreground='#CAA9E0',
                    fontsize=13,
                ),


                ################WAWAWAWAWAWA#################

                
                
                 widget.Image(
                    filename='~/.config/qtile/Assets/2.png',
                    background='#353446',
                ),


                widget.TextBox(
                    font='Kawbak Mono Bold',
                    background='#353446',
                    foreground='#CAA9E0',
                    text = '󰃟 ', 
                    fontsize=18,
                    ),
                widget.Backlight(
                    backlight_name = "intel_backlight", 
                    font='Kawbak Mono Bold',
                    background='#353446',
                    foreground='#CAA9E0',
                    format = '{percent:2.0%}', 
                    fontsize=13,
                    ),


                
                 widget.Image(
                    filename='~/.config/qtile/Assets/2.png',
                    background='#353446',
                ),


                widget.TextBox(
                    font='Kawbak Mono Bold',
                    background='#353446',
                    foreground='#CAA9E0',
                    text = ' ', 
                    fontsize=18,
                    ),
 
                widget.CPU(
                    font='Kawbak Mono Bold',
                    background='#353446',
                    foreground='#CAA9E0',
                    format = '{freq_current} GHz {load_percent}%', 
                    fontsize=13,
                    ),


                 widget.Image(
                    filename='~/.config/qtile/Assets/2.png',
                    background='#353446',
                ), 


                widget.TextBox(
                    font='Kawbak Mono Bold',
                    background='#353446',
                    foreground='#CAA9E0',
                    text = ' ', 
                    fontsize=18,
                    ),

                widget.ThermalSensor(
                    font='Kawbak Mono Bold',
                    background='#353446',
                    foreground='#CAA9E0',
                    tag_sensor = "CPU",
                    format = "{temp:.1f}{unit}",
                    fontsize=13,
                    ),



                widget.Image(
                    filename='~/.config/qtile/Assets/2.png',
                    background='#353446',
                ),

                widget.Wlan(
                    font='Kawbak Mono Bold',
                    background='#353446',
                    foreground='#CAA9E0',
                    format = "{essid} {percent:2.0%}", 
                    interface = "wlp61s0",
                    fontsize=13,
                    ),


                #####################WAWAWAWAWA######################







                 widget.Image(
                    filename='~/.config/qtile/Assets/5.png',
                    background='#353446',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/Misc/clock.png',
                    background='#282738',
                    margin_y=6,
                    margin_x=5,
                ),


                widget.Clock(
                    format='%I:%M %p',
                    background='#282738',
                    foreground='#CAA9E0',
                    font='Kawkab Mono Bold',
                    fontsize=13,
                ),

                widget.Spacer(
                    length=18,
                    background='#282738',
                ),

            ],
            30,
            border_color = '#282738',
            border_width = [0,0,0,0],
            margin = [3,15,5,15],
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = False
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"



