# Load Xresources
xrdb -load ~/.Xresources

# Load Polish characters
setxkbmap pl

# Stop screen from going blank
xset s off
xset -dpms
xset s noblank

# Faster key repeat and lower delay
xset r rate 175 30

# Set cursor
xsetroot -cursor_name left_ptr

# Hide cursor when not used
unclutter -idle 1 -jitter 10 &

# Start redshift
redshift &

exec i3
