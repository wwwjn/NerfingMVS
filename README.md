# NerfingMVS


> NerfingMVS: Guided Optimization of Neural Radiance Fields for Indoor Multi-view Stereo  
> [Yi Wei](https://weiyithu.github.io/), [Shaohui Liu](http://b1ueber2y.me/), [Yongming Rao](https://raoyongming.github.io/), [Wang Zhao](https://github.com/thuzhaowang), [Jiwen Lu](http://ivg.au.tsinghua.edu.cn/Jiwen_Lu/), [Jie Zhou](https://scholar.google.com/citations?user=6a79aPwAAAAJ&hl=en&authuser=1)  
> ICCV 2021 (Oral Presentation)  


## Installation
- Pull NerfingMVS repo.
  ```
  git clone --recursive git@github.com:weiyithu/NerfingMVS.git
  ```
- Install python packages with anaconda. (modified)
  ```
  conda create -n NerfingMVS python=3.7
  conda activate NerfingMVS
  conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 -c pytorch
  conda config --add channels conda-forge
  conda install imageio imageio-ffmpeg configargparse imagemagick
  pip install -r requirements.txt
  ```
 
- Add docker in /docker.
 
- We use COLMAP to calculate poses and sparse depths. However, original COLMAP does not have fusion mask for each view. Thus, we add masks to COLMAP and denote it as a submodule. Please follow https://colmap.github.io/install.html to install COLMAP in `./colmap` folder (Note that do not cover colmap folder with the original version). 
