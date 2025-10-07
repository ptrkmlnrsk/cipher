from src.buffer import Text

for text in contents['results']:
    status = text['status']
    if status == 'encrypted':
        Text(text=text['text'],
                    rot_type=text['rot_type'],
                    status=text['status'])
    else:
        pass