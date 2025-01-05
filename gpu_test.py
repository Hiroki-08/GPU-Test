import platform
import torch
import torchvision

# Check Python version
print("="*30)
print( "Python      :", platform.python_version())
print( "torch       :", torch.__version__)
print( "torchvision :", torchvision.__version__)

# Check availability of GPU
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
if torch.cuda.is_available():
    print( "Backends    : CUDA" )
    device = torch.device("cuda")
elif torch.backends.mps.is_available():
    print( "Backends    : MPS" )
    device = torch.device("mps")
else:
    print( "Backends    : CPU" )
    device = torch.device("cpu")
    
print("="*30)
