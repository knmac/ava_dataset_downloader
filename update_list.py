import os
import sys


def load_list(path):
    with open(path) as f:
        return set(map(str.strip, filter(None, f)))


def load_downloaded_videos(path):
    def get_f_name(path):
        name, _ = os.path.splitext(os.path.basename(path))
        return name
        
    return {get_f_name(f) for f in os.listdir(path)}
    
    
def save_list(vid_list, path):
    with open(path, 'w+') as f:
        for vid in vid_list:
            f.write(vid + '\n')
            
if __name__ == '__main__':
    vid_list = load_list(sys.argv[2])
    already_downloaded_vid_list = load_downloaded_videos(sys.argv[1])
    save_list(vid_list - already_downloaded_vid_list, sys.argv[2])

