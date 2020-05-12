from ffmpeg_normalize import FFmpegNormalize
#import os
import sys
import glob
import os

# os.mkdir("out")

norm = FFmpegNormalize(
    normalization_type='peak',
    target_level=-3.0,
    audio_codec='pcm_s24le',
    sample_rate=48000)

print(sys.argv[1])

for i, file in enumerate(glob.glob(sys.argv[1] + "/*.wav")):
    print(i, file)

for i, file in enumerate(glob.glob(sys.argv[1] + "/*.wav")):
    norm.add_media_file(file, './out/{}.wav'.format(i))

norm.run_normalization()

for i, file in enumerate(glob.glob(".out/*.wav")):
    os.system('sndfile-convert {} ./out/{}.sds'.format(file, i))
    print(i, file)

