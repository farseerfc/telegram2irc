config = {
    'irc': {
        'server': 'irc.freenode.net',
        'port'  : 6697              ,
        'nick'  : 'LittleSen'       ,
        'ssl'   : True,
        'blacklist': [
            '[Olaf]',
        ],
    },

    'telegram': {
        'server': '127.0.0.1'       ,
        'port'  : 1235              ,
        'me'    : 'user#107279837'  ,
    },

    'bindings':(
        ('#linuxba', 'chat#8531126') ,
        ('#archlinux-cn', 'chat#12889958'),
    )
}
