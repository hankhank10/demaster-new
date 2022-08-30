# this is the demaster script which removes nonsense like "Remastered" and "Live at" from track names
# latest can be downloaded from https://github.com/hankhank10/demaster

def strip_name(full_song_name):

    text_to_parse = full_song_name
    lower_text_to_parse = text_to_parse.lower

    offending_text = [
        '- Remast',
        '(Remast',
        '- remast',
        '(remast',
        'Remastered',
        'remastered',
        '- Live at',
        '- Live At',
        '- Live From',
        '- Live from',
        '(Live at',
        '(Live from',
        'Live at ',
        'Live At',
        'live at ,'
        '- Mono / Remast',
        '- From ',
        '(Single edit)',
        '(Single Edit)',
        '(single edit)',
        ]

    for x in range (1960,2025):
        new_offending_text = '- ' + str(x) + ' Rem'
        offending_text.append (new_offending_text)

    for x in range (1960,2025):
        new_offending_text = '(' + str(x) + ' Rem'
        offending_text.append (new_offending_text)

    for x in range (1960,2025):
        new_offending_text = '- ' + str(x) + ' rem'
        offending_text.append (new_offending_text)

    for x in range (1960,2025):
        new_offending_text = '(' + str(x) + ' rem'
        offending_text.append (new_offending_text)

    for x in range (1960,2025):
        new_offending_text = '- ' + str(x) + ' Mix'
        offending_text.append (new_offending_text)

    for x in range (1960,2025):
        new_offending_text = '- ' + str(x) + ' mix'
        offending_text.append (new_offending_text)

    for x in range (1960,2025):
        new_offending_text = '(' + str(x) + ' Mix'
        offending_text.append (new_offending_text)

    for x in range (1960,2025):
        new_offending_text = '(' + str(x) + ' mix'
        offending_text.append (new_offending_text)

    for x in range (1960,2025):
        new_offending_text = '- ' + str(x) + '/Live'
        offending_text.append (new_offending_text)

    for x in range (1960,2025):
        new_offending_text = '(' + str(x) + '/Live'
        offending_text.append (new_offending_text)

    for item in offending_text:
        if text_to_parse.find(item) >=0:
            split_out_text = text_to_parse.partition (item)
            text_to_return = split_out_text[0]
            text_to_return = text_to_return.rstrip()
            return text_to_return

    return full_song_name
