from twitch_chat_irc import twitch_chat_irc


connection = twitch_chat_irc.TwitchChatIRC('v_lan','oauth:8a1k7aagbcoh4m7bxsxpur6mlihbkz')
def do_something(message):
    print(message)

connection.listen('bratishkinoff',on_message=do_something)