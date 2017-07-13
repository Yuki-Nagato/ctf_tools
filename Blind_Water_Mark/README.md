# BlindWaterMark

盲水印 by python
From chishaxie/BlindWaterMark


### Demo

合成盲水印图

    python bwm.py encode 1483054559.png 选区_008.png image_enc.png


提取图中的盲水印 (需要原图)

    python bwm.py decode 1483054559.png image_enc.png waterMark.png


### Usage

    Usage: python bwm.py <cmd> [arg...] [opts...]
      cmds:
        encode <image> <watermark> <image(encoded)>
               image + watermark -> image(encoded)
        decode <image> <image(encoded)> <watermark>
               image + image(encoded) -> watermark
      opts:
        --debug,          Show debug
        --seed <int>,     Manual setting random seed (default is 20160930)
        --alpha <float>,  Manual setting alpha (default is 3.0)
