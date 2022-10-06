from datetime import datetime

def write_to_file(file_name='./history.txt',text=''):
    now = datetime.now()
    file_object = open(rf"{file_name}","a")
    file_object.write(f'{now}\n')
    file_object.write(
        f'''
            {text}\n
        '''
    )
    file_object.close()
    
