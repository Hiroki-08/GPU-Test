import platform
import torch
import torchvision

# Check Python version
print("="*30)
print( "Python      :", platform.python_version())
print( "torch       :", torch.__version__)
print( "torchvision :", torchvision.__version__)

# Check availability of GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print( "device      :", device)

print("="*30)
