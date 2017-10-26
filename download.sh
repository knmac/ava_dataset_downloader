#!/bin/bash
# variables
TRAIN_FN="ava_train_v1.0.csv"
TEST_FN="ava_test_v1.0.csv"

TRAIN_VID_LST="train_vid.lst"
TEST_VID_LST="test_vid.lst"

# install dependencies
pip install --user youtube-dl

# download csv files
if [ ! -f ${TRAIN_FN} ]; then
    curl \
        -o ${TRAIN_FN} \
        https://research.google.com/ava/download/ava_train_v1.0.csv
fi

if [ ! -f ${TEST_FN} ]; then
    curl \
        -o ${TEST_FN} \
        https://research.google.com/ava/download/ava_test_v1.0.csv
fi

# parse video list
python makelist.py ${TRAIN_FN} ${TRAIN_VID_LST}
python makelist.py ${TEST_FN} ${TEST_VID_LST}

# download videos
youtube-dl -ci –format mp4 -o 'train/%(id)s.%(ext)s' -a ${TRAIN_VID_LST}
youtube-dl -ci –format mp4 -o 'test/%(id)s.%(ext)s' -a ${TEST_VID_LST}

# clean up
rm ${TRAIN_FN} ${TEST_FN} ${TRAIN_VID_LST} ${TEST_VID_LST}
