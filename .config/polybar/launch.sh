#!/usr/bin/env sh

## Add this to your wm startup file.

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Display polybar for all monitors
for monitor in $(xrandr --query | grep " connected" | cut -d" " -f1); do
  MONITOR=$monitor polybar -c ~/.config/polybar/config.ini left &
  MONITOR=$monitor polybar -c ~/.config/polybar/config.ini right &
done
