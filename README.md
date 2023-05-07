# Diffusion-Challenge



🤗The Moroccan Djellaba is a symbolic element of the Moroccan Culture. It remains deeply rooted in the daily life of Moroccan women. She wears it during traditional celebrations and even in their daily routines. However, she faces constraints when choosing a Djellaba and staying in trend.To make this easier for them, we proposed a solution: "Vestiaire_Meghribi_Intelligent" based basically on Stable Diffusion.
# Features

## Stable diffussion
In our project, we used stable diffusion to personalize the text-to-image model for Moroccan dress products used for fashion, specifically the Djellaba. By leveraging stable diffusion, we were able to enhance the model's ability to generate images that accurately reflect the unique features of the Djellaba, including its design, color, and cultural significance.
## DataSet
In this project  we gathered our dataset by scraping a fashion website named Diamontic.in this case we used web scraping to collect images and related information of fashion products from the Diamontic website. This dataset will be used for training and testing our machine learning models to classify fashion products based on their attributes such as color, pattern, and style.
## FineTuning
In our project, we used FineTuning to adapt a pre-trained convolutional neural network for a new fashion classification task. Our goal was to train the model to recognize a traditional Moroccan dress, the djellaba, based on a given input image and provide specific size information. We collected a dataset of images of djellabas in various sizes and used transfer learning to fine-tune a pre-trained model to recognize the unique features of the garment. During the fine-tuning process.
## Training
Training process: During the training process, the stable diffusion model is repeatedly presented with batches of training data, and the model's weights are updated to minimize the loss function. The training process typically involves a large number of iterations, with each iteration taking a batch of input images and generating corresponding output images.
## Inference
we used inference to evaluate the model's accuracy on a validation set and made adjustments to the model based on the evaluation results. Despite having limited training data, we were able to achieve high accuracy on the djellaba recognition task, and the model was able to provide accurate size information based on the input image.
## ControlNet onepose
During our project, we utilized the ControlNet OnePose deep learning architecture to estimate the pose of a model in a given image. ControlNet OnePose is a specific implementation of the ControlNet architecture that is designed for single-pose estimation. Using OnePose, we were able to predict the 2D keypoint locations of the model in the image, as well as the corresponding 3D keypoint locations in a predefined coordinate system. By estimating the model's pose, we were able to extract important features such as the model's position, orientation, and body proportions from the image.
# Problems
### Data preparation:
This typically involves collecting and cleaning a large dataset of images that will be used to train the model.
### hardware environment:
The problem of limited resources concerning our hardware environment, especially GPU and RAM, refers to the constraints and limitations we faced when it comes to the available computational power and memory in our hardware setup.
# Installation
We highly recommend installing🤗the following dependencies and scripts to successfully run DreamBooth with the Diffusers library. These installations will provide you with the necessary tools to work with control nets, diffusion models, transformers, and accelerate the training and inference processes during running this project.

 This line downloads the train_dreambooth.py script from a GitHub repository. The -q flag is used to suppress the output of the wget command.

!wget -q :
    
```bash
!wget -q https://github.com/ShivamShrirao/diffusers/raw/main/examples/dreambooth/train_dreambooth.py
```
 This line downloads the convert_diffusers_to_original_stable_diffusion.py script from another GitHub :
 ```bash
!wget -q https://github.com/ShivamShrirao/diffusers/raw/main/scripts/convert_diffusers_to_original_stable_diffusion.py
```
 This line installs the diffusers package from the specified GitHub repository using pip. The -qq flag is used to suppress the output of the pip command:
  ```bash
  %pip install -qq git+https://github.com/ShivamShrirao/diffusers

```
 This line installs the triton package using pip. The -q flag is used to suppress the output of the pip command. The -U flag is used to upgrade the package to the latest version, and --pre is used to install pre-release versions if available:
 ```bash
%pip install -q -U --pre triton
```
This line installs multiple packages (accelerate, transformers, ftfy, bitsandbytes, gradio, natsort, safetensors, xformers) using pip. The -q flag is used to suppress the output of the pip command.
 ```bash
%pip install -q accelerate transformers ftfy bitsandbytes==0.35.0 gradio natsort safetensors xformers
```
This command installs the controlnet_aux package. It is likely a package that provides auxiliary functionality or utilities for working with control nets in deep learning models.
 ```bash
pip install controlnet_aux
```
This command installs three packages: diffusers, transformers, and accelerate.
diffusers: is a package that provides implementations of diffusion models, which are probabilistic generative models.
transformers: is a popular package for natural language processing (NLP) tasks, providing pre-trained models, tokenizers, and other utilities.
accelerate: is a library that provides tools for accelerating PyTorch training and inference, such as distributed training and mixed precision.
 ```bash
pip install diffusers transformers accelerate
```
This command installs the xformers package. It is likely a package that provides additional functionalities or enhancements for working with transformers in deep learning models.
 ```bash
pip install xformers
```
This command installs the torch and torchvision packages. torch is the main PyTorch library for deep learning, providing tensor computations and neural network operations. torchvision is a package that provides utilities for computer vision tasks, such as image transformations and pre-trained models.
 ```bash
pip install torch torchvision
```
This command installs the diffusers package, which was already mentioned above. It provides implementations of diffusion models for generative modeling tasks.
 ```bash
pip install diffusers
```
 This command installs the transformers package, which was already explained above. It is a popular package for NLP tasks, offering pre-trained models and other NLP utilities.
 ```bash
pip install transformers
```
This command installs the accelerate package using the ! syntax, which is used specifically in Jupyter Notebook or IPython to run shell commands. It is likely installing the same accelerate package mentioned earlier.
 ```bash
!pip install accelerate
```
# Credentials    
We are extremely grateful for the guidance and support provided by the AI Experts monitors, organizers, and all the staff of Math&Maroc and 1337AI club throughout the hackathon. Your supervision and dedication were instrumental in ensuring the smooth running of the event, and your expertise and insights were invaluable in helping our team overcome the challenges we encountered.

We would like to express our sincere appreciation to all the sponsors who made this event possible. Your contributions played a vital role in providing participants with the necessary resources and technology to develop their projects. Your support was crucial in fostering innovation and enabling participants to showcase their skills and ideas.

We would like to take this opportunity to thank you once again for your unwavering support and commitment. We are honored to have been a part of this incredible event and we are excited about the potential for future collaborations and endeavors.



 


