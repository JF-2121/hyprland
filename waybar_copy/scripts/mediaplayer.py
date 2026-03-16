#!/usr/bin/env python3
import gi
gi.require_version('Playerctl', '2.0')
from gi.repository import Playerctl, GLib
import json

def on_metadata(player, metadata, manager):
    info = {'text': '', 'class': 'custom-media', 'alt': player.props.player_name}
    if player.get_title() and player.get_artist():
        info['text'] = f"{player.get_artist()} - {player.get_title()}"
    elif player.get_title():
        info['text'] = player.get_title()
    print(json.dumps(info))

manager = Playerctl.PlayerManager()
def on_name_appeared(manager, name):
    player = Playerctl.Player.new_from_name(name)
    player.connect('metadata', on_metadata, manager)
    on_metadata(player, player.props.metadata, manager)

manager.connect('name-appeared', on_name_appeared)
for name in manager.props.player_names:
    on_name_appeared(manager, name)

GLib.MainLoop().run()
