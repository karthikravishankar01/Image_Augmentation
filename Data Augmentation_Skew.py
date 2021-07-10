

import Augmentor
# Passing the path of the image directory
p = Augmentor.Pipeline("D:\DDL\images")
  
# Defining augmentation parameters and generating 5 samples

p.skew(0.8, 0.2)
p.sample(70)
print('Success')
