from __future__ import print_function

import sys
import numpy as np


def main():
    # parse input
    if len(sys.argv) != 3:
        sys.exit(-1)
    input_fn = sys.argv[1]
    output_fn = sys.argv[2]

    # retrive video list
    content = open(input_fn).read().splitlines()
    videos = []
    for line in content:
        video_id = line.split(',')[0]
        videos.append(video_id)
    videos = np.unique(np.array(videos))
    print('%d videos found' % len(videos))

    # make list
    np.savetxt(output_fn, videos, fmt='%s')
    pass


if __name__ == '__main__':
    main()
